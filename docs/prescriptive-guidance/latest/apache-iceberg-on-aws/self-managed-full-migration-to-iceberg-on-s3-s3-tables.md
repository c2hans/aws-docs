---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/self-managed-full-migration-to-iceberg-on-s3-s3-tables.html
---

# Self-managed full migration to Iceberg on S3 / S3 Tables

Full data migration recreates the data files as well as the metadata. This approach takes longer and requires additional computing resources compared with [in-place migration](in-place-migration-to-self-managed-iceberg-on-s3.md). However, full data migration offers significant opportunities to improve table quality and optimize data storage and access patterns.

Full data migration also has no source-format restrictions — because it reads through the source and writes new Iceberg files, it works uniformly for Hive-style tables (CSV, JSON, Parquet, ORC) and for Delta Lake and Apache Hudi sources. It also supports both target hosting options: self-managed Iceberg on general Amazon S3 and Amazon S3 Tables. This makes it the natural fallback whenever an [in-place migration](in-place-migration-to-self-managed-iceberg-on-s3.md) path is unavailable or unsuitable for a given source format.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/7360169d-3cea-4326-aa67-8e00d306a1b6.png)

During full data migration, you can perform several beneficial operations, such as data validation to ensure integrity and correctness, schema modifications to better meet current requirements, and partition strategy adjustments for improved query performance. You can also re-sort data to optimize common access patterns, implement Iceberg hidden partitioning for enhanced query efficiency, and perform file format conversion (for example, from CSV to Parquet) if desired.

These capabilities make full data migration ideal for transitioning to Iceberg format and for comprehensively refining and optimizing your data storage strategy. Although full data migration requires more time and resources up front, the resulting improvements in data quality, organization, and query performance can provide long-term benefits.

To implement full data migration, use one of the following patterns:
+ **Single CTAS** — one `CREATE TABLE ... AS SELECT` ([CTAS](https://iceberg.apache.org/docs/latest/spark-ddl/#create-table--as-select)) in Athena or Spark. You can set the partition specification and table properties on the new Iceberg table with the `PARTITIONED BY` and `TBLPROPERTIES` clauses, and reshape the schema at migration time. Simple and self-contained; the natural choice when the migration fits within the engine's time and cost limits.
+ **Progressive CTAS \+ INSERT** — for very large tables, split the migration by a temporal (or other partition-friendly) column. A first CTAS copies one slice (for example, `WHERE year = 2020`), and repeated INSERTs handle the remaining slices (`WHERE year = 2021`, `WHERE year = 2022`, and so on). This pattern is also useful when a single CTAS would exceed engine time limits (see below) or when the migration has to run over several days and needs to be resumable.

**Engine tradeoffs**:
+ **Amazon Athena** is a quick way to migrate small-to-medium tables with CTAS/INSERT. Athena has a default DML query timeout of 30 minutes, which you can raise to a maximum of 240 minutes through a service-quota increase, so it isn't a fit for tables where a single CTAS would run longer. For large tables, either fall back to a Spark migration or split the work into progressive INSERTs that individually stay under the timeout.
+ **Apache Spark on Amazon EMR or AWS Glue** has no equivalent query timeout, and supports Iceberg's `WRITE ORDERED BY` clause to apply a **global sort order** at write time. Athena does not support `WRITE ORDERED BY`, so use Spark when you want to sort data on the fly during migration — see [Applying hidden partitioning and sorting at migration time (Spark)](#applying-hidden-partitioning-and-sorting-at-migration-time-spark) below.

The Spark examples below apply to both target hosting options; only the catalog reference and the presence of a `LOCATION` clause change:
+ **Self-managed Iceberg on Amazon S3** — set `<catalog>` to an Iceberg session catalog wired to the AWS Glue Data Catalog and keep the `LOCATION` clause.
+ **Amazon S3 Tables** — set `<catalog>` to the S3 Tables session catalog and omit the `LOCATION` clause (S3 Tables owns storage). Before running the migration, [enable the S3 Tables integration with AWS analytics services](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-aws.html) and pre-create the target namespace.

For Athena CTAS syntax (including the catalog-context requirement — three-part names aren't accepted on the target of `CREATE TABLE`), see [Creating a table and loading data with a single CTAS statement](working-with-iceberg-tables-by-using-athena-sql-queries.md) in the Athena guide — the source table in that example is the table you want to migrate.

## Applying hidden partitioning and sorting at migration time (Spark)
<a name="applying-hidden-partitioning-and-sorting-at-migration-time-spark"></a>

Full data migration is also the moment to introduce two Iceberg features that improve read performance on the target table:
+ [**Hidden partitioning**](https://iceberg.apache.org/docs/latest/partitioning/#icebergs-hidden-partitioning) — `PARTITIONED BY (days(event_timestamp))` derives the partition from `event_timestamp` without adding a materialized `day` column, so filters on `event_timestamp` get partition pruning automatically. A common improvement when the source uses materialized `year`/`month`/`day` columns or has no partitioning.
+ **Global sort order** — `WRITE ORDERED BY` sorts rows by the specified column(s) as they land in the target, which lets Iceberg prune more files at scan time using min/max column statistics — useful for tables queried by a high-cardinality column such as `user_id`. Athena does not support `WRITE ORDERED BY`, so use Spark on Amazon EMR or AWS Glue when sorting at migration time.

Replace `<catalog>` in the examples with the Iceberg session catalog wired to your target — the AWS Glue Data Catalog for a self-managed Iceberg target, or the S3 Tables catalog for an S3 Tables target. The `LOCATION` clause is only used for the self-managed target; omit it when the target catalog is S3 Tables.

### Hidden partitioning only
<a name="hidden-partitioning-only"></a>

The following one-statement CTAS creates the target with hidden partitioning by day and populates it from the source table. Replace `<bucket-name>` with your own bucket name:

```
spark.sql("""
CREATE TABLE <catalog>.mydb.events_iceberg
USING iceberg
PARTITIONED BY (days(event_timestamp))
LOCATION 's3://<bucket-name>/mydb/events_iceberg/'
AS SELECT
    event_id,
    user_id,
    event_type,
    event_timestamp,
    additional_data
FROM mydb.events_source
""")
```

### Hidden partitioning with a global sort order
<a name="hidden-partitioning-with-a-global-sort-order"></a>

Iceberg SQL does not support declaring a sort order at table creation time — `WRITE ORDERED BY` isn't accepted inside `CREATE TABLE` or `CREATE TABLE ... AS SELECT`. The sort order has to be applied with a separate `ALTER TABLE ... WRITE ORDERED BY` before the target is populated, which means the single CTAS pattern from the previous section splits into three statements: create the target with hidden partitioning, apply `ALTER TABLE ... WRITE ORDERED BY`, and then populate it with `INSERT INTO`.

**Create the target Iceberg table with hidden partitioning** - Replace `<bucket-name>` with your own bucket name:

```
spark.sql("""
CREATE TABLE <catalog>.mydb.events_iceberg (
    event_id        STRING,
    user_id         STRING,
    event_type      STRING,
    event_timestamp TIMESTAMP,
    additional_data STRING
)
USING iceberg
PARTITIONED BY (days(event_timestamp))
LOCATION 's3://<bucket-name>/mydb/events_iceberg/'
""")
```

**Specify the global sort order**:

```
spark.sql("""
ALTER TABLE <catalog>.mydb.events_iceberg
WRITE ORDERED BY user_id
""")
```

**Populate the table from the source** — writes are sorted by `user_id` within each daily partition, honoring the `WRITE ORDERED BY` declaration:

```
spark.sql("""
INSERT INTO <catalog>.mydb.events_iceberg
SELECT
    event_id,
    user_id,
    event_type,
    event_timestamp,
    additional_data
FROM mydb.events_source
""")
```

The sort order persists as a table property, so subsequent writes (from any writer that respects Iceberg's sort order) continue to write pre-sorted data. For more on sort orders and their impact on read performance, see [Best practices — optimizing read and write performance](optimizing-read-and-write-performance.md).
