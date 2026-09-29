---
source_url: https://docs.aws.amazon.com/solutions/integrating-sap-and-non-sap-data-using-snowflake-on-aws/index.html
---

---
title: 'Guidance for Integrating SAP and Non-SAP Data using Snowflake on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/integrating-sap-and-non-sap-data-using-snowflake-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Integrating SAP and Non-SAP Data using Snowflake on AWS

## Overview

This Guidance demonstrates how to accelerate your data-driven decision and unlock valuable business insights unifying SAP and non-SAP data while reducing operational complexity with Snowflake and SAP on AWS. This Guidance demonstrates how to implement a SAP Cloud Lakehouse using Snowflake on AWS, providing step-by-step instructions for comprehensive analytics integration. The solution leverages multiple integration pathways, including AWS Glue SAP OData connector for managed replication, SAP Business Data Cloud Datasphere replication flows, and AWS Partner Solutions. The implementation orchestrates data flow from SAP sources through Amazon S3 to Snowflake, where advanced transformation occurs using Streams and Tasks, enabling sophisticated machine learning applications with Amazon SageMaker and GenAI capabilities through Amazon Bedrock.

## Benefits

### Streamline SAP data integration

Deploy multiple flexible pathways to extract and process SAP data using AWS services and partner solutions. Reduce development time while maintaining data integrity as you transform business-critical information into actionable insights.

### Accelerate analytics capabilities

Transform raw enterprise data into business intelligence using AWS Glue, Amazon S3, and machine learning services. Enable your teams to build predictive models and generate AI-driven insights from both SAP and non-SAP data sources.

### Enhance decision-making processes

Democratize data access across your organization with integrated visualization and AI tools like Amazon QuickSight and Amazon Bedrock. Empower business users with self-service analytics capabilities while maintaining governance over your enterprise data assets.

## How it works

### Data Integration: AWS, SAP & Partner Solutions with Snowflake

This architecture diagram illustrates how to effectively integrate SAP and non-SAP data using AWS, SAP, and Partner solutions withSnowflake.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/integrating-sap-and-non-sap-data-using-snowflake-on-aws.pdf)Step 1Install and configure SNP Glue ABAP add-on on the SAP ABAP-based source system (such as S/4HANA, Enterprise Central Component (ECC), Customer Relationship Management (CRM), or Business Warehouse (BW) to stream real-time data to Snowflake snowpipes. This enables point-to-point replication without additional hardware/software.Step 2If currently using SAP data analytics products and looking for optimized SAP integration, configure SAP Business Data Cloud Datasphere data replication flow from SAP objects like Core Data Services (CDS) views using Confluent premium outbound connector to Kafka broker or Snowflake snowpipe. SAP Datasphere replication flows support Amazon Simple Storage Service (Amazon S3) premium outbound connector.Step 3For AWS fully managed replication, use AWS Glue SAP OData connector and Zero-ETL to replicate SAP CDS views and BW extractors using managed incremental data transfer to Apache Iceberg tables in Amazon S3.Step 4Various partner solutions such Theobald, Qlik, Boomi can be used to extract data from SAP to Amazon S3 using RFC and OData Protocols.Step 5Load data from Amazon S3 to Snowflake data cloud using external stage or volume functionality of Snowflake.Step 6AWS IoT SiteWise collects and processes IoT and OT data from industrial sources. Amazon Kinesis Data Streams processes this real-time data using Kafka and services for analytics.Step 7Amazon Managed Streaming for Apache Kafka (Amazon MSK) Connect facilitates the integration between Apache Kafka and Snowflake, while Amazon Kinesis Data Firehose transfers Kafka-streamed data into Snowflake for analytics and storage.### SAP & Non-SAP Data Integration with Snowflake ELT

This diagram illustrates how to model and consume SAP and non-SAP data using Snowflake-curated data using an ELT framework.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/integrating-sap-and-non-sap-data-using-snowflake-on-aws.pdf)Step 1Snowpipe ingestion loads both SAP and non-SAP data into Snowflake using Snowpipe in real-time or batches. This process ensures timely availability of enterprise data for decision-making and analytics.Step 2Data lake storage stores raw SAP and non-SAP data in Amazon S3 for processing and analytics. It serves as a central repository for structured and unstructured business data, enabling scalable and cost-efficient operations.Step 3Aggregation Using Streams and Tasks processes raw data using Snowflake Streams and Serverless Tasks for transformation. It automates data pipelines using dynamic tables.Step 4Feature Engineering and Transformation enhances data using Snowpark, SQL, and transformation logic. It refines raw data into meaningful business metrics for AI-driven insights and reporting.Step 5Model training with Amazon SageMaker AI trains machine learning models on Snowflake data, empowering businesses to build predictive models for customer insights, fraud detection, and demand forecasting.Step 6Machine learning inference deploys ML models using Snowflake user-defined functions (UDF), Amazon SageMaker AI, and Amazon Bedrock, which enables AI-driven automation, personalization, and real-time decision-making for enterprises.Step 7External data access connects Snowflake with external environments such as Jupyter notebooks and facilitates collaboration between data scientists and business analysts for advanced analytics.Step 8Facts & Dimensional Models structures harmonized data into dimensional models for analytics and reporting. This optimizes data for business intelligence, enabling better trend analysis and strategic decision-making.

Step 9Permanent tables and materialized views provide optimized views, data monetization, and native applications for insights, accelerating time-to-insight by enabling self-service analytics for business users.Step 10Publishing and consumption enable data access through catalogs, GenAI agents, dashboards, and applications and democratizes data access across the organization, driving innovation and informed decision-making.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-building-sap-cloud-lakehouse-using-snowflake-on-aws)

## Related content

- **Placeholder**: This quickstart demonstrates how to use Amazon Q Business and Amazon Q Code Transformation with Snowflake, enabling you to interact with your Snowflake data through natural language queries and transform legacy code into modern Snowpark applications.

[Learn more](https://quickstarts.snowflake.com/guide/getting_started_with_amazon_q_business%20and_cortex/index.html#0)

[Read usage guidelines](/solutions/guidance-disclaimers/)
