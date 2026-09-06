---
source_url: https://docs.aws.amazon.com/whitepapers/latest/patterns-for-ingesting-saas-data-into-aws-data-lakes/extract-transform-and-load-etl-using-custom-connectors-with-apache-spark.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Extract, transform and load (ETL) using custom connectors with Apache Spark
<a name="extract-transform-and-load-etl-using-custom-connectors-with-apache-spark"></a>

## AWS Glue: Introduction
<a name="aws-glue"></a>

 [AWS Glue](https://aws.amazon.com/glue/) is a serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development. AWS Glue provides all the capabilities needed for data integration so that you can start analyzing your data and putting it to use in minutes instead of months.

 [AWS Glue custom connectors](https://aws.amazon.com/about-aws/whats-new/2020/12/aws-glue-launches-aws-glue-custom-connectors/) make it easy to discover and integrate with a variety of additional data sources, such as SaaS applications or your custom data sources. With just a few clicks, you can search and select connectors from the [AWS Marketplace](https://aws.amazon.com/marketplace/) and begin your data preparation workflow in minutes. AWS is also releasing a new framework to develop, validate, and deploy your own custom connectors (bring your own connectors (BYOC)).

### Architecture overview
<a name="architecture-overview-1"></a>

 The following diagram depicts the architecture of the solution where data from any of the SaaS applications can be ingested into Amazon S3 using AWS Glue. Once the data is ingested in Amazon S3, you can catalog it using AWS AWS Glue Data Catalog, and start consuming this data using SQL in Amazon Athena.

![This is a diagram that shows data from Salesforce, Google BigQuery, and Data Warehouse being ingested into Amazon S3 using AWS Glue](http://docs.aws.amazon.com/whitepapers/latest/patterns-for-ingesting-saas-data-into-aws-data-lakes/images/aws-glue-based-data-ingestion-pattern.png)

### Usage patterns
<a name="usage-patterns-1"></a>

 Because AWS Glue ETL provides the data engineers with flexibility, scalability, and the open-source distributed computing power of Apache Spark framework, this option is an excellent choice for ingesting SaaS data into the AWS Cloud ecosystem (including Amazon S3 for data lake operations).

 Some use cases are as follows:
+  Enrich internal system data with data from SaaS applications during the ETL process.
+  Look up transformations with data from SaaS applications during ETL process.

 The flexibility can be applicable in multiple places during the ETL process using AWS Glue:
+  You can either use the existing connectors that can be found in the AWS Marketplace, or if you don’t see a pre-built connector for the SaaS application you are trying to connect to, then you can also build your own customer connector and use that in AWS Glue. The process to create your own connector is documented here: [Developing custom connectors](https://docs.aws.amazon.com/glue/latest/ug/connectors-chapter.html#developing-custom-connectors).
+  A connector is just an initial piece of the puzzle which allows you to connect to the source application. But often, the data that you want from the source may need to be transformed, normalized, or aligned in a specific format before it can be stored in Amazon S3. This is where AWS Glue shines: It provides the freedom to data engineers to customize their ETL process to cater to the complexities as defined by their use cases. The complexities may arise due to heavy customizations to the SaaS application, they may arise due to limitations of other low-code/no-code tools, or they may arise due to complex business/technical requirements around how the data should be persisted in the target storage.

 [AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/ug/what-is-glue-studio.html) is a new graphical interface that makes it easy to create, run, and monitor ETL jobs in AWS Glue. You can visually compose data transformation workflows and seamlessly run them on AWS Glue’s Apache Spark-based serverless ETL engine. Using AWS Glue Studio and AWS Marketplace connectors, you can create an ETL pipeline with ease. For example, refer to [Migrating data from Google BigQuery to Amazon S3 using AWS Glue custom connectors](https://aws.amazon.com/blogs/big-data/migrating-data-from-google-bigquery-to-amazon-s3-using-aws-glue-custom-connectors/).

### Considerations
<a name="considerations-1"></a>

 Using custom connectors in AWS Glue Studio has some [limitations](https://docs.aws.amazon.com/glue/latest/ug/connectors-chapter.html#connector-restrictions). However, data engineers have the option to [author jobs](https://docs.aws.amazon.com/glue/latest/dg/author-job.html) using the AWS Glue console and write their code themselves. They can use the custom connectors or use other open-source/paid connector codes to access any SaaS application. For example, refer to [Extract Salesforce.com data using AWS Glue and analyzing with Amazon Athena](https://aws.amazon.com/blogs/big-data/extracting-salesforce-com-data-using-aws-glue-and-analyzing-with-amazon-athena/).

 Also, keep in mind when using the AWS Glue ETL pattern for ingesting SaaS data, the source SaaS applications may have different limitations built in for bulk data extraction as well as API limits. For example, Salesforce has these limits for bulk data extraction: [Bulk API and Bulk API 2.0 Limits and Allocations](https://developer.salesforce.com/docs/atlas.en-us.234.0.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_bulkapi.htm).
