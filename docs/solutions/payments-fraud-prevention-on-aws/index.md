---
source_url: https://docs.aws.amazon.com/solutions/payments-fraud-prevention-on-aws/index.html
---

---
title: 'Guidance for Payments Fraud Prevention on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/payments-fraud-prevention-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Payments Fraud Prevention on AWS

## Overview

This Guidance shows how payment service providers can implement a near real-time fraud screening system on AWS by streaming data. Transactions are scored by risk using machine learning (ML) models, and notifications are sent to customers based on the risk level of the transactions.

## How it works

This high-level reference architecture shows how payment companies can implement a near real-time fraud screening system on AWS.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/payments-fraud-prevention-on-aws.pdf)

![Architecture diagram](/images/solutions/payments-fraud-prevention-on-aws/images/payments-fraud-prevention-on-aws-1.png)

1. **Step 1**: Large amounts of customer data stored in on-premises databases; file systems, and long-term historical data on mainframes is moved into Amazon Simple Storage Service (Amazon S3) using various data transfer services such as Amazon EMR, AWS Data Migration Service (AWS DMS), AWS DataSync, and Amazon Kinesis Data Streams.
1. **Step 2**: Configure AWS Glue to initiate your extract, transform, load (ETL) jobs to run as soon as new data becomes available in Amazon S3.
1. **Step 3**: Amazon Athena makes it easy to analyze data directly in Amazon S3 using standard SQL.
1. **Step 4**: Near real-time transactions are sent to Amazon Kinesis Data Streams. AWS Lambda integrates natively with Amazon Kinesis as a consumer to process data ingested through a data stream.
1. **Step 5**: Multiple Lambda functions is invoked from a single Amazon API Gateway for different kinds of inference.
1. **Step 6**: An Amazon SageMaker notebook instance with different machine learning (ML) models that will be trained on the dataset gives a prediction score to the endpoint.
1. **Step 7**: The fraud ring and profile analytics in near real-time that was queried through Amazon Athena is persisted in Amazon DynamoDB.
1. **Step 8**: The final aggregated score is calculated based on inferences and a notification is sent to an end user in the event of fraud through Amazon Pinpoint.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance shows how fully managed services such as AWS DataSync, Amazon EMR, and Kinesis allow you to break free from the complexities of database and data warehouse administration. You can send logs directly from your application to CloudWatch using the CloudWatch Logs API, or send events using an AWS SDK and Amazon EventBridge. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Raw data is ingested into Amazon S3. Amazon S3 supports both server-side encryption and client-side encryption for data uploads. You can encrypt metadata objects in your AWS Glue Data Catalog in addition to the data written to Amazon S3 and Amazon CloudWatch Logs by jobs, crawlers, and development endpoints. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The solution is modular and has the ability to scale based on the transactions. Serverless capabilities such as Kinesis and Lambda automatically scale throughput up or down based on demand. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Serverless architectures help to provision the exact resources that the workload needs. Lambda manages scaling automatically. You can optimize the individual Lambda functions used in your application to reduce latency and increase throughput. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance is designed to be fully optimized for cost, only using resources where necessary and only accessing data using the services appropriate for the business need. All costs should align with the defined goals for pricing and clearly defined KPIs for managing batch, compared with near real time requirements to ensure the optimum value benefits. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By extensively using managed services and dynamic scaling, you minimize the environmental impact of the backend services. Technologies that support data access and storage patterns should be monitored to ensure that assets such as data are stored in the optimum solution based on the read and write access patterns, paying close attention to the scaling of compute resources closely aligned to the demand. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
