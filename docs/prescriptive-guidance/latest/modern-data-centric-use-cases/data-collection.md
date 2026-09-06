---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-centric-use-cases/data-collection.html
---

# Data collection
<a name="data-collection"></a>

You can collect data from a variety of sources within AWS, but it's important to choose the right data collection tool for your use case. The following diagram shows how the data collection stage fits into the data engineering automation and access control lifecycle.

![Data collection diagram](http://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-centric-use-cases/images/guide-img/058e3d2f-f726-4dc0-989b-0f15dcd3bc33/images/497abb56-a9d5-46e2-9439-c9e4177c81bb.png)

AWS provides the following data collection tools:
+ [Amazon Kinesis](https://aws.amazon.com/kinesis/) helps you collect streaming data. Kinesis also offers seamless integration and processing capabilities.
+ [AWS Database Migration Service (AWS DMS)](https://aws.amazon.com/dms/) helps you ingest data from relational databases. AWS DMS has configuration options and direct connections between on-premises and database services, such as Amazon Simple Storage Service (Amazon S3), that are hosted on AWS.
+ [AWS Glue](https://aws.amazon.com/glue/) is an extract, transform, and load (ETL) tool that helps you ingest unstructured data.

There are several use cases for collecting unstructured or semi-structured data by using Amazon S3 for storage. For example, a manufacturing site's data collection use case could require historical data to be ingested for machine history data as XML files, event data as JSON files, and purchase data from a relational database. This use case could also require that all three data sources must be joined.

Before you start the data ingestion process, we recommend that you understand what data must be ingested, and then choose the right tool to collect this data.
