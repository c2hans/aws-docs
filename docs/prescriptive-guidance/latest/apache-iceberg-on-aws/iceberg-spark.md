---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/iceberg-spark.html
---

# Working with Iceberg tables by using Apache Spark

[Apache Spark](https://spark.apache.org/) is a distributed processing engine for large-scale data engineering, data science, and machine learning workloads, and the engine with the broadest Iceberg feature support. From Spark you can read from and write to Iceberg tables that are either self-managed on Amazon S3 or **hosted in Amazon S3 Tables** — the transformation code is the same, only the Spark session catalog configuration differs.

The Spark SQL and DataFrame code that operates on Iceberg tables is engine-agnostic — it looks the same whether you run it on **Amazon EMR (Spark)**, **AWS Glue Spark jobs**, or **open-source Apache Spark** on your own infrastructure. To avoid duplication across the [Amazon EMR](working-with-iceberg-in-amazon-emr-spark.md) and [AWS Glue](iceberg-glue.md) chapters, all of the Spark SQL and DataFrame examples for Iceberg live in this section. The Amazon EMR and AWS Glue chapters focus on the runtime-specific setup (cluster configuration, job parameters, Spark session catalog registration) and link here for the day-to-day read/write, upsert, time travel, and metadata code.

This section covers how to configure open-source Apache Spark to reach AWS-managed Iceberg catalogs, Iceberg format-version support and V3 feature availability across Amazon EMR / AWS Glue / open-source Apache Spark, the Iceberg feature-support matrix (DDL, DML, reads, security, maintenance, format), and end-to-end Spark SQL and DataFrame examples for creating, writing, reading, updating, upserting, deleting, time travel, incremental queries, and metadata tables.

**Note**
 The primary interface for interacting with Iceberg tables is SQL, so most of the examples combine Spark SQL with the DataFrames API. In the examples that follow, `{CATALOG_NAME}` is a placeholder for whichever catalog you registered — `spark.sql("SELECT * FROM my_iceberg_catalog.sales.orders")` and `spark.sql("SELECT * FROM s3_tables_catalog.sales.orders")` are equivalent from the Spark API's perspective; only the catalog name changes. Similarly, `{DB_NAME}` refers to a Glue database when using self-managed Iceberg, and to a namespace inside the table bucket when using S3 Tables.

**Where to configure the Spark catalog before running the examples in this section:**
+ **Amazon EMR (Spark)** → [Catalog configuration for Iceberg on Amazon EMR Spark](working-with-iceberg-in-amazon-emr-spark.md).
+ **AWS Glue** → [Spark configurations for Iceberg in AWS Glue](iceberg-glue.md).
+ **Open-source Apache Spark** → [Open-source Apache Spark setup](#open-source-apache-spark-setup) later in this section.

## Iceberg format version support in Apache Spark
<a name="iceberg-format-version-support-in-apache-spark"></a>

Apache Spark supports both Iceberg format version 2 and format version 3 through the Iceberg Spark runtime. The specific Iceberg release depends on the AWS runtime you use (Amazon EMR / AWS Glue) or the Iceberg-Spark runtime JAR you attach yourself for open-source Spark. The Version 3 row below reflects the runtimes required for **full V3 support** (row lineage, deletion vectors, default column values, nanosecond timestamps, geography and geometry types, and `variant` with shredding).

|
|
| **Format version** | **Amazon EMR** | **AWS Glue** | **Open-source Apache Spark** |
| --- |--- |--- |--- |
| Version 2 (V2) | Amazon EMR 6.5.0\+ (Iceberg 0.12.0\+) | AWS Glue 3.0\+ (Iceberg 0.13.1\+) | Apache Spark 3.3\+ with `iceberg-spark-runtime-3.3_2.13` 1.4.0\+ |
| Version 3 (V3) | Amazon EMR 8.1.0\+ (Iceberg 1.11.0\+) - for full V3 support | AWS Glue 6.0\+ (Iceberg 1.11.0) - for full V3 support | Apache Spark 4.1\+ with `iceberg-spark-runtime-4.1_2.13` 1.11.0\+ - for full V3 support |

When you create an Iceberg table with Spark without setting the `format-version` table property, Spark applies the [Iceberg default of V2](https://iceberg.apache.org/docs/latest/configuration/#table-behavior-properties). Add `TBLPROPERTIES ('format-version'='3')` on `CREATE TABLE` (or `ALTER TABLE ... SET TBLPROPERTIES ('format-version'='3')` on an existing table) to opt into V3. For per-runtime details, see [Iceberg format version support in Amazon EMR](working-with-iceberg-in-amazon-emr-spark.md) and [Iceberg format version support in AWS Glue](iceberg-glue.md).

### V3 feature support in Apache Spark
<a name="v3-feature-support-in-apache-spark"></a>

Iceberg V3 introduces several new capabilities on top of V2. The following table shows the **minimum runtime version at which each feature first became supported** across Amazon EMR, AWS Glue, and open-source Apache Spark.

|
|
| **V3 feature** | **Amazon EMR** | **AWS Glue** | **Open-source Apache Spark** |
| --- |--- |--- |--- |
| Row lineage | Yes (EMR 7.12.0\+) | Yes (Glue 5.1\+) | Yes (Spark 3.5\+ with Iceberg 1.10.0\+) |
| Deletion vectors | Yes (EMR 7.12.0\+) | Yes (Glue 5.1\+) | Yes (Spark 3.5\+ with Iceberg 1.10.0\+) |
| Default column values | Yes (Amazon EMR 8.1.0\+) | Yes (AWS Glue 6.0\+) | Yes (Spark 4.1\+ with Iceberg 1.11.0\+) |
| Nanosecond timestamps (`timestamp_ns`, `timestamptz_ns`) | Yes (Amazon EMR 8.1.0\+) | Yes (AWS Glue 6.0\+) | Yes (Spark 4.1\+ with Iceberg 1.11.0\+) |
| Geography type | Yes (Amazon EMR 8.1.0\+) | Yes (AWS Glue 6.0\+) | Yes (Spark 4.1\+ with Iceberg 1.11.0\+) |
| Geometry type | Yes (Amazon EMR 8.1.0\+) | Yes (AWS Glue 6.0\+) | Yes (Spark 4.1\+ with Iceberg 1.11.0\+) |
| Variant type (with shredding) | Yes (Amazon EMR 8.1.0\+) | Yes (AWS Glue 6.0\+) | Yes (Spark 4.1\+ with Iceberg 1.11.0\+) |

For full V3 support, use Amazon EMR 8.1.0\+, AWS Glue 6.0\+, or open-source Apache Spark 4.1\+ with `iceberg-spark-runtime-4.1_2.13` 1.11.0\+ (all on Iceberg 1.11.0\+).

**Note**
 Before you create a V3 Iceberg table with Spark — or upgrade an existing V2 table to V3 — verify that every downstream engine that reads or writes the table also supports V3, and specifically supports the V3 features you plan to use. Notable current gaps: [Amazon Athena](working-with-iceberg-tables-by-using-athena-sql-queries.md) does **not** support V3; [Amazon Redshift](working-with-iceberg-tables-by-using-amazon-redshift.md) supports V3 but only for **deletion vectors, row lineage, and default column values** (Redshift does not yet support `variant`, `geometry`/`geography`, or nanosecond timestamps). For the authoritative service-by-service matrix, see [Working with Iceberg table format specification version 3](table-spec-v3.md).

## Iceberg feature support
<a name="spark-iceberg-feature-support"></a>

The following table summarizes Iceberg feature support in Apache Spark (with the Iceberg Spark runtime) on Amazon EMR and AWS Glue, grouped by capability area. Behavior is the same on both hosting options (self-managed Iceberg on Amazon S3 and Amazon S3 Tables) unless a row calls out a difference.

|
|
| **Category** | **Feature** | **Supported** |
| --- |--- |--- |
| **DDL** | `CREATE TABLE ... USING iceberg` |  |
|  | `CREATE TABLE ... USING iceberg AS SELECT` (CTAS) |  with the AWS Glue Data Catalog. ✗ through the AWS Glue Iceberg REST endpoint (rejects `stageCreate`). Workaround for the AWS Glue Iceberg REST endpoint: `CREATE TABLE <table> (<schema>) WITH (<properties>); then INSERT INTO <table> SELECT ...;`. |
|  | `DROP TABLE` |  (removes the catalog registration only; add `PURGE` — `DROP TABLE <t> PURGE` — to also delete the underlying data files) |
|  | `SHOW TABLES` |  |
|  | `ALTER TABLE RENAME COLUMN` (schema evolution) |  |
|  | `ALTER TABLE ADD` / `DROP COLUMN` (schema evolution) |  |
|  | `ALTER TABLE ALTER COLUMN` (schema evolution - type promotion) |  |
|  | `ALTER TABLE SET TBLPROPERTIES` |  |
|  | `ALTER TABLE ADD` / `DROP` / `REPLACE PARTITION FIELD` (partition evolution) |  |
| **DML** | `INSERT INTO` / `INSERT OVERWRITE` |  |
|  | `UPDATE` |  copy-on-write **or** merge-on-read (per-table via the `write.update.mode` table property; default `copy-on-write`. Merge-on-read writes positional deletes on V2 and deletion vectors on V3) |
|  | `DELETE FROM` |  copy-on-write **or** merge-on-read (per-table via the `write.delete.mode` table property; default `copy-on-write`. Merge-on-read writes positional deletes on V2 and deletion vectors on V3) |
|  | `MERGE INTO` (upsert) |  copy-on-write **or** merge-on-read (per-table via the `write.merge.mode` table property; default `copy-on-write`. Merge-on-read writes positional deletes on V2 and deletion vectors on V3) |
|  | Writes honor table sort order (`WRITE ORDERED BY`) |  (Spark applies the sort order during writes; combine with `write.distribution-mode=range` for range-partitioned shuffles) |
| **Read** | Query Iceberg tables |  — V2: reads positional deletes , equality deletes ; V3: reads deletion vectors , equality deletes  |
|  | Time travel queries |  (`VERSION AS OF <id>`, `TIMESTAMP AS OF <ts>`; also branch and tag references) |
|  | Incremental queries |  (via the `start-snapshot-id` / `end-snapshot-id` DataFrame read options — see [Using incremental queries](#using-incremental-queries)) |
|  | Access Iceberg metadata tables (`.snapshots`, `.files`, `.partitions`, `.manifests`, `.history`, `.refs`, ...) |  (query with `SELECT ... FROM <catalog>.<db>.<table>.<metadata_table>`) |
| **Materialized views** | [AWS Glue Iceberg materialized view](apache-iceberg-materialized-views-in-aws-glue-data-catalog.md) |  (create, refresh via `REFRESH MATERIALIZED VIEW`, and query — requires Spark 3.5.6\+: Amazon EMR 7.12.0\+, AWS Glue 5.1\+, or Athena for Spark 3.5) |
| **Partitioning** | Hidden partitioning (all V2 partition transforms) |  |
|  | Partition evolution |  (via `ALTER TABLE ADD` / `DROP` / `REPLACE PARTITION FIELD`) |
|  | Metadata-only partition `DELETE` |  (when the `WHERE` clause aligns with the partition spec) |
| **Security** | AWS Lake Formation full-table access control |  — on [Amazon EMR 7.8.0\+](https://docs.aws.amazon.com/emr/latest/ManagementGuide/lake-formation-unfiltered-ec2-access.html) and [AWS Glue 5.0\+](https://docs.aws.amazon.com/en_en/glue/latest/dg/security-access-control-fta.html) through the Amazon EMR / AWS Glue Lake Formation Full table access integration; on **open-source Apache Spark 3.5\+** (`iceberg-spark-runtime-3.5_2.12` 1.6.1\+, 1.9.1\+ recommended) through the Glue Iceberg REST catalog endpoint (`spark.sql.catalog.<name>.type=rest`, `rest.sigv4-enabled=true`, `rest.signing-name=glue`), which returns credentials vended by Lake Formation. See [Open-source Apache Spark setup (self-managed Iceberg and S3 Tables)](#open-source-apache-spark-setup) below |
|  | AWS Lake Formation row/column access control |  on [Amazon EMR 6.15\+](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-lf-enable.html) and [AWS Glue 5.0\+](https://docs.aws.amazon.com/en_en/glue/latest/dg/security-lf-enable.html) (row and column filters on Iceberg tables governed by the AWS Glue Data Catalog \+ Lake Formation); ✗ on open-source Apache Spark (server-side row/column filtering is enforced only by the AWS-integrated runtimes) |
| **Maintenance** | Compaction (`CALL <catalog>.system.rewrite_data_files`) |  — supports `strategy => 'binpack'` (default) and `strategy => 'sort'`; Z-order is expressed via `strategy => 'sort'` with `sort_order => 'zorder(c1,c2,…)'` |
|  | Snapshot expiration (`CALL <catalog>.system.expire_snapshots`) |  |
|  | Orphan file cleanup (`CALL <catalog>.system.remove_orphan_files`) |  |
|  | Rollbacks (`CALL <catalog>.system.rollback_to_snapshot`, `rollback_to_timestamp`) |  |
| **Format** | Data files supported | Parquet , Avro , ORC  |
|  | Data-file compression: `snappy`, `zstd`, `gzip`, `brotli`, uncompressed |  |

## Open-source Apache Spark setup
<a name="open-source-apache-spark-setup"></a>

Open-source Apache Spark uses the same Iceberg Spark runtime as Amazon EMR and AWS Glue, but you configure the catalog directly on the `pyspark` (or `spark-submit` / `spark-shell`) command line, and you rely on the Iceberg REST catalog with SigV4 signing to reach AWS-managed catalogs. The two examples below target **open-source Apache Spark 3.5.2 with **`iceberg-spark-runtime-3.5_2.12`** 1.9.1** — the minimum runtime combination that supports SigV4-signed REST catalog access to AWS Glue and Amazon S3 Tables. The same pattern works on newer Iceberg-Spark runtimes; for full V3 support, use `iceberg-spark-runtime-4.1_2.13:1.11.0` instead (see [Iceberg format version support in Apache Spark](#iceberg-format-version-support-in-apache-spark)).

### Self-managed Iceberg on Amazon S3 (AWS Glue Iceberg REST endpoint)
<a name="self-managed-iceberg-on-amazon-s3-aws-glue-iceberg-rest-endpoint"></a>

Full-table Lake Formation permissions are enforced by the REST endpoint, which returns short-lived credentials scoped to what the caller is allowed to see. Replace `<AWS_ACCOUNT_ID>` with your AWS Account ID and `<AWS_REGION>` with your current AWS Region:

```
pyspark \
  --packages org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.9.1,software.amazon.awssdk:bundle:2.20.160,software.amazon.awssdk:url-connection-client:2.20.160 \
  --conf "spark.sql.defaultCatalog=mydatacatalog" \
  --conf "spark.sql.catalog.mydatacatalog=org.apache.iceberg.spark.SparkCatalog" \
  --conf "spark.sql.catalog.mydatacatalog.type=rest" \
  --conf "spark.sql.catalog.mydatacatalog.uri=https://glue.<AWS_REGION>.amazonaws.com/iceberg" \
  --conf "spark.sql.catalog.mydatacatalog.warehouse=<AWS_ACCOUNT_ID>" \
  --conf "spark.sql.catalog.mydatacatalog.rest.auth.type=sigv4" \
  --conf "spark.sql.catalog.mydatacatalog.rest.signing-name=glue" \
  --conf "spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"
```

### Amazon S3 Tables (S3 Tables REST endpoint)
<a name="amazon-s3-tables-s3-tables-rest-endpoint"></a>

The `warehouse` is the table-bucket ARN, and requests are signed for the `s3tables` service.:

```
pyspark \
  --packages org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.9.1,software.amazon.awssdk:bundle:2.20.160,software.amazon.awssdk:url-connection-client:2.20.160 \
  --conf "spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions" \
  --conf "spark.sql.defaultCatalog=spark_catalog" \
  --conf "spark.sql.catalog.spark_catalog=org.apache.iceberg.spark.SparkCatalog" \
  --conf "spark.sql.catalog.spark_catalog.type=rest" \
  --conf "spark.sql.catalog.spark_catalog.uri=https://s3tables.<AWS_REGION>.amazonaws.com/iceberg" \
  --conf "spark.sql.catalog.spark_catalog.warehouse=arn:aws:s3tables:<AWS_REGION>:<AWS_ACCOUNT_ID>:bucket/<table-bucket-name>" \
  --conf "spark.sql.catalog.spark_catalog.rest.auth.type=sigv4" \
  --conf "spark.sql.catalog.spark_catalog.rest.signing-name=s3tables" \
  --conf "spark.sql.catalog.spark_catalog.rest.signing-region=<AWS_REGION>" \
  --conf "spark.sql.catalog.spark_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO" \
  --conf "spark.hadoop.fs.s3a.aws.credentials.provider=org.apache.hadoop.fs.s3a.SimpleAWSCredentialProvider" \
  --conf "spark.sql.catalog.spark_catalog.rest-metrics-reporting-enabled=false"
```

Notes:
+ Replace `<AWS_REGION>`, `<AWS_ACCOUNT_ID>`, and `<table-bucket-name>` with your own values.
+ Both examples rely on the standard AWS credential provider chain (environment variables, `~/.aws/credentials`, IAM role, and so on) to obtain the caller identity that the REST endpoint uses to authorize access.
+ For **AWS Lake Formation full-table access control** on open-source Spark, use the self-managed pattern above — the Glue Iceberg REST endpoint returns credentials scoped by Lake Formation. Row-level and column-level Lake Formation filters are **not** enforced on open-source Spark (server-side filtering is only performed by the AWS-integrated Amazon EMR and AWS Glue runtimes); see the [Iceberg feature support](#spark-iceberg-feature-support) table above.

## Creating and writing Iceberg tables
<a name="creating-and-writing-iceberg-tables"></a>

You can use Spark SQL and Spark DataFrames to create and add data to Iceberg tables. The examples in this section create **format-version 2** tables through the `TBLPROPERTIES ('format-version'='2')` clause; the same statements work for **format-version 3** — just replace `'2'` with `'3'`. For V3 features such as default column values, nanosecond timestamps, `GEOMETRY`, `GEOGRAPHY`, `VARIANT`, and row lineage, see [Working with Iceberg V3](#spark-working-with-iceberg-v3) at the end of this section.

### Using Spark SQL
<a name="using-spark-sql"></a>

To write an Iceberg dataset, use standard Spark SQL statements such as `CREATE TABLE` and `INSERT INTO`.

#### Unpartitioned tables
<a name="unpartitioned-tables"></a>

Here's an example of creating an unpartitioned Iceberg table with Spark SQL:

```
spark.sql(f"""
    CREATE TABLE IF NOT EXISTS {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}_nopartitions (
        c_customer_sk             int,
        c_customer_id             string,
        c_first_name              string,
        c_last_name               string,
        c_birth_country           string,
        c_email_address           string)
    USING iceberg
    TBLPROPERTIES ('format-version'='2')
""")
```

To insert data into an unpartitioned table, use a standard `INSERT INTO` statement:

```
spark.sql(f"""
INSERT INTO {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}_nopartitions
SELECT c_customer_sk, c_customer_id, c_first_name, c_last_name, c_birth_country, c_email_address
FROM another_table
""")
```

#### Partitioned tables
<a name="partitioned-tables"></a>

Here's an example of creating a partitioned Iceberg table with Spark SQL:

```
spark.sql(f"""
    CREATE TABLE IF NOT EXISTS {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}_withpartitions (
        c_customer_sk             int,
        c_customer_id             string,
        c_first_name              string,
        c_last_name               string,
        c_birth_country           string,
        c_email_address           string)
    USING iceberg
    PARTITIONED BY (c_birth_country)
    TBLPROPERTIES ('format-version'='2')
""")
```

To insert data into a partitioned Iceberg table with Spark SQL, use a standard `INSERT INTO` statement:

```
spark.sql(f"""
INSERT INTO {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}_withpartitions
SELECT c_customer_sk, c_customer_id, c_first_name, c_last_name, c_birth_country, c_email_address
FROM another_table
""")
```

**Note**
 Starting with Iceberg 1.5.0, `hash` write distribution mode is the default when you insert data into partitioned tables. For more information, see [Writing Distribution Modes](https://iceberg.apache.org/docs/latest/spark-writes/#writing-distribution-modes) in the Iceberg documentation.

### Using the Dataframes API
<a name="using-the-dataframes-api"></a>

To write an Iceberg dataset, you can use the `DataFrameWriterV2` API.

To create an Iceberg table and write data to it, use the `df.writeTo(`t) function. If the table exists, use the `.append()` function. If it doesn't, use `.create().` The following examples use `.createOrReplace()`, which is a variation of `.create()` that's equivalent to `CREATE OR REPLACE TABLE AS SELECT`.

#### Unpartitioned tables
<a name="unpartitioned-tables"></a>

To create and populate an unpartitioned Iceberg table by using the `DataFrameWriterV2` API:

```
input_data.writeTo(f"{CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}_nopartitions") \
    .tableProperty("format-version", "2") \
    .createOrReplace()
```

To insert data into an existing unpartitioned Iceberg table by using the `DataFrameWriterV2` API:

```
input_data.writeTo(f"{CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}_nopartitions") \
    .append()
```

#### Partitioned tables
<a name="partitioned-tables"></a>

To create and populate a partitioned Iceberg table by using the `DataFrameWriterV2` API:

```
input_data.writeTo(f"{CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}_withpartitions") \
    .tableProperty("format-version", "2") \
    .partitionedBy("c_birth_country") \
    .createOrReplace()
```

To insert data into a partitioned Iceberg table by using the `DataFrameWriterV2` API:

```
input_data.writeTo(f"{CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}_withpartitions") \
    .append()
```

## Updating data in Iceberg tables
<a name="updating-data-in-iceberg-tables"></a>

The following example shows how to update data in an Iceberg table. This example modifies all rows that have an even number in the `c_customer_sk` column.

```
spark.sql(f"""
UPDATE {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}
SET c_email_address = 'even_row'
WHERE c_customer_sk % 2 == 0
""")
```

This operation uses the default copy-on-write strategy, so it rewrites all impacted data files.

## Upserting data in Iceberg tables
<a name="upserting-data-in-iceberg-tables"></a>

Upserting data refers to inserting new data records and updating existing data records in a single transaction. To upsert data into an Iceberg table, you use the `SQL MERGE INTO` statement.

The following example upserts the content of the table `{UPSERT_TABLE_NAME`} inside the table `{TABLE_NAME}`:

```
spark.sql(f"""
    MERGE INTO {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME} t
    USING {UPSERT_TABLE_NAME} s
        ON t.c_customer_id = s.c_customer_id
    WHEN MATCHED THEN UPDATE SET t.c_email_address = s.c_email_address
    WHEN NOT MATCHED THEN INSERT *
""")
```
+ If a customer record that's in `{UPSERT_TABLE_NAME}` already exists in `{TABLE_NAME}` with the same `c_customer_id`, the `{UPSERT_TABLE_NAME}` record `c_email_address` value overrides the existing value (update operation).
+ If a customer record that's in `{UPSERT_TABLE_NAME} does not exist in {TABLE_NAME}`, the `{UPSERT_TABLE_NAME}` record is added to `{TABLE_NAME}` (insert operation).

## Deleting data in Iceberg tables
<a name="deleting-data-in-iceberg-tables"></a>

To delete data from an Iceberg table, use the `DELETE FROM` expression and specify a filter that matches the rows to delete.

```
spark.sql(f"""
DELETE FROM {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}
WHERE c_customer_sk % 2 != 0
""")
```

If the filter matches an entire partition, Iceberg performs a metadata-only delete and leaves the data files in place. Otherwise, it rewrites only the affected data files.

The delete method takes the data files that are impacted by the `WHERE` clause and creates a copy of them without the deleted records. It then creates a new table snapshot that points to the new data files. Therefore, the deleted records are still present in the older snapshots of the table. For example, if you retrieve the previous snapshot of the table, you will see the data that you just deleted. For information about removing unneeded old snapshots with the related data files for cleanup purposes, see the section [Maintaining Iceberg Tables](maintaining-iceberg-tables.md) later in this guide.

## Evolving tables
<a name="evolving-tables"></a>

Iceberg supports in-place schema and partition evolution — metadata-only changes that never rewrite existing data files. Spark exposes both through `ALTER TABLE` on the target Iceberg table.

### Schema evolution
<a name="schema-evolution"></a>

For the full syntax, see [Iceberg ALTER TABLE](https://iceberg.apache.org/docs/latest/spark-ddl/#alter-table) in the Apache Iceberg documentation.

```
-- Add a column
spark.sql(f"""
ALTER TABLE {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}
ADD COLUMN shipping_address STRING
""")

-- Drop a column
spark.sql(f"""
ALTER TABLE {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}
DROP COLUMN shipping_address
""")

-- Rename a column
spark.sql(f"""
ALTER TABLE {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}
RENAME COLUMN status TO order_status
""")

-- Widen a column type (int → bigint, float → double, decimal precision increase)
spark.sql(f"""
ALTER TABLE {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}
ALTER COLUMN order_id TYPE BIGINT
""")
```

### Partition evolution
<a name="partition-evolution"></a>

For the full syntax, see [ALTER TABLE ... ADD / DROP / REPLACE PARTITION FIELD](https://iceberg.apache.org/docs/latest/spark-ddl/#alter-table--add-partition-field) in the Apache Iceberg documentation.

```
-- Change partition granularity
spark.sql(f"""
ALTER TABLE {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}
REPLACE PARTITION FIELD months(order_date) WITH days(order_date)
""")

-- Add a partition field
spark.sql(f"""
ALTER TABLE {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}
ADD PARTITION FIELD bucket(16, customer_id)
""")

-- Drop a partition field
spark.sql(f"""
ALTER TABLE {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}
DROP PARTITION FIELD bucket(16, customer_id)
""")
```

## Reading data
<a name="reading-data"></a>

You can read the latest status of your Iceberg tables in Spark with both Spark SQL and DataFrames.

Example using Spark SQL:

```
spark.sql(f"""
SELECT * FROM {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME} LIMIT 5
""")
```

Example using the DataFrames API:

```
df = spark.table(f"{CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}").limit(5)
```

## Using time travel
<a name="using-time-travel"></a>

Each write operation (insert, update, upsert, delete) in an Iceberg table creates a new snapshot. You can then use these snapshots for time travel—to go back in time and check the status of a table in the past.

For information about how to retrieve the history of snapshots for tables by using `snapshot-id` and timing values, see the [Accessing metadata](#accessing-metadata) section later in this guide.

The following time travel query displays the status of a table based on a specific `snapshot-id`.

Using Spark SQL:

```
spark.sql(f"""
SELECT * FROM {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME} VERSION AS OF {snapshot_id}
""")
```

Using the DataFrames API:

```
df_1st_snapshot_id = spark.read.option("snapshot-id", snapshot_id) \
     .format("iceberg") \
     .load(f"{CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}") \
     .limit(5)
```

The following time travel query displays the status of a table based on the last snapshot that was created before a specific timestamp, in milliseconds (`as-of-timestamp`).

Using Spark SQL:

```
spark.sql(f"""
SELECT * FROM {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME} TIMESTAMP AS OF '{snapshot_ts}'
""")
```

Using the DataFrames API:

```
df_1st_snapshot_ts = spark.read.option("as-of-timestamp", snapshot_ts) \
                          .format("iceberg") \
                          .load(f"{CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}") \
                          .limit(5)
```

## Using incremental queries
<a name="using-incremental-queries"></a>

You can also use Iceberg snapshots to read appended data incrementally.

**Note**
 Currently, this operation supports reading data from `append` snapshots. It doesn't support fetching data from operations such as `replace`, `overwrite`, or `delete`. Additionally, incremental read operations are not supported in the Spark SQL syntax.

The following example retrieves all the records appended to an Iceberg table between the snapshot `start-snapshot-id` (exclusive) and `end-snapshot-id` (inclusive).

```
df_incremental = (spark.read.format("iceberg")
    .option("start-snapshot-id", snapshot_id_start)
    .option("end-snapshot-id", snapshot_id_end)
    .load(f"{CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}")
)
```

## Accessing metadata
<a name="accessing-metadata"></a>

Iceberg provides access to its metadata through SQL. You can access the metadata for any given table (`<table_name>`)  by querying the namespace `<table_name>.<metadata_table>`. For a complete list of metadata tables, see [Inspecting tables](https://iceberg.apache.org/docs/latest/spark-queries/#inspecting-tables) in the Iceberg documentation.

The following example shows how to access the Iceberg history metadata table, which shows the history of commits (changes) for an Iceberg table.

Using Spark SQL (with the `%%sql` magic) from an Amazon EMR Studio notebook:

```
spark.sql(f"""
SELECT * FROM {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}.history LIMIT 5
""")
```

Using the DataFrames API:

```
spark.read.format("iceberg").load(f"{CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}.history").show(5,False)
```

## Working with Iceberg V3
<a name="spark-working-with-iceberg-v3"></a>

Iceberg format version 3 (V3) introduces capabilities on top of V2: deletion vectors, row lineage, default column values, nanosecond timestamps (`TIMESTAMP_NTZ(9)`), geospatial types (`GEOMETRY`, `GEOGRAPHY`), and semi-structured `VARIANT` (with shredding). Most of the SQL and DataFrame code shown earlier in this section applies unchanged to V3 tables — only the `TBLPROPERTIES ('format-version'='3')` clause on `CREATE TABLE` changes what the writer emits. The V3-specific patterns that are worth calling out separately are: **creating** a V3 table that exercises the new types and defaults, **upgrading** an existing V2 table to V3 in place, and **querying** the V3 row-lineage columns. For a full-V3 runtime use Amazon EMR 8.1.0\+, AWS Glue 6.0\+, or open-source Apache Spark 4.1\+ with `iceberg-spark-runtime-4.1_2.13` 1.11.0\+ (see [Iceberg format version support in Apache Spark](#iceberg-format-version-support-in-apache-spark)).

**Note**
 Before you create a V3 table with the examples below — or run the `ALTER TABLE ... SET TBLPROPERTIES ('format-version' = '3')` upgrade in [Upgrading a V2 table to V3](#spark-upgrading-a-v2-table-to-v3) — verify that every downstream engine that reads or writes the table supports V3, and specifically supports the V3 features you plan to use. Notable current gaps: [Amazon Athena](working-with-iceberg-tables-by-using-athena-sql-queries.md) does **not** support V3; [Amazon Redshift](working-with-iceberg-tables-by-using-amazon-redshift.md) supports V3 but only for **deletion vectors, row lineage, and default column values** (Redshift does not yet support `variant`, `geometry`/`geography`, or nanosecond timestamps). Upgrading from V2 to V3 is one-way, so plan the upgrade against your least-capable consumer. For the authoritative service-by-service matrix, see [Working with Iceberg table format specification version 3](table-spec-v3.md).

### Creating a V3 table
<a name="creating-a-v3-table"></a>

The following example creates a V3 Iceberg table that exercises the new V3 capabilities in a single schema: default column values, nanosecond timestamps, geospatial types, and semi-structured `VARIANT` payloads. It also sets `write.delete.mode = merge-on-read` so that subsequent `DELETE` / `UPDATE` / `MERGE INTO` operations write deletion vectors instead of rewriting data files. Partitioning combines a temporal transform (`days(event_time)`) with an identity partition on `vehicle_type`:

```
spark.sql(f"""
    CREATE TABLE IF NOT EXISTS {CATALOG_NAME}.{DB_NAME}.vehicle_telemetry (
        event_id       STRING,
        vehicle_id     STRING,
        vehicle_type   STRING DEFAULT 'UNKNOWN',
        event_time     TIMESTAMP_NTZ(9),
        location       GEOMETRY(4326),
        service_area   GEOGRAPHY(4326),
        sensor_payload VARIANT,
        speed_kmh      DOUBLE DEFAULT 0.0,
        region         STRING DEFAULT 'EMEA'
    )
    USING iceberg
    PARTITIONED BY (days(event_time), vehicle_type)
    TBLPROPERTIES (
        'format-version'    = '3',
        'write.delete.mode' = 'merge-on-read'
    )
""")
```

**Note**
To use geospatial capabilities, you must enable them by setting `spark.sql.geospatial.enabled` to `true`.

Insert a row that supplies values for the non-defaulted columns and lets Iceberg fill in the defaults for `speed_kmh` and `region` on any column that is omitted. The `sensor_payload` field is a nested JSON document parsed into `VARIANT` via `PARSE_JSON`:

```
spark.sql(f"""
    INSERT INTO {CATALOG_NAME}.{DB_NAME}.vehicle_telemetry (
        event_id, vehicle_id, vehicle_type, event_time,
        location, service_area, sensor_payload, speed_kmh
    ) VALUES (
        'EVT-001', 'VAN-042', 'VAN',
        CAST('2026-07-28 09:15:30.123456789' AS TIMESTAMP_NTZ(9)),
        ST_SetSrid(ST_GeomFromWKB(X'0101000000E17A14AE47E1C0BF1F85EB51B84E4940'), 4326),
        ST_SetSrid(ST_GeogFromWKB(X'0101000000E17A14AE47E1C0BF1F85EB51B84E4940'), 4326),
        PARSE_JSON('{{"fuel_pct": 0.72, "cargo_kg": 450, "door_open": false,
                      "engine": {{"rpm": 2100, "temp_c": 88.5}},
                      "route": {{"stops_remaining": 4, "eta_minutes": 35}}}}'),
        35.2
    )
""")
```

In this `INSERT`, the `region` column is not listed in the column list, so Iceberg populates it with the schema-defined default `'EMEA'`. The doubled braces (`{{` and `}}`) inside the JSON literal are Python f-string escape sequences that render as single braces — the actual JSON document Spark parses is `{"fuel_pct": 0.72, "cargo_kg": 450, …}`.

### Upgrading a V2 table to V3
<a name="spark-upgrading-a-v2-table-to-v3"></a>

Iceberg supports upgrading an existing V2 table to V3 in place — a metadata-only operation that does not rewrite the underlying data files. Row lineage is populated automatically from that point on any row inserted or updated after the upgrade:

```
spark.sql(f"""
ALTER TABLE {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}
SET TBLPROPERTIES ('format-version' = '3')
""")
```

The upgrade itself is **lightweight** — it commits a single new metadata JSON file that flips the `format-version` property and leaves every existing data file, manifest, and manifest list untouched — but it is also **one-way**: there is no `format-version = 2` downgrade path once a V3 snapshot has been committed. If you still query the table from an engine that does not yet support V3, keep the table at V2 until that engine catches up — Amazon Athena does not support V3 at all, and Amazon Redshift supports V3 only for deletion vectors, row lineage, and default column values (Redshift does not yet support `variant`, `geometry`/`geography`, or nanosecond timestamps).

### Querying row lineage
<a name="querying-row-lineage"></a>

Iceberg V3 tables carry two hidden metadata columns that record row-level provenance: `_row_id` (a stable identifier assigned to each row when it is first written) and `_last_updated_sequence_number` (the sequence number of the commit that most recently modified the row). These columns are not shown by `SELECT *` — reference them by name to include them in the result set. Row lineage is populated automatically on any V3 table (whether created as V3 or upgraded from V2 — see [Upgrading a V2 table to V3](#spark-upgrading-a-v2-table-to-v3)), and downstream consumers can use these columns to build incremental change-data-capture (CDC) pipelines without extra bookkeeping tables:

```
spark.sql(f"""
SELECT _row_id, _last_updated_sequence_number, *
FROM {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}
""")
```
