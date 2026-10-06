---
source_url: https://docs.aws.amazon.com/solutions/customer-lifetime-value-analytics-on-aws/index.html
---

---
title: 'Guidance for Customer Lifetime Value Analytics on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/customer-lifetime-value-analytics-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Customer Lifetime Value Analytics on AWS

## Overview

This Guidance demonstrates how to improve the accuracy of the Customer Lifetime Value (CLV) metric by combining the data from both historical and proprietary databases, unifying operational and real-time data, and delivering that data through a powerful business intelligence service. Using the scenario of a financial institution, this Guidance demonstrates how to leverage data from various sources, such as transaction systems, enterprise resource planning (ERP), customer clickstream data, as well as data from customer relationship management (CRM) software. A machine learning model can then be trained on those results and predict a CLV. The results are displayed in interactive dashboards to visualize customer profiles, revenue, and lifetime value, empowering users to unlock actionable insights.

## How it works

This architecture diagram shows how financial institutions can implement and leverage Customer Lifetime Value (CLV) using AWS services.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/customer-lifetime-value-analytics-on-aws.pdf)

![Architecture diagram](/images/solutions/customer-lifetime-value-analytics-on-aws/images/customer-lifetime-value-analytics-on-aws-1.png)

1. **Step 1**: Transactional data workload is modernized by moving from commercial database engines to (open source) Amazon Aurora, using AWS Database Migration Service (AWS DMS).
1. **Step 2**: AWS DMS replicates data from Amazon Relational Database Service (Amazon RDS) to the data warehouse with Amazon Redshift.
1. **Step 3**: Sales data is made available in an Amazon Simple Storage Service (Amazon S3) bucket (such as a CSV file) directly from the data source, which in this case is Salesforce.com (SFDC).
1. **Step 4**: You can generate clickstream data while using the application.
1. **Step 5**: An AWS Glue job copies data from the source Amazon S3 bucket (CSV from SFDC) towards the "Raw Data" Amazon S3 bucket.
1. **Step 6**: Amazon Kinesis Data Streams uses clickstream data through a data stream.
1. **Step 7**: Amazon Redshift can directly use streaming data from Kinesis Data Streams.
1. **Step 8**: An AWS Glue extract, transform, and load (ETL) job cleanses raw data and writes it into the "curated area" of the Amazon S3 bucket.
1. **Step 9**: Amazon Redshift centralizes historical revenues, customer profiles, and clickstream data to allow advanced customer spend and revenue analytics.
1. **Step 10**: Amazon QuickSight is used by the bank advisors and the marketing teams to visualize customer profiles, revenues, lifetime value, and make decisions.
1. **Step 11**: Amazon Redshift uses Amazon SageMaker to train a machine learning (ML) model and predict the Customer Lifetime Value (CLV) using historical data.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS CloudTrail and Amazon CloudWatch can be configured with this Guidance to ensure continuous monitoring and auditing of workloads, vital for maintaining high operational standards in any industry. CloudTrail provides governance, compliance, and operational auditing, while CloudWatch offers monitoring and observability. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Key Management Service (AWS KMS) has native data encryption integration with the services used in this Guidance. Whereas AWS Identity and Access Management (IAM) helps to both define minimum permissions for accessing every resource and reduce data exposure. Essential for safeguarding data and operations, these services offer robust security layers, crucial across industries. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon S3 and Elastic Load Balancing (ELB) help to ensure workloads are performing their intended functions correctly, consistently, while recovering quickly from failure. Specifically, Amazon S3 ensures data durability and availability, while ELB enhances application fault tolerance. Reliability is fundamental in this Guidance, and these services work in tandem to help ensure data integrity and consistent application performance. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Aurora is an AWS managed relational database engine, offering a high-performance, distributed storage system, ideal for data processing. Amazon Redshift is a fast, simple, cost-effective data warehouse service, enabling efficient large dataset handling through parallel query processing. These services are selected for their superior data processing capabilities, crucial for handling diverse datasets in a performance-focused environment. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The services configured throughout this Guidance are pivotal for cost management, offering scalable solutions that align with the financial objectives of any industry by optimizing resources and minimizing unnecessary expenses. For example, AWS DMS is a service that helps you migrate databases with minimal downtime, facilitating cost-effective data replication. A serverless architecture, particularly with AWS DMS, ensures operational cost efficiency through resource auto-scaling and serverless deployment. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance provides end users with insights on customer lifetime value. It allows bank advisors and marketing teams to target only the right customers and reduce the carbon footprint of all the customer engagement channels (like emails and printed proposals). It does this sustainability with the help of Amazon S3 that offers scalable storage, which reduces resource usage, and AWS Lambda, an event-driven service that optimizes computing resources. Selected for their efficient resource management, these services support eco-friendly goals by reducing the carbon footprint across industries. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
