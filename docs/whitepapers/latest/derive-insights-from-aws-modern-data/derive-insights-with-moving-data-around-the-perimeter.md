---
source_url: https://docs.aws.amazon.com/whitepapers/latest/derive-insights-from-aws-modern-data/derive-insights-with-moving-data-around-the-perimeter.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Derive insights with moving data around the perimeter
<a name="derive-insights-with-moving-data-around-the-perimeter"></a>

 In other situations, you want to move data from one purpose-built data store to another: data movement *around-the-perimeter*. For example, you might copy the product catalog data stored in your database to your search service to make it easier to look through your product catalog and offload the search queries from the database. We think of this concept as *data movement around the perimeter*.

![Diagram showing data movement around the perimeter](https://docs.aws.amazon.com/whitepapers/latest/derive-insights-from-aws-modern-data/images/data-movement-around-the-perimeter.png)

## Derive insights from your data lake, data warehouse and operational databases
<a name="derive-insights-from-your-data-lake-data-warehouse-and-operational-databases"></a>

 A data warehouse is a database optimized to analyze relational data coming from transactional systems and line of business applications. [Amazon Redshift](https://aws.amazon.com/redshift/) is a fast, fully managed data warehouse that makes it simple and cost-effective to analyze data using standard SQL and existing Business Intelligence (BI) tools.

 To get information from unstructured data that would not fit in a data warehouse, you can build a [data lake](https://aws.amazon.com/big-data/datalakes-and-analytics/what-is-a-data-lake/). A data lake is a centralized repository that allows you to store all your structured and unstructured data at any scale. With a data lake built on Amazon S3, you can easily run big data analytics and use ML to gain insights from your semi-structured (such as JSON, XML) and unstructured datasets.

 AWS is launching two new features to help you improve the way you manage your data warehouse and integrate with a data lake:
+  **Data Lake Export** to unload data from an Amazon Redshift cluster to S3 in [Apache Parquet](https://parquet.apache.org) format, an efficient open columnar storage format optimized for analytics.
+  **Federated Query** to be able, from an Amazon Redshift cluster, to query:
  +  Across data stored in the cluster
  +  In your S3 data lake
  +  In one or more [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS) for PostgreSQL and [Amazon Aurora](https://aws.amazon.com/rds/aurora/) PostgreSQL databases

 The following diagram illustrates the "moving the data around the perimeter" Modern Data approach with S3, Amazon Redshift, Amazon Aurora PostgreSQL, and Amazon EMR to derive analytics.

![Diagram showing how to derive insights from your data lake, data warehouse and operational databases](https://docs.aws.amazon.com/whitepapers/latest/derive-insights-from-aws-modern-data/images/insights-from-data-lakes-warehouses-and-databases.png)

 The steps that data follows through the architecture are as follows:

1.  **Using the Redshift data lake export** — You can unload the result of a Redshift query to an S3 data lake in Apache Parquet format. The Parquet format is up to 2x faster to unload, and consumes up to 6x less storage in S3, compared to text formats. [Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-using-spectrum.html) enables you to query data directly from files in S3 without moving data. Or, you can use [Amazon Athena](https://aws.amazon.com/athena), [Amazon EMR](https://aws.amazon.com/emr), or [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) to analyze the data.

1.  **Using the Redshift federated query** — You can also access data in Amazon RDS and Aurora PostgreSQL stores directly from your Amazon Redshift data warehouse. In this way, you can access data as soon as it is available. By using federated queries in Amazon Redshift, you can query and analyze data across operational databases, data warehouses, and data lakes.

 Refer to the blog post [New for Amazon Redshift – Data Lake Export and Federated Query](https://aws.amazon.com/blogs/aws/new-for-amazon-redshift-data-lake-export-and-federated-queries/) for additional details.
