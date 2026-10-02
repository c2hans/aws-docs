---
source_url: https://docs.aws.amazon.com/solutions/demand-forecasting-for-retail-on-aws/index.html
---

---
title: 'Guidance for Demand Forecasting for Retail on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/demand-forecasting-for-retail-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Demand Forecasting for Retail on AWS

Prepare for customer demand with accurate forecasts powered by machine learning

## Overview

This Guidance helps you improve the customer experience by using demand forecasting to estimate future customer demand. By predicting future demand and purchasing patterns, you can plan ahead for supply chain optimization and inventory management. This architecture shows the process of developing an estimate of future customer demand. Retail organizations can apply this Guidance to increase demand forecast accuracy, analyze various internal and external variables, and highlight low-code, no-code, or other advanced approaches.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/demand-forecasting-for-retail-on-aws.pdf)

![Architecture diagram](/images/solutions/demand-forecasting-for-retail-on-aws/images/demand-forecasting-for-retail-on-aws-1.png)

1. **Step 1**: Current and historical event data is gathered from retail stores (point of sale), manufacturing and distribution centers, customer relationship management (CRM), enterprise resource planning (ERP), enterprise performance management (EPM), and third-party systems like product vendors and logistic partners. For hybrid architectures, customers can use AWS Direct Connect or AWS Site-to-Site VPN.
1. **Step 2**: Data is ingested in batch or real-time pipelines. AWS provides many tools capable of pulling data from source endpoints, including services such as Amazon Kinesis for streaming data ingestion and Amazon IoT Core for IoT devices. Customers can use AWS Database Migration Service (AWS DMS) to fetch data from existing databases. Customers can also use AWS DataSync and AWS Storage Gateway for transfers. Optionally, customers can upload data into Amazon Simple Storage Service (Amazon S3) using the Amazon S3 CLI commands, API, or console. Customers can also use Amazon AppFlow for SAP and Salesforce.
1. **Step 3**: Data stores like Amazon S3, Amazon Timestream, Amazon Relational Database Service (Amazon RDS), Amazon DynamoDB, and Amazon Redshift provide an intermediate landing zone (also called a raw zone) for historical and real-time time series data, item metadata, and related time series data.
1. **Step 4**: Data transformation and feature engineering of raw data produce accurate machine learning (ML) models. During this step customers can select and query the data from various sources, cleanse and explore the data, check for outliers and statistical bias by visualizing the data, analyze feature importance, perform feature engineering and finally export the prepared data. In this tier, Amazon SageMaker Data Wrangler is a low-code/no-code option. With the Amazon SageMaker Data Wrangler data selection tool, you can quickly select data from multiple data sources such as Amazon Simple Storage Service (Amazon S3), Amazon Athena, Amazon Redshift, AWS Lake Formation, Snowflake, and Databricks Delta Lake; transform by using over 300 pre-configured data transformations; and exploration and visualize data. Another low-code option is AWS Glue DataBrew, which provides a visual data preparation tool that can help clean and normalize data to prepare for machine learning. Customers can also use Amazon EMR and Amazon SageMaker processing jobs, which are advanced options for data transformation and feature engineering. AWS Glue can also filter, aggregate, and reshape data. Amazon Athena can be used to perform federated queries on multiple relational, non-relational, object, and custom data sources. AWS Lambda can be used for data transformation.
1. **Step 5**: Prepared data is placed into special datasets on Amazon S3 and Amazon SageMaker Feature Store, ready to be ingested for training.
1. **Step 6**: In this step, training and hyperparameter tuning take place. Customers can use orchestrators like Amazon Step Functions, Amazon Managed Workflow for Apache Airflow, or Amazon SageMaker Pipeline to help orchestrate the end-to-end ML process.
1. **Step 6a**: Training can be performed in Amazon SageMaker Canvas or Amazon SageMaker Autopilot as low-code/no-code options. Customers can simply browse the data and select the target, then Amazon SageMaker generates a model. Additionally, Amazon SageMaker performs hyperparameter tuning according to the defined objective metrics. This option is perfect for business analysts and data analysts.
1. **Step 6b**: Optionally, customers can also use Amazon SageMaker Canvas, a fully managed service. Customers can use neural network algorithms like CNN-QR or DeepAR+ when an item's metadata dataset is available, or prophet, ARIMA, or ETS. Customers can use RETAIL data domain options available in SageMaker Canvas. This option is great for data engineers and developers.
1. **Step 6c**: Amazon SageMaker is an advanced option for developers and data scientists who can use build-in algorithms like DeepAR or AutoML libraries such as AutoGluon, or import existing models and perform transfer learning. Customers can use advanced options like data parallelism and model parallelism, then use built-in features like Amazon SageMaker Clarify for bias and SageMaker Model Monitor for monitoring.
1. **Step 7**: The output of the prior phase is a model that can be deployed for an ML inference to predict the forecast. There are two options, depending on the use case: Batch inference for asynchronous forecasting or real-time inference that leverages real-time API. For batch inference, the forecast is placed in Amazon S3 as a CSV file. For real-time inference, the model is hosted in SageMaker or SageMaker Canvas and served as an API for business applications to invoke and get predictions.
1. **Step 8**: The forecasted output can be consumed and distributed through various channels like Amazon QuickSight dashboards for business intelligence and analysis, exposed as an API using Amazon API Gateway for consumption, or pushed to a data lake or data warehouse like Amazon Redshift. Once the distribution channel is set up, the data can either be consumed by the source systems like ERP, EPM, or CRM, or by other internal or external applications. The entire process is iterative, where the latest business and customer data is fed in continuously and the model is retrained to ensure accuracy is maintained.
1. **Step 9**: Security: During the integration of various AWS services, AWS Identity and Access Management (IAM) roles are used to ensure least privileged access and AWS Key Management Service (AWS KMS) is used to ensure data encryption.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance highlights low-code and advanced options for customers to achieve more accurate forecasting. Each option (SageMaker and SageMaker Canvas) has service observability built in to ensure models train efficiently according to objective metrics. The entire flow is an iterative process that ensures the business objective is achieved and the process is efficient. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Direct Connect or Site-to-Site VPN is used to provide a secure connection between retail store or external systems and the AWS Cloud. Also, we leverage IAM and AWS KMS for securing and encrypting data. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Highly available and reliable managed services like Amazon S3, DynamoDB, AWS Glue, and SageMaker help with platform scalability and high availability. Options exist for regional failover for all services with proper architecting, but they are not called out in this design specifically. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Scalable and highly available services like DynamoDB and Amazon S3 are used as core components to improve performance. During model training, customers can leverage automatic tuning features, which can help achieve the most performant models. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Customers are only charged for the time the models are trained. Customers can additionally leverage spot instances and elastic inference. Customers can also use cost effective methods like batch inference and serverless inference, although these are not specifically mentioned. Serverless services like Lambda, Step Functions, Athena, and AWS Glue are used to reduce the cost of the solution. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

AWS managed services help with scale up and down according to business requirement and traffic and are inherently more sustainable than on-premises solutions. Additionally, we have leveraged serverless components to automate the process of infrastructure management and make it more sustainable. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
