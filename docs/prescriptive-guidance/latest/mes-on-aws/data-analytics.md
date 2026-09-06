---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/data-analytics.html
---

# Data and analytics
<a name="data-analytics"></a>

Traditional monolithic MES systems had limited or no analytics capabilities. Manufacturers had to rely on expensive third-party tools or complex methods of backend data extraction into spreadsheets for basic reports such as daily production, inventory levels, quality results, and so on. There was little possibility of combining MES data with other applications and system data for analytics. Microservice-based MES on AWS can solve the typical analytics challenges for MES and provide additional analytics capabilities to give manufacturers a competitive advantage. The AWS Cloud gives manufacturers choices from a set of purpose-built analytics services and built analytics platforms, and also provides purpose-built solutions such as Industrial Data Fabric for industrial customers.
+ [AWS analytics services](https://aws.amazon.com/big-data/datalakes-and-analytics/) are purpose-built to quickly extract data insights by using the most appropriate tool for the job and are optimized to give the best performance, scale, and cost for business needs.
+ [Industrial Data Fabric](https://aws.amazon.com/solutions/industrial/industrial-data-fabric/)** **helps manage data at scale from multiple data sources. Businesses can optimize operations across the value chain and functions by combining MES data with data siloed in various systems across manufacturing. Traditionally, systems and applications within manufacturing either don't communicate or communicate rigidly based on hierarchy. For example, a PLM system doesn't talk to an OT system such as SCADA or PLC. Therefore, the data from production and process design aren't combined because these systems aren't designed to work together. MES connects the two, but traditional monolith MES, too, is limited in its communication with enterprise applications and OT systems. The Industrial Data Fabric solution on AWS helps you create the data management architecture that enables scalable, unified, and integrated mechanisms to use data effectively.

## Architecture
<a name="data-analytics-architecture"></a>

The following diagram shows a sample architecture for data and analytics that combines data from IoT, MES, PLM, and ERP. This architecture is built only on AWS services. However, as mentioned previously, you can use an AWS Partner solution for data analytics, and address the unique requirements of your environment by combining services from AWS and AWS Partners.

![MES architecture for data and analytics](http://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/images/guide-img/093538ca-c7c9-4311-a0e9-8a876ae66d65/images/f5ec8ea0-99d7-4218-b363-2fcc67d16948.png)

1. The OT data sources to be combined are available on the local network.

1. AWS Outposts provides edge hardware.

1. AWS IoT Greengrass services include an ML component for local inference and other components for data ingestion, processing, streaming, and so on.

1. The local instance of a microservice for MES could be any microservice, and, depending on the requirements, there can be more than one microservice at the edge.

1. Local authentication and authorization allow MES users to securely access the local microservice for latency-sensitive use cases, such as real-time production reports, or in the event of connectivity interruptions.

1. IoT services such as AWS IoT Core receive data in the cloud, and AWS IoT SiteWise stores and processes the data.

1. Amazon API Gateway endpoint and Amazon MSK options keep the cloud and edge components of microservices in sync.

1. Amazon Kinesis streams the data from IoT services to S3 buckets. Kinesis allows buffering and processing of data before storing it in S3 buckets.

1. The industrial data lake includes S3 buckets, an AWS Glue crawler, and the AWS Glue Data Catalog. AWS Glue crawlers scan the S3 bucket that contains raw data to automatically infer schemas and partition structure, and populate the Data Catalog with the corresponding table definitions and statistics from the S3 bucket that contains processed data.

1. Machine learning services such as Amazon SageMaker AI are used to analyze the data in the data lake and to derive patterns for predicting future events.

1. The MES microservice consists of the cloud components of a microservice within MES.

1. Analytics services support serverless querying of data from data lakes, data warehouses (Amazon Athena), interactive visualization using business intelligence services (Amazon Quick), an optional cloud data warehouse to run complex queries (Amazon Redshift), and optional advance data processing (Amazon EMR).

1. Frontend web services include Amazon Cognito to authenticate users, Amazon Route 53 as a DNS service, and Amazon CloudFront to deliver content to end-users with low latency.

1. AWS Lambda enables interfaces between analytics services and other applications.

1. Interface services include API Gateway to manage APIs and AWS AppSync to consolidate APIs and create endpoints.
