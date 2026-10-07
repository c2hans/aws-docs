---
source_url: https://docs.aws.amazon.com/solutions/carbon-data-lake-on-aws/index.html
---

---
title: 'Guidance for Carbon Data Lake on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/carbon-data-lake-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Carbon Data Lake on AWS

## Overview

This Guidance, with the sample code, can be used to deploy a carbon data lake to the AWS Cloud using an AWS Cloud Development Kit (AWS CDK). It provides customers and partners with the foundational infrastructure that can be extended to support use cases including monitoring, tracking, reporting, and impact verification of greenhouse gas emissions. The carbon data lake Guidance sample code deploys a data lake and processing pipeline that assists with data ingestion, aggregation, automated processing, and CO2 equivalent calculation based on ingested greenhouse gas emissions data. Please note: This solution by itself will not make a customer compliant with any end-to-end carbon accounting solution. It provides the foundational infrastructure from which additional complementary solutions can be integrated.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/carbon-data-lake-on-aws.pdf)

![Architecture diagram](/images/solutions/carbon-data-lake-on-aws/images/carbon-data-lake-on-aws-1.png)

1. **Step 1**: Customer emissions data from various sources is mapped to a standard CSV upload template. The CSV is uploaded, either directly to the Amazon Simple Storage Service (Amazon S3) landing bucket, or through the user interface.
1. **Step 2**: Amazon S3 landing bucket provides a single landing zone for all ingested emissions data. Data ingress to the landing zone bucket triggers the data pipeline.
1. **Step 3**: AWS Step Functions workflow orchestrates the data pipeline including data quality check, data compaction, transformation, standardization, and enrichment with an emissions calculator AWS Lambda function.
1. **Step 4**: AWS Glue DataBrew provides data quality auditing and an alerting workflow, and Lambda functions provide integration with Amazon Simple Notification Service (Amazon SNS) and AWS Amplify web application.
1. **Step 5**: Lambda functions provide data lineage processing, queued by Amazon Simple Queue Service (Amazon SQS). Amazon DynamoDB provides NoSQL pointer storage for the data ledger, and a Lambda function provides data lineage audit functionality, tracing all data transformations for a given record.
1. **Step 6**: A Lambda function outputs calculated CO2 equivalent emissions by referencing a DynamoDB table with Customer provided emissions factors.
1. **Step 7**: Amazon S3 enriched bucket provides data object storage for analytics workloads and the DynamoDB calculated emissions table provides storage for GraphQL API (a query language for users API).
1. **Step 8**: Customers can deploy a prebuilt Amazon SageMaker notebook and a prebuilt Amazon QuickSight dashboard with artificial intelligence and machine learning stacks, and business intelligence stacks. Deployments come with prebuilt Amazon Athena queries to query data stored in Amazon S3. Each service includes Amazon S3 enriched object storage.
1. **Step 9**: Customers can deploy a Web Application stack that uses AWS AppSync for a GraphQL API backend to integrate with web applications and other data consumer applications. Amplify provides a serverless, pre-configured management application that includes basic data browsing, data visualization, data uploader, and application configuration.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Deploy this Guidance**: Use sample code to deploy this Guidance in your AWS account

[Sample code](https://github.com/aws-solutions-library-samples/guidance-for-carbon-data-lake-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

If any changes are required for the Guidance, they can be implemented and deployed using GitHub Issues. All new deployments are tested through unit, security, infrastructure, and deployment testing. Feedback can be visualized through the Step Functions workflow visuals. If data is not processed through the pipeline, the Step Functions workflow will visually depict at which point in the process the data processing failed. There are also Amazon SNS notifications that are sent when a pipeline fails for any reason. By using the Step Functions and Amazon SNS notifications, users can isolate the tech stack that caused a problem and evaluate the data submitted to the pipeline about the tech stack identified. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance applies a zero-trust model for authentication and authorization. All users to the web application are authenticated using Amazon Cognito user pools. All additional resources are granted least-privilege access and all access patterns are evaluated using the cdk-nag utility to check AWS Cloud Development Kit (AWS CDK) applications. All data is encrypted at rest and in transit using AWS Key Management Service (AWS KMS), Amazon S3, Lambda, AWS Glue DataBrew, and DynamoDB. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The services in this Guidance are highly available by default through AWS Managed Services (AMS). By enabling the provided sample code, all Amazon S3 bucket access is logged by default. Managed services such as Lambda and Step Functions emit Amazon CloudWatch metrics, and appropriate alarms can be configured to notify users about threshold breaches. All deployment and configuration changes are managed using AWS CDK, reducing the possibility of human error. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The README file contains specific directions to extend, modify, or add to the Guidance. AWS customers or partners can extend the Guidance by adding additional ingestion APIs such as: building custom emissions factor libraries, doing custom calculations, and creating custom visualizations, forecasting, or AI/ML tools. To decrease latency and improve performance, this Guidance is designed for deployment in any major AWS Region using AWS CDK regional context. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The services in this guidance are managed by AWS and are serverless. They were selected to meet the demand with only the minimum resources required. We evaluated and tested with simulated synthetic data sources, selecting services that optimize performance while reducing cost and carbon footprint. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By using an on-demand serverless architecture and Step Functions, this Guidance can continually scale to match the load with only the minimum resources. All data processing is compressed and each layer of the architecture deploys to a single Region by default. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
