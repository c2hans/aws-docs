---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/working-with-iceberg-tables-by-using-amazon-redshift.html
---

# Working with Iceberg tables by using Amazon Redshift

Amazon Redshift can read from and write to Apache Iceberg tables that are either **self-managed** on Amazon S3 (through the AWS Glue Data Catalog) or **hosted in Amazon S3 Tables** (through the `s3tablescatalog` federated catalog). This section covers supported features, compute and pricing, catalog selection, and end-to-end examples for creating, loading, updating, evolving, and querying tables in both storage options.

## Iceberg format version support in Amazon Redshift
<a name="iceberg-format-version-support-in-amazon-redshift"></a>

Amazon Redshift supports both Iceberg format version 2 and Iceberg format version 3.

|
|
| **Format version** | **Self-managed Iceberg on S3** | **Amazon S3 Tables** |
| --- |--- |--- |
| Version 2 (V2) | Yes | Yes |
| Version 3 (V3) | Yes | Yes |

When `CREATE TABLE` does not set the `format-version` table property, Redshift applies the [Iceberg default of V2](https://iceberg.apache.org/docs/latest/configuration/#table-behavior-properties). Add `TABLE PROPERTIES ('format-version'='3')` to create a V3 table (or `ALTER TABLE ... SET TABLE PROPERTIES ('format-version'='3')` to upgrade an existing V2 table).

**Note**
Amazon Redshift provisioned clusters that use [AWS Graviton-based RG instances](https://aws.amazon.com/blogs/aws/amazon-redshift-introduces-aws-graviton-based-rg-instances-with-an-integrated-data-lake-query-engine/), and Amazon Redshift Serverless, process data lake queries with an integrated data lake query engine that runs on their own compute. RA3 instance types use [Amazon Redshift Spectrum](https://docs.aws.amazon.com/it_it/redshift/latest/dg/c-using-spectrum.html), which runs on dedicated servers independent of the cluster.

### V3 feature support in Amazon Redshift
<a name="v3-feature-support-in-amazon-redshift"></a>

Iceberg V3 introduces several new capabilities on top of V2. The following table shows per-feature availability in Amazon Redshift SQL against V3 tables.

|
|
| **V3 feature** | **Supported** |
| --- |--- |
| Row lineage | Yes |
| Deletion vectors | Yes |
| Default column values | Yes |
| Nanosecond timestamps (`timestamp_ns`, `timestamptz_ns`) | No |
| Geography type | No |
| Geometry type | No |
| Variant type (with or without shredding) | No |
| Complex types (struct, list, map) | No |
| Binary | No |
| Uuid | No |
| Time | No |

**Notes**:
+ Amazon Redshift support for Apache Iceberg V3 is currently available only on Amazon Redshift Serverless (except the 4 RPU workgroup) and on provisioned clusters that use AWS Graviton-based RG instances.
+ After a V2 to V3 upgrade, Iceberg's `timestamptz` type maps to Amazon Redshift's `TIMESTAMPTZ` instead of `TIMESTAMP` (the V2 mapping), so queries that previously returned naive timestamps start returning values with time-zone information.

**Note**
 Before you create a V3 Iceberg table with Amazon Redshift — or upgrade an existing V2 table to V3 — verify that every downstream engine that reads or writes the table also supports V3. Notable current gap: [Amazon Athena](working-with-iceberg-tables-by-using-athena-sql-queries.md) does **not** support V3. For the authoritative service-by-service matrix, see [Working with Iceberg table format specification version 3](table-spec-v3.md).

## Iceberg feature support
<a name="redshift-iceberg-feature-support"></a>

The following table summarizes Iceberg feature support in Amazon Redshift SQL, grouped by capability area. Behavior is the same on both hosting options (self-managed Iceberg on Amazon S3 and Amazon S3 Tables) unless a row calls out a difference.

|
|
| **Category** | **Feature** | **Supported** |
| --- |--- |--- |
| **DDL** | `CREATE TABLE ... USING ICEBERG` |  |
|  | `CREATE TABLE AS SELECT` (CTAS) |  |
|  | `DROP TABLE` (removes the Data Catalog registration; data files remain in S3) |  |
|  | `SHOW TABLES` |  |
|  | `ALTER TABLE RENAME COLUMN` |  |
|  | `ALTER TABLE ADD` / `DROP COLUMN` |  |
|  | `ALTER TABLE ALTER COLUMN` (type widening) |  |
|  | `ALTER TABLE SET TABLE PROPERTIES` |  |
|  | `ALTER TABLE ADD` / `DROP` / `REPLACE PARTITION FIELD` |  |
| **DML** | `INSERT INTO` |  |
|  | `UPDATE` |  merge-on-read only (V2: writes positional deletes; V3: writes deletion vectors) |
|  | `DELETE` |  merge-on-read only (V2: writes positional deletes; V3: writes deletion vectors) |
|  | `MERGE` (upsert) |  merge-on-read only (V2: writes positional deletes; V3: writes deletion vectors) |
|  | Writes honor Iceberg table sort order | ✗ (Redshift does not apply the Iceberg `sort_order` table property during writes) |
| **Read** | Query Iceberg tables |  — V2: reads positional deletes , equality deletes ✗; V3: reads deletion vectors , equality deletes ✗ (Redshift cannot read tables that contain equality deletes) |
|  | Join Iceberg tables with native Redshift tables |  |
|  | Time travel queries | ✗ |
|  | Incremental queries | ✗ |
|  | Access Iceberg metadata tables (`$snapshots`, `$files`, ...) | ✗ (Redshift SQL does not expose Iceberg per-table metadata tables) |
| **Materialized views** | Redshift materialized view over an Iceberg table (create, refresh, and query) |  (V2 only — MVs are not supported on V3 tables) |
|  | [AWS Glue Iceberg materialized view](apache-iceberg-materialized-views-in-aws-glue-data-catalog.md) |  (query only) |
| **Partitioning** | Hidden partitioning (all V2 partition transforms except `void`) |  |
|  | Partition evolution |  (via `ALTER TABLE ADD` / `DROP` / `REPLACE PARTITION FIELD`) |
|  | Metadata-only partition `DELETE` |  |
| **Security** | AWS Lake Formation full-table access control |  |
|  | AWS Lake Formation row/column access control |  (row and column filters on Iceberg tables governed by the AWS Glue Data Catalog \+ Lake Formation) |
| **Maintenance** | `OPTIMIZE` / compaction | ✗ |
|  | Snapshot expiration | ✗ |
|  | Orphan file cleanup | ✗ |
|  | Sort order / Z-order compaction | ✗ |
| **Format** | Data files supported | Parquet , Avro ✗, ORC ✗ |
|  | Data-file compression: `snappy`, `zstd`, `gzip`, `brotli`, uncompressed |  |

**Notes**:
+ Iceberg write support (`INSERT`, `UPDATE`, `DELETE`, `MERGE`) is available on Redshift Serverless and on RG instance types. On RA3 instance types, Redshift Spectrum is used for reads only.
+ You can write to an Iceberg table that Redshift didn't create, provided the table is V2 or V3, uses Parquet, has no [Metadata compression](https://iceberg.apache.org/spec/#table-metadata-fields), and does not have Write-Audit-Publish (WAP) enabled.

## Compute and pricing
<a name="compute-and-pricing"></a>

The compute path — and therefore the billing model — that Redshift uses to run an Iceberg query depends on the target cluster or workgroup type:
+ **Redshift Serverless workgroups and RG provisioned clusters** run Iceberg queries on the workgroup's / cluster's own compute resources. There is **no separate charge** for data-lake queries — you pay the standard Serverless RPU or RG cluster price.
+ **DC2 and RA3 provisioned clusters** route Iceberg queries through [**Amazon Redshift Spectrum**](https://docs.aws.amazon.com/redshift/latest/dg/c-spectrum-overview.html), and are billed at Spectrum's per-TB-scanned rate on top of the cluster's provisioned price.

For the current per-RPU, per-node, and per-TB rates, see [Amazon Redshift pricing](https://aws.amazon.com/redshift/pricing/).

## Catalog configuration in Redshift
<a name="catalog-configuration-in-redshift"></a>

Redshift references Iceberg tables in one of two ways: through an **external schema** that maps a Redshift schema name onto a Data Catalog database, or through **three-part notation** (`<catalog>.<database>.<table>`). The catalog name changes with the hosting option; the DDL and DML syntax is otherwise the same. For more details see [Referencing Iceberg tables](https://docs.aws.amazon.com/redshift/latest/dg/referencing-iceberg-tables.html)

### Self-managed Iceberg on Amazon S3
<a name="self-managed-iceberg-on-amazon-s3"></a>

Two equivalent forms are supported:

**Option A — External schema over the AWS Glue Data Catalog**:

```
CREATE EXTERNAL SCHEMA my_iceberg
FROM DATA CATALOG
DATABASE 'iceberg_db'
IAM_ROLE 'arn:aws:iam::<aws-account-id>:role/RedshiftDataLakeRole';
```

Then reference tables as `my_iceberg.<table_name>`.

**Option B — Three-part notation over the auto-mounted **`awsdatacatalog`:

```
SELECT * FROM awsdatacatalog.iceberg_db.orders;
```

For both forms, `LOCATION` is required on `CREATE TABLE`, must be an empty S3 prefix in the same Region as the Redshift cluster, and must not overlap any existing S3 objects.

### Amazon S3 Tables
<a name="redshift-amazon-s3-tables"></a>

After enabling the S3 Tables integration with AWS analytics services (see [Getting started with Amazon S3 Tables](getting-started-with-amazon-s3-tables.md)), reference S3 Tables via three-part notation using the `@s3tablescatalog` suffix on the table bucket name (replace `<table-bucket-name>` with your own table bucket name):

```
SELECT * FROM "<table-bucket-name>@s3tablescatalog".sales.orders;
```

For an end-to-end setup walkthrough, see [Using Amazon S3 Tables with Amazon Redshift to query Apache Iceberg tables](https://aws.amazon.com/blogs/big-data/using-amazon-s3-tables-with-amazon-redshift-to-query-apache-iceberg-tables/).

## Creating Iceberg tables
<a name="creating-iceberg-tables"></a>

Use `CREATE TABLE ... USING ICEBERG` to create tables. `LOCATION` is required for self-managed Iceberg (external schemas and `awsdatacatalog`); it must be omitted for Amazon S3 Tables. See [Iceberg Create table](https://docs.aws.amazon.com/redshift/latest/dg/iceberg-writes-sql-syntax.html#iceberg-writes-create-table) for more details on creating Apache Iceberg tables on Amazon Redshift. For supported datatypes, see [Querying Iceberg supported data types](https://docs.aws.amazon.com/redshift/latest/dg/querying-iceberg-supported-data-types.html)

Redshift supports the following Iceberg partition transforms: `identity`, `bucket[N]`, `truncate[W]`, `year`, `month`, `day`, `hour`. Multi-level partitioning is supported, but the same source column can't appear in more than one transform. The examples in this section create **format-version 2** tables through the `TABLE PROPERTIES ('format-version'='2')` clause; the same statements work for **format-version 3** — just replace `'2'` with `'3'`. For V3 features such as default column values and row lineage, and for upgrading an existing V2 table to V3, see [Working with Iceberg V3](#working-with-iceberg-v3) at the end of this section.

### Creating a partitioned table
<a name="creating-a-partitioned-table"></a>

**Self-managed Iceberg on Amazon S3** (external schema) - Replace `<bucket-name>` with your own bucket name:

```
CREATE TABLE my_iceberg.orders (
    order_id     BIGINT,
    customer_id  VARCHAR,
    status       VARCHAR,
    order_ts     TIMESTAMP,
    amount       DECIMAL(10,2)
)
USING ICEBERG
LOCATION 's3://<bucket-name>/orders/'
PARTITIONED BY (day(order_ts))
TABLE PROPERTIES ('format-version'='2');
```

**Amazon S3 Tables** (three-part notation, no `LOCATION`) - Replace `<table-bucket-name>` with your own table bucket name:

```
CREATE TABLE "<table-bucket-name>@s3tablescatalog".sales.orders (
    order_id     BIGINT,
    customer_id  VARCHAR,
    status       VARCHAR,
    order_ts     TIMESTAMP,
    amount       DECIMAL(10,2)
)
USING ICEBERG
PARTITIONED BY (day(order_ts))
TABLE PROPERTIES ('format-version'='2');
```

### Creating a table and loading data with a single CTAS statement
<a name="creating-a-table-and-loading-data-with-a-single-ctas-statement"></a>

Use `CREATE TABLE ... USING ICEBERG AS SELECT ...` to create and populate an Iceberg table in one step. Add a `PARTITIONED BY` clause with an Iceberg [partition transform](https://iceberg.apache.org/docs/latest/partitioning/#icebergs-hidden-partitioning) (for example `day(transaction_time)`) to hidden-partition the target as it is created.

**Self-managed Iceberg on Amazon S3** (partitioned by day of `transaction_time`) - Replace `<bucket-name>` with your own bucket name:

```
CREATE TABLE my_iceberg.orders_ctas
USING ICEBERG
LOCATION 's3://<bucket-name>/orders_ctas/'
PARTITIONED BY (day(transaction_time))
TABLE PROPERTIES ('format-version'='2')
AS
SELECT * FROM stage.raw_orders WHERE transaction_time >= DATE '2026-01-01';
```

**Amazon S3 Tables** (same partition transform; `LOCATION` is omitted because the table bucket manages storage) - Replace `<table-bucket-name>` with your own table bucket name:

```
CREATE TABLE "<table-bucket-name>@s3tablescatalog".sales.orders_ctas
USING ICEBERG
PARTITIONED BY (day(transaction_time))
AS
SELECT * FROM stage.raw_orders WHERE transaction_time >= DATE '2026-01-01';
```

**Note**
CTAS does not inherit `DEFAULT` column values from the source table. If the target needs defaults, add them after creation with `ALTER TABLE ... ALTER COLUMN ... SET DEFAULT`.

## Inserting, updating, deleting, and merging data
<a name="inserting-updating-deleting-and-merging-data"></a>

Redshift supports the full DML surface — `INSERT`, `UPDATE`, `DELETE`, `MERGE` — against Iceberg tables in both storage options. See [Redshift Iceberg writes](https://docs.aws.amazon.com/redshift/latest/dg/iceberg-writes-sql-syntax.html#iceberg-writes-update) for more details on DML support.

```
-- INSERT
INSERT INTO my_iceberg.orders
VALUES (1001, 'C001', 'pending', TIMESTAMP '2026-06-01 10:15:00', 49.90);

-- UPDATE
UPDATE my_iceberg.orders
SET   status = 'shipped'
WHERE order_id = 1001;

-- DELETE
DELETE FROM my_iceberg.orders
WHERE order_ts < DATE '2026-01-01';

-- MERGE (upsert)
MERGE INTO my_iceberg.orders AS t
USING     stage.raw_orders    AS s
   ON     t.order_id = s.order_id
WHEN MATCHED THEN
    UPDATE SET status = s.status, amount = s.amount
WHEN NOT MATCHED THEN
    INSERT (order_id, customer_id, status, order_ts, amount)
    VALUES (s.order_id, s.customer_id, s.status, s.order_ts, s.amount);
```

The same statements against S3 Tables use the three-part `"<table-bucket-name>@s3tablescatalog".<namespace>.<table>` identifier in place of `my_iceberg.orders` — the DML body is identical.

**Note**
On V3 tables, `UPDATE` and `DELETE` produce deletion vectors rather than positional delete files. This makes update-heavy workloads noticeably faster than the equivalent V2 pattern.

## Evolving tables
<a name="evolving-tables"></a>

Iceberg supports in-place schema and partition evolution — metadata-only changes that never rewrite existing data files. Amazon Redshift exposes both through `ALTER TABLE` on the target Iceberg table.

### Schema evolution
<a name="schema-evolution"></a>

For full syntax and limitations, see [Altering table definitions](https://docs.aws.amazon.com/redshift/latest/dg/iceberg-alter-table.html).

```
-- Add a column
ALTER TABLE iceberg_schema.orders ADD COLUMN shipping_address VARCHAR;

-- Drop a column
ALTER TABLE iceberg_schema.orders DROP COLUMN shipping_address;

-- Rename a column
ALTER TABLE iceberg_schema.orders RENAME COLUMN status TO order_status;

-- Widen a column type (int → bigint, float → double, decimal precision increase)
ALTER TABLE iceberg_schema.orders ALTER COLUMN order_id TYPE BIGINT;
```

### Partition evolution
<a name="partition-evolution"></a>

For full syntax, see [ALTER TABLE ADD, DROP, and REPLACE PARTITION FIELD](https://docs.aws.amazon.com/redshift/latest/dg/iceberg-alter-table.html#iceberg-alter-table-partition-field).

```
-- Change partition granularity
ALTER TABLE iceberg_schema.orders
REPLACE PARTITION FIELD month(order_date) WITH day(order_date);

-- Add a partition field
ALTER TABLE iceberg_schema.orders
ADD PARTITION FIELD bucket(16, customer_id);

-- Drop a partition field
ALTER TABLE iceberg_schema.orders
DROP PARTITION FIELD bucket(16, customer_id);
```

## Working with Iceberg V3
<a name="working-with-iceberg-v3"></a>

Iceberg format version 3 (V3) introduces capabilities on top of V2. Amazon Redshift supports V3 for **deletion vectors, row lineage, and default column values**; it does not yet support `variant`, `geometry`/`geography`, `uuid`, `time`, `binary`, complex types (struct/list/map) or nanosecond timestamps (see [V3 feature support in Amazon Redshift](#v3-feature-support-in-amazon-redshift) at the top of this section). Most of the SQL shown earlier applies unchanged to V3 tables — only the `TABLE PROPERTIES ('format-version'='3')` clause on `CREATE TABLE` changes what the writer emits. The V3-specific patterns worth calling out separately are: **creating** a V3 table with `DEFAULT` columns, **upgrading** an existing V2 table to V3 in place, and **querying** the V3 row-lineage columns.

**Note**
 Before you create a V3 table with the examples below — or run the `ALTER TABLE … SET TABLE PROPERTIES ('format-version' = '3')` upgrade in [Upgrading a V2 table to V3](#upgrading-a-v2-table-to-v3) — verify that every downstream engine that reads or writes the table also supports V3. Notable current gap: [Amazon Athena](working-with-iceberg-tables-by-using-athena-sql-queries.md) does **not** support V3. Upgrading from V2 to V3 is one-way, so plan the upgrade against your least-capable consumer. For the authoritative service-by-service matrix, see [Working with Iceberg table format specification version 3](table-spec-v3.md).

### Creating a V3 table
<a name="creating-a-v3-table"></a>

V3 lets you specify **default column values** with the `DEFAULT` clause (literal values only; not supported on V2). The following examples create a partitioned V3 table with two `DEFAULT` columns.

**Self-managed Iceberg on Amazon S3** - Replace `<bucket-name>` with your own bucket name:

```
CREATE TABLE my_iceberg.orders_v3 (
    order_id     BIGINT,
    customer_id  VARCHAR,
    status       VARCHAR DEFAULT 'pending',
    priority     INT     DEFAULT 0,
    order_ts     TIMESTAMP
)
USING ICEBERG
LOCATION 's3://<bucket-name>/orders_v3/'
PARTITIONED BY (day(order_ts))
TABLE PROPERTIES ('format-version'='3');
```

**Amazon S3 Tables** - Replace `<table-bucket-name>` with your own table bucket name:

```
CREATE TABLE "<table-bucket-name>@s3tablescatalog".sales.orders_v3 (
    order_id     BIGINT,
    customer_id  VARCHAR,
    status       VARCHAR DEFAULT 'pending',
    priority     INT     DEFAULT 0,
    order_ts     TIMESTAMP
)
USING ICEBERG
PARTITIONED BY (day(order_ts))
TABLE PROPERTIES ('format-version'='3');
```

### Upgrading a V2 table to V3
<a name="upgrading-a-v2-table-to-v3"></a>

Upgrade an existing V2 table to V3 with `ALTER TABLE`. The upgrade itself is **lightweight** — it commits a single new metadata JSON file that flips the `format-version` property and leaves every existing data file, manifest, and manifest list untouched. For more details and caveats about upgrading Iceberg V2 tables to V3 on Amazon Redshift see [Iceberg V3 upgrades on Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/iceberg-v3-features.html#iceberg-v3-upgrading)

```
ALTER TABLE iceberg_table
SET TABLE PROPERTIES ('format-version' = '3');
```

The first write after the upgrade starts populating row lineage; files not yet rewritten carry it only after a later write or compaction touches them. On subsequent `DELETE`, `UPDATE`, or `MERGE` operations, Amazon Redshift merges V2 positional deletes into deletion vectors for the data files affected by the operation.

The upgrade is also **one-way** — there is no `format-version = 2` downgrade path once a V3 snapshot has been committed. If you still query the table from an engine that does not yet support V3 (for example, [Amazon Athena](working-with-iceberg-tables-by-using-athena-sql-queries.md)), keep the table at V2 until that engine catches up.

### Querying row lineage
<a name="querying-row-lineage"></a>

Iceberg V3 tables carry two hidden metadata columns that record row-level provenance: `_row_id` (a stable identifier assigned to each row when it is first written) and `_last_updated_sequence_number` (the sequence number of the commit that most recently modified the row). These columns are not shown by `SELECT *` — reference them by name to include them in the result set. Row lineage is populated automatically on any V3 table (whether created as V3 or upgraded from V2 — see [Upgrading a V2 table to V3](#upgrading-a-v2-table-to-v3)), and downstream consumers can use these columns to build incremental change-data-capture (CDC) pipelines without extra bookkeeping tables:

```
SELECT _row_id, _last_updated_sequence_number, *
FROM my_schema.my_iceberg_v3_table;
```

## Considerations and limitations
<a name="considerations-and-limitations"></a>

For the current list of considerations and limitations when using Amazon Redshift with Iceberg tables, see [Considerations when using Apache Iceberg tables with Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/querying-iceberg.html#querying-iceberg-considerations),[Amazon Redshift Iceberg V3 limitations](https://docs.aws.amazon.com/redshift/latest/dg/iceberg-v3-features.html#iceberg-v3-limitations) and [Iceberg Writes transaction semantics](https://docs.aws.amazon.com/redshift/latest/dg/iceberg-writes-transaction-semantics.html) in the AWS documentation. For best practices on using Apache Iceberg with Amazon Redshift see [Referencing Iceberg best practices.](https://docs.aws.amazon.com/redshift/latest/dg/referencing-iceberg-tables.html#referencing-iceberg-best-practices)

The main write-path limitations to be aware of up front are:
+ **No Iceberg write statements inside stored procedures.** `INSERT`, `UPDATE`, `DELETE`, and `MERGE` against Iceberg tables cannot run inside a stored procedure. Issue them from a client session or a scheduled query instead.
+ `MERGE`** requires **`s3:DeleteObject`** on general-purpose Amazon S3 buckets.** Amazon Redshift writes intermediate data files in the target table location while a `MERGE` runs and garbage-collects them at the end. If the Redshift role cannot delete objects in the bucket, the garbage-collection step fails and the query returns an insufficient-permissions error. This does not apply to Amazon S3 Tables, where garbage collection is handled by the S3 Tables service.
+ **One Iceberg write target per multi-statement transaction.** A transaction that writes to an Iceberg table can read from any table, but it can only write to one Iceberg table. Writes to a second Iceberg table, writes to a Redshift managed storage (RMS) table in the same transaction, `COPY`, `UNLOAD`, `GRANT`, `REVOKE`, `ANALYZE`, and any DDL are not allowed inside the transaction and will cause it to abort.
+ **No Iceberg DDL inside a transaction.** `CREATE TABLE`, `CREATE TABLE AS`, `ALTER TABLE`, `CREATE MATERIALIZED VIEW`, `DROP TABLE`, and `DROP MATERIALIZED VIEW` on Iceberg tables must run as standalone statements outside a transaction block.
+ **Writing to Iceberg tables not created by Amazon Redshift** is supported only when the table is Iceberg v2 or v3, uses Parquet as its default data format, does not have metadata compression enabled, and does not use the Write-Audit-Publish (WAP) workflow.
+ **Orphan files from aborted transactions.** If a multi-statement Iceberg transaction fails or rolls back, the data and metadata files written during the transaction become orphan files. Enable orphan file removal on the table so they get cleaned up.
