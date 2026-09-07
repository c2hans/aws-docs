---
source_url: https://docs.aws.amazon.com/whitepapers/latest/next-generation-oss/network-analytics.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Network Analytics
<a name="network-analytics"></a>

 This section presents a network analytics architecture on AWS that provides flexibility, scalability, and innovation through Machine Learning (ML) integration. The components to a network analytics solution can be divided in four categories: ingestion, storage, processing and analysis, and consumption. The following reference architecture illustrates the AWS services that support the proposed architecture.

![Diagram showing Network Analytics Architecture on AWS](https://docs.aws.amazon.com/whitepapers/latest/next-generation-oss/images/network-analytics-architecture.png)

 Data can be ingested through [AWS Transfer for Secure File Transfer Protocol](https://aws.amazon.com/aws-transfer-family) (SFTP) to periodically collect data from NFx, Domain Managers, Custom Edge collectors, and legacy network performance analytics solutions. Similarly, you can leverage [Kinesis](https://aws.amazon.com/kinesis/) and/or [Amazon MSK](https://aws.amazon.com/msk/) to inject real-time performance data such as events-driven messages (for example, UE attach). Kinesis supports real-time data streaming where data collected is available in milliseconds to enable real-time analytics use cases.

 Amazon S3 provides flexible, scalable, and performant storage. Amazon S3 enables DSPs to manage data and access controls, query-in-place for analytics, and provide a wide range of cost-effective storage classes. [AWS Lake Formation](https://aws.amazon.com/lake-formation/) (Lake Formation) provides an effective, simple way to secure the data lake supporting your network analytics solution. You can use one single data lake for your data, whether it is untransformed network performance data or enriched performance data. You can govern access to the data by allowing read instructions from an operations team to a given table while allowing a development team the ability to alter it. Data lakes provide you with the ability to reduce data duplication by governing what can be consumed and how it can be consumed, and providing one viewpoint of DSP’s performance (and configuration) data.

 An [AWS Glue Crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) crawls into your data lake to identify the format and create the tables (or updates) in your Data Catalog. It creates the structure that allows you to query your data. For example, if an operator initiates ingestion and loads data into the [Amazon S3](https://aws.amazon.com/s3/) buckets for a new NFx, DSPs can define the AWS Glue Crawler that will go through the NFx performance data and identify its metadata. Once the [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html) is built using the AWS Glue Crawler, DSPs have the ability to easily query their data using [Amazon Athena](https://aws.amazon.com/athena/) (a serverless interactive query service that allows you to analyze data in Amazon S3). DSPs can access their network data on the fly and perform complex SQL queries.

 [EMR](https://aws.amazon.com/emr/) can be leveraged to process the vast amount of network data. EMR makes it easy for the operator to set up, operate, and scale their big data environment by automating time-consuming tasks (like provisioning capacity and tuning clusters). Similarly, DSPs can leverage [Kinesis](https://docs.aws.amazon.com/kinesis/index.html) to ingest real-time data and run an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html) function to transform the ingested data.

 DSPs can leverage [Amazon Redshift (Redshift)](https://aws.amazon.com/redshift/) as a data warehouse solution to create specialized views and procedures, and support their network analytics needs. [AWS Glue ETL](https://docs.aws.amazon.com/glue/latest/dg/orchestrate-using-workflows.html) jobs can be leveraged to create a database schema in Redshift and copy data from Amazon S3 to Redshift.

 [Amazon Quick](https://aws.amazon.com/quicksight/) makes it easy for DSPs to build dashboards showing the performance of their network, share that information across engineering and leadership groups, and support quick integration with ML-powered insights. QuickSight reads from Redshift, from Amazon S3 through Athena, [etc](https://docs.aws.amazon.com/quicksight/latest/user/supported-data-sources.html)., making it a great Business Intelligence (BI) tool to correlate data at various stages of a given analysis path.

 AWS services integrate easily with existing DSPs’ in-house consumption solutions by providing the tools, APIs, and security necessary. For example, DSPs can perform SQL queries towards Redshift to feed into their legacy reporting systems using the same SQL queries used in their current set of queries.
