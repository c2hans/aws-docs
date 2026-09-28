---
source_url: https://docs.aws.amazon.com/solutions/identification-of-problematic-betting-and-gaming-on-aws/index.html
---

---
title: 'Guidance for Identification of Problematic Betting & Gaming on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/identification-of-problematic-betting-and-gaming-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Identification of Problematic Betting & Gaming on AWS

## Overview

This Guidance shows how to create an automated responsible gaming mechanism to protect your players from problematic betting and gaming behavior. By using technology from AWS and AWS Partner Databricks, you can build an impartial, scalable, artificial intelligence and machine learning (AI/ML) workflow that creates a risk score, predicts problematic behavior, and notifies you in near real-time. You can then automate responses that intervene, helping to reduce harm that players may experience due to problematic play.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/identification-of-problematic-betting-and-gaming-on-aws.pdf)

![Architecture diagram](/images/solutions/identification-of-problematic-betting-and-gaming-on-aws/images/identification-of-problematic-betting-and-gaming-on-aws-1.png)

1. **Step 1**: Amazon Kinesis agents encrypt and send data to Amazon Kinesis Data Streams, which forwards it to Amazon Kinesis Data Firehose for risk evaluation, formatting, and storage of raw data using Amazon Simple Storage Service (Amazon S3).
1. **Step 2**: The Databricks Lakehouse Platform (Databricks) running on the Amazon Elastic Compute Cloud (Amazon EC2) extract, transform, load (ETL) and training cluster reads raw data from Amazon S3 and transforms the data to clean data, then to curated data, writing it back to Amazon S3 using the Delta Lake format.
1. **Step 3**: Access to Amazon S3 is brokered by an Amazon S3 gateway endpoint, providing secure, reliable connectivity without requiring an internet gateway or network address translation device.
1. **Step 4**: Amazon QuickSight provides dashboards that access curated data.
1. **Step 5**: The ML model creates a risk score to predict problematic play and publishes that model to an Amazon EC2 inference cluster.
1. **Step 6**: Kinesis Data Firehose invokes an AWS Lambda function to send wagers through representational state transfer to the Databricks Lakehouse Platform on the Amazon EC2 inference cluster (Databricks cluster) for risk evaluation, which returns a risk score for each player wager.
1. **Step 7**: Lambda evaluates the risk score and forwards it to Amazon EventBridge if it exceeds a customer-configured threshold.
1. **Step 8**: EventBridge sends notification events to Amazon Simple Notification Service (Amazon SNS) or to Amazon Pinpoint or Amazon Connect Customer using Lambda. Monitoring and logging information is sent to Amazon CloudWatch.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses EventBridge, which lets you make small architectural changes and simplifies data redirection. Kinesis Data Streams supports a configurable retention period of its streaming data to reduce downstream impact in the event of downtime. You can also use the lifecycle management features of the Amazon S3 Intelligent-Tiering storage class so that raw ML data can automatically move to the optimal access tier based on access frequency. Additionally, you can use CloudWatch for detailed monitoring and logging. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance uses Amazon Virtual Private Cloud (Amazon VPC) so that your data resides only within a network under your full control. Kinesis Data Streams encrypts your data in transit and also provides server-side encryption to automatically encrypt your data at rest. Amazon S3 encrypts all object uploads to all buckets. You can also block public access to all of your objects at the bucket- or the account-level with the Amazon S3 Block Public Access feature. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses Kinesis Data Streams, which lets you configure a seven-day data retention period so that downstream systems can reprocess data in the event of data loss or a processing failure. Amazon S3, which is designed to provide 99.999999999 percent object durability, stores objects redundantly across multiple facilities to increase the reliability of your data storage. Additionally, Lambda runs functions in multiple Availability Zones (AZs) so that it can complete processing in the event of a service interruption to a single AZ. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses Lambda, which automatically provisions separate implementation environments for each concurrent request so that it can scale to meet your capacity needs without overprovisioning resources. You can configure the Transmission Control Protocol (TCP) keep alive feature to avoid creating new TCP connections for subsequent function invocations. Additionally, Kinesis Data Streams provides an on-demand capacity mode that automatically scales to accommodate your workload throughput needs. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses Kinesis Data Streams, which provides a managed, serverless architecture for data streaming, so that you don’t need to deploy, configure, or maintain streaming server hardware and software. You only pay for what you use, and you can shift to more cost-effective provisioned capacity when traffic is steadier, reducing costs. Additionally, enhanced shard-level monitoring lets you gain insights into traffic patterns so that you can merge underused shards for further cost savings. This Guidance also lets you use S3 Intelligent-Tiering to automatically move your data to the most cost-effective access tier. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses serverless services like Kinesis Data Streams and Lambda, which distribute their environmental impact across many users through multi-tenant control planes. Additionally, Kinesis Data Streams provides an on-demand capacity mode, which uses automatic scaling so that only the resources required to handle the current workload are running. Likewise, Lambda automatically scales the number of implementation environments up and down so that no idle resources are running. ARM-based AWS Graviton processors increase the price performance of Lambda by up to 34 percent over x86-based functions, further minimizing hardware requirements. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
