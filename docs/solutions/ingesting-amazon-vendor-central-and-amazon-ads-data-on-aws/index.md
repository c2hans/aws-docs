---
source_url: https://docs.aws.amazon.com/solutions/ingesting-amazon-vendor-central-and-amazon-ads-data-on-aws/index.html
---

---
title: 'Guidance for Ingesting Amazon Vendor Central and Amazon Ads Data on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/ingesting-amazon-vendor-central-and-amazon-ads-data-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Ingesting Amazon Vendor Central and Amazon Ads Data on AWS

## Overview

This Guidance details the best practices for integrating the Amazon Ads and Amazon Selling Partner APIs. From creating a reporting workflow with AWS Step Functions, to storing and processing data using Amazon Simple Storage Service (Amazon S3) with AWS Glue, this Guidance covers the best approach to designing an Amazon Ads and Amazon Retail data pipeline on AWS. The data accumulated from this pipeline can be combined with data retrieved from Amazon Marketing Cloud (AMC) through [Amazon Marketing Cloud Insights on AWS](https://aws.amazon.com/solutions/implementations/amazon-marketing-cloud-insights-on-aws/) to formulate an Amazon Ads and Amazon Retail data lake on AWS. This data lake can then be visualized with a business intelligence tool, like Amazon QuickSight.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/ingesting-amazon-vendor-central-and-amazon-ads-data-on-aws.pdf)

![Architecture diagram](/images/solutions/ingesting-amazon-vendor-central-and-amazon-ads-data-on-aws/images/ingesting-amazon-vendor-central-and-amazon-ads-data-on-aws-1.png)

1. **Step 1**: Amazon EventBridge is used to schedule a job which starts an AWS Step Functions state machine. The state machine processes a series of AWS Lambda functions to facilitate the creation of reports.
1. **Step 2**: The state machine invokes a Lambda function (Create Request Initiation) to create a report request from the Amazon Ads API or Amazon Selling Partner API. API credentials should be stored within AWS Secrets Manager and used when making calls to the APIs. The state machine then moves into a series of polling steps, invoking a Lambda function (Check Report Status) to check the report request status, before finally downloading the report. The metadata for each report downloaded is stored in Amazon DynamoDB.
1. **Step 3**: The Lambda function (Download Report) writes the report into a raw Amazon Simple Storage Service (Amazon S3) bucket with a prefix which contains the specific report type and report date. Lambda uses AWS Key Management Service (AWS KMS), managed by AWS, to encrypt the reports as they're written to the Amazon S3 bucket.
1. **Step 4**: A Step Functions state machine is invoked by notifications from Amazon S3 objects as they're inserted into the bucket. When no more objects are received after a given time, the data transformation Step Functions state machine starts and invokes a Lambda function.
1. **Step 5**: A Lambda function (Update Metadata) stores the task token for Step Functions initiation ID in the DynamoDB table. Data is processed utilizing an AWS Glue job to read the data from the raw Amazon S3 bucket, and transformed to a usable format.
1. **Step 6**: The AWS Glue job writes the transformed data to the standard Amazon S3 bucket along with AWS Glue Data Catalog metadata. The AWS KMS Customer Managed Key (CMK) is used to encrypt the bucket contents and the AWS Glue metadata.
1. **Step 7**: Amazon Simple Notification Service (Amazon SNS) is used to send notifications as new data is transformed into the standard Amazon S3 bucket.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Operational excellence is the focus on running and monitoring systems effectively, and we accomplish that here with the help of Step Functions, which is used to visualize the overall workflow when the API report is created and downloaded. Additionally, Amazon CloudWatch can be used in this Guidance to help you visualize metrics and logs across all services used. Lastly, Amazon SNS lets you know when reports have succeeded or failed. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM), CloudWatch, AWS KMS, and Secrets Manager collectively protect data, systems, and assets in ways that improves your security posture. First, IAM policies are scoped down to provide least privilege access required for the services to function properly. By scoping IAM policies to the minimum permission required, you limit unauthorized access to resources. Second, AWS KMS provides encryption for both data at-rest and data in-transit using Pretty Good Privacy (PGP) encryption of data files. Third, Secrets Manager provides secure storage for API keys and hashes. AWS KMS and Secrets Manager are used to ensure that data and sensitive information is secured properly using encryption and hashing. And fourth, CloudWatch monitors logs and metrics across all services used to detect unexpected and unwanted behaviour. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Lambda, Amazon S3, and DynamoDB help ensure your workloads perform their intended functions correctly and consistently, as well as help your workloads recover quickly from failure. With Lambda, you can initiate code without managing infrastructure. It also runs your function in multiple Availability Zones to ensure that it is available to process events in case of a service interruption in a single zone. Amazon S3 stores multiple copies of data across Availability Zones and provides 99.999999999% (11 9's) of durability of the data stored within the buckets. Furthermore, DynamoDB provides a serverless data store and stores multiple copies of data across Availability Zones while maintaining consistent and fast performance. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda and AWS Glue help you structure and streamline your allocation of IT and computing resources. Lambda supports parallelization and concurrency with automatic scaling and can handle many concurrent processes to support the ingestion of multiple data pipeline workflows. AWS Glue jobs can scale both horizontally and vertically by letting you set the number of workers and the worker type to support small and large extract, transform, and load (ETL) processes. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

AWS Glue is a serverless ETL service and only incurs cost when an AWS Glue job is occurring. When no AWS Glue job occurs, AWS Glue does not incur cost. And, AWS Glue scales both vertically and horizontally, allowing you to tune your ETL processes to be the most cost efficient. AWS Glue is cost efficient, resilient, highly performant, and scales to support any dataset transformation size. In addition, Amazon S3 stores reporting data and allows you to choose how data is stored into different tiers. You can configure Amazon S3 Lifecycle Policies to ensure older data is stored on storage tiers with less cost. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda offers autoscaling, as well as the ability to scale from zero to peak demands to ensure only the required capacity is utilized. Also, DynamoDB removes unused resources from the database based on time to live (TTL), set by you, so only necessary storage is utilized. DynamoDB supports both provisioned and on-demand capacity to ensure only the necessary capacity is used to support the workload. Data stored in DynamoDB is compressed so minimal storage space is utilized. These services help ensure the lowest footprint of compute and data storage while lowering overall carbon generation, as services are only utilized as-needed with the most performant resources available. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
