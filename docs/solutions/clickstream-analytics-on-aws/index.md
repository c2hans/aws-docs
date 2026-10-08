---
source_url: https://docs.aws.amazon.com/solutions/clickstream-analytics-on-aws/index.html
---

---
title: 'Guidance for Clickstream Analytics on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/clickstream-analytics-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Clickstream Analytics on AWS

## Overview

This Guidance demonstrates how to harness the power of clickstream analytics by automating the deployment of a comprehensive data pipeline for web and mobile applications. It helps organizations transform raw user interaction data into actionable business intelligence through a configurable AWS solution that streamlines data collection, ingestion, analysis, and visualization. The solution shows immediate business value by providing pre-built dashboards and analytics models that reveal critical user behavior patterns, enhance customer understanding, and optimize marketing effectiveness. Through purpose-built SDKs and APIs, companies can efficiently capture both standard and custom events, enabling data-driven decision making and product innovation while maximizing return on marketing investments.

## Benefits

### Out-of-the-box analytics

This solution offers a comprehensive view of dashboards. Furthermore, exploration models allow you to perform complex analytics, such as event, funnel, path, and retention analysis, enabling a deeper understanding of user behavior and engagement patterns.

### Complete data ownership

Clickstream data are available at the finest granularity within the security perimeter of an AWS account. You can query, extract, share, and join the user behavior data for multiple use cases.

### Cost effective

This solution is built on top of AWS serverless analytics services that auto scale for your data volume without requiring you to reserve any resources. Also, unlike other third-party solutions, this solution has no license charge, so you pay only for your actual AWS service usage.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/clickstream-analytics-on-aws.pdf)

![Architecture diagram](/images/solutions/clickstream-analytics-on-aws/images/clickstream-analytics-on-aws-1.png)

1. **Step 1**: An Amazon Cognito user pool or OpenID Connect (OIDC) handles authentication.
1. **Step 2**: Amazon CloudFront distributes the frontend web UI assets hosted in an Amazon Simple Storage Service (Amazon S3) bucket.
1. **Step 3**: Amazon API Gateway manages the backend APIs and routes traffic to AWS Lambda.
1. **Step 4**: Amazon DynamoDB stores persistent data from the web UI console.
1. **Step 5**: AWS CloudFormation, AWS Step Functions, Amazon EventBridge, and AWS Lambda orchestrate the lifecycle management of data pipelines.
1. **Step 6**: The data pipeline, consisting of Application Load Balancer, Amazon Elastic Container Service (Amazon ECS), Amazon Managed Streaming for Apache Kafka (Amazon MSK), Amazon Kinesis Data Streams, Amazon S3, Amazon EMR Serverless, Amazon Redshift, and Amazon QuickSight, provides scalable clickstream ingestion through load-balanced processing, buffered storage, ETL, and warehouse analytics.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](/solutions/latest/clickstream-analytics-on-aws/solution-overview.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-clickstream-analytics-on-aws)

## See it in action

### Solution Web Console

### Analytics Studio

### Event Analysis

### Funnel Analysis

### Path Analysis

### Analyses

## Related content

- **Hands-On Workshop**: In this workshop, you will get hands-on experience in using the Clickstream Analytics on AWS solution. It will guide you through an end-to-end process of building a production-level data pipeline, and collecting and analyzing clickstream data from an App.

[Learn more](https://catalog.workshops.aws/clickstream)

[Read usage guidelines](/solutions/guidance-disclaimers/)
