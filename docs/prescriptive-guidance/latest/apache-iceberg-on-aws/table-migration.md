---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/table-migration.html
---

# Migrating existing tables to Iceberg
<a name="table-migration"></a>

This section focuses on migrating your existing Hive-style tables to Iceberg format. It applies to tables that use traditional Hive-compatible formats such as [Apache Parquet](https://parquet.apache.org/) or [Apache ORC](https://orc.apache.org/). This information doesn't apply to tables that already use modern table formats such as Linux Foundation Delta Lake or Apache Hudi.

To migrate your current Hive-style tables to Iceberg format, you can use either in-place or full data migration:
+ **In-place migration** is the process of generating Iceberg's metadata files on top of existing data files.
+ **Full data migration** creates the Iceberg metadata layer and also rewrites existing data files from the original table to the new Iceberg table.

The following sections provide a detailed overview of each migration method, including step-by-step instructions and considerations for implementation. For more information about these migration strategies, see the [Table Migration](https://iceberg.apache.org/docs/latest/table-migration/) section of the Iceberg documentation.

After you review the details of the in-place and full data migration methods, see the following two key sections to aid your decision-making process:
+ [Choosing a migration strategy](#migration-strategy) provides guidance through a series of questions and scenarios, to help you determine the most suitable migration approach based on your specific requirements and use cases.
+ [Migration options summary](#migration-options) provides a comprehensive table that compares key characteristics and considerations across different migration options. This table serves as a quick reference guide and offers a feature comparison to help you understand the technical trade-offs between methods.

## In-place migration
<a name="table-migration-inplace"></a>

In-place migration eliminates the need to rewrite all your data files. Instead, Iceberg metadata files are generated and linked to your existing data files. This method is typically faster and more cost-effective, especially for large datasets or tables that have compatible file formats such as Parquet, Avro, and ORC.

**Note**
In-place migration cannot be used when migrating to [Amazon S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables.html).

Iceberg offers two main options for implementing in-place migration:
+ Using the [snapshot](https://iceberg.apache.org/docs/latest/spark-procedures/#snapshot) procedure to create a new Iceberg table while keeping the source table unchanged. For more information, see [Snapshot Table](https://iceberg.apache.org/docs/latest/table-migration/#snapshot-table) in the Iceberg documentation.
+ Using the [migrate](https://iceberg.apache.org/docs/latest/spark-procedures/#migrate) procedure to create a new Iceberg table as a substitution for the source table. For more information, see [Migrate Table](https://iceberg.apache.org/docs/latest/table-migration/#migrate-table) in the Iceberg documentation. Although this procedure works with Hive Metastore (HMS), it isn't currently compatible with the AWS Glue Data Catalog. The *Replicating the table migration procedure in AWS Glue Data Catalog* section later in this guide provides a workaround for achieving a similar outcome with the Data Catalog.

After you perform in-place migration by using either `snapshot` or `migrate`, some data files might remain unmigrated. This typically happens when writers continue writing to the source table during or after migration. To incorporate these remaining files into your Iceberg table, you can use the [add\_files](https://iceberg.apache.org/docs/latest/spark-procedures/#add_files) procedure. For more information, see [Add Files](https://iceberg.apache.org/docs/latest/table-migration/#add-files) in the Iceberg documentation.

Let's say you have a Parquet-based `products` table that was created and populated in Athena as follows:

```
CREATE EXTERNAL TABLE mydb.products (
    product_id INT,
    product_name STRING
)
PARTITIONED BY (category STRING)
STORED AS PARQUET
LOCATION 's3://DOC-EXAMPLE-BUCKET/products/';

INSERT INTO mydb.products
VALUES
    (1001, 'Smartphone', 'electronics'),
    (1002, 'Laptop', 'electronics'),
    (2001, 'T-Shirt', 'clothing'),
    (2002, 'Jeans', 'clothing');
```

The following sections explain how you can use the `snapshot` and `migrate` procedures with this table.

### Option 1: snapshot procedure
<a name="in-place-snapshot"></a>

The `snapshot` procedure creates a new Iceberg table that has a different name but replicates the schema and partitioning of the source table. This operation leaves the source table completely unchanged both during and after the action. It effectively creates a lightweight copy of the table, which is particularly useful for testing scenarios or data exploration without risking modifications to the original data source. This approach enables a transition period where both the original table and the Iceberg table remain available (see the notes at the end of this section). When testing is complete, you can move your new Iceberg table to production by transitioning all writers and readers to the new table.

You can run the `snapshot` procedure by using Spark in any Amazon EMR deployment model (for example, Amazon EMR on EC2, Amazon EMR on EKS, EMR Serverless) and AWS Glue.

To test in-place migration with the `snapshot` Spark procedure, follow these steps:

1. Launch a Spark application and configure the Spark session with the following settings:
   + `"spark.sql.extensions":"org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"`
   + `"spark.sql.catalog.spark_catalog":"org.apache.iceberg.spark.SparkSessionCatalog"`
   + `"spark.sql.catalog.spark_catalog.type":"glue"`
   + `"spark.hadoop.hive.metastore.client.factory.class":"com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory"`

1. Run the `snapshot` procedure to create a new Iceberg table that points to the original table data files:

   ```
   spark.sql(f"""
   CALL system.snapshot(
   source_table => 'mydb.products',
   table => 'mydb.products_iceberg',
   location => 's3://DOC-EXAMPLE-BUCKET/products_iceberg/'
   )
   """
   ).show(truncate=False)
   ```

   The output dataframe contains the `imported_files_count` (the numbers of files that were added).

1. Validate the new table by querying it:

   ```
   spark.sql(f"""
   SELECT * FROM mydb.products_iceberg LIMIT 10
   """
   ).show(truncate=False)
   ```

Notes:
+ After you run the procedure, any data file modifications on the source table will throw the generated table out of sync. New files that you add won't be visible in the Iceberg table, and files that you removed will affect query capabilities in the Iceberg table. To avoid the synchronization issues:
  + If the new Iceberg table is intended for production use, stop all processes that write to the original table and redirect them to the new table.
  + If you need a transition period or if the new Iceberg table is for testing purposes, see [Keeping Iceberg tables in sync after in-place migration](#migrate-sync) later in this section for guidance on maintaining table synchronization.
+ When you use the `snapshot` procedure, the `gc.enabled` property is set to `false` in the table properties of the created Iceberg table. This setting prohibits actions such as `expire_snapshots`, `remove_orphan_files`, or `DROP TABLE` with the `PURGE` option, which would physically delete data files. Iceberg delete or merge operations, which do not directly impact source files, are still allowed.
+ To make your new Iceberg table fully functional, with no limits on actions that physically delete data files, you can change the `gc.enabled` table property to `true`. However, this setting will allow actions that impact source data files, which could corrupt access to the original table. Therefore, change the `gc.enabled` property only if you no longer need to maintain the original table's functionality. For example:

  ```
  spark.sql(f"""
  ALTER TABLE mydb.products_iceberg
  SET TBLPROPERTIES ('gc.enabled' = 'true');
  """)
  ```

### Option 2: migrate procedure
<a name="option-2--migrate-procedure.99300099-6a34-54b1-b68f-5507a05a6f46"></a>

The `migrate` procedure creates a new Iceberg table that has the same name, schema, and partitioning as the source table. When this procedure runs, it locks the source table and renames it to `<table_name>_BACKUP_` (or a custom name specified by the `backup_table_name` procedure parameter).

**Note**
If you set the `drop_backup` procedure parameter to `true`, the original table will not be retained as a backup.

Consequently, the `migrate` table procedure requires all modifications that affect the source table to be stopped before the action is performed. Before you run the `migrate` procedure:
+ Stop all writers that interact with the source table.
+ Modify readers and writers that don't natively support Iceberg to enable Iceberg support.

For example:
+ Athena continues to work without modification.
+ Spark requires:
  + Iceberg Java Archive (JAR) files to be included in the classpath (see the [Working with Iceberg in Amazon EMR](iceberg-emr.md) and [Working with Iceberg in AWS Glue](iceberg-glue.md) sections earlier in this guide).
  + The following Spark session catalog configurations (using `SparkSessionCatalog` to add Iceberg support while maintaining built-in catalog functionalities for non-Iceberg tables):
    + `"spark.sql.extensions":"org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"`
    + `"spark.sql.catalog.spark_catalog":"org.apache.iceberg.spark.SparkSessionCatalog"`
    + `"spark.sql.catalog.spark_catalog.type":"glue"`
    + `"spark.hadoop.hive.metastore.client.factory.class":"com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory"`

After you run the procedure, you can restart your writers with their new Iceberg configuration.

Currently, the `migrate` procedure isn't compatible with the AWS Glue Data Catalog, because the Data Catalog doesn't support the `RENAME` operation. Therefore, we recommend that you use this procedure only when you're working with Hive Metastore. If you're using the Data Catalog, see the next section for an alternative approach.

You can run the `migrate` procedure across all Amazon EMR deployment models (Amazon EMR on EC2, Amazon EMR on EKS, EMR Serverless) and AWS Glue, but it requires a configured connection to Hive Metastore. Amazon EMR on EC2 is the recommended choice because it provides a built-in Hive Metastore configuration, which minimizes setup complexity.

To test in-place migration with the `migrate` Spark procedure from an Amazon EMR on EC2 cluster that's configured with Hive Metastore, follow these steps:

1. Launch a Spark application and configure the Spark session to use the Iceberg Hive catalog implementation. For example, if you're using the `pyspark` CLI:

   ```
   pyspark --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions --conf spark.sql.catalog.spark_catalog=org.apache.iceberg.spark.SparkSessionCatalog --conf spark.sql.catalog.spark_catalog.type=hive
   ```

1. Create a `products` table in Hive Metastore. This is the source table, which already exists in a typical migration.

   1. Create the `products` external Hive table in Hive Metastore to point to the existing data in Amazon S3:

      ```
      spark.sql(f"""
      CREATE EXTERNAL TABLE products (
          product_id INT,
          product_name STRING
      )
      PARTITIONED BY (category STRING)
      STORED AS PARQUET
      LOCATION 's3://DOC-EXAMPLE-BUCKET/products/';
      """
      )
      ```

   1. Add the existing partitions by using the `MSCK REPAIR TABLE` command:

      ```
      spark.sql(f"""
      MSCK REPAIR TABLE products
      """
      )
      ```

   1. Confirm that the table contains data by running a `SELECT` query:

      ```
      spark.sql(f"""
      SELECT * FROM products
      """
      ).show(truncate=False)
      ```

      Sample output:
![Sample output from data validation during Iceberg table migration.](http://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/fcf5b249-cca9-4d04-bb56-bc1de5946861.jpeg)

1. Use the Iceberg `migrate` procedure:

   ```
   df_res=spark.sql(f"""
   CALL system.migrate(
   table => 'default.products'
   )
   """
   )

   df_res.show()
   ```

   The output dataframe contains the `migrated_files_count` (the numbers of files that were added to the Iceberg table):
![Sample output from file count validation during Iceberg table migration.](http://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/863b19b0-a6eb-4f5b-a7b2-b136e0e7328b.png)

1. Confirm that the backup table was created:

   ```
   spark.sql("show tables").show()
   ```

   Sample output:
![Sample output from backup validation during Iceberg table migration.](http://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/026434f6-1793-474d-ac44-471e65cdd899.png)

1. Validate the operation by querying the Iceberg table:

   ```
   spark.sql(f"""
   SELECT * FROM products
   """
   ).show(truncate=False)
   ```

**Note**
After you run the procedure, all current processes that query or write to the source table will be impacted if they aren't properly configured with Iceberg support. Therefore, we recommend that you follow these steps: (1) Stop all processes by using the source table before migration. (2) Perform the migration. (3) Reactivate the processes by using the proper Iceberg settings.

**Note**
If data file modifications occur during the migration process (new files are added or files are removed), the generated table will get out of sync. For synchronization options, see [Keeping Iceberg tables in sync after in-place migration](#migrate-sync) later in this section.

### Replicating the table migration procedure in AWS Glue Data Catalog
<a name="replicating-the-table-migration-procedure-in-9999999999999999gludclong-.60def318-3ea2-58aa-b2d1-7027a48b4120"></a>

You can replicate the migrate procedure's outcome in AWS Glue Data Catalog (backing up the original table and replacing it with an Iceberg table) by following these steps:

1. Use the snapshot procedure to create a new Iceberg table that points to the original table's data files.

1. Back up the original table metadata in the Data Catalog:

   1. Use the [GetTable](https://docs.aws.amazon.com/glue/latest/webapi/API_GetTable.html) API to retrieve the source table definition.

   1. Use the [GetPartitions](https://docs.aws.amazon.com/glue/latest/webapi/API_GetPartitions.html) API to retrieve the source table partition definition.

   1. Use the [CreateTable](https://docs.aws.amazon.com/glue/latest/webapi/API_CreateTable.html) API to create a backup table in the Data Catalog.

   1. Use the [CreatePartition](https://docs.aws.amazon.com/glue/latest/webapi/API_CreatePartition.html) or [BatchCreatePartition](https://docs.aws.amazon.com/glue/latest/webapi/API_BatchCreatePartition.html) API to register partitions to the backup table in the Data Catalog.

1. Change the `gc.enabled` Iceberg table property to `false` to enable full table operations.

1. Drop the original table.

1. Locate the Iceberg table metadata JSON file in the metadata folder of the table's root location.

1. Register the new table in the Data Catalog by using the [register\_table](https://iceberg.apache.org/docs/latest/spark-procedures/#register_table) procedure with the original table name and the location of the `metadata.json` file that was created by the `snapshot` procedure:

   ```
   spark.sql(f"""
   CALL system.register_table(
       table => 'mydb.products',
       metadata_file => '{iceberg_metadata_file}'
   )
   """
   ).show(truncate=False)
   ```

### Keeping Iceberg tables in sync after in-place migration
<a name="migrate-sync"></a>

The `add_files` procedure provides a flexible way to incorporate existing data into Iceberg tables. Specifically, it registers existing data files (such as Parquet files) by referencing their absolute paths in Iceberg's metadata layer. By default, the procedure adds files from all table partitions to an Iceberg table, but you can selectively add files from specific partitions. This selective approach is particularly useful in several scenarios:
+ When new partitions are added to the source table after initial migration.
+ When data files are added to or removed from existing partitions after initial migration. However, re-adding modified partitions requires partition deletion first. More information about this is provided later in this section.

Here are some considerations for using the `add_file` procedure after in-place migration (`snapshot` or `migrate`) has been performed, to keep the new Iceberg table in sync with the source data files:
+ When new data is added to new partitions in the source table, use the `add_files` procedure with the `partition_filter` option to selectively incorporate these additions into the Iceberg table:

  ```
  spark.sql(f"""
  CALL system.add_files(
  source_table => 'mydb.products',
  table => 'mydb.products_iceberg',
  partition_filter => map('category', 'electronics')
  ).show(truncate=False)
  ```

  or:

  ```
  spark.sql(f"""
  CALL system.add_files(
  source_table => '`parquet`.`s3://DOC-EXAMPLE-BUCKET/products/`',
  table => 'mydb.products_iceberg',
  partition_filter => map('category', 'electronics')
  ).show(truncate=False)
  ```
+ The `add_files` procedure scans for files either in the entire source table or in specific partitions when you specify the `partition_filter` option, and attempts to add all files it finds to the Iceberg table. By default, the `check_duplicate_files` procedure property is set to `true`, which prevents the procedure from running if files already exist in the Iceberg table. This is important because there is no built-in option to skip previously added files, and disabling `check_duplicate_files` will cause files to be added twice, creating duplicates. When new files are added to the source table, follow these steps:

  1. For new partitions, use `add_files` with a `partition_filter` to import only files from the new partition.

  1. For existing partitions, first delete the partition from the Iceberg table, and then re-run `add_files` for that partition, specifying the `partition_filter`. For example:

     ```
     # We initially perform in-place migration with snapshot
     spark.sql(f"""
     CALL system.snapshot(
     source_table => 'mydb.products',
     table => 'mydb.products_iceberg',
     location => 's3://DOC-EXAMPLE-BUCKET/products_iceberg/'
     )
     """
     ).show(truncate=False)

     # Then on the source table, some new files were generated under the category='electronics' partition. Example:
     spark.sql("""
     INSERT INTO mydb.products
     VALUES (1003, 'Tablet', 'electronics')
     """)

     # We delete the modified partition from the Iceberg table. Note this is a metadata operation only
     spark.sql("""
     DELETE FROM mydb.products_iceberg WHERE category = 'electronics'
     """)

     # We add_files from the modified partition
     spark.sql("""
     CALL system.add_files(
       source_table => 'mydb.products',
       table => 'mydb.products_iceberg',
       partition_filter => map('category', 'electronics')
     )
     """).show(truncate=False)
     ```

  Choosing the right in-place migration strategy

  To choose the best in-place migration strategy, consider the questions in the following table.
**Note**
Every `add_files` operation generates a new Iceberg table snapshot with appended data.

|
|
| Question | Recommendation | Explanation |
| --- |--- |--- |
| Do you want to quickly migrate without rewriting data while keeping both Hive and Iceberg tables accessible for testing or gradual transition? | `snapshot` procedure followed by `add_files` procedure | Use the `snapshot` procedure to create a new Iceberg table by cloning the schema and referencing data files, without modifying the source table. Use the `add_files` procedure to incorporate partitions that were added or modified after migration, noting that re-adding modified partitions requires partition deletion first. |
| Are you using Hive Metastore and do you want to replace your Hive table with an Iceberg table immediately, without rewriting the data? | `migrate` procedure followed by `add_files` procedure | Use the `migrate` procedure to create an Iceberg table, back up the source table, and replace the original table with the Iceberg version. This option is compatible with Hive Metastore but not with AWS Glue Data Catalog. <br />Use the `add_files` procedure to incorporate partitions that were added or modified after migration, noting that re-adding modified partitions requires partition deletion first. |
| Are you using AWS Glue Data Catalog and do you want to replace your Hive table with an Iceberg table immediately, without rewriting the data? | Adaptation of the `migrate` procedure, followed by `add_files` procedure | Replicate `migrate` procedure behavior:<br />1. Use `snapshot` to create an Iceberg table.<br />2. Back up the original table metadata by using AWS Glue APIs.<br />3. Enable `gc.enabled` on Iceberg table properties.<br />4. Drop the original table.<br />5. Use `register_table` to create a new table entry with the original name.This option requires manual handling of AWS Glue API calls for metadata backup.<br />Use the `add_files` procedure to incorporate partitions that were added or modified after migration, noting that re-adding modified partitions requires partition deletion first. |

## Full data migration
<a name="table-migration-full"></a>

Full data migration recreates the data files as well as the metadata. This approach takes longer and requires additional computing resources compared with in-place migration. However, full data migration offers significant opportunities to improve table quality and optimize data storage and access patterns.

During full data migration, you can perform several beneficial operations, such as data validation to ensure integrity and correctness, schema modifications to better meet current requirements, and partition strategy adjustments for improved query performance. You can also re-sort data to optimize common access patterns, implement Iceberg hidden partitioning for enhanced query efficiency, and perform file format conversion (for example, from CSV to Parquet) if desired.

These capabilities make full data migration ideal for transitioning to Iceberg format and for comprehensively refining and optimizing your data storage strategy. Although full data migration requires more time and resources up front, the resulting improvements in data quality, organization, and query performance can provide long-term benefits. To implement full data migration, use one of the following options:
+ Use the `CREATE TABLE ... AS SELECT` ([CTAS](https://iceberg.apache.org/docs/latest/spark-ddl/#create-table--as-select)) statement in Spark (on Amazon EMR or AWS Glue) or in Athena. You can set the partition specification and table properties for the new Iceberg table by using the `PARTITIONED BY` and `TBLPROPERTIES` clauses. You can change the schema and partitioning for the new table according to your needs instead of inheriting them from the source table.
+ Read from the source table and write the data as a new Iceberg table by using Spark on Amazon EMR or AWS Glue. For more information, see [Creating a table](https://iceberg.apache.org/docs/nightly/spark-getting-started/#creating-a-table) in the Iceberg documentation.

## Choosing a migration strategy
<a name="migration-strategy"></a>

When transitioning to Iceberg format, the choice between in-place and full migration is crucial. To determine the most suitable approach for your specific needs, consider the following questions and recommendations:

|
|
| Question | Recommendation |
| --- |--- |
| **What is the data file format (for example, CSV or Apache Parquet)?** | Consider in-place migration if your table file format is Parquet, ORC, or Avro.For other formats such as CSV, JSON, and so on, use full data migration. |
| **Do you want to update or consolidate the table schema?** | If you want to evolve the table schema by using Iceberg native capabilities, consider in-place migration. For example, you can rename columns after the migration. (The schema can be changed in the Iceberg metadata layer.)If you want to remove entire columns because they are no longer needed, we recommend that you use full data migration. |
| **Would the table benefit from changing the partition strategy?** | If Iceberg's partitioning approach meets your requirements (for example, new data is stored by using the new partition layout while existing partitions remain as is), consider in-place migration.If you want to use hidden partitions in your table, consider full data migration. For more information about hidden partitions, see the [Best practices](best-practices-read.md#read-partitioning) section. |
| **Would the table benefit from adding or changing the sort order strategy?** | Adding or changing the sort order of your data requires rewriting the dataset. In this case, consider using full data migration.For large tables where it's prohibitively expensive to rewrite all the table partitions, consider using in-place migration and run compaction (with sorting enabled) for the most frequently accessed partitions. |
| **Does the table have many small files?** | Merging small files into larger files requires rewriting the dataset. In this case, consider using full data migration.For large tables where it's prohibitively expensive to rewrite all the table partitions, consider using in-place migration and run compaction (with sorting enabled) for the most frequently accessed partitions. |

## Migration options summary
<a name="migration-options"></a>

This table summarizes the main characteristics and considerations for each migration option.

|
|
| Feature | In-place migration | Full data migration |
| --- |--- |--- |
| [snapshot](#table-migration-inplace) | [migrate](#table-migration-inplace) | [CTAS or (CREATE TABLE \+ INSERT)](#table-migration-full) |
| **Data layout improvements as part of the migration process** |  |  |  |
| Re-sort data | No | No | Yes |
| Change partitioning (for example, to use Iceberg hidden partitioning) | No | No | Yes |
| Change table schema | No | No | Yes |
| Optimize file size | No | No | Yes |
| Validate the schema of existing data before adding the data | No | No | Yes |
| **Supported file formats** | Parquet, Avro, ORC | Parquet, Avro, ORC | Parquet, Avro, ORC, JSON, CSV |
| **Source table replacement by an Iceberg table** | No<br />(creates a new table,  but with additional steps you can replace the source table) | Yes<br />(creates a backup table and substitutes the source table with an Iceberg table) | No<br />(creates a new table) |
| **Source table impact** |  |  |  |
| File deletion operations on Iceberg table (`expire_snapshot `operations, dropping a table with purge) | Corrupts source table | Corrupts backup table | Safe, source unaffected |
| **Iceberg table impact** |  |  |  |
| Impact if source table files are removed | Corrupts Iceberg table | Corrupts Iceberg table | No impact on Iceberg table |
| Impact if new files are added on source table location | Not visible on new table<br />(need to incorporate partition with `add_files`) | Not visible on new table<br />(need to incorporate partition with `add_files`) | Not visible on new table<br />(need to `INSERT INTO` the new table) |
| **Cost** | Low | Low | Higher (full data rewrite) |
| **Migration speed** | Fast | Fast | Slower |
| **Can be used to migrate to Amazon S3 Tables** | No | No | Yes |
| **Requires manual DDL** | No<br />(schema and partitions are copied from source table) | No<br />(schema and partitions are copied from source table) | If using CTAS, requires only specifying the partitioning |
| **Best use** | Quick migration without rewriting data, allowing side-by-side use of Hive and Iceberg for testing or gradual transition. | Replacing a Hive table in place without rewriting data, when an immediate switchover is acceptable. | Full Iceberg optimization with data rewrite. Ideal when redesigning partitions or schema, or improving layout and performance. Always recommended if possible. |
