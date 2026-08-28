---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-centric-use-cases/data-preparation-cleaning.html
---

# Data preparation and cleaning
<a name="data-preparation-cleaning"></a>

Data preparation and cleaning is one of the most important yet most time-consuming stages of the data lifecycle. The following diagram shows how the data preparation and cleaning stage fits into the data engineering automation and access control lifecycle.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-centric-use-cases/images/guide-img/058e3d2f-f726-4dc0-989b-0f15dcd3bc33/images/7188e577-3f8c-4520-bfe3-a383d5410673.png)

Here are some examples of data preparation or cleaning:
+ Mapping text columns to codes
+ Ignoring empty columns
+ Filling empty data fields with `0`, `None`, or `''`
+ Anonymizing or masking personally identifiable information (PII)

If you have a large workload that has a variety of data, then we recommend that you use [Amazon EMR](https://aws.amazon.com/emr/) or [AWS Glue](https://aws.amazon.com/glue/) for your data preparation and cleaning tasks. Amazon EMR and AWS Glue both work with unstructured, semi-structured, and relational data, and both can use Apache Spark to create a `DataFrame` or `DynamicFrame` to work with horizontal processing. Moreover, you can use [AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/) to clean and process data with a no-code approach. Additionally, DataBrew can profile your dataset with column statistics, provide data lineages, and include data quality rules for all or specified columns.

For smaller workloads that don't require distributed processing and can be completed in under 15 minutes, we recommend that you use [AWS Lambda](https://aws.amazon.com/lambda/) for data preparation and cleaning. Lambda is a cost-effective and lightweight option for smaller workloads. For highly secure data that can't enter the cloud, we recommend that you perform data anonymization on Amazon Elastic Compute Cloud (Amazon EC2) instances by using an [AWS Outposts](https://aws.amazon.com/outposts/) server.

It's essential to choose the right AWS service for data preparation and cleaning and to understand the tradeoffs involved with your choice. For example, consider a scenario where you're choosing from AWS Glue, DataBrew, and Amazon EMR. AWS Glue is ideal if the ETL job is infrequent. An infrequent job takes place once a day, once a week, or once a month. You can further assume that your data engineers are proficient in writing Spark code (for big data use cases) or scripting in general. If the job is more frequent, running AWS Glue constantly can get expensive. In this case, Amazon EMR provides distributed processing capabilities and offers both a serverless and server-based version. If your data engineers don't have the right skillset or if you must deliver results fast, then DataBrew is a good option. DataBrew can reduce the effort to develop code and speed up the data preparation and cleaning process.

After the processing is completed, the data from the ETL process is stored on AWS. The choice of storage depends on what type of data you're dealing with. For example, you could be working with non-relational data like graph data, key-value pair data, images, text files, or relational structured data.

As shown in the following diagram, you can use the following AWS services for data storage:
+ [Amazon S3](https://aws.amazon.com/s3/) stores unstructured data or semi-structured data (for example, Apache Parquet files, images, and videos).
+ [Amazon Neptune](https://aws.amazon.com/neptune/) stores graph datasets that you can query by using SPARQL or GREMLIN.
+ [Amazon Keyspaces (for Apache Cassandra)](https://aws.amazon.com/keyspaces/) stores datasets that are compatible with Apache Cassandra.
+ [Amazon QLDB](https://aws.amazon.com/qldb/) stores ledger datasets.

**Important**
Existing customers will be able to use Amazon QLDB until end of support on 07/31/2025. For more details, see [Migrate an Amazon QLDB Ledger to Amazon Aurora PostgreSQL](https://aws.amazon.com/blogs/database/migrate-an-amazon-qldb-ledger-to-amazon-aurora-postgresql/).
+ [Amazon Aurora](https://aws.amazon.com/rds/aurora/) stores relational datasets.
+ [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) stores key-value or document data in a NoSQL database.
+ [Amazon Redshift](https://aws.amazon.com/redshift/) stores workloads for structured data in a data warehouse.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-centric-use-cases/images/guide-img/058e3d2f-f726-4dc0-989b-0f15dcd3bc33/images/4e689460-233a-457a-b330-9cd7290a44a7.png)

By using the right service with the correct configurations, you can store your data in the most efficient and effective way. This minimizes the effort involved in data retrieval.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
