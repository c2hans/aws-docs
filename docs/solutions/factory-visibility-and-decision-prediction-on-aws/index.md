---
source_url: https://docs.aws.amazon.com/solutions/factory-visibility-and-decision-prediction-on-aws/index.html
---

---
title: 'Guidance for Factory Visibility and Decision Prediction on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/factory-visibility-and-decision-prediction-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Factory Visibility and Decision Prediction on AWS

## Overview

This Guidance helps provide visibility into aerospace manufacturing data, including current job status, shortages, and abnormalities. Stakeholders, from mechanics to CEOs, will be able to access safety, quality, delivery, cost, and attendance analytics across multiple product lines at an individual, department, or company level. This Guidance also embeds artificial intelligence and machine learning (AI/ML) to predict optimal manufacturing sequences and recovery, allowing leaders to quickly identify issues and make predictive changes to minimize their impact.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/factory-visibility-and-decision-prediction-on-aws.pdf)

![Architecture diagram](/images/solutions/factory-visibility-and-decision-prediction-on-aws/images/factory-visibility-and-decision-prediction-on-aws-1.png)

1. **Step 1**: Authorized users authenticate with single sign-on (SSO) through Amazon Cognito and AWS Directory Service.
1. **Step 2**: Enterprise Resource Planning (ERP), Material Requirement Planning (MRP), and Human Resources (HR) systems synchronize to cloud storage nightly using AWS Glue.
1. **Step 3**: Amazon Kinesis Data Firehose streams manufacturing and procurement events in near real time.
1. **Step 4**: AWS Glue ingests all data directly into managed, serverless data stores, including Amazon Redshift Serverless and AWS Lake Formation.
1. **Step 5**: Streaming manufacturing and procurement events invoke processes in AWS Lambda to update data with near real-time production status.
1. **Step 6**: Predict completion, cost, scrap, rework, and more using past and current production data with ML inference in Amazon SageMaker for "what-if" scenarios.
1. **Step 7**: Initiate user notifications for immediate action through email and SMS using Amazon Simple Notification Service (Amazon SNS).
1. **Step 8**: Production leaders access near real-time intelligence using a secure web portal with Amazon API Gateway, which provides a RESTful API for creating dynamic views.
1. **Step 9**: Create advanced, low-code/no-code graphical views and alerts in the web portal from the data warehouse using Amazon QuickSight and Lambda.
1. **Step 10**: Administer consistent security and cost controls across multiple accounts through AWS Organizations. Monitor cloud activity and costs through Amazon CloudWatch and AWS Cost Explorer.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Try out this Guidance**: Explore an interactive demo of this Guidance

[Explore demo](https://demos.awsplayer.com/guidance/factory-visibility-and-intelligence/index.html)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Customers evaluate their business priorities to identify the manufacturing and procurement key performance indicators (KPIs) that need monitoring. This Guidance is configurable to compute and report the signals of most value. You can evaluate your data compliance requirements and deploy data and security controls to AWS Regions that meet those requirements. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance uses fully managed services with native support for data-at-rest encryption, such as Amazon S3 and Amazon Redshift. Encryption keys are managed by AWS Key Management Service (AWS KMS), which enforces automation of key rotation. Data decryption is performed automatically by these services without user intervention or access to key material, after role-based authentication of the requester. The Guidance uses fully managed services to automate transfer of data, with built-in protocol-level enforcement of data encryption and user authentication (for example, through HTTPS and transport layer security [TLS] 1.3). [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

External data transfers occur through AWS-managed services, such as API Gateway, AWS Glue, and Amazon Kinesis Data Firehose, which provide high availability and resiliency to network faults. Internal traffic flows on the highly available AWS network within a single Region. Lambda functions that connect data consumers and producers automatically deploy across multiple Availability Zones within a Region, to provide high resilience and availability. CloudWatch metrics are configured for workload performance metrics such as data transfer rates, storage usage, concurrent Lambda requests, and latencies for web response. Alerts are configured in CloudWatch or through Amazon SNS (invoked by Lambda) to notify administrators of critical events. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses fully managed, serverless services which automatically scale the computing resources required to match current demand. Serverless database services can be configured for a capacity range that should be evaluated by the customer against predicted and actual usage. Predicted usage is based on expected number of simultaneous users, and actual usage is based on utilization metrics in the database or CloudWatch. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The predominant data transfer is inbound—it includes the nightly synchronization of on-premises ERP, MRP, and HR databases in addition to near real-time inbound streaming of production events. Inbound-to-AWS data transfers are free. Outbound transfers are limited to web portal traffic, which are used to see summary dashboards and maintenance activity, both of which require relatively little network traffic and data transfer cost. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses Amazon S3 to store streaming event logs. Amazon S3 can be configured for lifecycle management to automatically archive infrequently-accessed data to lower cost storage tiers or delete it altogether. Amazon Redshift can be configured to automatically generate backups, which are generated incrementally to minimize redundant storage. The Guidance can be implemented to automatically delete database rows that are outdated or are no longer required, with custom code that runs periodically. This capability is particularly efficient if tables are partitioned by time period. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
