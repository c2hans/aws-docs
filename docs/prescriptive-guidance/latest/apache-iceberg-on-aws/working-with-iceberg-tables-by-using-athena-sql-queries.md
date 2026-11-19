---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/working-with-iceberg-tables-by-using-athena-sql-queries.html
---

# Working with Iceberg tables by using Athena SQL queries

[Amazon Athena](https://aws.amazon.com/athena/) provides built-in support for Apache Iceberg. You can query Iceberg tables that are **self-managed** on Amazon S3 (through the AWS Glue Data Catalog) or **hosted in Amazon S3 Tables** (through the `s3tablescatalog federated catalog) without additional configuration beyond the service prerequisites in the `[Getting started](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html) section of the Athena documentation. This section covers supported features, catalog selection, and end-to-end examples for creating, loading, updating, and querying tables in both storage options.

## Iceberg format version support in Athena
<a name="iceberg-format-version-support-in-athena"></a>

The following table summarizes which Iceberg format versions Athena supports for each storage option.

|
|
| **Iceberg format version** | **Self-managed Iceberg on S3** | **Amazon S3 Tables** |
| --- |--- |--- |
| Version 2 (V2) | Yes | Yes |
| Version 3 (V3) | No | No |

**Notes**:
+ Athena creates new Iceberg tables in format version 2 through the console, CLI, or SDK. Athena does not support **reading or writing** V3 tables, and it does not support any of the V3-specific features (deletion vectors, row lineage, `variant`, `geometry`/`geography`, nanosecond timestamps, default column values).
+ If you plan to query the table from Athena but create it with another engine (Apache Spark on Amazon EMR or AWS Glue), make sure the writer sets the `format-version`[ table property](https://iceberg.apache.org/docs/latest/configuration/#reserved-table-properties) to `2`.
+ Upgrading a table from V2 to V3 is a **one-way** operation. Be careful before upgrading a table that you still query from Athena — after the upgrade the table won't be queryable with Athena. Keep the table in V2 for as long as Athena is a required consumer.

## Iceberg feature support
<a name="iceberg-feature-support"></a>

The following table summarizes Iceberg feature support in Athena SQL, grouped by capability area. Behavior is the same on both hosting options (self-managed Iceberg on Amazon S3 and Amazon S3 Tables) unless a row calls out a difference.

|
|
| **Category** | **Feature** | **Supported** |
| --- |--- |--- |
| **DDL** | `CREATE TABLE` |  |
|  | `CREATE TABLE AS SELECT` (CTAS) |  |
|  | `DROP TABLE` |  (removes the Data Catalog registration **and** deletes the underlying data files — Iceberg tables are treated as managed tables in Athena) |
|  | `SHOW TABLES` |  |
|  | `ALTER TABLE CHANGE COLUMN` (schema evolution - rename column, type promotion, column ordering) |  |
|  | `ALTER TABLE ADD` / `DROP COLUMNS` (schema evolution) |  |
|  | `ALTER TABLE SET TBLPROPERTIES` |  |
|  | `ALTER TABLE ADD` / `DROP` / `REPLACE PARTITION FIELD` (partition evolution) | ✗ |
| **DML** | `INSERT INTO` |  |
|  | `UPDATE` |  merge-on-read only (writes positional deletes on V2; copy-on-write is not supported and CoW table properties are silently ignored) |
|  | `DELETE FROM` |  merge-on-read only (writes positional deletes on V2) |
|  | `MERGE INTO` (upsert) |  merge-on-read only (writes positional deletes on V2) |
|  | Writes honor Iceberg table sort order | ✗ (Athena SQL does not apply the Iceberg `sort_order` table property during `INSERT` / `UPDATE` / `MERGE` writes) |
| **Read** | Query Iceberg tables |  — V2: reads positional deletes , equality deletes . V3 is not supported for reading or writing in Athena |
|  | Time travel queries |  (`FOR TIMESTAMP AS OF <ts>`, `FOR VERSION AS OF <snapshot_id>`) |
|  | Incremental queries | ✗ |
|  | Access Iceberg metadata tables (`$snapshots`, `$files`, `$partitions`, `$manifests`, ...) |  (query with `SELECT ... FROM "<db>"."<table>$<metadata_table>"`) |
| **Materialized views** | [AWS Glue Iceberg materialized view](apache-iceberg-materialized-views-in-aws-glue-data-catalog.md) |  (query only) |
| **Partitioning** | Hidden partitioning (V2 partition transforms) |  |
|  | Partition evolution | ✗ (`ALTER TABLE ... ADD` / `DROP` / `REPLACE PARTITION FIELD` is not available in Athena SQL) |
|  | Metadata-only partition `DELETE` |  (when the `WHERE` clause aligns with the partition spec) |
| **Security** | AWS Lake Formation full-table access control |  |
|  | AWS Lake Formation row/column access control |  (row and column filters on Iceberg tables governed by the AWS Glue Data Catalog \+ Lake Formation) |
| **Maintenance** | Compaction (`OPTIMIZE ... REWRITE DATA USING BIN_PACK`) | Self-managed Iceberg: (binpack strategy only)<br />S3 Tables: ✗ |
|  | Snapshot expiration (`VACUUM`) | Self-managed Iceberg: (combined with orphan file removal in a single statement) S3 Tables: ✗ |
|  | Orphan file cleanup (`VACUUM`) | Self-managed Iceberg: (combined with snapshot expiration in a single statement) <br />S3 Tables: ✗ |
|  | Sort order / Z-order compaction | ✗ |
|  | Rollbacks | ✗ |
| **Format** | Data files supported | Parquet , Avro , ORC  |
|  | Data-file compression: `snappy`, `zstd`, `gzip`, `brotli`, uncompressed |  (defaults to `zstd` on Athena engine v3) |

**Notes**:
+ All DDL operations supported for Iceberg tables are supported for S3 Tables with the following exceptions:
  + `ALTER TABLE RENAME`, `CREATE VIEW`, and `ALTER DATABASE` are not supported.
  + `OPTIMIZE` and `VACUUM` – You can manage compaction and snapshot management in S3. For more information, see [S3 Tables maintenance documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance.html).
+ DDL queries on S3 Tables registered as Athena data sources are not supported.
+ In workgroups with SSE-KMS, CSE-KMS encryption enabled, you can't run write operations like `INSERT`, `UPDATE`, `DELETE`, or `MERGE` on S3 Tables.
+ In workgroups with S3 Requester Pays option enabled, you can't run DML operations on S3 Tables.

## Catalog configuration in Athena
<a name="catalog-configuration-in-athena"></a>

The main setup difference between the two storage options is which catalog Athena queries against. The DDL and DML syntax is the same in either case – only the catalog qualifier changes.

### Self-managed Iceberg on S3
<a name="self-managed-iceberg-on-s3"></a>

Athena reads self-managed Iceberg tables through the AWS Glue Data Catalog, which appears in the Athena query editor as `AwsDataCatalog`. This is the default catalog, so no extra configuration is required.

Query examples:

```
-- Using the default catalog (AwsDataCatalog)
SELECT * FROM mydb.products;

-- Fully qualified (catalog.database.table)
SELECT * FROM "AwsDataCatalog"."mydb"."products";
```

### Amazon S3 Tables
<a name="amazon-s3-tables"></a>

To query S3 Tables from Athena, first enable the integration between your S3 table buckets and AWS analytics services. This registers each table bucket as a federated catalog in the AWS Glue Data Catalog under the name `s3tablescatalog/<table-bucket-name>`. See [Getting started with Amazon S3 Tables](getting-started-with-amazon-s3-tables.md) for setup steps.

After the integration is enabled, choose the S3 Tables catalog in the Athena query editor **Data source** dropdown (for example `s3tablescatalog/<table-bucket-name>`), or use three-part naming to query it from anywhere (replace `<table-bucket-name>` with your own table bucket name):

```
-- Three-part naming: catalog.namespace.table
SELECT * FROM "s3tablescatalog/<table-bucket-name>"."sales"."orders";

-- Join across storage options in a single query
SELECT o.order_id, c.customer_name
FROM   "s3tablescatalog/<table-bucket-name>"."sales"."orders" o
JOIN   "AwsDataCatalog"."mydb"."customers" c
  ON   o.customer_id = c.id;
```

### Programmatic access with the Athena API and CLI
<a name="programmatic-access-with-the-athena-api-and-cli"></a>

Both catalogs are addressable through the Athena API and AWS CLI in exactly the same way you address them from the query editor. Submit the SQL as the `--query-string` argument, pick a workgroup, and set an S3 result output location that your caller has write access to.

**Self-managed Iceberg on Amazon S3** (`AwsDataCatalog`) - Replace `<bucket-name>` with your own bucket name):

```
aws athena start-query-execution \
    --query-string 'SELECT * FROM "AwsDataCatalog"."sales"."orders" LIMIT 10' \
    --work-group "primary" \
    --result-configuration OutputLocation=s3://<bucket-name>/athena-query-results/
```

**Amazon S3 Tables** (`s3tablescatalog/<table-bucket-name>`) - Replace `<table-bucket-name>` with your own table bucket name and `<bucket-name>` with your own bucket name:

```
aws athena start-query-execution \
    --query-string 'SELECT * FROM "s3tablescatalog/<table-bucket-name>"."sales"."orders" LIMIT 10' \
    --work-group "primary" \
    --result-configuration OutputLocation=s3://<bucket-name>/athena-query-results/
```

## Creating Iceberg tables
<a name="creating-iceberg-tables"></a>

To create Iceberg tables with Athena SQL, you can use the following boilerplate code. For more information, see the Iceberg syntax detailed in the [Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-creating-tables.html#querying-iceberg-partitioning) (replace `<bucket-name>` with your own bucket name). Replace the placeholders with your own values:
+ `<db_name>` - the target database.
+ `<table_name>` - the Iceberg table to create.
+ `<partition_transform>` - the Iceberg hidden-partition transform applied to `col_ts`, such as `year`, `month`, `day`, `hour`, or `bucket(N, col)`.
+ `<bucket-name>` - the general-purpose Amazon S3 bucket that holds the table's data and metadata (only used in `LOCATION`, for self-managed Iceberg on S3).

```
CREATE TABLE <db_name>.<table_name> (
    col_1 string,
    col_2 string,
    col_3 bigint,
    col_ts timestamp)
PARTITIONED BY (col_1, <partition_transform>(col_ts))
LOCATION 's3://<bucket-name>/<db_name>/<table_name>/'   -- optional; only for self-managed Iceberg on S3. Omit for Amazon S3 Tables.
TBLPROPERTIES (
    'table_type' = 'ICEBERG',                     -- required for self-managed Iceberg only. Optional for Amazon S3 Tables as only support ICEBERG.
    'format' = 'PARQUET',                         -- optional; defaults to PARQUET
    'write_compression' = 'zstd'                  -- optional; defaults to zstd (Athena engine v3)
)
```

**Setting the catalog for **`CREATE TABLE`

Athena's `CREATE TABLE` statement does **not** accept a three-part `catalog.database.table` name in the DDL – you can only use `database.table` (or a bare `table`). The catalog must come from the current query context:
+ In the Athena query editor or Sagemaker Unified Studio Query Editor, pick the **Data source** (catalog) and **Database** from the dropdowns before running the DDL.
+ With `aws athena start-query-execution`, pass `--query-execution-context Catalog=<catalog>,Database=<database>`.

For self-managed Iceberg on S3 backed by AWS Glue, the catalog is `AwsDataCatalog`. For Amazon S3 Tables, the catalog is `s3tablescatalog/<table-bucket-name>` (this contains a slash, so quote it on the CLI).

Example — create the Iceberg table in a table bucket via the CLI - Replace `<table-bucket-name>` with your own table bucket name and `<bucket-name>` with your own bucket name:

```
aws athena start-query-execution \
  --query-string "CREATE TABLE my_namespace.my_table (
      col_1 string,
      col_2 string,
      col_3 bigint,
      col_ts timestamp)
    PARTITIONED BY (col_1, day(col_ts))" \
  --query-execution-context Catalog="s3tablescatalog/<table-bucket-name>",Database=my_namespace \
  --work-group primary \
  --result-configuration OutputLocation=s3://<bucket-name>/athena-query-results/
```

For the other data-plane statements — `INSERT`, `UPDATE`, `MERGE INTO`, `DELETE`, `SELECT`, `SHOW`, `DESCRIBE`, and the `SELECT` clause of CTAS — Athena **does** accept the full three-part `"catalog"."database"."table"` form. Later examples on this page use that shape to reference S3 Tables without changing the query context.

The following sections show how to customize this boilerplate for nonpartitioned tables, partitioned tables, and CTAS statements — with side-by-side examples for self-managed Iceberg on Amazon S3 and Amazon S3 Tables.

### Creating a nonpartitioned table
<a name="creating-a-nonpartitioned-table"></a>

**Self-managed Iceberg on Amazon S3** (default `AwsDataCatalog`) - Replace `<bucket-name>` with your own bucket name):

```
CREATE TABLE athena_iceberg_table (
    color string,
    date string,
    name string,
    price bigint,
    product string,
    ts timestamp)
LOCATION 's3://<bucket-name>/ice_warehouse/iceberg_db/athena_iceberg_table/'
TBLPROPERTIES (
    'table_type' ='ICEBERG'
)
```

**Amazon S3 Tables** (set the query context to catalog `s3tablescatalog/<table-bucket-name>`, database `iceberg_db`):

```
CREATE TABLE iceberg_db.athena_iceberg_table (
    color string,
    date string,
    name string,
    price bigint,
    product string,
    ts timestamp)
```

For S3 Tables, you don't specify `LOCATION` (the table bucket manages storage) and you don't need `TBLPROPERTIES ('table_type'='ICEBERG')` (all tables in a table bucket are Iceberg by definition). The S3 Tables catalog is selected through the query context (query editor dropdown or `--query-execution-context Catalog=...`) – it can't appear as a prefix in the `CREATE TABLE` name.

### Creating a partitioned table
<a name="creating-a-partitioned-table"></a>

The following statement creates a partitioned table based on the date by using Iceberg's concept of [hidden partitioning](https://iceberg.apache.org/docs/latest/partitioning/#icebergs-hidden-partitioning). It uses the `day()` transform to derive daily partitions from a timestamp column. Iceberg doesn't store this value as a new column in the dataset; the value is derived on the fly when you write or query data.

**Self-managed Iceberg on Amazon S3**- Replace `<bucket-name>` with your own bucket name):

```
CREATE TABLE athena_iceberg_table_partitioned (
    color string,
    date string,
    name string,
    price bigint,
    product string,
    ts timestamp)
PARTITIONED BY (day(ts))
LOCATION 's3://<bucket-name>/ice_warehouse/iceberg_db/athena_iceberg_table/'
TBLPROPERTIES (
    'table_type' = 'ICEBERG'
)
```

**Amazon S3 Tables** (query context set to the S3 Tables catalog \+ database; omit `LOCATION` and `TBLPROPERTIES` not needed if using defaults):

```
CREATE TABLE iceberg_db.athena_iceberg_table_partitioned (
    color string,
    date string,
    name string,
    price bigint,
    product string,
    ts timestamp)
PARTITIONED BY (day(ts))
```

### Creating a table and loading data with a single CTAS statement
<a name="creating-a-table-and-loading-data-with-a-single-ctas-statement"></a>

In the partitioned and nonpartitioned examples above, the Iceberg tables are created empty. You can load data into them by using the `INSERT` or `MERGE` statement. Alternatively, you can use a `CREATE TABLE AS SELECT (CTAS)` statement to create and load data into an Iceberg table in a single step.

CTAS is the best way in Athena to create a table and load data in a single statement. The following example illustrates how to use CTAS to create a partitioned Iceberg table (`iceberg_ctas_table`) – partitioned by day derived from a `transaction_time` column – from an existing Hive/Parquet source table (`hive_table`). Partitions on the target Iceberg table are declared through the `partitioning` table property using Iceberg [partition transforms](https://iceberg.apache.org/docs/latest/partitioning/#icebergs-hidden-partitioning).

Because CTAS is a DDL statement, the same catalog rules as `CREATE TABLE` apply: the target uses only `database.table` (or a bare `table`), and the destination catalog \+ database must come from the query context – the query editor **Data source** / **Database** dropdowns, or `--query-execution-context Catalog=<catalog>,Database=<database>` on `aws athena start-query-execution`.

**Self-managed Iceberg on Amazon S3** - Replace `<bucket-name>` with your own bucket name):

```
CREATE TABLE iceberg_ctas_table WITH (
  table_type = 'ICEBERG',
  is_external = false,
  location = 's3://<bucket-name>/ice_warehouse/iceberg_db/iceberg_ctas_table/',
  partitioning = ARRAY['day(transaction_time)']
) AS
SELECT * FROM "iceberg_db"."hive_table"
```

**Amazon S3 Tables** (CTAS into a table bucket – set the query context to the S3 Tables catalog \+ destination database, then omit `location`, `table_type`, and `is_external`; the `SELECT` clause can still reach any other catalog by its three-part name):

```
CREATE TABLE iceberg_ctas_table WITH (
  partitioning = ARRAY['day(transaction_time)']
) AS
SELECT * FROM "AwsDataCatalog"."iceberg_db"."hive_table"
```

CTAS is also the recommended path for migrating existing Hive or Parquet tables into a table bucket, because S3 Tables requires Iceberg format and rewrites the source data as it copies it. See [Migrating existing tables to Iceberg](table-migration.md).

To learn more about CTAS, see the [Athena CTAS documentation](https://docs.aws.amazon.com/athena/latest/ug/ctas.html).

## Inserting, updating, and deleting data
<a name="inserting-updating-and-deleting-data"></a>

Athena supports data changes on Iceberg tables through `INSERT INTO`, `UPDATE`, `MERGE INTO`, and `DELETE FROM` statements. Unlike `CREATE TABLE`, these data-plane statements accept both two-part `<database>.<table>` (when the query context is set to the target catalog) and three-part `"<catalog>"."<database>"."<table>"` names. Substitute `<catalog>` with one of:
+ `AwsDataCatalog` – self-managed Iceberg tables governed by the AWS Glue Data Catalog.
+ `s3tablescatalog/<table-bucket-name>` – tables stored in an Amazon S3 Tables bucket.

**Note**
 Athena SQL always uses merge-on-read with positional deletes for `UPDATE`, `MERGE INTO`, and `DELETE FROM` – copy-on-write is not supported. Table properties `write.update.mode`, `write.merge.mode`, and `write.delete.mode` set to `copy-on-write` are silently ignored: the query does not fail, but Athena continues to use merge-on-read.

### INSERT INTO
<a name="insert-into"></a>

The following statement inserts a row using the three-part name form:

```
INSERT INTO "<catalog>"."iceberg_db"."ice_table" VALUES (
    'red', '2022-07-19T03:47:29', 'PersonNew', 178, 'Tuna', now()
)
```

### UPDATE
<a name="update"></a>

Update columns on rows that match a predicate. The following example uses the two-part `database.table` form (assumes the query context is `AwsDataCatalog`):

```
UPDATE "<catalog>".athena_iceberg_db.customer_iceberg
SET c_last_name = 'Doe',
    c_email_address = 'johnTonya@example.com'
WHERE c_customer_sk = 15
```

### DELETE
<a name="delete"></a>

Delete rows that match a predicate:

```
DELETE FROM "<catalog>".athena_iceberg_db.customer_iceberg
WHERE c_customer_sk = 15
```

### MERGE INTO
<a name="merge-into"></a>

`MERGE INTO` applies a change set from a source table (`s`) to a target Iceberg table (`t`) in a single statement. The following example implements insert / update / delete based on an `operation` marker column in the source:

```
MERGE INTO "<catalog>".athena_iceberg_db.web_sales_iceberg t
USING "<catalog>".athena_iceberg_db.merge_table s
    ON t.ws_order_number = s.ws_order_number
   AND t.ws_item_sk     = s.ws_item_sk
WHEN MATCHED AND s.operation = 'D' THEN DELETE
WHEN MATCHED AND s.operation = 'U' THEN UPDATE SET
    ws_order_number  = s.ws_order_number,
    ws_item_sk       = s.ws_item_sk,
    ws_quantity      = s.ws_quantity,
    ws_sales_price   = s.ws_sales_price,
    ws_warehouse_sk  = s.ws_warehouse_sk,
    ws_sales_time    = s.ws_sales_time
WHEN NOT MATCHED THEN INSERT (
    ws_order_number, ws_item_sk, ws_quantity, ws_sales_price, ws_warehouse_sk, ws_sales_time
) VALUES (
    s.ws_order_number, s.ws_item_sk, s.ws_quantity, s.ws_sales_price, s.ws_warehouse_sk, s.ws_sales_time
)
```

For more information, see the [Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-updating-iceberg-table-data.html).

## Evolving tables
<a name="evolving-tables"></a>

Iceberg supports in-place schema and partition evolution – metadata-only changes that never rewrite existing data files. Athena SQL exposes **schema evolution** through `ALTER TABLE`; **partition evolution** is not currently supported in Athena SQL (see the [Iceberg feature support](#iceberg-feature-support) table above).

### Schema evolution
<a name="schema-evolution"></a>

For full syntax, see [Evolve Iceberg table schema](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-evolving-table-schema.html).

```
-- Add a column (note: ADD COLUMNS is plural in Athena)
ALTER TABLE iceberg_db.orders ADD COLUMNS (shipping_address string);

-- Drop a column
ALTER TABLE iceberg_db.orders DROP COLUMN shipping_address;

-- Rename a column (order_id → new_order_id - original column type specified)
ALTER TABLE iceberg_db.orders CHANGE COLUMN order_id new_order_id int;

-- Widen a column type (int → bigint, float → double, decimal precision increase) and rename
ALTER TABLE iceberg_db.orders CHANGE COLUMN order_id order_id bigint;
```

Athena does not support `ALTER TABLE REPLACE COLUMNS` on Iceberg tables – use `CHANGE COLUMN` instead (see the [Athena CHANGE COLUMN docs](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-alter-table-change-column.html)).

### Partition evolution
<a name="partition-evolution"></a>

Athena SQL does not currently support Iceberg partition evolution – the `ALTER TABLE ... ADD` / `DROP` / `REPLACE PARTITION FIELD` statements are not available. Once a table's partition spec has been evolved outside of Athena, Athena reads the resulting table back normally (both the historical and the new partition spec are honored by the Iceberg reader).

## Querying Iceberg tables with time travel
<a name="querying-iceberg-tables-with-time-travel"></a>

Athena supports **time travel** queries. Because Iceberg keeps each write as a new snapshot, you can look back into older versions of a table in two ways – by **snapshot ID** (deterministic, references an exact write) or by **timestamp** (Athena resolves it to the snapshot that was current at that instant). Snapshot IDs are visible in the `$snapshots`[ metadata table](#querying-iceberg-metadata-tables).

Substitute `<catalog>` with `AwsDataCatalog` for self-managed Iceberg tables or with `s3tablescatalog/<table-bucket-name>` for Amazon S3 Tables (or omit the catalog qualifier entirely when the query context already points at the right catalog).

**Time travel by snapshot ID** (`FOR VERSION AS OF`):

```
SELECT * FROM <catalog>.athena_iceberg_db.customer_iceberg
FOR VERSION AS OF 5418594889737463157
WHERE c_customer_sk = 15
```

**Time travel by timestamp** (`FOR TIMESTAMP AS OF`):

```
SELECT * FROM <catalog>.athena_iceberg_db.customer_iceberg
FOR TIMESTAMP AS OF TIMESTAMP '2024-04-16 17:21:49.771 UTC'
WHERE c_customer_sk = 15
```

For syntax and additional examples of time travel queries, see the [Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-table-data.html#querying-iceberg-time-travel-and-version-travel-queries).

## Querying Iceberg metadata tables
<a name="querying-iceberg-metadata-tables"></a>

Iceberg exposes each table's operational metadata through a set of virtual **metadata tables** that you can query from Athena with standard `SELECT` statements. The syntax is `"<database>"."<table>$<metadata_table>"`. Athena supports the following metadata tables:

|
|
| **Metadata table** | **What it shows** |
| --- |--- |
| `$snapshots` | One row per snapshot, with commit timestamp, snapshot ID, parent snapshot ID, and per-operation summary counters (added/deleted files, records, and so on) |
| `$history` | One row per snapshot in the table's history, including which snapshots are ancestors of the current one – useful for auditing writes and rollbacks |
| `$files` | One row per **data file** currently referenced by the table, with path, partition values, record count, and column-level lower/upper bounds. **Note:** `$files` in Athena does not surface delete files (positional deletes, equality deletes) |
| `$partitions` | Aggregated per-partition statistics – record count, total file size, and file count for each partition |
| `$manifests` | One row per manifest file – location, snapshot it belongs to, and how many data files it references |
| `$refs` | One row per named reference (branch or tag), with the referenced snapshot ID and retention properties – useful for auditing branches and tag policies |

Metadata queries are useful for troubleshooting layout issues, sizing compaction runs, deciding when to expire snapshots, and auditing writers.

### Example — query the $snapshots metadata table
<a name="example-query-the-object-object-metadata-table"></a>

The following query returns the ten most recent snapshots of the `orders` table, along with the operation type and a compact view of the summary counters. Substitute `<catalog>` with `AwsDataCatalog` for self-managed Iceberg tables or with `s3tablescatalog/<table-bucket-name>` for Amazon S3 Tables:

```
SELECT
    committed_at,
    snapshot_id,
    parent_id,
    operation,
    summary['added-data-files']    AS added_data_files,
    summary['added-records']       AS added_records,
    summary['deleted-data-files']  AS deleted_data_files
FROM <catalog>."sales"."orders$snapshots"
ORDER BY committed_at DESC
LIMIT 10;
```

Combining `$snapshots` with time travel is a common pattern – take a `snapshot_id` from `$snapshots`, then use it in a `FOR VERSION AS OF <snapshot_id>` clause to query the table's state at that point in history.
