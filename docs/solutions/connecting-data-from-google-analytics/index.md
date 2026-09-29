---
source_url: https://docs.aws.amazon.com/solutions/connecting-data-from-google-analytics/index.html
---

---
title: 'Guidance for Connecting Data from Google Analytics® to AWS Clean Rooms'
canonical_url: https://docs.aws.amazon.com/solutions/connecting-data-from-google-analytics/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Connecting Data from Google Analytics® to AWS Clean Rooms

## Overview

This Guidance demonstrates how to ingest Google Analytics v4 data into AWS for marketing analytics. It explores each stage of building the solution including: data ingestion, transformation, data cataloging, and analysis.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/connecting-data-from-google-analytics.pdf)

![Architecture diagram](/images/solutions/connecting-data-from-google-analytics/images/connecting-data-from-google-analytics-1.png)

1. **Step 1**: Amazon EventBridge scheduled rule performs and starts the AWS Step Functions workflow.
1. **Step 2**: Google BigQuery access credentials are securely stored in AWS Secrets Manager and encrypted with AWS Key Management Service (AWS KMS).
1. **Step 3**: AWS Glue job will ingest data using the AWS Marketplace Google BigQuery Connector for AWS Glue. The Connector simplifies the process of connecting AWS Glue jobs to extract data from BigQuery. This AWS Glue job will encrypt, normalize, and hash the data.
1. **Step 4**: The output of the AWS Glue job is written to the target Amazon Simple Storage Service (Amazon S3) bucket:prefix location in parquet format. After an AWS Clean Rooms collaboration, custom audience data such as emails, phone numbers, or mobile advertiser IDs are hashed, encrypted, and stored in designated prefixes. The output file setting is partitioned by date and encrypted with AWS KMS.
1. **Step 5**: AWS Glue crawler job is activated to 'refresh' the table definition and its associated meta-data in the AWS Glue Data Catalog.
1. **Step 6**: The data consumer queries the data output with Amazon Athena.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: A detailed guide is provided to experiment and use within your AWS account. Each stage of building the Guidance, including deployment, usage, and cleanup, is examined to prepare it for deployment. The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open implementation guide](https://aws-solutions-library-samples.github.io/advertising-marketing/connecting-data-from-google-analytics.html)
[Open sample code on GitHub](https://github.com/aws-samples/connecting-data-from-google-analytics)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch Events delivers a near real-time stream of system events that describe changes in resources. Amazon CloudWatch logs enables you to monitor, store, and access log files from various resources to notify when certain thresholds are met. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) is used to set and manage fine-grained access control. Least-privilege policies are used to grant only the permissions required to perform the task. AWS KMS ensures data persists in encrypted format for protection from unauthorized access. Secrets Manager enables you to rotate, manage, and retrieve database credentials such as API Keys and other secrets throughout their lifecycle. AWS Glue supports using resource policies to control access to Data Catalog resources. These resources include databases, tables, connections, and user-defined functions, along with the Data Catalog APIs that interact with these resources. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

To support a highly available network, serverless technologies used in this solution have built-in fault tolerance and automatically scale based on the demand. The applications utilize the AWS global infrastructure that is built around AWS Regions and Availability Zones. AWS Regions provide multiple, physically separated, and isolated Availability Zones that are connected with low-latency, high-throughput, and highly redundant networking. Services automatically fail over between Availability Zones without interruption. AWS Glue is subject to region-specific service quota that may affect reliability. You can contact AWS Support to request a quota increase based on needs. Step Functions can be used to set up retries, backoff rates, max attempts, intervals, and timeouts for any failed AWS Glue job. Amazon CloudWatch is used to collect and track metrics, collect and monitor log files, and can be used to set alarms. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses serverless technologies and inherits the tenets of serverless: no server management, built-in fault tolerance, continuous scaling, and pay-for-value services. In addition, use of serverless services allows comparative testing against varying load levels and minimizes undifferentiated tasks like capacity provisioning and patching, so that the user can focus more on business needs. Auto scaling is available for AWS Glue ETL jobs. With auto scaling enabled, AWS Glue automatically adds and removes workers from the cluster depending on the parallelism at each stage of the job run. Amazon S3 automatically scales to high request rates. There are no limits to the number of prefixes in a bucket and you can increase read or write performance by using parallelization. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Serverless architecture uses a pay-per-value pricing model and the user pays only for the resources they consume. This Guidance uses AWS Serverless services including AWS Glue, Data Catalog, Amazon S3, EventBridge, and Step Functions that have no upfront costs and are designed to scale based on demand. With AWS Glue, you pay an hourly rate (billed by the second) for crawlers (discovering data) and ETL jobs (processing and loading data) but may incur cost for marketplace Google BigQuery Connector. For the Data Catalog, you pay a simple monthly fee for storing and accessing the metadata. With Amazon S3, you pay for storing objects in buckets. With EventBridge free tier, you can schedule rules to initiate data processing using Step Functions workflow where you are charged based on the number of state transitions. Leveraging Athena as a serverless, scalable, and interactive query service makes it easy to analyze data directly in Amazon S3 using standard SQL and you pay only for the queries you run. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Serverless services used in this guidance (AWS Glue,Amazon S3) automatically optimizes the resources utilization in response to demand. You can extend this guidance by using Amazon S3 lifecycle configuration to define policies to move objects to different storage classes based on access pattern. By using serverless services, your applications maximize overall resource utilization as compute is only used as needed. The efficient use of serverless resources reduces the overall energy required to operate the workload. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
