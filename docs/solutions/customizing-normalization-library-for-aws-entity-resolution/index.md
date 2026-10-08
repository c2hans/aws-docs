---
source_url: https://docs.aws.amazon.com/solutions/customizing-normalization-library-for-aws-entity-resolution/index.html
---

---
title: 'Guidance for Customizing Normalization Library for AWS Entity Resolution'
canonical_url: https://docs.aws.amazon.com/solutions/customizing-normalization-library-for-aws-entity-resolution/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Customizing Normalization Library for AWS Entity Resolution

## Overview

This Guidance demonstrates how to customize and apply normalization rules on data as it arrives and prepare it for AWS Entity Resolution. Normalization standardizes the input data through tasks such as removing extra spaces and special characters or standardizing to lowercase. This Guidance provides a cloud development kit (CDK) code that demonstrates how to read the data input from an Amazon Simple Storage Service (Amazon S3) bucket, apply the normalization rules, and prepare the resultant dataset for use in AWS Entity Resolution.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/customizing-normalization-library-for-aws-entity-resolution.pdf)

![Architecture diagram](/images/solutions/customizing-normalization-library-for-aws-entity-resolution/images/customizing-normalization-library-for-aws-entity-resolution-1.png)

1. **Step 1**: The Amazon Simple Storage Service (Amazon S3) bucket hosts the input data source. Server-side encryption with Amazon S3 managed keys (SSE-S3) encrypt data in the bucket. As new data arrives in the bucket, it initiates a notification.
1. **Step 2**: Amazon S3 sends the notification to the AWS Lambda function, which then initiates an AWS Step Functions workflow.
1. **Step 3**: Lambda within the Step Function initiates an AWS Glue job to pass information related to the new data files.
1. **Step 4**: The AWS Glue job executes the normalization rules on the newly arrived data and writes the output to an S3 bucket, encrypted using SSE-S3.
1. **Step 5**: Once the AWS Glue job succeeds, Lambda invokes a crawler to crawl the recently written files to the cleansed S3 bucket.
1. **Step 6**: The AWS Glue Crawler crawls the newly written files in the S3 bucket and updates the AWS Glue Data Catalog table with updated information related to schema and partition, if applicable.
1. **Step 7**: As new data gets written into the S3 bucket with cleansed data, Amazon EventBridge notifies AWS Entity Resolution that there is new data available for entity resolution.
1. **Step 8**: AWS Entity Resolution performs the entity resolution on the data and writes the corresponding output to an S3 bucket, encrypted using SSE-S3.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/advertising-marketing/customizing-normalization-library-for-aws-entity-resolution.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-customizing-normalization-library-for-aws-entity-resolution/)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Every service in this Guidance publishes metrics to Amazon CloudWatch, through which you can configure dashboards and alarms. Amazon CloudWatch Events deliver a near real-time stream of system events that describe changes in resources. Use alarms or Amazon SNS to notify incident management systems of events and escalate based on severity. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The data at rest in the S3 bucket is encrypted. AWS Glue supports using resource policies to control access to AWS Glue Data Catalog resources. These resources include databases, tables, connections, and user-defined functions, along with the AWS Glue Data Catalog APIs that interact with these resources. You can turn on encryption of objects in the AWS Glue Data Catalog and encrypt connection passwords using AWS Key Management Service (AWS KMS). [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance needs to implement throttling and retries. AWS Glue is subject to a Region-specific service quota that may affect reliability. You can contact AWS Support to request a quota increase based on your workload. Additionally, you can use Step Functions to set up retries, backoff rates, max attempts, intervals, and timeouts for any failed AWS Glue job. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

You can experiment and test each Guidance component, enabling you to perform comparative testing against varying load levels, configurations, and services. For example, auto scaling is available for AWS Glue extract, transform, load (ETL) jobs. With auto scaling enabled, AWS Glue automatically adds and removes workers from the cluster depending on the parallelism at each stage of the job run. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The services in this Guidance are designed to help you optimize costs based on your workload. When Amazon Glue performs data transformations, you pay only for infrastructure during the time the processing is occurring. For the AWS Glue Data Catalog, you pay a monthly fee for storing and accessing the metadata. With Amazon S3, you pay for storing objects in buckets. With EventBridge Free Tier, you can schedule rules to initiate data processing using the Step Functions workflow, and you will be charged based on the number of state transitions. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Serverless services used in this Guidance, such as AWS Glue and Amazon S3, automatically optimize resource utilization in response to demand. You can also use Amazon S3 lifecycle configuration to define policies that move objects to different storage classes based on access pattern. This helps free up storage resources that would otherwise unnecessarily be used to store infrequently accessed objects. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
