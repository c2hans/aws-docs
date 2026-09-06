---
source_url: https://docs.aws.amazon.com/whitepapers/latest/derive-insights-from-aws-modern-data/derive-insights-with-outside-in-data-movement.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Derive insights with outside-in data movement
<a name="derive-insights-with-outside-in-data-movement"></a>

 You can also move data in the other direction: from the *outside-in*. For example, you can copy query results for sales of products in a given Region from your data warehouse into your data lake, to run product recommendation algorithms against a larger data set using machine learning. Think of this concept as *outside-in data movement*.

![Diagram showing outside-in data movement](http://docs.aws.amazon.com/whitepapers/latest/derive-insights-from-aws-modern-data/images/outside-in-data-movement.png)

## Derive insights from Amazon DynamoDB data for real-time prediction with Amazon SageMaker AI
<a name="derive-insights-from-amazon-dynamodb-data-for-real-time-prediction-with-amazon-sagemaker"></a>

 [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) is a fast NoSQL database used by applications that need consistent, single-digit millisecond latency. Customers want to move valuable data in DynamoDB into S3 to derive insights. This data in S3 can be the primary source for understanding customers’ past behavior, predicting future behavior, and generating downstream business value.

 The following diagram illustrates the Modern Data outside-in data movement with DynamoDB data to derive personalized recommendations.

![Diagram showing how to derive insights from Amazon DynamoDB data for real-time prediction with Amazon SageMaker AI](http://docs.aws.amazon.com/whitepapers/latest/derive-insights-from-aws-modern-data/images/real-time-prediction-insights.png)

 The steps that data follows through the architecture are as follows:

1.  [Export DynamoDB tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DataExport.html) as JSON into Amazon S3.

1.  Exported JSON files are converted to comma-separated value (`.csv`) format to use as a data source for [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) by using AWS Glue.

1.  Amazon SageMaker AI renews the model artifact and updates the endpoint.

1.  The converted `.csv` file is available for ad hoc queries with Athena.

## Derive insights from Amazon Aurora data with Apache Hudi, AWS Glue, AWS DMS, and Amazon Redshift
<a name="derive-insights-from-amazon-aurora-data-with-apache-hudi-aws-glue-aws-dms-and-amazon-redshift"></a>

 [AWS Database Migration Service](https://aws.amazon.com/dms) (AWS DMS) can replicate the data from your source systems to Amazon S3. When the data is in Amazon S3, customers process it based on their analytics requirements. A typical requirement is to sync the data in S3 with the updates on the source systems. Although it’s easy to apply updates on a relational database management system (RDBMS) that backs an online source application, it’s difficult to apply this CDC process on your data lakes. [Apache Hudi](https://hudi.apache.org/) is a good way to solve this problem. Currently, you can use [Hudi on Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hudi.html) to create Hudi tables.

 The following diagram illustrates the Modern Data outside-in data movement with Amazon Aurora Postgres-changed data to derive analytics.

![Diagram showing how to derive insights from Amazon Aurora data with Apache Hudi, AWS Glue, AWS DMS, and Amazon Redshift](http://docs.aws.amazon.com/whitepapers/latest/derive-insights-from-aws-modern-data/images/insights-from-hudi-glue-dms.png)

 The steps that data follows through the architecture are as follows:

1.  AWS DMS replicates the data from the Aurora cluster to the raw S3 bucket.

1.  Use [Apache Hudi](https://hudi.apache.org/) to create tables in the [AWS Glue](https://aws.amazon.com/glue) Data Catalog using AWS Glue jobs. An AWS Glue job (HudiJob) that is scheduled to run at a frequency set in the ScheduleToRunGlueJob parameter.

1.  This job reads the data from the raw S3 bucket, writes to the curated S3 bucket, and creates a Hudi table in the Data Catalog.

1.  The job also creates an [Amazon Redshift](https://aws.amazon.com/redshift) external schema in the Amazon Redshift cluster.

1.  You can now query the Hudi table in [Amazon Athena](https://aws.amazon.com/athena) or [Amazon Redshift](https://aws.amazon.com/redshift/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc).

 Refer to the blog post [Creating a source to Lakehouse data replication pipe using Apache Hudi, AWS Glue, AWS DMS, and Amazon Redshift](https://aws.amazon.com/blogs/big-data/creating-a-source-to-lakehouse-data-replication-pipe-using-apache-hudi-aws-glue-aws-dms-and-amazon-redshift/) for additional details.
