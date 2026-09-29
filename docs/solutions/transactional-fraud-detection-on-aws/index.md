---
source_url: https://docs.aws.amazon.com/solutions/transactional-fraud-detection-on-aws/index.html
---

---
title: 'Guidance for Transactional Fraud Detection on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/transactional-fraud-detection-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Transactional Fraud Detection on AWS

## Overview

This Guidance shows how to build a serverless workflow to identify patterns of fraudulent activity within streaming data through both micro- and macroanalysis. Amazon Timestream helps analyze microlevel indicators, such as activities occurring within a short timeframe. Amazon Neptune then uses that data to flag potentially fraudulent activity within a macrolevel fraud graph, and performs in-depth, context-specific analysis on that flagged data. By using these services in tandem, you can improve detection capabilities and enrich the analysis of fraud impact. This Guidance can also apply to other uses requiring both micro- and macrolevel analysis, such as customer data platforms and trading risk platforms.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/transactional-fraud-detection-on-aws.pdf)

![Architecture diagram](/images/solutions/transactional-fraud-detection-on-aws/images/transactional-fraud-detection-on-aws-1.png)

1. **Step 1**: The applications sends real-time transaction data to a data ingestion API.
1. **Step 2**: Analyze the transaction data stream using an adapter between Amazon Kinesis Data Streams and Amazon Timestream. The adapter is deployed as an Amazon Managed Service for Apache Flink application.
1. **Step 3**: Send the analyzed stream to a Timestream transaction table.
1. **Step 4**: A Timestream scheduled query identifies aggregate metrics, such as aggregated high-value transactions made by an account in the last 5 minutes.
1. **Step 5**: The aggregated transaction metrics are stored in another Timestream table.
1. **Step 6**: Analyze the transaction data stream with an adapter between Kinesis Data Streams and Amazon Neptune based on AWS Lambda.
1. **Step 7**: Store graph data in a Neptune database for macroanalysis.
1. **Step 8**: Neptune data is made available an Amazon Athena connector for Neptune.
1. **Step 9**: Analyze the data points and graphs using a custom script (one-time analysis) with an Amazon SageMaker notebook.
1. **Step 10**: Athena provides federated access for downstream systems.
1. **Step 11**: Visualize the suspected fraud accounts and their network of accounts by using Amazon QuickSight dashboards.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-transactional-fraud-detection-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

As managed services, Neptune, Timestream, Kinesis Data Streams, and Amazon Managed Service for Apache Flink minimize your operational burden. Additionally, Lambda is serverless and event driven, automatically scaling to meet the unpredictable demand of fraud detection—for example, seasonal and hourly variations. Finally, Amazon CloudWatch helps you quickly detect, track, troubleshoot, and resolve operational issues at scale. These services work together to help you achieve maximum uptime with minimal effort. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM), which enables you to centrally manage security, lets you create roles and policies so that only authorized users can access resources. Amazon Virtual Private Cloud (Amazon VPC) lets you isolate various resources within a private environment, and CloudWatch keeps all telemetry data within your account. These services all support data encryption at rest and in transit, and they keep your data in the AWS Cloud at all times. As a result, you reduce the number of potential attack vectors, minimizing the risk of inadvertent data disclosures. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Timestream and Neptune replicate data across at least three Availability Zones, providing 99.99 percent durability and reliability. Additionally, Timestream and Lambda are serverless services, and Neptune offers a serverless option. As a result, your solution can automatically adjust its capacity to meet demand, reducing downtime and increasing reliability. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

As serverless services, Kinesis Data Streams supports high-throughput data ingestion. Timestream is also serverless, scaling up and down with workload demand, and it can ingest trillions of events daily. Additionally, Neptune provides a serverless option that supports automatic scaling, helping you optimize reads and writes. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Kinesis Data Streams, Amazon Managed Service for Apache Flink, Neptune, Timestream, and Lambda provide serverless capabilities,optimizing the overall cost of the solution. Serverless technology provides flexible and scalable usage-based infrastructure and enables quicker time to release, helping you avoid the cost of overprovisioning infrastructure. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Kinesis Data Streams, Amazon Managed Service for Apache Flink, Neptune, Timestream, and Lambda are serverless or provide serverless options, helping you achieve better sustainability. By scaling up and down to meet workload requirements, serverless infrastructure helps you avoid the extra energy expenditure of overprovisioning. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
