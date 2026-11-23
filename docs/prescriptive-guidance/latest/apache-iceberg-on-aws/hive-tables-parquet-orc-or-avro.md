---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/hive-tables-parquet-orc-or-avro.html
---

# Hive tables (Parquet, ORC, or Avro)

Iceberg provides three Spark procedures for in-place migration from Hive-format tables:
+ `snapshot` — creates a new Iceberg table alongside the source table. The source table stays unchanged.
+ `migrate` — replaces the source table in place with an Iceberg table and backs up the original. Works with Hive Metastore; a workaround is needed for AWS Glue Data Catalog (see [Replicating the migrate procedure in AWS Glue Data Catalog](#replicating-the-migrate-procedure-in-aws-glue-data-catalog)).
+ `add_files` — incorporates additional data files (from new or modified partitions) into an already-migrated Iceberg table. Typically used to keep the Iceberg table in sync with the source table after the initial `snapshot` or `migrate` call (see [Keeping Iceberg tables in sync after in-place migration](#keeping-iceberg-tables-in-sync-after-in-place-migration)).

Say you have a Parquet-based `products` table that was created and populated in Athena as follows. Replace `<bucket-name>` with your own bucket name:

```
CREATE EXTERNAL TABLE mydb.products (
    product_id INT,
    product_name STRING
)
PARTITIONED BY (category STRING)
STORED AS PARQUET
LOCATION 's3://<bucket-name>/products/';

INSERT INTO mydb.products
VALUES
    (1001, 'Smartphone', 'electronics'),
    (1002, 'Laptop', 'electronics'),
    (2001, 'T-Shirt', 'clothing'),
    (2002, 'Jeans', 'clothing');
```

The following sections show how each procedure works with this table.

## Option 1: snapshot procedure
<a name="option-1-snapshot-procedure"></a>

The `snapshot` procedure creates a new Iceberg table that has a different name but replicates the schema and partitioning of the source table. This operation leaves the source table completely unchanged both during and after the action. It effectively creates a lightweight copy of the table, which is particularly useful for testing scenarios or data exploration without risking modifications to the original data source. This approach enables a transition period where both the original table and the Iceberg table remain available (see the notes at the end of this section). When you complete testing, you can move your new Iceberg table to production by transitioning all writers and readers to the new table.

You can run the `snapshot` procedure by using Spark in any Amazon EMR deployment model (for example, Amazon EMR on EC2, Amazon EMR on EKS, EMR Serverless) and AWS Glue.

To test in-place migration with the `snapshot` Spark procedure, follow these steps:

1. Launch a Spark application and configure the Spark session with the following settings:
   + `"spark.sql.extensions":"org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"`
   + `"spark.sql.catalog.spark_catalog":"org.apache.iceberg.spark.SparkSessionCatalog"`
   + `"spark.sql.catalog.spark_catalog.type":"glue"`
   + `"spark.hadoop.hive.metastore.client.factory.class":"com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory"`

1. Run the `snapshot` procedure to create a new Iceberg table that points to the original table data files. Replace `<bucket-name>` with your own bucket name:

   ```
   spark.sql(f"""
   CALL system.snapshot(
   source_table => 'mydb.products',
   table => 'mydb.products_iceberg',
   location => 's3://<bucket-name>/products_iceberg/'
   )
   """
   ).show(truncate=False)
   ```

   The output dataframe contains the `imported_files_count` (the number of files that were added).

1. Validate the new table by querying it:

   ```
   spark.sql(f"""
   SELECT * FROM mydb.products_iceberg LIMIT 10
   """
   ).show(truncate=False)
   ```

Notes:
+ After you run the procedure, any data file modifications on the source table will throw the generated table out of sync. New files that you add won't be visible in the Iceberg table, and files that you remove will affect query capabilities in the Iceberg table. To avoid the synchronization issues:
  + If the new Iceberg table is intended for production use, stop all processes that write to the original table and redirect them to the new table.
  + If you need a transition period or if the new Iceberg table is for testing purposes, see [Keeping Iceberg tables in sync after in-place migration](#keeping-iceberg-tables-in-sync-after-in-place-migration) later in this section for guidance on maintaining table synchronization.
+ When you use the `snapshot` procedure, the `gc.enabled` property is set to `false` in the table properties of the created Iceberg table. This setting prohibits actions such as `expire_snapshots`, `remove_orphan_files`, or `DROP TABLE` with the `PURGE` option, which would physically delete data files. Iceberg delete or merge operations, which do not directly impact source files, are still allowed.
+ To make your new Iceberg table fully functional, with no limits on actions that physically delete data files, you can change the `gc.enabled` table property to `true`. However, this setting will allow actions that impact source data files, which could corrupt access to the original table. Therefore, change the `gc.enabled` property only if you no longer need to maintain the original table's functionality. For example:

  ```
  spark.sql(f"""
  ALTER TABLE mydb.products_iceberg
  SET TBLPROPERTIES ('gc.enabled' = 'true');
  """)
  ```

## Option 2: migrate procedure
<a name="option-2-migrate-procedure"></a>

The `migrate` procedure creates a new Iceberg table that has the same name, schema, and partitioning as the source table. When this procedure runs, it locks the source table and renames it to `<table_name>_BACKUP_` (or a custom name specified by the `backup_table_name` procedure parameter).

**Note**
 If you set the `drop_backup` procedure parameter to `true`, the original table will not be retained as a backup.

Consequently, the `migrate` table procedure requires all modifications that affect the source table to be stopped before the action is performed. Before you run the `migrate` procedure:
+ Stop all writers that interact with the source table.
+ Modify readers and writers that don't natively support Iceberg to enable Iceberg support.

For example:
+ Athena continues to work without modification.
+ Spark requires:
  + Iceberg Java Archive (JAR) files to be included in the classpath (see the [Working with Iceberg in Amazon EMR (Spark)](working-with-iceberg-in-amazon-emr-spark.md) and [Working with Iceberg in AWS Glue](iceberg-glue.md) sections earlier in this guide).
  + The following Spark session catalog configurations (using `SparkSessionCatalog` to add Iceberg support while maintaining built-in catalog functionalities for non-Iceberg tables):
    + `"spark.sql.extensions":"org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"`
    + `"spark.sql.catalog.spark_catalog":"org.apache.iceberg.spark.SparkSessionCatalog"`
    + `"spark.sql.catalog.spark_catalog.type":"glue"`
    + `"spark.hadoop.hive.metastore.client.factory.class":"com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory"`

After you run the procedure, you can restart your writers with their new Iceberg configuration.

Currently, the `migrate` procedure isn't compatible with the AWS Glue Data Catalog, because the Data Catalog doesn't support the `RENAME` operation. Therefore, we recommend that you use this procedure only when you're working with Hive Metastore. If you're using the Data Catalog, see the [**Replicating the migrate procedure in AWS Glue Data Catalog**](#replicating-the-migrate-procedure-in-aws-glue-data-catalog) section for an alternative approach.

You can run the `migrate` procedure across all Amazon EMR deployment models (Amazon EMR on EC2, Amazon EMR on EKS, EMR Serverless) and AWS Glue, but it requires a configured connection to Hive Metastore. Amazon EMR on EC2 is the recommended choice because it provides a built-in Hive Metastore configuration, which minimizes setup complexity.

To test in-place migration with the `migrate` Spark procedure from an Amazon EMR on EC2 cluster that's configured with Hive Metastore, follow these steps:

1. Launch a Spark application and configure the Spark session to use the Iceberg Hive catalog implementation. For example, if you're using the `pyspark` CLI:

   ```
   pyspark --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions --conf spark.sql.catalog.spark_catalog=org.apache.iceberg.spark.SparkSessionCatalog --conf spark.sql.catalog.spark_catalog.type=hive
   ```

1. Create a `products` table in Hive Metastore. This is the source table, which already exists in a typical migration.

1. Create the `products` external Hive table in Hive Metastore to point to the existing data in Amazon S3. Replace `<bucket-name>` with your own bucket name:

   ```
   spark.sql(f"""
   CREATE EXTERNAL TABLE products (
       product_id INT,
       product_name STRING
   )
   PARTITIONED BY (category STRING)
   STORED AS PARQUET
   LOCATION 's3://<bucket-name>/products/';
   """
   )
   ```

1. Add the existing partitions by using the `MSCK REPAIR TABLE` command:

   ```
   spark.sql(f"""
   MSCK REPAIR TABLE products
   """
   )
   ```

1. Confirm that the table contains data by running a `SELECT` query:

   ```
   spark.sql(f"""
   SELECT * FROM products
   """
   ).show(truncate=False)
   ```

1. Use the Iceberg `migrate` procedure:

   ```
   df_res=spark.sql(f"""
   CALL system.migrate(
   table => 'default.products'
   )
   """
   )

   df_res.show()
   ```

   The output dataframe contains the `migrated_files_count` (the number of files that were added to the Iceberg table).

1. Confirm that the backup table was created:

   ```
   spark.sql("show tables").show()
   ```

1. Validate the operation by querying the Iceberg table:

   ```
   spark.sql(f"""
   SELECT * FROM products
   """
   ).show(truncate=False)
   ```

**Note**
 After you run the procedure, all current processes that query or write to the source table will be impacted if they aren't properly configured with Iceberg support. Therefore, we recommend that you follow these steps: (1) Stop all processes that use the source table before migration. (2) Perform the migration. (3) Reactivate the processes with the proper Iceberg settings.

**Note**
 If data file modifications occur during the migration process (new files are added or files are removed), the generated table will get out of sync. For synchronization options, see [Keeping Iceberg tables in sync after in-place migration](#keeping-iceberg-tables-in-sync-after-in-place-migration).

## Replicating the migrate procedure in AWS Glue Data Catalog
<a name="replicating-the-migrate-procedure-in-aws-glue-data-catalog"></a>

You can replicate the migrate procedure's outcome in AWS Glue Data Catalog (backing up the original table and replacing it with an Iceberg table) by following these steps:

1. Use the `snapshot` procedure to create a new Iceberg table that points to the original table's data files.

1. Back up the original table metadata in the Data Catalog:

   1. Use the [GetTable](https://docs.aws.amazon.com/glue/latest/webapi/API_GetTable.html) API to retrieve the source table definition.

   1. Use the [GetPartitions](https://docs.aws.amazon.com/glue/latest/webapi/API_GetPartitions.html) API to retrieve the source table partition definition.

   1. Use the [CreateTable](https://docs.aws.amazon.com/glue/latest/webapi/API_CreateTable.html) API to create a backup table in the Data Catalog.

   1. Use the [CreatePartition](https://docs.aws.amazon.com/glue/latest/webapi/API_CreatePartition.html) or [BatchCreatePartition](https://docs.aws.amazon.com/glue/latest/webapi/API_BatchCreatePartition.html) API to register partitions to the backup table in the Data Catalog.

1. Change the `gc.enabled` Iceberg table property to `true` to enable full table operations.

1. Use the [DeleteTable](https://docs.aws.amazon.com/glue/latest/webapi/API_DeleteTable.html) API to remove the original table from the Data Catalog. This removes only the table definition. The data files in Amazon S3 are not deleted.

1. In the Glue Data Catalog, retrieve the `metadata_location` table property of the Iceberg table created by the `snapshot` procedure, and note the location of the latest `metadata.json` file.

1. Use the [DeleteTable](https://docs.aws.amazon.com/glue/latest/webapi/API_DeleteTable.html) API to remove the Iceberg table created by the `snapshot` procedure from the Data Catalog. The metadata and data files in Amazon S3 are not deleted.

1. Register the new table in the Data Catalog by using the `register_table` procedure with the original table name and the `metadata.json` location you noted in step 5:

   ```
   spark.sql(f"""
   CALL system.register_table(
       table => 'mydb.products',
       metadata_file => '{iceberg_metadata_file}'
   )
   """
   ).show(truncate=False)
   ```

## Keeping Iceberg tables in sync after in-place migration
<a name="keeping-iceberg-tables-in-sync-after-in-place-migration"></a>

The `add_files` procedure provides a flexible way to incorporate existing data into Iceberg tables. Specifically, it registers existing data files (such as Parquet files) by referencing their absolute paths in Iceberg's metadata layer. By default, the procedure adds files from all table partitions to an Iceberg table, but you can selectively add files from specific partitions. This selective approach is particularly useful in several scenarios:
+ When new partitions are added to the source table after initial migration.
+ When data files are added to or removed from existing partitions after initial migration. However, re-adding modified partitions requires partition deletion first (see below).

Here are some considerations for using the `add_files` procedure after in-place migration (`snapshot` or `migrate`) has been performed, to keep the new Iceberg table in sync with the source data files:
+ When new data is added to new partitions in the source table, use the `add_files` procedure with the `partition_filter` option to selectively incorporate these additions into the Iceberg table:

  ```
  spark.sql(f"""
  CALL system.add_files(
  source_table => 'mydb.products',
  table => 'mydb.products_iceberg',
  partition_filter => map('category', 'electronics')
  )
  """).show(truncate=False)
  ```

  or (Replace `<bucket-name>` with your own bucket name):

  ```
  spark.sql(f"""
  CALL system.add_files(
  source_table => '`parquet`.`s3://<bucket-name>/products/`',
  table => 'mydb.products_iceberg',
  partition_filter => map('category', 'electronics')
  )
  """).show(truncate=False)
  ```
+ The `add_files` procedure scans for files either in the entire source table or in specific partitions when you specify the `partition_filter` option, and attempts to add all files it finds to the Iceberg table. By default, the `check_duplicate_files` procedure property is set to `true`, which prevents the procedure from running if files already exist in the Iceberg table. This is important because there is no built-in option to skip previously added files, and disabling `check_duplicate_files` will cause files to be added twice, creating duplicates. When new files are added to the source table, follow these steps:

1. For new partitions, use `add_files` with a `partition_filter` to import only files from the new partition.

1. For existing partitions, first delete the partition from the Iceberg table, and then re-run `add_files` for that partition, specifying the `partition_filter`. For example - replace `<bucket-name>` with your own bucket name:

   ```
   # We initially perform in-place migration with snapshot
   spark.sql(f"""
   CALL system.snapshot(
   source_table => 'mydb.products',
   table => 'mydb.products_iceberg',
   location => 's3://<bucket-name>/products_iceberg/'
   )
   """
   ).show(truncate=False)

   # Then on the source table, some new files were generated under the category='electronics' partition
   spark.sql("""
   INSERT INTO mydb.products
   VALUES (1003, 'Tablet', 'electronics')
   """)

   # We delete the modified partition from the Iceberg table (this is a metadata operation only)
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

**Note**
Every `add_files` operation generates a new Iceberg table snapshot with appended data.

**Choosing between snapshot and migrate**:

|
|
| **Question** | **Recommendation** | **Explanation** |
| --- |--- |--- |
| Do you want to quickly migrate without rewriting data while keeping both Hive and Iceberg tables accessible for testing or gradual transition? | `snapshot` followed by `add_files` | Use `snapshot` to create a new Iceberg table by cloning the schema and referencing data files, without modifying the source table. Use `add_files` to incorporate partitions that were added or modified after migration (re-adding modified partitions requires partition deletion first). |
| Are you using Hive Metastore and do you want to replace your Hive table with an Iceberg table immediately, without rewriting the data? | `migrate` followed by `add_files` | Use `migrate` to create an Iceberg table, back up the source table, and replace the original table with the Iceberg version. Compatible with Hive Metastore but not with AWS Glue Data Catalog. Use `add_files` to incorporate partitions that were added or modified after migration. |
| Are you using AWS Glue Data Catalog and do you want to replace your Hive table with an Iceberg table immediately, without rewriting the data? | [Adaptation of the ](#replicating-the-migrate-procedure-in-aws-glue-data-catalog)`migrate`[ procedure (see Replicating the migrate procedure in AWS Glue Data Catalog), followed by ](#replicating-the-migrate-procedure-in-aws-glue-data-catalog)`add_files` | Replicate `migrate` behavior with `snapshot` \+ Glue-API metadata backup \+ `gc.enabled = true` \+ drop original \+ `register_table`. Requires manual handling of AWS Glue API calls for the metadata backup. |
