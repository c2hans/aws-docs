---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-amazon-redshift-cluster-to-an-aws-region-in-china.html
---

# Migrate an Amazon Redshift cluster to an AWS Region in China
<a name="migrate-an-amazon-redshift-cluster-to-an-aws-region-in-china"></a>

*Jing Yan, Amazon Web Services*

## Summary
<a name="migrate-an-amazon-redshift-cluster-to-an-aws-region-in-china-summary"></a>

This pattern provides a step-by-step approach to migrate an Amazon Redshift cluster to an AWS Region in China from another AWS Region.

This pattern uses SQL commands to recreate all the database objects, and uses the UNLOAD command to move this data from Amazon Redshift to an Amazon Simple Storage Service (Amazon S3) bucket in the source Region. The data is then migrated to an S3 bucket in the AWS Region in China. The COPY command is used to load data from the S3 bucket and transfer it to the target Amazon Redshift cluster.

Amazon Redshift doesn't currently support cross-Region features such as snapshot copying to AWS Regions in China. This pattern provides a way to work around that limitation. You can also reverse the steps in this pattern to migrate data from an AWS Region in China to another AWS Region.

## Prerequisites and limitations
<a name="migrate-an-amazon-redshift-cluster-to-an-aws-region-in-china-prereqs"></a>

*Prerequisites*
+ Active AWS accounts in both a China Region and an AWS Region outside China
+ Existing Amazon Redshift clusters in both a China Region and an AWS Region outside China

*Limitations*
+ This is an offline migration, which means the source Amazon Redshift cluster cannot perform write operations during the migration.

## Architecture
<a name="migrate-an-amazon-redshift-cluster-to-an-aws-region-in-china-architecture"></a>

**Source technology stack  **
+ Amazon Redshift cluster in an AWS Region outside China

**Target technology stack  **
+ Amazon Redshift cluster in an AWS Region in China

**Target architecture **

![Migration of Amazon Redshift cluster data in S3 bucket in an AWS Region to bucket in a China Region.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/f7d241d9-b700-406b-95a0-3e47e7f0fa60/images/b6016e3d-76db-4176-8f99-f804da94d3f2.png)

## Tools
<a name="migrate-an-amazon-redshift-cluster-to-an-aws-region-in-china-tools"></a>

**Tools**
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/gsg/GetStartedWithS3.html) – Amazon Simple Storage Service (Amazon S3) is an object storage service that offers scalability, data availability, security, and performance. You can use Amazon S3 to store data from Amazon Redshift, and you can copy data from an S3 bucket to Amazon Redshift.
+ [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html) – Amazon Redshift is a fully managed, petabyte-scale data warehouse service in the cloud.
+ [psql](https://www.postgresql.org/docs/8.4/app-psql.html) – psql is a terminal-based front-end to PostgreSQL.

## Epics
<a name="migrate-an-amazon-redshift-cluster-to-an-aws-region-in-china-epics"></a>

### Prepare for migration in the source Region
<a name="prepare-for-migration-in-the-source-region"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch and configure an EC2 instance in the source Region. | Sign in to the AWS Management Console and open the Amazon Elastic Compute Cloud (Amazon EC2) console. Your current Region is displayed in the navigation bar at the top of the screen. This Region cannot be an AWS Region in China. From the Amazon EC2 console dashboard, choose "Launch instance," and create and configure an EC2 instance. Important: Ensure your EC2 security groups for inbound rules allow unrestricted access to TCP port 22 from your source machine. For instructions on how to launch and configure an EC2 instance, see the "Related resources" section. | DBA, Developer |
| Install the psql tool. | Download and install PostgreSQL. Amazon Redshift does not provide the psql tool, it is installed with PostgreSQL. For more information about using psql and installing PostgreSQL tools, see the "Related resources" section. | DBA |
| Record the Amazon Redshift cluster details.  | Open the Amazon Redshift console, and choose "Clusters" in the navigation pane. Then choose the Amazon Redshift cluster name from the list. On the "Properties" tab, in the "Database configurations" section, record the "Database name" and "Port." Open the "Connection details" section and record the "Endpoint," which is in the "endpoint:<port>/<databasename>" format. Important: Ensure your Amazon Redshift security groups for inbound rules allow unrestricted access to TCP port 5439 from your EC2 instance. | DBA |
| Connect psql to the Amazon Redshift cluster.  | At a command prompt, specify the connection information by running the "psql -h <endpoint> -U <userid> -d <databasename> -p <port>" command. At the psql password prompt, enter the password for the "<userid>" user. You are then connected to the Amazon Redshift cluster and can interactively enter commands. | DBA |
| Create an S3 bucket.  | Open the Amazon S3 console, and create an S3 bucket to hold the files exported from Amazon Redshift. For instructions on how to create an S3 bucket, see the "Related resources" section. | DBA, AWS General |
| Create an IAM policy that supports unloading data. | Open the AWS Identity and Access Management (IAM) console and choose "Policies." Choose "Create policy," and choose the "JSON" tab. Copy and paste the IAM policy for unloading data from the "Additional information" section. Important: Replace "s3\_bucket\_name" with your S3 bucket’s name. Choose "Review policy," and enter a name and description for the policy. Choose "Create policy." | DBA |
| Create an IAM role to allow UNLOAD operation for Amazon Redshift. | Open the IAM console and choose "Roles." Choose "Create role," and choose "AWS service" in "Select type of trusted entity." Choose "Redshift" for the service, choose "Redshift – Customizable," and then choose "Next." Choose the "Unload" policy you created earlier, and choose "Next." Enter a "Role name," and choose "Create role." | DBA |
| Associate IAM role with the Amazon Redshift cluster.  | Open the Amazon Redshift console, and choose "Manage IAM roles." Choose "Available roles" from the dropdown menu and choose the role you created earlier. Choose "Apply changes." When the "Status" for the IAM role on the "Manage IAM roles" shows as "In-sync", you can run the UNLOAD command. | DBA |
| Stop write operations to the Amazon Redshift cluster. | You must remember to stop all write operations to the source Amazon Redshift cluster until the migration is complete. | DBA |

### Prepare for migration in the target Region
<a name="prepare-for-migration-in-the-target-region"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch and configure an EC2 instance in the target Region. | Sign in to the AWS Management Console for a Region in China, either Beijing or Ningxia. From the Amazon EC2 console, choose "Launch instance," and create and configure an EC2 instance. Important: Make sure your Amazon EC2 security groups for inbound rules allow unrestricted access to TCP port 22 from your source machine. For further instructions on how to launch and configure an EC2 instance, see the "Related resources" section. | DBA |
| Record the Amazon Redshift cluster details.  | Open the Amazon Redshift console, and choose "Clusters" in the navigation pane. Then choose the Amazon Redshift cluster name from the list. On the "Properties" tab, in the "Database configurations" section, record the "Database name" and "Port." Open the "Connection details" section and record the "Endpoint," which is in the "endpoint:<port>/<databasename>" format. Important: Make sure your Amazon Redshift security groups for inbound rules allow unrestricted access to TCP port 5439 from your EC2 instance. | DBA |
| Connect psql to the Amazon Redshift cluster.  | At a command prompt, specify the connection information by running the "psql -h <endpoint> -U <userid> -d <databasename> -p <port>" command. At the psql password prompt, enter the password for the "<userid>" user. You are then connected to the Amazon Redshift cluster and can interactively enter commands. | DBA |
| Create an S3 bucket.  | Open the Amazon S3 console, and create an S3 bucket to hold the exported files from Amazon Redshift. For help with this and other stories, see the "Related resources" section. | DBA |
| Create an IAM policy that supports copying data. | Open the IAM console and choose "Policies." Choose "Create policy," and choose the "JSON" tab. Copy and paste the IAM policy for copying data from the "Additional information" section. Important: Replace "s3\_bucket\_name" with your S3 bucket’s name. Choose "Review policy," enter a name and description for the policy. Choose "Create policy." | DBA |
| Create an IAM role to allow COPY operation for Amazon Redshift. | Open the IAM console and choose "Roles." Choose "Create role," and choose "AWS service" in "Select type of trusted entity." Choose "Redshift" for the service, choose "Redshift – Customizable," and then choose "Next." Choose the "Copy" policy you created earlier, and choose "Next." Enter a "Role name," and choose "Create role." | DBA |
| Associate IAM role with the Amazon Redshift cluster.  | Open the Amazon Redshift console, and choose "Manage IAM roles." Choose "Available roles" from the dropdown menu and choose the role you created earlier. Choose "Apply changes." When the "Status" for the IAM role on the "Manage IAM roles" shows as "In-sync", you can run the "COPY" command. | DBA |

### Verify source data and object information before beginning the migration
<a name="verify-source-data-and-object-information-before-beginning-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify the rows in the source Amazon Redshift tables. | Use the scripts in the "Additional information" section to verify and record the number of rows in the source Amazon Redshift tables. Remember to split the data evenly for the UNLOAD and COPY scripts. This will improve the data unloading and loading efficiency, because the data quantity covered by each script will be balanced. | DBA |
| Verify the number of database objects in the source Amazon Redshift cluster. | Use the scripts in the "Additional information" section to verify and record the number of databases, users, schemas, tables, views, and user-defined functions (UDFs) in your source Amazon Redshift cluster. | DBA |
| Verify SQL statement results before migration. | Some SQL statements for data validation should be sorted according to actual business and data situations. This is to verify the imported data to ensure it is consistent and displayed correctly. | DBA |

### Migrate data and objects to the target Region
<a name="migrate-data-and-objects-to-the-target-region"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Generate Amazon Redshift DDL scripts.  | Generate Data Definition Language (DDL) scripts by using the links from the "SQL statements to query Amazon Redshift" section in the "Additional information" section. These DDL scripts should include the "create user," "create schema," "privileges on schema to user," "create table/view," "privileges on objects to user," and "create function" queries. | DBA |
| Create objects in the Amazon Redshift cluster for the target Region. | Run the DDL scripts by using the AWS Command Line Interface (AWS CLI) in the AWS Region in China. These scripts will create objects in the Amazon Redshift cluster for the target Region. | DBA |
| Unload source Amazon Redshift cluster data to the S3 bucket. | Run the UNLOAD command to unload data from the Amazon Redshift cluster in the source Region to the S3 bucket. | DBA, Developer  |
| Transfer source Region S3 bucket data to target Region S3 bucket. | Transfer the data from your source Region S3 bucket to the target S3 bucket. Because the "$ aws s3 sync" command cannot be used, make sure you use the process outlined in the "Transferring Amazon S3 data from AWS Regions to AWS Regions in China" article in the "Related resources" section. | Developer |
|  Load data into the target Amazon Redshift cluster.  | In the psql tool for your target Region, run the COPY command to load data from the S3 bucket to the target Amazon Redshift cluster. | DBA |

### Verify the data in the source and target Regions after the migration
<a name="verify-the-data-in-the-source-and-target-regions-after-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify and compare the number of rows in the source and target tables. | Verify and compare the number of table rows in the source and target Regions to ensure all are migrated. | DBA |
| Verify and compare the number of source and target database objects. | Verify and compare all database objects in the source and target Regions to ensure all are migrated. | DBA |
| Verify and compare SQL script results in the source and target Regions. | Run the SQL scripts prepared before the migration. Verify and compare the data to ensure that the SQL results are correct. | DBA |
| Reset the passwords of all users in the target Amazon Redshift cluster.  | After the migration is complete and all data is verified, you should reset all user passwords for the Amazon Redshift cluster in the AWS Region in China. | DBA |

## Related resources
<a name="migrate-an-amazon-redshift-cluster-to-an-aws-region-in-china-resources"></a>
+ [Transferring Amazon S3 data from AWS Regions to AWS Regions in China](https://aws.amazon.com/cn/blogs/storage/transferring-amazon-s3-data-from-aws-regions-to-aws-regions-in-china/)
+ [Creating an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html)
+ [Resetting an Amazon Redshift user password](https://docs.aws.amazon.com/redshift/latest/dg/r_ALTER_USER.html)
+ [psql documentation](https://www.postgresql.org/docs/8.4/static/app-psql.html)

## Additional information
<a name="migrate-an-amazon-redshift-cluster-to-an-aws-region-in-china-additional"></a>

*IAM policy for unloading data*

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:ListBucket"],
      "Resource": ["arn:aws:s3:::s3_bucket_name"]
    },
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:DeleteObject"],
      "Resource": ["arn:aws:s3:::s3_bucket_name/*"]
    }
  ]
}
```

*IAM policy for copying data*

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:ListBucket"],
      "Resource": ["arn:aws:s3:::s3_bucket_name"]
    },
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::s3_bucket_name/*"]
    }
  ]
}
```

*SQL statements to query Amazon Redshift*

```
##Database

select * from pg_database where datdba>1;

##User

select * from pg_user where usesysid>1;

##Schema

SELECT n.nspname AS "Name",

  pg_catalog.pg_get_userbyid(n.nspowner) AS "Owner"

FROM pg_catalog.pg_namespace n

WHERE n.nspname !~ '^pg_' AND n.nspname <> 'information_schema'

ORDER BY 1;

##Table

select count(*) from pg_tables where schemaname not in ('pg_catalog','information_schema');

select schemaname,count(*) from pg_tables where schemaname not in ('pg_catalog','information_schema') group by schemaname order by 1;

##View

SELECT

    n.nspname AS schemaname,c.relname AS viewname,pg_catalog.pg_get_userbyid(c.relowner) as "Owner"

FROM

    pg_catalog.pg_class AS c

INNER JOIN

    pg_catalog.pg_namespace AS n

    ON c.relnamespace = n.oid

WHERE relkind = 'v' and n.nspname not in ('information_schema','pg_catalog');

##UDF

SELECT

   n.nspname AS schemaname,

   p.proname AS proname,

   pg_catalog.pg_get_userbyid(p.proowner) as "Owner"

FROM pg_proc p

LEFT JOIN pg_namespace n on n.oid = p.pronamespace

WHERE p.proowner != 1;
```

*SQL scripts to generate DDL statements*
+ [Get\_schema\_priv\_by\_user script](https://github.com/awslabs/amazon-redshift-utils/blob/master/src/AdminViews/v_get_schema_priv_by_user.sql)
+ [Generate\_tbl\_ddl script](https://github.com/awslabs/amazon-redshift-utils/blob/master/src/AdminViews/v_generate_tbl_ddl.sql)
+ [Generate\_view\_ddl](https://github.com/awslabs/amazon-redshift-utils/blob/master/src/AdminViews/v_generate_view_ddl.sql)
+ [Generate\_user\_grant\_revoke\_ddl](https://github.com/awslabs/amazon-redshift-utils/blob/master/src/AdminViews/v_generate_user_grant_revoke_ddl.sql)
+ [Generate\_udf\_ddl](https://github.com/awslabs/amazon-redshift-utils/blob/master/src/AdminViews/v_generate_udf_ddl.sql)
