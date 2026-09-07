---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/iceberg-spark.html
---

# Working with Iceberg tables by using Apache Spark
<a name="iceberg-spark"></a>

This section provides an overview of using Apache Spark to interact with Iceberg tables. The examples are boilerplate code that can run on Amazon EMR or AWS Glue.

**Note**
The primary interface for interacting with Iceberg tables is SQL, so most of the examples will combine Spark SQL with the DataFrames API.

## Creating and writing Iceberg tables
<a name="spark-create-data"></a>

You can use Spark SQL and Spark DataFrames to create and add data to Iceberg tables.

### Using Spark SQL
<a name="using-spark-sql.08b2e798-9951-54fc-8ca4-46e5d1af535f"></a>

To write an Iceberg dataset, use standard Spark SQL statements such as `CREATE TABLE` and `INSERT INTO`.

#### Unpartitioned tables
<a name="unpartitioned-tables.4befe354-2995-5a0f-88ca-60dd3b4cd800"></a>

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
    OPTIONS ('format-version'='2')
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
<a name="partitioned-tables.93613d0e-6f87-57e2-8898-5676252b2a39"></a>

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
    OPTIONS ('format-version'='2')
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
<a name="using-the-dataframes-api.bc51b1f8-6451-54c4-abdb-78b286827a87"></a>

To write an Iceberg dataset, you can use the `DataFrameWriterV2` API.

To create an Iceberg table and write data to it, use the `df.writeTo(`t) function. If the table exists, use the `.append()` function. If it doesn't, use `.create().` The following examples use `.createOrReplace()`, which is a variation of `.create()` that's equivalent to `CREATE OR REPLACE TABLE AS SELECT`.

#### Unpartitioned tables
<a name="unpartitioned-tables.0603ba50-210b-5c8b-80b1-c19c018a3c4d"></a>

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
<a name="partitioned-tables.4987e5ee-2d3c-5b05-af02-f6c0347e3d73"></a>

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
<a name="spark-update-data"></a>

The following example shows how to update data in an Iceberg table. This example modifies all rows that have an even number in the `c_customer_sk` column.

```
spark.sql(f"""
UPDATE {CATALOG_NAME}.{db.name}.{table.name}
SET c_email_address = 'even_row'
WHERE c_customer_sk % 2 == 0
""")
```

This operation uses the default copy-on-write strategy, so it rewrites all impacted data files.

## Upserting data in Iceberg tables
<a name="spark-upsert-data"></a>

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
+ If a customer record that's in `{UPSERT_TABLE_NAME}` doesn't exist in `{TABLE_NAME}`, the `{UPSERT_TABLE_NAME}` record is added to `{TABLE_NAME}` (insert operation).

## Deleting data in Iceberg tables
<a name="spark-delete-data"></a>

To delete data from an Iceberg table, use the `DELETE FROM` expression and specify a filter that matches the rows to delete.

```
spark.sql(f"""
DELETE FROM {CATALOG_NAME}.{db.name}.{table.name}
WHERE c_customer_sk % 2 != 0
""")
```

If the filter matches an entire partition, Iceberg performs a metadata-only delete and leaves the data files in place. Otherwise, it rewrites only the affected data files.

The delete method takes the data files that are impacted by the `WHERE` clause and creates a copy of them without the deleted records. It then creates a new table snapshot that points to the new data files. Therefore, the deleted records are still present in the older snapshots of the table. For example, if you retrieve the previous snapshot of the table, you'll see the data that you just deleted. For information about removing unneeded old snapshots with the related data files for cleanup purposes, see the section [Maintaining files by using compaction](best-practices-compaction.md) later in this guide.

## Reading data
<a name="spark-read-data"></a>

You can read the latest status of your Iceberg tables in Spark with both Spark SQL and DataFrames.

Example using Spark SQL:

```
spark.sql(f"""
SELECT * FROM {CATALOG_NAME}.{db.name}.{table.name} LIMIT 5
""")
```

Example using the DataFrames API:

```
df = spark.table(f"{CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}").limit(5)
```

## Using time travel
<a name="spark-time-travel"></a>

Each write operation (insert, update, upsert, delete) in an Iceberg table creates a new snapshot. You can then use these snapshots for time travel—to go back in time and check the status of a table in the past.

For information about how to retrieve the history of snapshots for tables by using `snapshot-id` and timing values, see the [Accessing metadata](#spark-metadata) section later in this guide.

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
SELECT * FROM dev.{db.name}.{table.name} TIMESTAMP AS OF '{snapshot_ts}'
""")
```

Using the DataFrames API:

```
df_1st_snapshot_ts = spark.read.option("as-of-timestamp", snapshot_ts) \
                          .format("iceberg") \
                          .load(f"dev.{DB_NAME}.{TABLE_NAME}") \
                          .limit(5)
```

## Using incremental queries
<a name="spark-incremental-queries"></a>

You can also use Iceberg snapshots to read appended data incrementally.

**Note**
  Currently, this operation supports reading data from `append` snapshots. It doesn't support fetching data from operations such as `replace`, `overwrite`, or `delete`.  Additionally, incremental read operations aren't supported in the Spark SQL syntax.

The following example retrieves all the records appended to an Iceberg table between the snapshot `start-snapshot-id` (exclusive) and `end-snapshot-id` (inclusive).

```
df_incremental = (spark.read.format("iceberg")
    .option("start-snapshot-id", snapshot_id_start)
    .option("end-snapshot-id", snapshot_id_end)
    .load(f"glue_catalog.{DB_NAME}.{TABLE_NAME}")
)
```

## Accessing metadata
<a name="spark-metadata"></a>

Iceberg provides access to its metadata through SQL. You can access the metadata for any given table (`<table_name>`)  by querying the namespace `<table_name>.<metadata_table>`. For a complete list of metadata tables, see [Inspecting tables](https://iceberg.apache.org/docs/latest/spark-queries/#inspecting-tables) in the Iceberg documentation.

The following example shows how to access the Iceberg history metadata table, which shows the history of commits (changes) for an Iceberg table.

Using Spark SQL (with the `%%sql` magic) from an Amazon EMR Studio notebook:

```
Spark.sql(f"""
SELECT * FROM {CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}.history LIMIT 5
""")
```

Using the DataFrames API:

```
spark.read.format("iceberg").load("{CATALOG_NAME}.{DB_NAME}.{TABLE_NAME}.history").show(5,False)
```

Sample output:

![Sample metadata output from an Iceberg table](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/92081edb-bc77-4951-81c9-b1f4ca4dd963.png)
