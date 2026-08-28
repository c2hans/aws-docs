---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/export-data-by-using-aws-glue.html
---

# Export data by using AWS Glue
<a name="export-data-by-using-aws-glue"></a>

You can archive MySQL data in Amazon S3 by using AWS Glue, which is a serverless analytical service for big data scenarios. AWS Glue is powered by Apache Spark, a widely used distributed cluster-computing framework that supports many database sources.

The off-loading of archived data from the database to Amazon S3 can be performed with a few lines of code in an AWS Glue job. The biggest advantage that AWS Glue offers is horizontal scalability and a pay-as-you-go model, providing operational efficiency and cost optimization.

The following diagram shows a basic architecture for database archiving.

![Description follows the diagram.](http://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/images/guide-img/1d38fd71-63ca-45ea-bf1f-9f493d5364d0/images/5db5ff9a-6662-4418-9d3c-6bc1eceaf572.png)

1. MySQL database creates the archive or backup table to be off-loaded in Amazon S3.

1. An AWS Glue job is initiated by one of the following approaches:
   + Synchronously as a step within an [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) state machine
   + Asynchronously by an [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) event
   + Through a manual request by using AWS CLI or an [AWS SDK](https://docs.aws.amazon.com/glue/latest/dg/sdk-general-information-section.html)

1. DB credentials are retrieved from [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html).

1. The AWS Glue job uses a Java Database Connectivity (JDBC) connection to access the database, and read the table.

1. AWS Glue writes the data in Amazon S3 in Parquet format, which is an open, columnar, space-saving data format.

## Configuring the AWS Glue Job
<a name="configuring-the-aws-glue-job.c10436a0-e80b-557e-9c7f-708852e7569c"></a>

To work as intended, the AWS Glue job requires the following components and configurations:
+ [AWS Glue connections](https://docs.aws.amazon.com/glue/latest/dg/glue-connections.html) – This is an AWS Glue Data Catalog object that you attach to the job to access the database. A job can have multiple connections for making calls to multiple databases. The connections contain the securely stored database credentials.
+ [GlueContext](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-glue-context.html) – This is a custom wrapper over the [SparkContext](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkContext.html) The GlueContext class provides higher-order API operations to interact with Amazon S3 and database sources. It enables integration with Data Catalog. It also removes the need to rely on drivers for database connection, which is handled within the Glue connection. Additionally, the GlueContext class provides ways to handle Amazon S3 API operations, which is not possible with the original SparkContext class.
+ IAM policies and roles – Because AWS Glue interacts with other AWS services, you must set up appropriate roles with the least privilege required. Services that require appropriate permissions to interact with AWS Glue include the following:
  + Amazon S3
  + AWS Secrets Manager
  + AWS Key Management Service (AWS KMS)

## Best Practices
<a name="best-practices.1d43a307-76d9-5433-b115-8575da72c623"></a>
+ For reading entire tables that have a large number of rows to be off-loaded, we recommend using the read replica endpoint to increase read throughput without degrading performance of the main writer instance.
+ To achieve efficiency in the number of nodes used for processing the job, turn on [auto scaling](https://docs.aws.amazon.com/glue/latest/dg/auto-scaling.html) in AWS Glue 3.0.
+ If the S3 bucket is a part of data lake architecture, we recommend off-loading data by organizing it into physical partitions. The partition scheme should be based on the access patterns. Partitioning based on date values is one of the most recommended practices.
+ Saving the data into open formats such as Parquet or Optimized Row Columnar (ORC) helps to make the data available to other analytical services such as Amazon Athena and Amazon Redshift.
+ To make the off-loaded data read-optimized by other distributed services, the number of output files must be controlled. It is almost always beneficial to have a smaller number of larger files instead of a large number of small files. Spark has built-in config files and methods to control part-file generation.
+ Archived data by definition are often-accessed datasets. To achieve cost efficiency for storage, the Amazon S3 class should be transitioned into less expensive tiers. This can be done using two approaches:
  + Synchronously transitioning the tier while offloading – If you know beforehand that the off-loaded data must be transitioned as part of the process, you can use the GlueContext mechanism [transition\_s3\_path](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-glue-context.html#aws-glue-api-crawler-pyspark-extensions-glue-context-transition_s3_path) within the same AWS Glue job that writes the data into Amazon S3.
  + Asynchronously transitioning using [S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) – Set up the S3 Lifecycle rules with appropriate parameters for Amazon S3 storage class transitioning and expiration. After this is configured on the bucket, it will persist forever.
+ Create and configure a subnet with a [sufficient IP address range](https://repost.aws/knowledge-center/glue-specified-subnet-free-addresses) within the virtual private cloud (VPC) where the database is deployed. This will avoid AWS Glue job failures caused by an insufficient number of network addresses when a large number of data processing units (DPUs) are configured.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
