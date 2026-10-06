---
source_url: https://docs.aws.amazon.com/solutions/connecting-data-from-adobe-experience-platform/index.html
---

---
title: 'Guidance for Connecting Data from Adobe Experience Platform® to AWS Clean Rooms'
canonical_url: https://docs.aws.amazon.com/solutions/connecting-data-from-adobe-experience-platform/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Connecting Data from Adobe Experience Platform® to AWS Clean Rooms

## Overview

This Guidance demonstrates how to import data from an Adobe Experience Platform (AEP) to AWS Clean Rooms. Using AWS services, customers can import their profile information from AEP into their AWS account, then process, normalize, and prepare it for marketing campaigns.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/connecting-data-from-adobe-experience-platform.pdf)

![Architecture diagram](/images/solutions/connecting-data-from-adobe-experience-platform/images/connecting-data-from-adobe-experience-platform-1.png)

1. **Step 1**: The AEP admin schedules a "daily" export job in the AEP to push the profile data to the customer's Amazon Simple Storage Service (Amazon S3) bucket within a pre-defined prefix.
1. **Step 2**: Create a rule in Amazon EventBridge to schedule the data processing in AWS Step Function once a day.
1. **Step 3**: The AWS Lambda function decrypts the files from the source Amazon S3 bucket using AWS Key Management Service (AWS KMS) and places them in a different prefix for AWS Glue DataBrew to pick up and process.
1. **Step 4**: AWS Glue DataBrew recipe will be executed to ingest the data from the decrypted source Amazon S3 bucket:prefix location. The data will be normalized, and Personal Identifiable Information (PII) data will be hashed (SHA256).
1. **Step 5**: The output of the AWS Glue DataBrew recipe will be written to the target Amazon S3 bucket:prefix location in parquet format. The output file setting will be an "overwrite" as the profile data is a full refresh. An AWS Glue Crawler job is triggered to "refresh" the table definition and its associated meta-data.
1. **Step 6**: The output of the AWS Glue DataBrew recipe will be written to the target Amazon S3 bucket:prefix location in parquet format. The output file setting will be an "overwrite" as the profile data is a full refresh. An AWS Glue Crawler job is triggered to "refresh" the table definition and its associated meta-data.
1. **Step 7**: The AWS Lambda function starts after the AWS Glue Crawler completes its run. The AWS Lambda will move the source data files to an "archive" prefix location as part of clean-up activity.
1. **Step 8**: An event will be published to Amazon Simple Notification Service (Amazon SNS) to inform the user that the new data files are now available for consumption within AWS Clean Rooms.
1. **Step 9**: The user utilizes the latest data within AWS Clean Rooms to collaborate with other data producers
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/advertising-marketing/connecting-data-from-adobe-experience-platform.html)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses a multi-tier architecture where every tier is independently scalable, deployable, and testable. The various facets of this multi-tier architecture are compute, storage, data management (catalog), and orchestration that are decoupled from each other. Observability is built-in, with every service publishing metrics to CloudWatch where dashboards and alarms can be configured. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Resources are protected using an Amazon S3 bucket to block public access. The data at rest in Amazon S3 is encrypted using Amazon S3-managed keys (SSE-S3). The data in transit from the external system into Amazon S3 is encrypted (with AWS KMS) and transferred over HTTPS. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Every service or technology chosen for each architecture layer is serverless and fully managed by AWS, making the overall architecture elastic, highly available, and fault-tolerant. Step Functions include error handling and notifications/alarms in case of failures. CloudWatch logs and metrics are used to track logs and events. CloudWatch alarms are configured to send notifications when thresholds are crossed.- [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The selection of AWS managed services for this architecture are purpose-built for Extract, Transform, and Load (ETL) applications (using AWS Glue and AWS Step Functions). A detailed implementation guide is provided for the user to experiment and use this Guidance within their AWS account. The serverless architecture reduces the amount of underlying infrastructure you need to manage, allowing you to focus on solving your business needs. You can use automated deployments to deploy the isolated customer data platform (CDP) tenants into any region quickly, providing data residence and reduced latency. In addition, you can experiment and test each CDP layer, enabling you to perform comparative testing against varying load levels, configurations, and services. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Using serverless technologies, you only pay for the resources you consume. As the data ingestion velocity increases and decreases, the costs will align with usage. When AWS Glue is performing data transformations, you only pay for the infrastructure while the processing is occurring. In addition, through a tenant isolation model and resource tagging, you can automate cost usage alerts and measure costs specific to each tenant, application module, and service. IAM policies are created using the least-privilege access, such that every policy is restricted to the specific resource and operation [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By using serverless services extensively, you get the most out of your resources. Compute is only used when needed. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
