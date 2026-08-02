---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aurora-postgresql-integration/amazon-s3.html
---

# Aurora PostgreSQL-Compatible integration with Amazon S3
<a name="amazon-s3"></a>

Amazon Simple Storage Service (Amazon S3) is an object storage service that provides scalable, durable, highly available, and cost-effective data storage. Amazon Aurora PostgreSQL-Compatible Edition integrates with Amazon S3 through the `aws_s3` extension, which provides direct read and write access to S3 buckets. This integration facilitates data exchange, including data ingestion, backups, and other data-related operations.

## aws\_s3 use cases and high-level steps
<a name="aws-s3"></a>

The most common high-level use cases and benefits of integrating with Amazon S3 are the following:
+ **Data ingestion from Amazon S3** ‒ Use the `aws_s3` extension to load data from comma-separated values (CSV), JSON, or other file formats stored in Amazon S3 directly into an Aurora PostgreSQL-Compatible table. This is particularly useful for batch data-ingestion processes, ETL (extract, transform, and load) workflows, or data migrations.
+ **Data export to Amazon S3** ‒ Export data from Aurora PostgreSQL-Compatible tables to CSV, JSON, or other file formats, and store the data in Amazon S3. This is useful for data archiving, backups, or sharing data with other systems or services.
+ **Querying data directly from Amazon S3** ‒ Query data stored in CSV or JSON files in Amazon S3 directly from your Aurora PostgreSQL-Compatible database without loading the data into tables. This is useful for one-time data analysis or exploratory data processing.
+ **Backup and restore** ‒ Use Amazon S3 as a backup destination for your Aurora PostgreSQL-Compatible databases. This provides an additional layer of data protection, and you can restore databases from the Amazon S3 backups if needed.

To integrate your Aurora PostgreSQL-Compatible DB cluster with an S3 bucket, use the following high-level steps:

1. Connect to your Aurora PostgreSQL-Compatible cluster by using a PostgreSQL client, and create the `aws_s3` extension:

   ```
   create extension aws_s3
   ```

1. Set up access to an S3 bucket and required roles. For detailed steps, see the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PostgreSQL.S3Import.html#USER_PostgreSQL.S3Import.AccessPermission).

1. Use a psql query to import or export the data from the database:
   + To import the file from Amazon S3 to an Aurora PostgreSQL-Compatible table, run the following commands:

     ```
     SELECT aws_s3.table_import_from_s3( 'Table_Name', '',  '(format text)',
                                                        aws_commons.create_s3_uri('S3_BUCKETNAME', 'FileName.dat','Region-Name')  );
     ```
   + To export the file to Amazon S3 from the Aurora PostgreSQL-Compatible table, run the following command:

     ```
     SELECT * FROM aws_s3.query_export_to_s3('TABLE_NAME', aws_commons.create_s3_uri('S3_BUCKETNAME', 'FileName.dat', 'Region-Name') );
     ```
   + To export to Amazon S3 by using an SQL query, run the following command:

     ```
     SELECT * FROM aws_s3.query_export_to_s3('SELECT * FROM data_table', aws_commons.create_s3_uri('S3_BUCKETNAME', 'FileName.dat', 'Region-Name') );
     ```
