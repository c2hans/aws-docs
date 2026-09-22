---
source_url: https://docs.aws.amazon.com/solutions/enterprise-search-and-audit-for-amazon-s3/index.html
---

---
title: 'Guidance for Enterprise Search and Audit for Amazon S3'
canonical_url: https://docs.aws.amazon.com/solutions/enterprise-search-and-audit-for-amazon-s3/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Enterprise Search and Audit for Amazon S3

## Overview

This Guidance helps customers create a single aggregation point for either an enterprise or a disparate collection of AWS accounts that host Amazon Simple Storage Service (Amazon S3) object data. Currently, customers cannot view object-level metadata across an entire organization or search for objects across S3 buckets or accounts. This architecture aggregates object PUT, DELETE, and GET calls into a searchable interface, so customers can search based on object tags, accounts, bucket names, and prefixes. With this search functionality, customers can identify which objects are not encrypted, find S3 buckets that have been inactive for a long period, search object tags, and see read requests on an object level.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/enterprise-search-and-audit-for-amazon-s3.pdf)

![Architecture diagram](/images/solutions/enterprise-search-and-audit-for-amazon-s3/images/enterprise-search-and-audit-for-amazon-s3-1.png)

1. **Step 1**: Any account (1, 2, or N) generates an event for Amazon Simple Storage Service (Amazon S3) operations, such as GET, PUT, DELETE, or storage tier updates.
1. **Step 2**: The event gets recorded in Amazon EventBridge and in an Amazon S3 logging bucket for the specific event source bucket.
1. **Step 3**: EventBridge in the individual account (1, 2 or N) sends data to EventBridge in the AWS aggregation account, and the event is then forwarded to Amazon Simple Notification Service (Amazon SNS) which then distributes events to different Amazon Simple Queue Service (Amazon SQS).
1. **Step 4**: AWS Lambda functions process events from Amazon SQS in batches. Lambda functions create HEAD requests to the source bucket to get the metadata of each object. For GET requests, Lambda functions process log files from the logging buckets to record GET requests.
1. **Step 5**: All data is pushed to an Amazon OpenSearch Service cluster, which hosts metadata for all objects.
1. **Step 6**: An S3 static site hosts a React JavaScript site that allows authorized users to browse OpenSearch Service metadata through Amazon API Gateway and Lambda functions.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-enterprise-search-and-audit-for-amazon-s3)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

You can set up Amazon CloudWatch metrics and alarms for OpenSearch Service to monitor CPU, memory, and storage. All other services in this architecture are serverless and managed by AWS. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

You can encrypt data in-transit with transport layer security (TLS). You can encrypt data at rest in OpenSearch Service, which is the only component in this architecture that stores data. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

OpenSearch Service is the only service in this architecture that permanently stores data and that would require data recovery. OpenSearch Service takes hourly snapshots, or backups of a cluster’s index and state. In the case of disaster recovery, you can use these snapshots to create a new OpenSearch Service cluster. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

EventBridge offers cross-account and cross-Region event shipping. Amazon SQS is purpose-built for queueing. Lambda and API Gateway are designed to scale automatically without requiring human intervention. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Serverless services in this architecture such as EventBridge, Amazon SQS, Lambda, and API Gateway use pay as you go pricing, meaning you only pay for the amount of resources you actually use. We recommend using Amazon EC2 Reserved Instances (RIs) for OpenSearch Service, which can provide a discount of up to 72% compared to on-demand pricing. Additionally, Lambda is eligible for Compute Savings Plans, a flexible pricing model that can reduce costs by up to 66%. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This architecture uses multiple serverless services, such as Amazon SQS, Lambda, EventBridge, and API Gateway, that offer automatic scaling based on demand. This helps ensure maximum utilization of resources. Although OpenSearch Service is a managed service, it can also be configured to scale based on changes in demand. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
