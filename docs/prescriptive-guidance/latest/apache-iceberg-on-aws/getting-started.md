---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/getting-started.html
---

# Getting started with Iceberg tables in Athena SQL
<a name="getting-started"></a>

Amazon Athena provides built-in support for Iceberg. You can use Iceberg without any additional steps or configuration except for setting up the service prerequisites detailed in the [Getting started](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html) section of the Athena documentation. This section provides a brief introduction to creating tables in Athena. For more information, see [Working with Iceberg tables by using Athena SQL](iceberg-athena.md) later in this guide.

You can create Iceberg tables on AWS by using different engines. Those tables work seamlessly across AWS services. To create your first Iceberg tables with Athena SQL, you can use the following boilerplate code.

```
CREATE TABLE <table_name> (
    col_1 string,
    col_2 string,
    col_3 bigint,
    col_ts timestamp)
PARTITIONED BY (col_1, <<<partition_transform>>>(col_ts))
LOCATION 's3://<bucket>/<folder>/<table_name>/'
TBLPROPERTIES (
    'table_type' ='ICEBERG'
)
```

The following sections provide examples of creating partitioned and nonpartitioned Iceberg table in Athena. For more information, see the Iceberg syntax detailed in the [Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-creating-tables.html#querying-iceberg-partitioning).

## Creating a nonpartitioned table
<a name="nonpartitioned-table"></a>

The following example statement customizes the boilerplate SQL code to create a nonpartitioned Iceberg table in Athena. You can add this statement to the query editor in the [Athena console](https://console.aws.amazon.com/athena/) to create the table.

```
CREATE TABLE athena_iceberg_table (
    color string,
    date string,
    name string,
    price bigint,
    product string,
    ts timestamp)
LOCATION 's3://DOC_EXAMPLE_BUCKET/ice_warehouse/iceberg_db/athena_iceberg_table/'
TBLPROPERTIES (
    'table_type' ='ICEBERG'
)
```

For step-by-step instructions for using the query editor, see [Getting started](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html) in the Athena documentation.

## Creating a partitioned table
<a name="partitioned-table"></a>

The following statement creates a partitioned table based on the date by using Iceberg's concept of [hidden partitioning](https://iceberg.apache.org/docs/latest/partitioning/#icebergs-hidden-partitioning). It uses the `day()` transform to derive daily partitions, using the `dd-mm-yyyy` format, out of a timestamp column. Iceberg doesn't store this value as a new column in the dataset. Instead, the value is derived on the fly when when you write or query data.

```
CREATE TABLE athena_iceberg_table_partitioned (
    color string,
    date string,
    name string,
    price bigint,
    product string,
    ts timestamp)
PARTITIONED BY (day(ts))
LOCATION 's3://DOC_EXAMPLE_BUCKET/ice_warehouse/iceberg_db/athena_iceberg_table/'
TBLPROPERTIES (
    'table_type' ='ICEBERG'
)
```

## Creating a table and loading data with a single CTAS statement
<a name="ctas-statement"></a>

In the partitioned and nonpartitioned examples in the previous sections, the Iceberg tables are created as  empty tables. You can load data to the tables by using the `INSERT `or `MERGE` statement. Alternatively, you can use a `CREATE TABLE AS SELECT (CTAS)` statement to create and load data into an Iceberg table in a single step.

CTAS is the best way in Athena to create a table and load data in a single statement. The following example illustrates how to use CTAS to create an Iceberg table (`iceberg_ctas_table`) from an existing Hive/Parquet table (`hive_table`) in Athena.

```
CREATE TABLE iceberg_ctas_table WITH (
  table_type = 'ICEBERG',
  is_external = false,
  location = 's3://DOC_EXAMPLE_BUCKET/ice_warehouse/iceberg_db/iceberg_ctas_table/'
) AS
SELECT * FROM "iceberg_db"."hive_table" limit 20
---
SELECT * FROM "iceberg_db"."iceberg_ctas_table" limit 20
```

To learn more about CTAS, see the [Athena CTAS documentation](https://docs.aws.amazon.com/athena/latest/ug/ctas.html).

## Inserting, updating, and deleting data
<a name="updating-data"></a>

Athena supports different ways of writing data to an Iceberg table by using the `INSERT INTO`, `UPDATE`, `MERGE INTO`, and `DELETE FRO`M statements.

**Note**
Athena SQL doesn't currently support the copy-on-write approach. `UPDATE`, `MERGE INTO`, and `DELETE FROM` operations always use the merge-on-read approach with positional deletes, regardless of specified table properties. If you set up table properties such as `write.update.mode`, `write.merge.mode`, and `write.delete.mode` to use copy-on-write, your queries won't fail, but Athena will ignore them and keep using merge-on-read.

The following statement uses `INSERT INTO` to add data to an Iceberg table:

```
INSERT INTO "iceberg_db"."ice_table" VALUES (
    'red', '222022-07-19T03:47:29', 'PersonNew', 178, 'Tuna', now()
)

SELECT * FROM "iceberg_db"."ice_table"
where color = 'red' limit 10;
```

Sample output:

![Sample input from an INSERT statement](http://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/e97a8db8-fb5a-44c3-8f98-a182fc2f7401.png)

For more information, see the [Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-updating-iceberg-table-data.html).

## Querying Iceberg tables
<a name="querying-iceberg-tables"></a>

You can run regular SQL queries against your Iceberg tables by using Athena SQL, as illustrated in the previous example.

In addition to the usual queries, Athena also supports time travel queries for Iceberg tables. As discussed previously, you can change existing records through updates or deletes in an Iceberg table, so it's convenient to use time travel queries to look back into older versions of your table based on a timestamp or a snapshot ID.

For example, the following statement updates a color value for `Person5`, and then displays an earlier value from January 4, 2023:

```
UPDATE ice_table SET color='new_color' WHERE name='Person5'

SELECT * FROM "iceberg_db"."ice_table" FOR TIMESTAMP AS OF TIMESTAMP '2023-01-04 12:00:00 UTC'
```

Sample output:

![Sample output from an Iceberg time travel query](http://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/d6a10a40-b520-4e66-a26d-25a0cf5b6605.png)

For syntax and additional examples of time travel queries, see the [Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-table-data.html#querying-iceberg-time-travel-and-version-travel-queries).

## Iceberg table anatomy
<a name="iceberg-table-anatomy"></a>

Now that we've covered the basic steps of working with Iceberg tables, let's dive deeper into the intricate details and design of an Iceberg table.

To enable the features [described earlier](data-lakes.md#iceberg-intro) in this guide, Iceberg is designed with hierarchical layers of data and metadata files. These layers manage metadata intelligently to optimize query planning and execution.

The following diagram portrays the organization of an Iceberg table through two perspectives: the AWS services used to store the table and the file placement in Amazon S3.

![Anatomy of an Iceberg table](http://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/0fbc54c9-adeb-4ea9-a334-3857f2b2945e.png)

As shown in the diagram, an Iceberg table consists of three main layers:
+ **Iceberg catalog**: AWS Glue Data Catalog integrates natively with Iceberg and is, for most use cases, the best option for workloads that run on AWS. Services that interact with Iceberg tables (for example, Athena) use the catalog to find the current snapshot version of the table, either to read or to write data.
+ **Metadata layer**: Metadata files, namely the manifest files and manifest list files, keep track of information such as the schema of the tables, the partition strategy, and the location of the data files, as well as column-level statistics such as minimum and maximum ranges for the records that are stored in each data file. These metadata files are stored in Amazon S3 within the table path.
  + **Manifest files** contain a record for each data file, including its location, format, size, checksum, and other relevant information.
  + **Manifest lists** provide an index of the manifest files. As the number of manifest files grows in a table, breaking up that information into smaller subsections helps reduce the number of manifest files that need to be scanned by queries.
  + **Metadata files** contain information about the whole Iceberg table, including the manifest lists, the schemas, partition metadata, snapshot files, and other files that are used to manage the table's metadata.
+ **Data layer**: This layer contains the files that have the data records that queries will run against. These files can be stored in different formats, including [Apache Parquet](https://parquet.apache.org/), [Apache Avro](https://avro.apache.org/), and [Apache ORC](https://orc.apache.org/).
  + **Data files** contain the data records for a table.
  + **Delete files** encode row-level delete and update operations in an Iceberg table. Iceberg has two types of delete files, as described in the [Iceberg documentation](https://iceberg.apache.org/spec/#delete-formats). These files are created by operations by using the merge-on-read mode.
