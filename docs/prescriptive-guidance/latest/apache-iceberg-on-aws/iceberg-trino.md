---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/iceberg-trino.html
---

# Working with Iceberg tables by using Trino
<a name="iceberg-trino"></a>

This section describes how to set up and operate Iceberg tables by using [Trino](https://trino.io/docs/current/) on [Amazon EMR](https://docs.aws.amazon.com/emr/). The examples are boilerplate code that you can run on an Amazon EMR on EC2 cluster. The code examples and configurations in this section assume that you're using Amazon EMR release **emr-7.9.0**.

## Amazon EMR on EC2 setup
<a name="trino-emr-setup"></a>

1. Create an `iceberg.properties` file with the following content. The `iceberg.file-format=parquet` setting determines the default storage format for new tables if the format isn't explicitly specified in the `CREATE TABLE` statement.

   ```
   connector.name=iceberg
   iceberg.catalog.type=glue
   iceberg.file-format=parquet
   fs.native-s3.enabled=true
   ```

1. Upload the `iceberg.properties` file to your S3 bucket.

1. Create a bootstrap action that copies the `iceberg.properties` file from your S3 bucket and stores it as a Trino configuration file on the Amazon EMR cluster that you will be creating. Make sure to replace `<S3-bucket-name>` with your S3 bucket name.

   ```
   #!/bin/bash
   set -ex
   sudo aws s3 cp s3://<S3-bucket-name>/iceberg.properties /etc/trino/conf/catalog/iceberg.properties
   ```

1. Create an Amazon EMR cluster with Trino installed and specify the execution of the previous script as a bootstrap action. Here's a sample AWS Command Line Interface (AWS CLI) command for creating the cluster:

   ```
   aws emr create-cluster --release-label emr-7.9.0 \
   --applications Name=Trino \
   --region <region> \
   --name Trino_Iceberg_Cluster \
   --bootstrap-actions '[{"Path":"s3://<S3-bucket-name>/bootstrap.sh","Name":"Add iceberg.properties"}]' \
   --instance-groups '[{"InstanceGroupType":"MASTER","InstanceCount":1,"InstanceType":"m5.xlarge"},{"InstanceGroupType":"CORE","InstanceCount":3,"InstanceType":"m5.xlarge"}]' \
   --service-role "<IAM-service-role>" \
   --ec2-attributes '{"KeyName":"<key-name>","InstanceProfile":"<EMR-EC2-instance-profile>"}'
   ```

   where you replace:
   + `<S3-bucket-name>` with your S3 bucket name
   + `<region>` with your specific AWS Region
   + `<key-name>` with your key pair. If the key pair doesn't exist, it will be created.
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

## Creating Iceberg tables
<a name="trino-create-table"></a>

To create an Iceberg table, you can use the `CREATE TABLE` statement.  Here's an example of creating a partitioned table that uses Iceberg hidden partitioning:

```
CREATE TABLE iceberg.iceberg_db.iceberg_table (
             userid int,
             firstname varchar,
             city varchar)
        WITH (
             format = 'PARQUET',
             partitioning = ARRAY['city', 'bucket(userid, 16)'],
             location = 's3://<S3-bucket>/<prefix>');
```

**Note**
If you don't specify the format, the `iceberg.file-format` value that you configured in the previous section will be used.

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
<a name="trino-read-data"></a>

You can read the latest status of your Iceberg table by using a `SELECT` statement, as follows:

```
SELECT * FROM iceberg.iceberg_db.iceberg_table;
```

## Upserting data into Iceberg tables
<a name="trino-upsert-data"></a>

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
<a name="trino-delete-data"></a>

To delete data from an Iceberg table, use the `DELETE FROM` expression and specify a filter that matches the rows to delete. Here's an example:

```
DELETE FROM iceberg.iceberg_db.iceberg_table WHERE userid IN (1003, 1004);
```

## Querying Iceberg table metadata
<a name="trino-query-metadata"></a>

Iceberg provides access to its metadata through SQL. You can access the metadata for any given table (`<table_name>`)  by querying the namespace `"<table_name>.$<metadata_table>"`. For a complete list of metadata tables, see [Inspecting tables](https://iceberg.apache.org/docs/latest/spark-queries/#inspecting-tables) in the Iceberg documentation.

Here's an example list of queries to inspect Iceberg metadata:

```
SELECT  FROM iceberg.iceberg_db."iceberg_table$snapshots";
SELECT  FROM iceberg.iceberg_db."iceberg_table$history";
SELECT  FROM iceberg.iceberg_db."iceberg_table$partitions";
SELECT  FROM iceberg.iceberg_db."iceberg_table$files";
SELECT  FROM iceberg.iceberg_db."iceberg_table$manifests";
SELECT  FROM iceberg.iceberg_db."iceberg_table$refs";
SELECT * FROM iceberg.iceberg_db."iceberg_table$metadata_log_entries";
```

For example, this query:

```
 SELECT * FROM iceberg.iceberg_db."iceberg_table$snapshots";
```

provides the output:

![Output from querying Iceberg table metadata.](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/25cd9e5f-eb1a-4ffd-b2c1-de25e1a2d5fb.png)

## Using time travel
<a name="trino-time-travel"></a>

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

## Considerations when using Iceberg with Trino
<a name="trino-considerations"></a>

Trino write operations on Iceberg tables follow the [merge-on-read](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/best-practices-write.html#write-update-strategy) design, so they create positional delete files instead of rewriting entire data files that are impacted by updates or deletes. If you want to use the copy-on-write approach, consider using Spark for write operations.
