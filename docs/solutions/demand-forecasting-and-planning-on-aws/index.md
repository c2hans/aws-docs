---
source_url: https://docs.aws.amazon.com/solutions/demand-forecasting-and-planning-on-aws/index.html
---

---
title: 'Guidance for Demand Forecasting & Planning on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/demand-forecasting-and-planning-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Demand Forecasting & Planning on AWS

## Overview

This Guidance helps consumer packaged goods (CPG) companies connect data from databases and ecommerce sites to create forecasts and increase visibility into inventory, sales, and marketing campaigns. In this Guidance, sales data with anomalous behaviors are sent to dashboards where alerts can be configured, so companies can take appropriate action. A time-series, machine learning forecasting service is also deployed in this Guidance, designed to analyze business metrics to help companies forecast easily and accurately.

## How it works

This architecture shows how data is collected from your databases and ecommerce sites, processed, and exported to a dashboard for visibility and forecasting.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/demand-forecasting-and-planning-on-aws.pdf)

![Architecture diagram](/images/solutions/demand-forecasting-and-planning-on-aws/images/demand-forecasting-and-planning-on-aws-1.png)

1. **Step 1**: AWS Database Migration Service (AWS DMS) will connect with your databases using change data capture (CDC). Data about sales, products, and marketing campaigns is collected and sent to Amazon Kinesis Data Streams. Optionally, you can send data from your e-commerce site to Kinesis Data Streams directly.
1. **Step 2**: Amazon Managed Service for Apache Flink identifies sales with anomalous behavior and sends to a data stream for outliers.
1. **Step 3**: Amazon Kinesis Data Firehose sends data to an Amazon Simple Storage Service (Amazon S3) staged data bucket in parquet format. Items that were in the data stream as outliers are sent to this analysis bucket and are consumed by Amazon QuickSight with alerts configured.
1. **Step 4**: A scheduled AWS Glue job runs Extract, Transform, and Load (ETL) to convert the staged data and the pre-processed data into the forecast format. It prepares the target time series, related time series, and item metadata datasets.
1. **Step 5**: An Amazon S3 event notification is sent to an Amazon EventBridge, invokes a rule, and calls AWS Step Functions. It creates datasets, a dataset group, and a predictor. It also analyzes metrics, creates a forecast, and exports results using Amazon SageMaker Canvas.
1. **Step 6**: An Amazon S3 event notification invokes an AWS Glue job. This enriches the exported forecast with data from the stage data bucket, and prepares it for Amazon Athena.
1. **Step 7**: A dashboard is available in QuickSight with forecasted values. Optionally, a webpage will call forecasts for a product and store it in Amazon DynamoDB.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance is designed to provide you with the information necessary to help you understand your internal business state. For instance, each component sends logs and metrics to Amazon CloudWatch for monitoring. And DynamoDB is used to process information, such as last forecast completion time and number of items analyzed, providing transparency to your business users. You can also choose to deploy this Guidance with AWS CloudFormation that allows for small and frequent changes, and adapt it to fit within a continuous integration and continuous delivery (CI/CD) pipeline. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance provides a selection of capabilities that helps ensure you have robust identity management in place. With Amazon S3, all buckets have encryption enabled and are configured to restrict access for only those services that should interact with it. The other services in this Guidance use AWS Identity and Access Management (IAM) policies with least-privilege access, allowing users to connect and complete only the necessary actions. QuickSight is provisioned with a login page for business users, and if you deploy the option of a webpage for forecasts with DynamoDB, you can use Amazon Cognito for authentication. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance supports a reliable architecture for each application level. The components that process data, such as AWS Lambda, AWS Glue, Step Functions, and Athena are serverless, reducing concerns with scalability and scaling. In the data layer, this Guidance uses Amazon S3 that provides 11 9s of durability and DynamoDB that scales automatically to adapt to the application's load. And Forecast and QuickSight are fully managed services that provide automated recovery from failures and scalability. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The services selected for were purpose-built for this Guidance. The fully managed services, such as QuickSight, will adapt its capacity for the number of interactions, providing performance as it scales. DynamoDB auto-scales horizontally, allowing consistency in performance even with peak loads. You can experiment with this Guidance by adjusting Lambda and AWS Glue to process data faster and according to the needs of retraining the model. SageMaker Canvas will explore and process a series of adjustments based on the user’s data to achieve the best performance without the need for the user to understand machine learning extensively. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The components in this Guidance are serverless, providing a pay-as-you-go approach, avoiding oversized, provisioned resources to help you keep the costs related to the number of completions and the amount of data to be processed. From the data perspective, ETL is processed by a scheduled AWS Glue job, stored in Amazon S3, and read by Athena, avoiding spends with servers. SageMaker Canvas will be retrained only when scheduled, avoiding costs with this process as well. QuickSight provides cost per active user, allowing you to start with costs only for dedicated analysts. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses a serverless first approach, which means that there are no compute idle resources. The fully managed services in this Guidance scale as demand grows, reducing and optimizing the number of resources running. For example, AWS Glue will process on schedule, turn on its resources, process ETL, store it on Amazon S3, and turn the servers and the resources down. This directly reduces energy consumption and the impact of your carbon footprint. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
