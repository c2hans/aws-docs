---
source_url: https://docs.aws.amazon.com/solutions/social-media-data-pipeline-on-aws/index.html
---

---
title: 'Guidance for Social Media Data Pipeline on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/social-media-data-pipeline-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Social Media Data Pipeline on AWS

## Overview

This Guidance helps customers use social media feeds to derive better business outcomes and an improved customer experience. Social media feeds provide data to run successful customer sentiment analysis, targeted campaigns, targeted ads, and content moderation. This Guidance demonstrates an end-to-end pipeline to build a near real-time social media corpus on AWS using cloud-native, serverless computing. With this pipeline, customers can capture time-sensitive information about current trends and product feedback from social media feeds.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/social-media-data-pipeline-on-aws.pdf)

![Architecture diagram](/images/solutions/social-media-data-pipeline-on-aws/images/social-media-data-pipeline-on-aws-1.png)

1. **Step 1**: Amazon EventBridge rules activate AWS Lambda functions to get the Twitter trends for a specific region, which are stored in Amazon DynamoDB. AWS Systems Manager (parameter store) is used for inputs such as location and credentials.
1. **Step 2**: Scheduled Lambda functions get the latest trends from DynamoDB and publish them as events to EventBridge event bus for processing. EventBridge supports loosely-coupled event-driven applications at scale.
1. **Step 3**: EventBridge rules activate AWS Step Functions for each event. Step Functions validates, tracks, and pushes the message to Amazon Simple Queue Service (Amazon SQS) to retrieve tweets. SQS is used in this architecture to manage the Twitter API throttling and errors.
1. **Step 4**: For the batch of SQS messages, Lambda fetches the tweets using Search API and transforms and pushes the messages to EventBridge. DynamoDB stores "pagination" tokens and other details.
1. **Step 5**: EventBridge invokes Lambda to fetch and transform popular subreddits and comments and publish them to EventBridge. DynamoDB stores search state.
1. **Step 6**: EventBridge receives the messages from all sources in a common format.
1. **Step 7**: Each message initiates Step Functions to validate, transform, and load the data to the targeted storage location.
1. **Step 8**: Amazon Comprehend detects the language model if not present in the message.
1. **Step 9**: Amazon Simple Storage Service (Amazon S3) provides durable and scalable storage for corpus.
1. **Step 10**: As an optional step, use Amazon Kinesis to push the metadata information to other sources, such as Amazon Redshift, for better analytics and querying.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch captures service-level metrics for all the workload components. Application and transaction-specific logs are pushed to CloudWatch Logs. CloudWatch dashboards provide a centralized view to monitor resources and understand workload state. This unified view can be customized for metrics and alarms. CloudWatch alarms and events alert you of risks or anomalies so you can take proactive actions to maintain the health of your workload. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance features a data pipeline focused on service-to-service communications rather than points of user interaction. AWS service-to-service communication is configured with Identity and Access Management (IAM) service-linked roles with fine-grained access polices. Data transfer is protected by transport layer security (TLS)-based communication for AWS service and social media platform integrations. AWS services in this Guidance use storage-level encryption to protect data at rest. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance is based on loosely-coupled, event driven architecture, and it uses near real-time or scheduled events to communicate between decoupled services. Most of the service interactions are asynchronous in nature through an intermediate durable storage layer, such as an SQS queue or a streaming data platform, such as Kinesis or Step Functions. Additionally, social media platform feeds are the major data source for this architecture. The pipeline is designed to accommodate throttling constraints imposed by social media platforms. You can perform reliability load testing for the end-to-end workflow on a production-like environment to validate that the workload meets scaling and performance requirements. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

We chose purpose-built services for this Guidance that will help achieve optimal performance, such as Amazon S3 for the data lake, DynamoDB for config data, and Amazon Comprehend for language models. We also selected these services because they can optimize costs, scale as business needs grow, and maintain high availability to prevent downtime. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses a serverless architecture designed to scale based on demand. This helps you grow with increasing business needs, while keeping costs down during the entry phase and non-peak times. Once you identify workload patterns in production, you can explore additional cost optimization features, such as the DynamoDB pricing model for provisioned capacity. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses AWS service features that optimize data access patterns and storage requirements so that you don’t store data that you no longer need. For example, with DynamoDB Time to Live (TTL), you can define a timestamp that indicates when items should expire. DynamoDB will then delete the item from your table without consuming any write throughput. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
