---
source_url: https://docs.aws.amazon.com/solutions/credit-card-fraud-detection-using-mainframe-data-replication-on-aws/index.html
---

---
title: 'Guidance for Credit Card Fraud Detection Using Mainframe Data Replication on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/credit-card-fraud-detection-using-mainframe-data-replication-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Credit Card Fraud Detection Using Mainframe Data Replication on AWS

## Overview

This Guidance demonstrates how to build a real-time fraud detection system using payment data replicated from your mainframe database. The replicated data powers three parallel workflows. First, it trains an Amazon Fraud Detector machine learning (ML) model to continuously improve detection accuracy. Second, it adds payment history details to authorization request messages, providing more context for merchants. Third, it analyzes data to generate insights and dashboards for business users, with natural language querying capabilities. These functions improve fraud detection capabilities and enable more informed decision-making for both merchants and the card-issuing financial institution.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/credit-card-fraud-detection-using-mainframe-data-replication-on-aws.pdf)

![Architecture diagram](/images/solutions/credit-card-fraud-detection-using-mainframe-data-replication-on-aws/images/credit-card-fraud-detection-using-mainframe-data-replication-on-aws-1.png)

1. **Step 1**: Your bank receives the card payment authorization requests on your mainframe.
1. **Step 2**: The authorization process makes a real-time call to AWS to get the fraud score using AWS compute.
1. **Step 3**: The integration application on AWS enriches the request with customer and merchant historical data stored on Amazon Relational Database Service (Amazon RDS).
1. **Step 4**: Artificial intelligence and machine learning (AI/ML) models running on Amazon SageMaker generate the fraud score and return it to the mainframe so that it can approve or decline the transaction.
1. **Step 5**: The authorization history message is inserted into an IBM Db2, virtual storage access method (VSAM), or IBM information management system (IMS) database.
1. **Step 6**: The Precisely publisher agent captures the database change records and publishes them to the apply agent running on an Amazon Elastic Compute Cloud (Amazon EC2) instance.
1. **Step 7**: The Precisely apply agent publishes the change records to Amazon Managed Streaming for Apache Kafka (Amazon MSK).
1. **Step 8**: An Amazon MSK connector process reads the messages from Amazon MSK and inserts them into the Amazon RDS history database. The same data is read during scoring.
1. **Step 9**: Amazon Data Firehose (successor to Amazon Kinesis Data Firehose) streams the data from Amazon MSK to Amazon Simple Storage Service (Amazon S3).
1. **Step 10**: Amazon Redshift consumes data from Amazon MSK. Business dashboards are created using Amazon QuickSight, which also provides the capability to query data using natural language.
1. **Step 11**: Amazon Simple Notification Service (Amazon SNS) and Amazon EventBridge send alerts and notifications.
1. **Step 12**: SageMaker trains the AI/ML model offline using the transaction data stored in Amazon S3 along with other internal and external data.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/migration/credit-card-fraud-detection-using-mainframe-data-replication-on-aws.html)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch monitors and tracks the flow of replicated messages. By reconciling messages at different points in the replication pipe, it can detect breaks in the dataflow. It can then alert you so that you can troubleshoot performance issues. Amazon MSK, Amazon Data Firehose, and EventBridge enable you to replay the replicated messages, restarting them from a specified point in time. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM)lets youcontrol authentication and authorization between various AWS services. To limit unauthorized access to resources, this Guidance scopes all IAM policies down to the minimum permissions required for the service to function properly. Additionally, AWS Secrets Manager securely stores and AWS Key Management Service (AWS KMS) encrypts the credentials used by Amazon RDS and Amazon MSK. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The Precisely apply engine runs on Amazon EC2 and uses standby instances to pick up the replication process if active instances fail. Additionally, Amazon MSK stores multiple copies of the data so that you can quickly recover it in case of failure. You can then replay the data, restarting from a point in time that you specify. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon MSK can distribute the replicated records into multiple partitions, thus enabling multiple consumers to process the records in parallel. These processes can also consume the messages from a specific Apache Kafka consumer group assigned to the process without interfering with others. Additionally, Amazon Data Firehose and EventBridge help in removing bottlenecks by processing the messages asynchronously. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon EC2 automatically scales up and down the number of compute instances that serve the fraud scoring requests coming from the mainframe. This helps you minimize costs because only the minimum number of compute instances required to run at any given time are provisioned. Additionally, SageMaker helps you lower costs by optimizing inferencing. It provides over 70 instance types and sizes for deploying ML models, such as instances powered by ML-optimized AWS Inferentia and AWS Graviton chipsets. Finally, you can use Amazon S3 Intelligent-Tiering to automatically move old data to cheaper storage tiers, lowering your overall storage costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance runs on AWS infrastructure, which is 3.6 times more energy efficient than the median of surveyed US enterprise data centers. It is also up to 5 times more energy efficient than the average European enterprise data center. As an example of AWS sustainable infrastructure, Amazon EC2 scales automatically to meet demand so that solutions don’t need to provision idle compute. By migrating mainframe data from your data centers to AWS, you can ultimately minimize the environmental impact of your processing workloads. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
