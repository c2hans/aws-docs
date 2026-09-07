---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-an-etl-service-pipeline-to-load-data-incrementally-from-amazon-s3-to-amazon-redshift-using-aws-glue.html
---

# Build an ETL service pipeline to load data incrementally from Amazon S3 to Amazon Redshift using AWS Glue
<a name="build-an-etl-service-pipeline-to-load-data-incrementally-from-amazon-s3-to-amazon-redshift-using-aws-glue"></a>

*Rohan Jamadagni and Arunabha Datta, Amazon Web Services*

## Summary
<a name="build-an-etl-service-pipeline-to-load-data-incrementally-from-amazon-s3-to-amazon-redshift-using-aws-glue-summary"></a>

This pattern provides guidance on how to configure Amazon Simple Storage Service (Amazon S3) for optimal data lake performance, and then load incremental data changes from Amazon S3 into Amazon Redshift by using AWS Glue, performing extract, transform, and load (ETL) operations.

The source files in Amazon S3 can have different formats, including comma-separated  values (CSV), XML, and JSON files. This pattern describes how you can use AWS Glue to convert the source files into a cost-optimized and performance-optimized  format like Apache Parquet. You can query Parquet files directly from Amazon Athena and Amazon Redshift Spectrum. You can also load Parquet files into Amazon Redshift, aggregate them, and share the aggregated data with consumers, or visualize the data by using Amazon Quick Sight.

## Prerequisites and limitations
<a name="build-an-etl-service-pipeline-to-load-data-incrementally-from-amazon-s3-to-amazon-redshift-using-aws-glue-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ An S3 source bucket that has the right privileges and contains CSV, XML, or JSON files.

**Assumptions**
+ The CSV, XML, or JSON source files are already loaded into Amazon S3 and are accessible from the account where AWS Glue and Amazon Redshift are configured.
+ Best practices for loading the files, splitting the files, compression, and using a manifest are followed, as discussed in the [Amazon Redshift documentation](https://docs.aws.amazon.com/redshift/latest/dg/t_Loading-data-from-S3.html).
+ The source file structure is unaltered.
+ The source system is able to ingest data into Amazon S3 by following the folder structure defined in Amazon S3.
+ The Amazon Redshift cluster spans a single Availability Zone. (This architecture is appropriate because AWS Lambda, AWS Glue, and Amazon Athena are serverless.) For high availability, cluster snapshots are taken at a regular frequency.

**Limitations**
+ The file formats are limited to those that are [currently supported by AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format.html).
+ Real-time downstream reporting isn't supported.

## Architecture
<a name="build-an-etl-service-pipeline-to-load-data-incrementally-from-amazon-s3-to-amazon-redshift-using-aws-glue-architecture"></a>

**Source technology stack**
+ S3 bucket with CSV, XML, or JSON files

**Target technology stack**
+ S3 data lake (with partitioned Parquet file storage)
+ Amazon Redshift

**Target architecture**

![Architecture for loading incremental changes from Amazon S3 to Amazon Redshift using AWS Glue.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/105b58ec-56c1-464a-8e69-f625360caa14/images/626aa365-e6e6-4874-a873-1c71adbe5306.png)

**Data flow**

![Data flow for loading incremental changes from Amazon S3 to Amazon Redshift using AWS Glue.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/105b58ec-56c1-464a-8e69-f625360caa14/images/29569e48-9f2d-4f48-bc59-1f33949d01ca.png)

## Tools
<a name="build-an-etl-service-pipeline-to-load-data-incrementally-from-amazon-s3-to-amazon-redshift-using-aws-glue-tools"></a>
+ [Amazon S3](https://aws.amazon.com/s3/) – Amazon Simple Storage Service (Amazon S3) is a highly scalable object storage service. Amazon S3 can be used for a wide range of storage solutions, including websites, mobile applications, backups, and data lakes.
+ [AWS Lambda](https://aws.amazon.com/lambda/) – AWS Lambda lets you run code without provisioning or managing servers. AWS Lambda is an event-driven service; you can set up your code to automatically initiate from other AWS services.
+ [Amazon Redshift](https://aws.amazon.com/redshift/) – Amazon Redshift is a fully managed, petabyte-scale data warehouse service. With Amazon Redshift, you can query petabytes of structured and semi-structured data across your data warehouse and your data lake using standard SQL.
+ [AWS Glue](https://aws.amazon.com/glue/) – AWS Glue is a fully managed ETL service that makes it easier to prepare and load data for analytics. AWS Glue discovers your data and stores the associated metadata (for example, table definitions and schema) in the AWS Glue Data Catalog. Your cataloged data is immediately searchable, can be queried, and is available for ETL.
+ [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) – AWS Secrets Manager facilitates protection and central management of secrets needed for application or service access. The service stores database credentials, API keys, and other secrets, and eliminates the need to hardcode sensitive information in plaintext format. Secrets Manager also offers key rotation to meet security and compliance needs. It has built-in integration for Amazon Redshift, Amazon Relational Database Service (Amazon RDS), and Amazon DocumentDB. You can store and centrally manage secrets by using the Secrets Manager console, the command-line interface (CLI), or Secrets Manager API and SDKs.
+ [Amazon Athena](https://aws.amazon.com/athena/) – Amazon Athena is an interactive query service that makes it easy to analyze data that's stored in Amazon S3. Athena is serverless and integrated with AWS Glue, so it can directly query the data that's cataloged using AWS Glue. Athena is elastically scaled to deliver interactive query performance.

## Epics
<a name="build-an-etl-service-pipeline-to-load-data-incrementally-from-amazon-s3-to-amazon-redshift-using-aws-glue-epics"></a>

### Create the S3 buckets and folder structure
<a name="create-the-s3-buckets-and-folder-structure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Analyze source systems for data structure and attributes. | Perform this task for each data source that contributes to the Amazon S3 data lake. | Data engineer |
| Define the partition and access strategy. | This strategy should be based on the frequency of data captures, delta processing, and consumption needs. Make sure that S3 buckets are not open to the public and that access is controlled by specific service role-based policies only. For more information, see the [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/using-folders.html). | Data engineer |
| Create separate S3 buckets for each data source type and a separate S3 bucket per source for the processed (Parquet) data. | Create a separate bucket for each source, and then create a folder structure that's based on the source system's data ingestion frequency; for example, `s3://source-system-name/date/hour`. For the processed (converted to Parquet format) files, create a similar structure; for example, `s3://source-processed-bucket/date/hour`. For more information about creating S3 buckets, see the [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html). | Data engineer |

### Create a data warehouse in Amazon Redshift
<a name="create-a-data-warehouse-in-amazon-redshift"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch the Amazon Redshift cluster with the appropriate parameter groups and maintenance and backup strategy. | Use the Secrets Manager database secret for admin user credentials while creating the Amazon Redshift cluster. For information about creating and sizing an Amazon Redshift cluster, see the [Amazon Redshift documentation](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/event-publishing-redshift-cluster.html) and the [Sizing Cloud Data Warehouses](https://d1.awsstatic.com/whitepapers/Size-Cloud-Data-Warehouse-on-AWS.pdf) whitepaper. | Data engineer |
| Create and attach the IAM service role to the Amazon Redshift cluster. | The AWS Identity and Access Management (IAM) service role ensures access to Secrets Manager and the source S3 buckets. For more information, see the AWS documentation on [authorization](https://docs.aws.amazon.com/redshift/latest/mgmt/authorizing-redshift-service.html) and [adding a role](https://docs.aws.amazon.com/redshift/latest/dg/c-getting-started-using-spectrum-add-role.html). | Data engineer |
| Create the database schema. | Follow Amazon Redshift best practices for table design. Based on the use case, choose the appropriate sort and distribution keys, and the best possible compression encoding. For best practices, see the [AWS documentation](https://docs.aws.amazon.com/redshift/latest/dg/c_designing-tables-best-practices.html). | Data engineer |
| Configure workload management. | Conﬁgure workload management (WLM) queues, short query acceleration (SQA), or concurrency scaling, depending on your requirements. For more information, see [Implementing workload management](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-implementing-workload-management.html) in the Amazon Redshift documentation. | Data engineer |

### Create a secret in Secrets Manager
<a name="create-a-secret-in-secrets-manager"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a new secret to store the Amazon Redshift sign-in credentials in Secrets Manager. | This secret stores the credentials for the admin user as well as individual database service users. For instructions, see the [Secrets Manager documentation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html). Choose **Amazon Redshift Cluster** as the secret type. Additionally, on the **Secret rotation** page, turn on the rotation. This will create the appropriate user in the Amazon Redshift cluster and will rotate the key secrets at defined intervals. | Data engineer |
| Create an IAM policy to restrict Secrets Manager access. | Restrict Secrets Manager access to only Amazon Redshift administrators and AWS Glue. | Data engineer |

### Configure AWS Glue
<a name="configure-aws-glue"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| In the AWS Glue Data Catalog, add a connection for Amazon Redshift. | For instructions, see the [AWS Glue documentation](https://docs.aws.amazon.com/glue/latest/dg/console-connections.html). | Data engineer |
| Create and attach an IAM service role for AWS Glue to access Secrets Manager, Amazon Redshift, and S3 buckets. | For more information, see the [AWS Glue documentation](https://docs.aws.amazon.com/glue/latest/dg/create-service-policy.html). | Data engineer |
| Define the AWS Glue Data Catalog for the source. | This step involves creating a database and required tables in the AWS Glue Data Catalog. You can either use a crawler to catalog the tables in the AWS Glue database, or deﬁne them as Amazon Athena external tables. You can also access the external tables deﬁned in Athena through the AWS Glue Data Catalog. See the AWS documentation for more information about [deﬁning the Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html) and [creating an external table](https://docs.aws.amazon.com/athena/latest/ug/creating-tables.html) in Athena. | Data engineer |
| Create an AWS Glue job to process source data. | The AWS Glue job can be a Python shell or PySpark to standardize, deduplicate, and cleanse the source data ﬁles. To optimize performance and avoid having to query the entire S3 source bucket, partition the S3 bucket by date, broken down by year, month, day, and hour as a pushdown predicate for the AWS Glue job. For more information, see the [AWS Glue documentation](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-partitions.html). Load the processed and transformed data to the processed S3 bucket partitions in Parquet format. You can query the Parquet ﬁles from Athena. | Data engineer |
| Create an AWS Glue job to load data into Amazon Redshift. | The AWS Glue job can be a Python shell or PySpark to load the data by upserting the data, followed by a complete refresh. For details, see the [AWS Glue documentation](https://docs.aws.amazon.com/glue/latest/dg/author-job.html) and the *Additional information* section. | Data engineer |
| (Optional) Schedule AWS Glue jobs by using triggers as necessary. | The incremental data load is primarily driven by an Amazon S3 event that causes an AWS Lambda function to call the AWS Glue job. Use AWS Glue trigger-based scheduling for any data loads that demand time-based instead of event-based scheduling. | Data engineer |

### Create a Lambda function
<a name="create-a-lambda-function"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create and attach an IAM service-linked role for AWS Lambda to access S3 buckets and the AWS Glue job. | Create an IAM service-linked role for AWS Lambda with a policy to read Amazon S3 objects and buckets, and a policy to access the AWS Glue API to start an AWS Glue job. For more information, see the [Knowledge Center](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-execution-role-s3-bucket/). | Data engineer |
| Create a Lambda function to run the AWS Glue job based on the defined Amazon S3 event. | The Lambda function should be initiated by the creation of the Amazon S3 manifest ﬁle. The Lambda function should pass the Amazon S3 folder location (for example, source\_bucket/year/month/date/hour) to the AWS Glue job as a parameter. The AWS Glue job will use this parameter as a pushdown predicate to optimize ﬁle access and job processing performance. For more information, see the [AWS Glue documentation](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html). | Data engineer |
| Create an Amazon S3 PUT object event to detect object creation, and call the respective Lambda function. | The Amazon S3 PUT object event should be initiated only by the creation of the manifest ﬁle. The manifest ﬁle controls the Lambda function and the AWS Glue job concurrency, and processes the load as a batch instead of processing individual ﬁles that arrive in a speciﬁc partition of the S3 source bucket. For more information, see the [Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html). | Data engineer |

## Related resources
<a name="build-an-etl-service-pipeline-to-load-data-incrementally-from-amazon-s3-to-amazon-redshift-using-aws-glue-resources"></a>
+ [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/gsg/GetStartedWithS3.html)
+ [AWS Glue documentation](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)
+ [Amazon Redshift documentation](https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html)
+ [AWS Lambda](https://aws.amazon.com/lambda/)
+ [Amazon Athena](https://aws.amazon.com/athena/)
+ [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)

## Additional information
<a name="build-an-etl-service-pipeline-to-load-data-incrementally-from-amazon-s3-to-amazon-redshift-using-aws-glue-additional"></a>

**Detailed approach for upsert and complete refresh**

**Upsert**: This is for datasets that require historical aggregation, depending on the business use case. Follow one of the approaches described in [Updating and inserting new data](https://docs.aws.amazon.com/redshift/latest/dg/t_updating-inserting-using-staging-tables-.html) (Amazon Redshift documentation) based on your business needs.

**Complete refresh**: This is for small datasets that don't need historical aggregations. Follow one of these approaches:

1. Truncate the Amazon Redshift table.

1. Load the current partition from the staging area

or:

1. Create a temporary table with current partition data.

1. Drop the target Amazon Redshift table.

1. Rename the temporary table to the target table.
