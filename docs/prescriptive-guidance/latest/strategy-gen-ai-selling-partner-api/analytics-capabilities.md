---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-gen-ai-selling-partner-api/analytics-capabilities.html
---

# Implementing an analytics strategy for your Amazon selling partner data
<a name="analytics-capabilities"></a>

This section provides a detailed strategy for how Amazon vendors and sellers can perform advanced analytics on the data ingested from the Amazon Selling Partner API (SP-API). These analytics capabilities can provide:
+ Insights into sales performance, inventory management, brand analytics, and other key metrics.
+ The ability to create custom calculations, filters, and visualizations to address your specific needs.

The following architecture diagram shows how you use AWS Glue to discover, prepare, move, and integrate the data in the data lake so that you can use it for analytics and insights.

![Using analytics services and AWS Glue to unlock insights from the Amazon Selling Partner API data](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-gen-ai-selling-partner-api/images/guide-img/fd951ab0-b7f5-4ded-9451-ea838cf4c59a/images/128d7652-9056-400a-a328-b5c8cba378ea.png)

The architecture diagram includes the following components:

1. [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html) is used to build the scalable data lake and to centrally manage the security, access control, and audit trails.

1. [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is used as the data lake storage.

1. [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) is used to catalog, transform, enrich, move, and replicate data across multiple data stores and the data lake. AWS Glue simplifies complex, manual, and expensive traditional data integration processes, and it supports increased data volumes and data diversity.

1. [Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/what-is-datazone.html) helps you catalog, discover, share, and govern data across the organization.

1. [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) provides interactive querying, analyzing, and processing capabilities.

1. [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html) is used as a cloud data warehouse. With [zero-ETL integration](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.html), you can perform near real-time analytics on petabytes of transactional data, or you can use Amazon Redshift ML capabilities to derive real-time insights.

1. [Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) provides ML-powered business intelligence. [Quick Q](https://docs.aws.amazon.com/quicksight/latest/user/working-with-quicksight-q.html), powered by machine learning, uses natural language processing to answer your business questions quickly.

1. [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html) is a managed cluster platform that simplifies running big data frameworks to process and analyze vast amounts of data on AWS. Using these frameworks and related open-source projects, you can process data for analytics purposes and business intelligence workloads.

1. [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) can be used for operational analytics. It also provides vector database search capabilities.

1. [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) can be used to build, train, and deploy ML models, and to add artificial intelligence to your applications.
