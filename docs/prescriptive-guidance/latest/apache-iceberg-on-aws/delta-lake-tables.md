---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/delta-lake-tables.html
---

# Delta Lake tables

For Delta Lake source tables, you can use two tools to produce Iceberg metadata over the Parquet data files that Delta already tracks:
+ [**Apache XTable**](https://xtable.apache.org/) — a sync utility that reads the Delta transaction log and writes Iceberg metadata over the same data files. You run it standalone (from your laptop, a Docker container on [Amazon ECS](https://aws.amazon.com/ecs/) or [Amazon EKS](https://aws.amazon.com/eks/), or an Amazon EC2 instance) in **full mode** on the first run (translates the entire table's metadata from scratch) and **incremental mode** on subsequent runs (syncs only the metadata for changes committed since the last sync).
+ [**Delta Lake UniForm**](https://docs.delta.io/latest/delta-uniform.html) — automatic Iceberg-metadata generation at every Delta write. You enable it with a Delta table property; the Delta writer emits Iceberg metadata alongside the Delta commit, so no external process runs.

**Delta version considerations**: In Delta Lake 3.x, UniForm does **not** populate per-data-file column statistics (min/max values, null counts) in the Iceberg manifest files it generates, which limits query performance on the Iceberg side. Those manifest-level statistics are what let an Iceberg reader skip whole data files during scan planning: the engine compares a query's predicates against each file's min/max (and null counts) and prunes files that cannot contain matching rows — all from the manifest, without opening the files. When those statistics aren't tracked in the Iceberg manifest files (as with UniForm on Delta Lake 3.x), the engine can't prune at planning time and instead falls back to inspecting each Parquet file's footer statistics at scan time — the footers carry the same min/max and null-count metadata, but reading them means opening every candidate file, which adds I/O and defers pruning from planning to scan. For Delta 3.x sources, Apache XTable is the recommended path. Delta Lake 4.x resolves this — UniForm populates full column statistics in the manifest files and works out of the box.

**Trade-off between the two tools**:
+ **UniForm** is automatic at every write, so no external process is required — but the Delta writer becomes responsible for producing the Iceberg metadata.
+ **XTable** is decoupled — the source cluster doesn't need to know about Iceberg — but you must schedule the sync utility yourself (see the **production scheduling** note under [Option 1: Apache XTable](#option-1-apache-xtable) below).

Deletion vectors impose a hard constraint for both tools — see the limitation notes under [Option 1: Apache XTable](#option-1-apache-xtable) and [Option 2: Delta Lake Uniform](#option-2-delta-lake-uniform) before picking a tool.

## Option 1: Apache XTable
<a name="option-1-apache-xtable"></a>

XTable has two operating modes:
+ **Full mode** — captures the current state of the Delta table and produces the complete Iceberg metadata from scratch. This is what happens on the first run.
+ **Incremental mode** — detects new Delta commits since the last sync and produces the corresponding Iceberg snapshots. XTable automatically selects this mode on subsequent runs when a prior Iceberg metadata state exists.

The utility needs two YAML configuration files: one for the target Iceberg catalog and one for the source-to-target dataset mapping.

`glueDataCatalog.yaml` — target catalog configuration (AWS Glue Data Catalog). Replace `s3://<bucket-name>/<warehouse-dir>/` with your Iceberg warehouse location (default location where databases and tables are created if not explicitly specified):

```
catalogImpl: org.apache.iceberg.aws.glue.GlueCatalog
catalogName: glue
catalogOptions:
  warehouse: s3://<bucket-name>/<warehouse-dir>/
  catalog-impl: org.apache.iceberg.aws.glue.GlueCatalog
  io-impl: org.apache.iceberg.aws.s3.S3FileIO
```

`datasetConfig.yaml` — source Delta table and target Iceberg table. Replace `<bucket-name>` with your own bucket name:

```
sourceFormat: DELTA
targetFormats:
  - ICEBERG
datasets:
  - tableBasePath: s3://<bucket-name>/your-database/your-delta-table/
    tableName: your_iceberg_table
    namespace: your_database
    partitionSpec: country:VALUE
```

**Initial full sync**:

```
java -jar xtable-utilities_2.12-0.3.0-incubating-bundled.jar \
    --datasetConfig datasetConfig.yaml \
    --icebergCatalogConfig glueDataCatalog.yaml
```

**Incremental sync** — same command; XTable detects the existing Iceberg state and runs incrementally:

```
java -jar xtable-utilities_2.12-0.3.0-incubating-bundled.jar \
    --datasetConfig datasetConfig.yaml \
    --icebergCatalogConfig glueDataCatalog.yaml
```

**Production scheduling**: For production use, run this command on a schedule with [AWS Step Functions](https://aws.amazon.com/step-functions/), [Amazon EventBridge Scheduler](https://aws.amazon.com/eventbridge/scheduler/), or [Amazon MWAA](https://aws.amazon.com/managed-workflows-for-apache-airflow/) — pick whichever fits how the rest of your data pipeline is orchestrated. The command is idempotent; if there are no new Delta commits since the last sync, XTable produces no new Iceberg snapshot.

### Reference example: end-to-end XTable sync of a Delta table
<a name="reference-example-end-to-end-xtable-sync-of-a-delta-table"></a>

The example below walks through a full-plus-incremental sync of a Delta table to Iceberg. The Delta table lives in the source database `mydb`, is registered in the AWS Glue Data Catalog, and stores data under `s3://<bucket-name>/mydb/customers_delta/`. The `datasetConfig.yaml` for this run points at that path (`sourceFormat: DELTA`) and sets `tableName: customers_iceberg`. Replace `<bucket-name>` with your own bucket name:

**Step 1: Create and populate the source Delta table**

```
spark.sql("""
CREATE TABLE mydb.customers_delta (
  id      INT,
  name    STRING,
  country STRING
)
USING delta
PARTITIONED BY (country)
LOCATION 's3://<bucket-name>/mydb/customers_delta/'
""")

spark.sql("""
INSERT INTO mydb.customers_delta VALUES
  (1, 'Johnn Doe',    'USA'),
  (2, 'Janee Doe',  'USA'),
  (3, 'Mary Major',   'UK'),
  (4, 'Richhard Roe', 'UK');
""")

spark.sql("""
UPDATE mydb.customers_delta
SET name =
  CASE
    WHEN id = 1 THEN 'John Doe'
    WHEN id = 4 THEN 'Richard Roe'
    ELSE name
  END
WHERE id IN (1, 4)
""")
```

The Delta table has two commits (INSERT \+ UPDATE) and reflects the final state.

**Step 2: Run the XTable initial sync**

Point `datasetConfig.yaml` at the Delta table (`sourceFormat: DELTA`, `tableBasePath: s3://<bucket-name>/mydb/customers_delta/`) and run the following command:

```
java -jar xtable-utilities_2.12-0.3.0-incubating-bundled.jar \
    --datasetConfig datasetConfig.yaml \
    --icebergCatalogConfig glueDataCatalog.yaml
```

XTable runs in full mode and creates **one Iceberg snapshot** capturing the latest committed state.

**Step 3: Additional Delta writes**

```
spark.sql("""
INSERT INTO mydb.customers_delta VALUES
  (5, 'Alejandro Rosalez', 'ES'),
  (6, 'Martha Rivera',  'ES');
""")

spark.sql("""
UPDATE mydb.customers_delta
SET name = 'Jane Doe'
WHERE id = 2
""")
```

**Step 4: Run the XTable incremental sync**

```
java -jar xtable-utilities_2.12-0.3.0-incubating-bundled.jar \
    --datasetConfig datasetConfig.yaml \
    --icebergCatalogConfig glueDataCatalog.yaml
```

XTable creates **two new Iceberg snapshots** — one per Delta commit landed since the previous sync (INSERT \+ UPDATE). Iceberg table has three snapshots total. XTable records the last-synced Delta version in the Iceberg snapshot summary so subsequent runs only replicate new commits.

### Limitation on deletion vectors
<a name="limitation-on-deletion-vectors"></a>

Apache XTable does not model Delta's deletion vectors. On a Delta source, updates and deletes with deletion vectors mark rows for removal without rewriting the underlying Parquet files, but XTable's Iceberg metadata sees both the base Parquet file (containing the original row) and the newer Parquet file (containing the updated row) as valid inputs. The Iceberg reader has no signal to filter out the pre-deletion-vector rows, and duplicate rows appear in the Iceberg output. For Delta sources that use deletion vectors, [UniForm](#option-2-delta-lake-uniform) is not an alternative either — see the [UniForm limitation](#uniform-limitation-on-deletion-vectors) below.

Three workarounds, from most invasive to least:
+ **Turn off deletion vectors on the Delta source for future writes.** This option fits when you don't rely on Deletion Vectors (DVs) write performance on the Delta side. Disable DVs through the table property and materialize any existing DVs so no sidecars remain. After this one-time rewrite, every XTable sync produces clean Iceberg metadata:

  ```
  # Turn off deletion vectors for future writes
  spark.sql("""
      ALTER TABLE mydb.customers_delta
      SET TBLPROPERTIES ('delta.enableDeletionVectors' = 'false')
  """)

  # Materialize existing DVs into rewritten data files, so no DV sidecars remain
  spark.sql("""
      REORG TABLE mydb.customers_delta APPLY (PURGE)
  """)
  ```
+ **Keep deletion vectors enabled on the Delta source and purge them before each XTable sync.** This option fits batch workloads where ingestion into the Delta source and XTable syncs happen at separate times: run `REORG ... APPLY (PURGE)` to materialize the DVs accumulated since the last sync, then run the XTable sync. The Delta source retains DV write performance between syncs:

  ```
  # Just before syncing: materialize existing DVs into rewritten data files
  spark.sql("""
      REORG TABLE mydb.customers_delta APPLY (PURGE)
  """)
  ```

  Then run the XTable sync as usual.
+ [**Self-managed full data migration**](self-managed-full-migration-to-iceberg-on-s3-s3-tables.md) — rewrites the data as an independent Iceberg table, which resolves the issue without touching the Delta source. Pick this when neither of the above is acceptable (for example, the Delta source is owned by another team and can't be reorganized).

## Option 2: Delta Lake UniForm
<a name="option-2-delta-lake-uniform"></a>

Enable UniForm on an existing Delta table with a `REORG ... UPGRADE UNIFORM` statement in Spark SQL configured for Delta Lake:

```
REORG TABLE mydb.delta_table APPLY (UPGRADE UNIFORM(ICEBERG_COMPAT_VERSION=2));
```

After UniForm is enabled, every subsequent Delta write also produces Iceberg metadata — Iceberg-side readers see the latest state without an external sync utility. Iceberg-capable engines that support UniForm (Amazon Redshift, Amazon Athena, and others) can read the UniForm-enabled Delta table directly from the AWS Glue Data Catalog under its existing name.

### Reference example: end-to-end UniForm on a Delta table
<a name="reference-example-end-to-end-uniform-on-a-delta-table"></a>

The example walks through enabling UniForm on an existing Delta table and observing how each subsequent Delta write also produces an Iceberg snapshot without any external process.

**Step 1: Create and populate the source Delta table** - Replace `<bucket-name>` with your own bucket name:

```
spark.sql("""
CREATE TABLE mydb.customers_delta (
  id      INT,
  name    STRING,
  country STRING
)
USING delta
PARTITIONED BY (country)
LOCATION 's3://<bucket-name>/mydb/customers_delta/'
""")

spark.sql("""
INSERT INTO mydb.customers_delta VALUES
  (1, 'John Smith',    'USA'),
  (2, 'Mary Johnson',  'USA'),
  (3, 'Marco Rossi',   'Italy'),
  (4, 'Sofia Bianchi', 'Italy');
""")

spark.sql("""
UPDATE mydb.customers_delta
SET name =
  CASE
    WHEN id = 1 THEN 'John2'
    WHEN id = 4 THEN 'Sofia2'
    ELSE name
  END
WHERE id IN (1, 4)
""")
```

**Step 2: Enable UniForm**

```
spark.sql("""
REORG TABLE mydb.customers_delta APPLY (UPGRADE UNIFORM(ICEBERG_COMPAT_VERSION=2))
""")
```

The REORG bootstraps Iceberg metadata over the current Delta state and produces **one Iceberg snapshot** reflecting the four rows. The same `mydb.customers_delta` catalog entry now serves both Delta and Iceberg readers.

**Step 3: Additional Delta writes — Iceberg snapshots produced automatically**

```
spark.sql("""
INSERT INTO mydb.customers_delta VALUES
  (5, 'Alice Brown', 'UK'),
  (6, 'Bob Wilson',  'UK');
""")
```

UniForm produces a **new Iceberg snapshot** alongside the Delta commit. The Iceberg table now has two snapshots.

```
spark.sql("""
UPDATE mydb.customers_delta
SET name = 'Mary2'
WHERE id = 2
""")
```

UniForm produces **another Iceberg snapshot** — three snapshots total. Query `mydb.customers_delta` from any Iceberg-capable engine at any point and you see the current Delta state without running an external sync utility.

### Limitation on deletion vectors
<a name="uniform-limitation-on-deletion-vectors"></a>

Unlike XTable, which has no Deletion Vector awareness and would double-count masked rows, UniForm handles DVs correctly — but at the cost of disabling them. The `REORG TABLE ... APPLY (UPGRADE UNIFORM(ICEBERG_COMPAT_VERSION=2))` operation materializes any existing DVs into clean base files, disables `enableDeletionVectors`, and turns on Iceberg Compat V2 in one atomic commit.

Future writes use copy-on-write, which materializes every change by rewriting the full base files — significantly more I/O than DV-based sparse updates, especially on wide tables.

If retaining DV write performance on the Delta source is a hard requirement, UniForm isn't the right fit — pick instead either [XTable with periodic DV purge](#limitation-on-deletion-vectors) (DVs stay enabled on Delta between syncs and are purged only right before each sync ), or [self-managed full data migration](self-managed-full-migration-to-iceberg-on-s3-s3-tables.md) into an independent Iceberg table.
