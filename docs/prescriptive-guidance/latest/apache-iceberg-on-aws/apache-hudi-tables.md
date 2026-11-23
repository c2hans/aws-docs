---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/apache-hudi-tables.html
---

# Apache Hudi tables

For Apache Hudi source tables, in-place migration to Iceberg is done with [**Apache XTable**](https://xtable.apache.org/) — a sync utility that reads the Hudi commit log and writes an Iceberg metadata layer over the same Parquet data files that Hudi already tracks. The base data is not rewritten; only the Iceberg metadata is produced. Review the [Limitation on merge-on-read tables](#limitation-on-merge-on-read-tables) below before starting a migration.

XTable has two operating modes:
+ **Full mode** — captures the current state of the Hudi table and produces the complete Iceberg metadata from scratch. This is what happens on the first run.
+ **Incremental mode** — detects new Hudi commits since the last sync and produces the corresponding Iceberg snapshots. Automatically selected on subsequent runs when a prior Iceberg metadata state exists.

**Source-side performance note**: If the source Hudi table was created with the built-in metadata table (`hoodie.metadata.enable=true`) and the column-statistics index (`hoodie.metadata.index.column.stats.enable=true`) turned on, XTable reads the file listings and column min/max statistics directly from Hudi's metadata and each sync is materially faster on large tables. When those settings are off, XTable falls back to enumerating the underlying S3 objects and opening every Parquet footer to reconstruct the same information — both of which get expensive as the table grows. These properties are set at Hudi table-creation time and generally cannot be flipped on later, so this is a note about what to look for in the source table's configuration rather than a directive to change it.

You can run XTable standalone from your laptop, a Docker container (on [Amazon ECS](https://aws.amazon.com/ecs/) or [Amazon EKS](https://aws.amazon.com/eks/)), or an Amazon EC2 instance. The utility needs two YAML configuration files: one for the target Iceberg catalog and one for the source-to-target dataset mapping.

`glueDataCatalog.yaml` — target catalog configuration (AWS Glue Data Catalog). Replace `s3://<bucket-name>/<warehouse-dir>/` with your Iceberg warehouse location (default location where databases and tables are created if not explicitly specified):

```
catalogImpl: org.apache.iceberg.aws.glue.GlueCatalog
catalogName: glue
catalogOptions:
  warehouse: s3://<bucket-name>/<warehouse-dir>/
  catalog-impl: org.apache.iceberg.aws.glue.GlueCatalog
  io-impl: org.apache.iceberg.aws.s3.S3FileIO
```

`datasetConfig.yaml` — source Hudi table and target Iceberg table. Replace `<bucket-name>` with your own bucket name:

```
sourceFormat: HUDI
targetFormats:
  - ICEBERG
datasets:
  - tableBasePath: s3://<bucket-name>/your_database/your-hudi-table/
    tableName: your_iceberg_table
    namespace: your_database
    partitionSpec: country:VALUE
```

**Initial full sync** — first run of the XTable utility. XTable operates in full mode automatically because no prior Iceberg state exists:

```
java -jar xtable-utilities_2.12-0.3.0-incubating-bundled.jar \
    --datasetConfig datasetConfig.yaml \
    --icebergCatalogConfig glueDataCatalog.yaml
```

**Incremental sync** — subsequent runs detect new Hudi commits since the last sync and produce the corresponding Iceberg snapshots. The command is identical to the full sync; XTable inspects the existing Iceberg metadata to decide which mode to run:

```
java -jar xtable-utilities_2.12-0.3.0-incubating-bundled.jar \
    --datasetConfig datasetConfig.yaml \
    --icebergCatalogConfig glueDataCatalog.yaml
```

**Production scheduling**: For production use, run this command on a schedule with [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html), [Amazon EventBridge Scheduler](https://aws.amazon.com/eventbridge/scheduler/), or [Amazon MWAA](https://aws.amazon.com/managed-workflows-for-apache-airflow/) — pick whichever fits how the rest of your data pipeline is orchestrated. The command is idempotent; if there are no new Hudi commits since the last sync, XTable produces no new Iceberg snapshot.

## Reference example: end-to-end XTable sync of a Hudi CoW table
<a name="reference-example-end-to-end-xtable-sync-of-a-hudi-cow-table"></a>

The example below walks through a full-plus-incremental sync of a Hudi copy-on-write (CoW) table to Iceberg. The Hudi table lives in the source database `mydb`, is registered in the AWS Glue Data Catalog, and stores data under `s3://<bucket-name>/mydb/customers_hudi_cow/`. The `datasetConfig.yaml` for this run points at that path and sets `tableName: customers_iceberg`.

**Step 1: Create the source Hudi table - **Replace `<bucket-name>` with your own bucket name:

```
spark.sql("""
CREATE TABLE mydb.customers_hudi_cow (
  id      INT,
  name    STRING,
  country STRING
)
USING hudi
PARTITIONED BY (country)
OPTIONS (
  type            = 'cow',
  primaryKey      = 'id',
  preCombineField = 'id'
)
LOCATION 's3://<bucket-name>/mydb/customers_hudi_cow/'
""")
```

**Step 2: Populate the table**

```
spark.sql("""
INSERT INTO mydb.customers_hudi_cow VALUES
  (1, 'Johnn Doe',    'USA'),
  (2, 'Janee Doe',  'USA'),
  (3, 'Mary Major',   'UK'),
  (4, 'Richhard Roe', 'UK');
""")

spark.sql("""
UPDATE mydb.customers_hudi_cow
SET name =
  CASE
    WHEN id = 1 THEN 'John Doe'
    WHEN id = 4 THEN 'Richard Roe'
    ELSE name
  END
WHERE id IN (1, 4)
""")
```

The Hudi table now has two commits (the initial INSERT and the UPDATE) and reflects the final state: John Doe, Janee Doe, Mary Major, Richard Roe.

**Step 3: Run the XTable initial sync**

```
java -jar xtable-utilities_2.12-0.3.0-incubating-bundled.jar \
    --datasetConfig datasetConfig.yaml \
    --icebergCatalogConfig glueDataCatalog.yaml
```

XTable runs in **full mode** (no prior Iceberg state exists) and creates **one Iceberg snapshot** capturing the latest committed state of the Hudi table. Query `mydb.customers_iceberg` — you see the four rows with the applied updates.

**Step 4: Additional Hudi writes**

```
spark.sql("""
INSERT INTO mydb.customers_hudi_cow VALUES
  (5, 'Alejandro Rosalez', 'ES'),
  (6, 'Martha Rivera',  'ES');
""")

spark.sql("""
UPDATE mydb.customers_hudi_cow
SET name = 'Jane Doe'
WHERE id = 2
""")
```

Two more Hudi commits (an INSERT and an UPDATE) have landed since the last sync.

**Step 5: Run the XTable incremental sync**

Same command as Step 3:

```
java -jar xtable-utilities_2.12-0.3.0-incubating-bundled.jar \
    --datasetConfig datasetConfig.yaml \
    --icebergCatalogConfig glueDataCatalog.yaml
```

XTable detects that Iceberg metadata already exists and runs in **incremental mode**. It creates **two new Iceberg snapshots** — one per Hudi commit that landed since the previous sync (the INSERT and the UPDATE from Step 4). The Iceberg table now has three snapshots total.

**Note**
XTable tracks the last-synced Hudi instant in the **Iceberg snapshot summary** of each snapshot it produces. On subsequent runs, XTable reads that value from the current Iceberg snapshot to determine which Hudi commits still need to be replicated, so incremental syncs only process new commits.

## Limitation on merge-on-read tables
<a name="limitation-on-merge-on-read-tables"></a>

On a Hudi copy-on-write (CoW) source, XTable produces an Iceberg view that reflects the latest committed dataset faithfully. On a Hudi merge-on-read (MoR) source, XTable produces an Iceberg view that behaves like a **read-optimized view** — the Iceberg table exposes the latest compacted dataset, so records that live only in un-compacted MoR log files are not visible on the Iceberg side until Hudi compaction has folded them into the base files. If a MoR source stream is written frequently and compacted rarely, Iceberg readers can lag behind Hudi readers by whatever the compaction cadence is.

Two workarounds:
+ **Trigger Hudi compaction on the source table**, then re-run the XTable sync. Use the Hudi `run_compaction` Spark procedure to schedule (`op => 'schedule'`) and then execute (`op => 'run'`) a compaction plan. The `DynamoDBBasedLockProvider` coordinates concurrent writers by taking a lock in a DynamoDB table you provision separately.

  Schedule the compaction:

  ```
  spark.sql("""
  CALL spark_catalog.system.run_compaction(
      table   => 'mydb.customers_hudi_mor',
      op      => 'schedule',
      options =>
        'hoodie.compact.inline.max.delta.commits=1,
         hoodie.compact.inline.max.delta.seconds=0,
         hoodie.write.lock.provider=org.apache.hudi.aws.transaction.lock.DynamoDBBasedLockProvider,
         hoodie.write.lock.dynamodb.table=hudi_locks,
         hoodie.write.lock.dynamodb.region=us-east-1'
  )
  """).show(truncate=False)
  ```

  Execute the compaction:

  ```
  spark.sql("""
  CALL spark_catalog.system.run_compaction(
      table   => 'mydb.customers_hudi_mor',
      op      => 'run',
      options =>
        'hoodie.write.lock.provider=org.apache.hudi.aws.transaction.lock.DynamoDBBasedLockProvider,
         hoodie.write.lock.dynamodb.table=hudi_locks,
         hoodie.write.lock.dynamodb.region=us-east-1'
  )
  """).show(truncate=False)
  ```

  After compaction completes, the base Parquet files reflect the latest state and the log files are consumed. A subsequent XTable incremental sync picks up the compaction commit and brings the Iceberg table in line with the Hudi source.
+ [Self-managed full data migration](self-managed-full-migration-to-iceberg-on-s3-s3-tables.md) — rewrites the data as an independent Iceberg table, which resolves the visibility issue without touching the Hudi source. Choose this when the Hudi source cannot be modified to run a compaction.
