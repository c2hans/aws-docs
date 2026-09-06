---
source_url: https://docs.aws.amazon.com/whitepapers/latest/big-data-analytics-options/amazon-athena.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon Athena
<a name="amazon-athena"></a>

[Amazon Athena](https://aws.amazon.com/athena/) is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to setup or manage, and you can start analyzing data immediately. You don’t need to load your data into Athena, as it works directly with data stored in S3. Just log into the Athena Console, define your table schema, and start querying. Amazon Athena uses Presto with full ANSI SQL support and works with a variety of standard data formats, including CSV, JSON, ORC, Apache Parquet, and Apache Avro.

## Ideal usage patterns
<a name="ideal-usage-patterns-athena"></a>
+  **Interactive ad hoc querying for web logs** — Athena is a good tool for interactive one-time SQL queries against data on Amazon S3. For example, you could use Athena to run a query on web and application logs to troubleshoot a performance issue. You simply define a table for your data and start querying using standard SQL. Athena integrates with Amazon Quick for easy visualization.
+  **To query staging data before loading into Redshift** — You can stage your raw data in S3 before processing and loading it into Amazon Redshift, and then use Athena to query that data.
+  **Send AWS service logs to S3 for analysis with Athena — ** CloudTrail, CloudFront, ELB/ALB and [VPC flow logs](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/flow-logs.html) can be analyzed with Athena. AWS CloudTrail logs include details about any API calls made to your AWS services, including from the console. CloudFront logs can be used to explore users’ surfing patterns across web properties served by CloudFront. Querying ELB/ALB logs allows you to see the source of traffic, latency, and bytes transferred to and from Elastic Load Balancing instances and backend applications. VPC flow logs capture information about the IP traffic going to and from network interfaces in VPCs in the [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC). The logs enable you to investigate network traffic patterns and identify threats and risks across your VPC estate.
+  **Building Interactive Analytical Solutions with notebook-based solutions such as RStudio, Jupyter, or Zeppelin — ** Data scientists and Analysts are often concerned about managing the infrastructure behind big data platforms while running notebook-based solutions such as RStudio, Jupyter, and Zeppelin. Amazon Athena makes it easy to analyze data using standard SQL without the need to manage infrastructure. Integrating these notebook-based solutions with Amazon Athena gives data scientists a powerful platform for building interactive analytical solutions.
+  **Query data in relational, non-relational, object and custom data sources leveraging Athena Federated Query** — The Amazon Athena federated query allows the user to run SQL queries across data in relational, non-relational, object and custom data sources, with options to either query the data in place or extract the data from these data sources and store it in S3.

## Cost model
<a name="cost-model-athena"></a>

 Amazon Athena has simple pay-as-you-go pricing, with no up-front costs or minimum fees, and you’ll only pay for the resources you consume. It is priced per query, $5 per TB of data scanned, and charges based on the amount of data scanned by the query. You can save from 30% to 90% on your per-query costs and get better performance by compressing, partitioning, and converting your data into columnar formats. Converting data to the columnar format allows Athena to read only the columns it needs to process the query.

 You are charged for the number of bytes scanned by Amazon Athena, rounded up to the nearest megabyte, with a 10 MB minimum per query. There are no charges for Data Definition Language (DDL) statements like `CREATE/ALTER/DROP TABLE`, statements for managing partitions, or failed queries. Canceled queries are charged based on the amount of data scanned.

Because federated queries invoke Lambda functions in your account, you are charged for Lambda when a Federated query is made.

## Performance
<a name="performance-athena"></a>

You can improve the performance of your query by compressing, partitioning, and converting your data into columnar formats. Amazon Athena supports open source columnar data formats such as Apache Parquet and Apache ORC. Converting your data into a compressed, columnar format lowers your cost and improves query performance by enabling Athena to scan less data from S3 when running your query.

## Durability and availability
<a name="durability-and-availability-athena"></a>

 Amazon Athena is highly available and executes queries using compute resources across multiple facilities, automatically routing queries appropriately if a particular facility is unreachable. Athena uses Amazon S3 as its underlying data store, making your data highly available and durable. Amazon S3 provides durable infrastructure to store important data and is designed for durability of 99.999999999% of objects. Your data is redundantly stored across multiple facilities and multiple devices in each facility.

## Scalability and elasticity
<a name="scalability-and-elasticity-athena"></a>

 Athena is serverless, so there is no infrastructure to setup or manage, and you can start analyzing data immediately. Because it is serverless it can scale automatically, as needed.

## Security, authorization, and encryption
<a name="security-authorization-and-encryption-athena"></a>

 Amazon Athena allows you to control access to your data by using [AWS IAM](https://aws.amazon.com/iam/) policies, Access Control Lists (ACLs), and Amazon S3 bucket policies. With IAM policies, you can grant users fine-grained control to your S3 buckets. By controlling access to data in S3, you can restrict users from querying it using Athena. You can query data that’s been protected by:
+  Server-side encryption with an S3-managed key
+  Server-side encryption with an AWS KMS-managed key
+  Client-side encryption with an AWS KMS-managed key

 Amazon Athena also can directly integrate with AWS Key Management System (KMS) to encrypt your result sets.

## Interfaces
<a name="interfaces-athena"></a>

Querying can be done by using the Athena Console. Athena also supports CLI, API via SDK and JDBC. Athena also integrates with Amazon Quick for creating visualizations based on the Athena queries.

[Athena Federated Query](https://docs.aws.amazon.com/athena/latest/ug/connect-to-a-data-source.html) leverages Lambda as data source connectors as its extension to make queries in sources other than S3. Sources such as Amazon CloudWatch Logs, DynamoDB, [Amazon DocumentDB](https://aws.amazon.com/documentdb/), Amazon RDS, JDBC-compliant Postgres, and MySQL databases are natively supported by Athena Federated Query. For others, you can use Athena Query Federation SDKs to write custom connectors.

## Anti-patterns
<a name="anti-patterns-athena"></a>

 Amazon Athena has the following anti-patterns:
+  **Enterprise Reporting and Business Intelligence Workloads** – Amazon Redshift is a better tool for enterprise reporting and BI workloads involving iceberg queries or cached data at the nodes. Data warehouses pull data from many sources, format and organize it, store it, and support complex, high speed queries that produce business reports. The query engine in Amazon Redshift has been optimized to perform especially well on data warehouse workloads.
+  **ETL Workloads** **–** You should use Amazon EMR/AWS Glue if you are looking for an ETL tool to process extremely large datasets and analyze them with the latest big data processing frameworks such as Spark, Hadoop, Presto, or Hbase.
+  **RDBMS –** Athena is not a relational/transactional database. It is not meant to be a replacement for SQL engines like MySQL.
