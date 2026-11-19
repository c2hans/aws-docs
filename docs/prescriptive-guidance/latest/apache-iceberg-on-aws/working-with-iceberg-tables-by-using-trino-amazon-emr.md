---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/working-with-iceberg-tables-by-using-trino-amazon-emr.html
---

# Working with Iceberg tables by using Trino (Amazon EMR)

[Trino](https://trino.io/docs/current/) is a distributed SQL query engine designed for fast, interactive analytics on large datasets. From Trino running on [Amazon EMR on EC2, you can read from and write to Apache Iceberg tables that you either ](https://docs.aws.amazon.com/emr/)**self-managed on Amazon S3** (through the AWS Glue Data Catalog) or **hosted in Amazon S3 Tables** (through the S3 Tables Iceberg REST catalog) — the SQL surface is the same in both cases, only the Trino Iceberg catalog properties file differs.

This section covers Iceberg format-version support, the Iceberg feature-support matrix, catalog configuration for both hosting options together with cluster setup on Amazon EMR on EC2, and end-to-end examples for creating tables, inserting / upserting / deleting data, reading, querying metadata, time travel, and evolving tables. The code examples and configurations assume **Amazon EMR release emr-7.14.0**.

## Iceberg format version support in Trino
<a name="iceberg-format-version-support-in-trino"></a>

Trino supports Iceberg format version 2 as generally available. Format version 3 support was added as **experimental.** Amazon EMR does not yet include it: the latest release, **emr-7.14.0**, ships **Trino 479**, which is below the 483 threshold.

Because V3 on Trino is still experimental, and because the guidance in this document targets what Amazon EMR ships and supports today, **the remainder of this section covers Iceberg V2 only**. If you need V3 features (deletion vectors, row lineage, `variant`, `geometry`/`geography`, nanosecond timestamps, default column values), use a V3-capable engine — see [Working with Iceberg in Amazon EMR (Spark)](working-with-iceberg-in-amazon-emr-spark.md) (EMR 8.1\+) or [Working with Iceberg in AWS Glue](iceberg-glue.md) (Glue 6.0\+).

|
|
| **Format version** | **Supported** |
| --- |--- |
| Version 2 (V2) | Yes |
| Version 3 (V3) | Experimental (Trino 483\+; Amazon EMR emr-7.14.0 includes Trino 479, which does not support V3) — not covered in this guide |

## Iceberg feature support
<a name="trino-iceberg-feature-support"></a>

The following table summarizes Iceberg V2 feature support in the Trino Iceberg connector on Amazon EMR, grouped by capability area. Both hosting options (self-managed Iceberg on Amazon S3 and Amazon S3 Tables) behave the same unless a row calls out a difference.

|
|
| **Category** | **Feature** | **Supported** |
| --- |--- |--- |
| **DDL** | `CREATE TABLE` |  |
|  | `CREATE TABLE ... AS SELECT` (CTAS) |  on both hosting options for the configs documented below (native AWS Glue Data Catalog, S3 Tables Iceberg REST endpoint) |
|  | `DROP TABLE` |  (removes the catalog registration **and** deletes the underlying data files — the Trino Iceberg connector always instructs the catalog to purge data on drop; there is no separate `PURGE` keyword) |
|  | `SHOW TABLES` |  |
|  | `ALTER TABLE RENAME COLUMN` (schema evolution) |  |
|  | `ALTER TABLE ADD` / `DROP COLUMN` (schema evolution) |  |
|  | `ALTER TABLE ALTER COLUMN` (schema evolution - type widening) |  |
|  | `ALTER TABLE SET PROPERTIES` (partition spec, compression, and other table properties) |  |
|  | Change partition spec |  (via `ALTER TABLE ... SET PROPERTIES partitioning = ARRAY[...]`; no dedicated `ADD PARTITION FIELD` syntax) |
| **DML** | `INSERT INTO` |  |
|  | `UPDATE` |  merge-on-read only (writes positional deletes on V2; the Trino Iceberg connector does not implement copy-on-write) |
|  | `DELETE FROM` |  merge-on-read for row-level deletes (writes positional deletes on V2); metadata-only when the predicate aligns with the partition spec |
|  | `MERGE INTO` (upsert) |  merge-on-read only |
|  | Writes honor table sort order (`sorted_by` table property) |  |
| **Read** | Query Iceberg tables |  — V2: reads positional deletes , equality deletes ; V3: experimental (see the format-version section above) |
|  | Time travel queries |  (`FOR VERSION AS OF <id>`, `FOR TIMESTAMP AS OF <ts>`) |
|  | Incremental queries | ✗ |
|  | Access Iceberg metadata tables (`$snapshots`, `$files`, `$partitions`, `$manifests`, `$history`, `$refs`, ...) |  (query with `SELECT ... FROM "<schema>"."<table>$<metadata_table>"`) |
| **Materialized views** | [AWS Glue Iceberg materialized view](apache-iceberg-materialized-views-in-aws-glue-data-catalog.md) |  (query only) |
| **Partitioning** | Hidden partitioning (all V2 partition transforms) |  |
|  | Partition evolution |  (via `ALTER TABLE ... SET PROPERTIES partitioning = ARRAY[...]`) |
|  | Metadata-only partition `DELETE` |  (when the `WHERE` clause aligns with the partition spec) |
| **Security** | AWS Lake Formation full-table access control | ✗ (Trino on Amazon EMR does not integrate with AWS Lake Formation for Iceberg) |
|  | AWS Lake Formation row/column access control | ✗ (Trino on Amazon EMR does not integrate with AWS Lake Formation for Iceberg) |
| **Maintenance** | Compaction (`ALTER TABLE ... EXECUTE optimize`) |  (binpack strategy only) |
|  | Snapshot expiration (`ALTER TABLE ... EXECUTE expire_snapshots`) |  |
|  | Orphan file cleanup (`ALTER TABLE ... EXECUTE remove_orphan_files`) |  |
|  | Sort order / Z-order compaction | ✗ |
|  | Rollbacks (`ALTER TABLE ... EXECUTE rollback_to_snapshot`, `rollback_to_timestamp`) |  |
| **Format** | Data files supported | Parquet , Avro , ORC  |
|  | Data-file compression: `snappy`, `zstd`, `gzip`, `brotli`, uncompressed |  |

## Amazon EMR on EC2 setup
<a name="amazon-emr-on-ec2-setup"></a>

Trino discovers Iceberg tables through a **catalog properties file** that you place in `/etc/trino/conf/catalog/`. You can register multiple catalogs on the same cluster — one for self-managed Iceberg on S3 and one for Amazon S3 Tables — and query both from the same session. The following two subsections describe the properties files for each hosting option; a later subsection shows the shared cluster bootstrap and creation steps.

### Self-managed Iceberg on Amazon S3
<a name="self-managed-iceberg-on-amazon-s3"></a>

Create an `iceberg.properties` file with the following content. The `iceberg.file-format=parquet` setting determines the default storage format for new tables if you don't explicitly specify the format in the `CREATE TABLE` statement.

```
connector.name=iceberg
iceberg.catalog.type=glue
iceberg.file-format=parquet
fs.native-s3.enabled=true
```

The catalog surface for this connector will be visible in Trino as `iceberg`, so tables are addressed as `iceberg.<database>.<table>`.

### Amazon S3 Tables
<a name="trino-amazon-s3-tables"></a>

Each S3 Tables catalog properties file registers **exactly one table bucket** — the `iceberg.rest-catalog.warehouse` value is the ARN of a single table bucket. If you need Trino to see multiple table buckets, create one properties file per bucket in `/etc/trino/conf/catalog/`. A convenient convention is to name the file after the bucket it targets, for example `iceberg_<table-bucket-name>.properties`, so the Trino catalog surface reflects which bucket each catalog maps to.

For each bucket, create the properties file with the following content. Replace `<aws-region>`, `<aws-account-id>`, `<table-bucket-name>`, and the `s3.iam-role` ARN with your own values.

```
connector.name=iceberg
iceberg.catalog.type=rest
iceberg.rest-catalog.uri=https://s3tables.<aws-region>.amazonaws.com/iceberg
iceberg.rest-catalog.warehouse=arn:aws:s3tables:<aws-region>:<aws-account-id>:bucket/<table-bucket-name>
iceberg.rest-catalog.security=SIGV4
iceberg.rest-catalog.signing-name=s3tables
fs.native-s3.enabled=true
s3.region=<aws-region>
s3.iam-role=<ARN of the IAM ROLE with permissions to S3 Tables>
```

The catalog surface for this connector will be visible in Trino under the file name (without the `.properties` suffix). Using the naming convention above, tables in a bucket named `<table-bucket-name>` can be referred as `iceberg_<table-bucket-name>.<namespace>.<table>`. Add another `iceberg_<other_bucket>.properties` file for each additional bucket you want to expose.

**Note**
 The IAM role referenced in `s3.iam-role` must have permissions to call the S3 Tables API on the target table bucket and to read/write the underlying S3 data. Use one IAM role per bucket (or one role with policies scoped per bucket ARN) to keep least-privilege boundaries clean. For an end-to-end walkthrough of this configuration, see the AWS blog post [Query Amazon S3 Tables from open-source Trino using Apache Iceberg REST endpoint](https://aws.amazon.com/blogs/storage/query-amazon-s3-tables-from-open-source-trino-using-apache-iceberg-rest-endpoint/).

### Cluster bootstrap and creation
<a name="cluster-bootstrap-and-creation"></a>

1. Upload the properties files to your S3 bucket. This is `iceberg.properties` for self-managed Iceberg, plus **one **`iceberg_<bucket>.properties`** file per S3 table bucket** you want Trino to expose.

1. Create a bootstrap action that copies the properties files from your S3 bucket and stores them as Trino catalog configuration files on the Amazon EMR cluster that you will be creating. Make sure to replace `<bucket-name>` with your S3 bucket name and to add one `cp` line per S3 table bucket catalog.

   ```
   #!/bin/bash
   set -ex
   # Self-managed Iceberg (Glue-backed)
   sudo aws s3 cp s3://<bucket-name>/iceberg.properties /etc/trino/conf/catalog/iceberg.properties
   # One line per S3 table bucket
   sudo aws s3 cp s3://<bucket-name>/iceberg_analytics.properties    /etc/trino/conf/catalog/iceberg_analytics.properties
   sudo aws s3 cp s3://<bucket-name>/iceberg_finance.properties      /etc/trino/conf/catalog/iceberg_finance.properties
   ```

   Add one copy line per catalog you plan to use.

1. Create an Amazon EMR cluster with Trino installed and specify the execution of the previous script as a bootstrap action. Here's a sample AWS Command Line Interface (AWS CLI) command for creating the cluster:

   ```
   aws emr create-cluster --release-label emr-7.14.0 \
   --applications Name=Trino \
   --region <region> \
   --name Trino_Iceberg_Cluster \
   --bootstrap-actions '[{"Path":"s3://<bucket-name>/bootstrap.sh","Name":"Add iceberg.properties"}]' \
   --instance-groups '[{"InstanceGroupType":"MASTER","InstanceCount":1,"InstanceType":"m5.xlarge"},{"InstanceGroupType":"CORE","InstanceCount":3,"InstanceType":"m5.xlarge"}]' \
   --service-role "<IAM-service-role>" \
   --ec2-attributes '{"InstanceProfile":"<EMR-EC2-instance-profile>"}'
   ```

   where you replace:
   + `<bucket-name>` with your S3 bucket name
   + `<region>` with your specific AWS Region
   + `<IAM-service-role>` with your Amazon EMR service role that follows the [principle of least privilege](https://aws.amazon.com/blogs/security/techniques-for-writing-least-privilege-iam-policies/).
   + `<EMR-EC2-instance-profile>` with your [instance profile](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-iam-ec2.html).

1. When the Amazon EMR cluster has been initialized, you can initialize a Trino session by running the following command:

   ```
   trino-cli
   ```

1. In the Trino CLI, you can view the catalogs by running:

   ```
   SHOW CATALOGS;
   ```

   You should see the built-in `system` catalog, plus one catalog per properties file you deployed — for example `iceberg` for self-managed Iceberg, and one `iceberg_<table-bucket-name>` catalog per S3 table bucket. Query examples in the rest of this section use the `iceberg` catalog name for readability; substitute the appropriate `iceberg_<table-bucket-name>.<namespace>.<table>` identifier to run the same statements against a specific S3 table bucket.

## Creating Iceberg tables
<a name="creating-iceberg-tables"></a>

To create an Iceberg table, you can use the `CREATE TABLE` statement. If the target schema (database) does not exist yet, create it first with `CREATE SCHEMA` - Replace `<bucket-name>` with your own bucket name and `<prefix>` with the preferred table location:

```
CREATE SCHEMA IF NOT EXISTS iceberg.iceberg_db
    WITH (location = 's3://<bucket-name>/<prefix>/');
```

```
CREATE TABLE iceberg.iceberg_db.iceberg_table (
             userid int,
             firstname varchar,
             city varchar)
        WITH (
             format = 'PARQUET',
             partitioning = ARRAY['city', 'bucket(userid, 16)'],
             location = 's3://<bucket-name>/<prefix>');
```

**Note**
 If you don't specify the format, the `iceberg.file-format` value that you configured in the previous section is used.

To insert data, use the `INSERT INTO` command. Here's an example:

```
INSERT INTO iceberg.iceberg_db.iceberg_table (userid, firstname, city)
VALUES
    (1001, 'John', 'New York'),
    (1002, 'Mary', 'Los Angeles'),
    (1003, 'Mateo', 'Chicago'),
    (1004, 'Shirley', 'Houston'),
    (1005, 'Diego', 'Miami'),
    (1006, 'Nikki', 'Seattle'),
    (1007, 'Pat', 'Boston'),
    (1008, 'Terry', 'San Francisco'),
    (1009, 'Richard', 'Denver'),
    (1010, 'Pat', 'Phoenix');
```

## Reading from Iceberg tables
<a name="reading-from-iceberg-tables"></a>

You can read the latest status of your Iceberg table by using a `SELECT` statement, as follows:

```
SELECT * FROM iceberg.iceberg_db.iceberg_table;
```

## Upserting data into Iceberg tables
<a name="upserting-data-into-iceberg-tables"></a>

You can perform an upsert operation (simultaneously insert new records and update existing ones) by using the `MERGE INTO` statement. Here's an example:

```
MERGE INTO iceberg.iceberg_db.iceberg_table target
USING (
      VALUES
        (1001, 'John Updated', 'Boston'),       -- Update existing user
        (1002, 'Mary Updated', 'Seattle'),      -- Update existing user
        (1011, 'Martha', 'Portland'),           -- Insert new user
        (1012, 'Paulo', 'Austin')               -- Insert new user
    ) AS source (userid, firstname, city)
   ON target.userid = source.userid
 WHEN MATCHED THEN
      UPDATE SET
        firstname = source.firstname,
        city = source.city
 WHEN NOT MATCHED THEN
      INSERT (userid, firstname, city)
      VALUES (source.userid, source.firstname, source.city);
```

## Deleting records from Iceberg tables
<a name="deleting-records-from-iceberg-tables"></a>

To delete data from an Iceberg table, use the `DELETE FROM` expression and specify a filter that matches the rows to delete. Here's an example:

```
DELETE FROM iceberg.iceberg_db.iceberg_table WHERE userid IN (1003, 1004);
```

## Querying Iceberg table metadata
<a name="querying-iceberg-table-metadata"></a>

Iceberg provides access to its metadata through SQL. You can access the metadata for any given table (`<table_name>`)  by querying the namespace `"<table_name>.$<metadata_table>"`. For a complete list of metadata tables, see [Inspecting tables](https://iceberg.apache.org/docs/latest/spark-queries/#inspecting-tables) in the Iceberg documentation.

Here's an example list of queries to inspect Iceberg metadata:

```
SELECT * FROM iceberg.iceberg_db."iceberg_table$snapshots";
SELECT * FROM iceberg.iceberg_db."iceberg_table$history";
SELECT * FROM iceberg.iceberg_db."iceberg_table$partitions";
SELECT * FROM iceberg.iceberg_db."iceberg_table$files";
SELECT * FROM iceberg.iceberg_db."iceberg_table$manifests";
SELECT * FROM iceberg.iceberg_db."iceberg_table$refs";
SELECT * FROM iceberg.iceberg_db."iceberg_table$metadata_log_entries";
```

For example, this query:

```
 SELECT * FROM iceberg.iceberg_db."iceberg_table$snapshots";
```

provides the output:

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/a4008618-1cc1-4775-ab00-8bd30c9e55e7.png)

## Using time travel
<a name="using-time-travel"></a>

Each write operation (insert, update, upsert, or delete) in an Iceberg table creates a new snapshot. You can then use these snapshots for time travel—to go back in time and check the status of a table in the past.

The following time travel query displays the status of a table based on a specific `snapshot_id`:

```
SELECT *
FROM iceberg.iceberg_db.iceberg_table FOR VERSION AS OF 241938428756831817;
```

The following time travel query displays the status of a table based on a specific timestamp:

```
SELECT *
FROM iceberg.iceberg_db.iceberg_table FOR TIMESTAMP AS OF TIMESTAMP '2025-05-28 16:09:40.268 UTC'
```

## Evolving tables
<a name="evolving-tables"></a>

Iceberg supports in-place schema and partition evolution — metadata-only changes that never rewrite existing data files. Trino exposes both through `ALTER TABLE` on the target Iceberg table.

### Schema evolution
<a name="schema-evolution"></a>

For the full syntax, see [Iceberg connector — ALTER TABLE](https://trino.io/docs/current/connector/iceberg.html#alter-table) in the Trino documentation.

```
-- Add a column
ALTER TABLE iceberg.iceberg_db.iceberg_table ADD COLUMN shipping_address VARCHAR;

-- Drop a column
ALTER TABLE iceberg.iceberg_db.iceberg_table DROP COLUMN shipping_address;

-- Rename a column
ALTER TABLE iceberg.iceberg_db.iceberg_table RENAME COLUMN firstname TO first_name;

-- Widen a column type (integer → bigint, decimal precision increase)
ALTER TABLE iceberg.iceberg_db.iceberg_table ALTER COLUMN userid SET DATA TYPE BIGINT;
```

### Partition evolution
<a name="partition-evolution"></a>

Trino updates the Iceberg partition spec by setting the `partitioning` table property to the new set of partition columns (with transforms). Iceberg records this as a **new spec while leaving existing data files partitioned under the previous spec — Iceberg does not rewrite data files.** Pass the full desired set of partition fields each time; the list you provide replaces the previous partition spec.

```
-- Change partition granularity (from month to day of order_date)
ALTER TABLE iceberg.iceberg_db.iceberg_table
SET PROPERTIES partitioning = ARRAY['day(order_date)'];

-- Add a partition field (list the full desired set)
ALTER TABLE iceberg.iceberg_db.iceberg_table
SET PROPERTIES partitioning = ARRAY['day(order_date)', 'bucket(customer_id, 16)'];

-- Drop a partition field (list only the fields you want to keep)
ALTER TABLE iceberg.iceberg_db.iceberg_table
SET PROPERTIES partitioning = ARRAY['day(order_date)'];
```

## Considerations when using Iceberg with Trino
<a name="considerations-when-using-iceberg-with-trino"></a>

Trino write operations on Iceberg tables follow the [merge-on-read](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/best-practices-write.html#write-update-strategy) design, so they create positional delete files instead of rewriting entire data files that are impacted by updates or deletes. If you want to use the copy-on-write approach, consider using Spark for write operations.

Additional considerations when using S3 Tables through the S3 Tables Iceberg REST catalog:
+ Table maintenance (compaction, snapshot expiration, orphan-file cleanup) is performed automatically by the S3 Tables service, so you don't need to run maintenance procedures from Trino for tables in a table bucket.
+ Views are not supported through the S3 Tables Iceberg REST catalog.
+ The IAM role in `s3.iam-role` is used for all data access from the connector. Scope its policy to the specific table bucket ARN to enforce least privilege.
