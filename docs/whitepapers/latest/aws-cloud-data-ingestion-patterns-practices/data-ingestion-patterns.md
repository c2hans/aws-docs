---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-cloud-data-ingestion-patterns-practices/data-ingestion-patterns.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data ingestion patterns
<a name="data-ingestion-patterns"></a>

 Organizations often want to use the cloud to optimize their data analytics and data storage solutions. These optimizations can be in the form of reducing costs, reducing the undifferentiated heavy lifting of infrastructure provisioning and management, achieving better scale and/or performance, or using innovation in the cloud.

 Depending upon the current architecture and target Modern Data architecture, there are certain common ingestion patterns that can be observed.

 **Homogeneous data ingestion patterns** — These are patterns where the primary objective is to move the data into the destination in the same format or same storage engine as it is in the source. In these patterns, your primary objectives may be speed of data transfer, data protection (encryption in transit and at rest), preserving the data integrity and automating where continuous ingestion is required. These patterns usually fall under the "extract and load" piece of extract, transform, load (ETL), and can be an intermediary step before transformations are done after the ingestion.

 This paper covers the following use cases for this pattern:
+  **Relational data ingestion between same data engines** (for example, Microsoft SQL Server to Amazon RDS for SQL Server or SQL Server on Amazon EC2, or Oracle to Amazon RDS for Oracle.) This use case can apply to migrating your peripheral workload into the AWS Cloud or for scaling your workload to expand on new requirements like reporting.
+  **Data files ingestion from on-premises storage to an AWS Cloud data lake** (for example, ingesting parquet files from Apache Hadoop to Amazon Simple Storage Service (Amazon S3) or ingesting CSV files from a file share to Amazon S3). This use case may be one time to migrate your big data solutions, or may apply to building a new data lake capability in the cloud.
+  **Large objects** (BLOB, photos, videos) ingestion into Amazon S3 object storage.

 **Heterogeneous data ingestion patterns** — These are patterns where data must be transformed as it is ingested into the destination data storage system. These transformations can be simple like changing the data type/format of the data to meet the destination requirement or can be as complex as running machine learning to derive new attributes in the data. This pattern is usually where data engineers and ETL developers spend most of their time to cleanse, standardize, format, and shape the data based on the business and technology requirements. As such, it follows a traditional ETL model. In this pattern, you may be integrating data from multiple sources and may have a complex step of applying transformation. The primary objectives here are same as in homogeneous data ingestion, with the added objective of meeting the business and technology requirements to transform the data.

 This paper covers the following use cases for this pattern:
+  Relational data ingestion between different data engines (for example, Microsoft SQL Server to Amazon Aurora relational database or Oracle to Amazon RDS for MySQL).
+  Streaming data ingestion from data sources like Internet of Things (IoT) devices or log files to a central data lake or peripheral data storage.
+  Relational data source to non-relational data destination and vice versa (for example, Amazon DocumentDB solution to Amazon Redshift or MySQL to Amazon DynamoDB).
+  File format transformations while ingesting data files (for example, changing CSV format files on file share to Parquet on Amazon S3).

 The tools that can be used in each of the preceding patterns depend upon your use case. In many cases, the same tool can be used to meet multiple use cases. Ultimately, the decision on using the right tool for the right job will depend upon your overall requirements for data ingestion in the Modern Data architecture. An important aspect of your tooling will also be workflow scheduling and automation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
