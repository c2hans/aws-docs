---
source_url: https://docs.aws.amazon.com/solutions/modern-insurance-data-lakes-on-aws/index.html
---

---
title: 'Guidance for Modern Insurance Data Lakes on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/modern-insurance-data-lakes-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Modern Insurance Data Lakes on AWS

## Overview

This Guidance demonstrates how to build a modern, serverless data lake on AWS tailored for the insurance industry. It enables you to collect data from disparate core systems and third parties, set up self-service data access, and set the foundation for business intelligence (BI) and machine learning (ML) features that drive informed decision-making. This Guidance helps you leverage data effectively through a data lake architectural pattern that allows you to quickly get started on the cloud, reducing the time it takes to extract value from your data.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/modern-insurance-data-lakes-on-aws.pdf)

![Architecture diagram](/images/solutions/modern-insurance-data-lakes-on-aws/images/modern-insurance-data-lakes-on-aws-1.png)

1. **Step 1**: Business analysts define the data pipeline operations using low-code configuration files stored in an Amazon Simple Storage Service (Amazon S3) bucket. Data sources upload source data files, such as policies and claims, to the Collect S3 bucket.
1. **Step 2**: An ObjectCreated event invokes an AWS Lambda function that reads metadata from the incoming source data, logs all actions, and starts the AWS Step Functions workflow.
1. **Step 3**: Step Functions calls AWS Glue jobs that map the data to your predefined data dictionary. These jobs then perform the transformations and data quality checks for both the Cleanse and Consume layers.
1. **Step 4**: Amazon DynamoDB contains lookup values used by the lookup and multi-lookup transforms; extract, transform, and load (ETL) metadata such as job audit logs, data lineage output logs, and data quality results are written here.
1. **Step 5**: AWS Glue jobs store cleansed and curated data in Amazon S3 as compressed, partitioned Apache Parquet files. AWS Glue jobs also create and update the AWS Glue Data Catalog databases and tables.
1. **Step 6**: AWS Glue jobs store source data file validation failures in an Amazon S3 Quarantine folder and Data Catalog table which can populate an exception queue dashboard that allows a human to review and take appropriate action.
1. **Step 7**: Amazon Athena runs SQL queries using the Data Catalog databases and tables.
1. **Step 8**: Amazon QuickSight dashboards and reports pull data from the data lake on a near real-time or scheduled basis.
1. **Step 9**: AWS CodePipeline manages the full DevSecOps cycle for the infrastructure, application, and pipeline configuration.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code for ETL](https://github.com/aws-solutions-library-samples/aws-insurancelake-etl)
[Go to sample code for infrastructure](https://github.com/aws-solutions-library-samples/aws-insurancelake-infrastructure)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Lambda functions, Step Functions state machines, and AWS Glue job output logs curate diagnostic and status information in Amazon CloudWatch logs. Data lineage, job audit data, and data quality results stored in DynamoDB enable publishing metrics and audit data to operational dashboards. Automated deployment of data lake environments using CodePipeline and consistent tagging of infrastructure and ETL resources across stacks facilitate centralized customization in AWS Cloud Development Kit (AWS CDK). Diagnostic logs and metrics in CloudWatch for Step Functions, Lambda, and AWS Glue provide near real-time transparency for effective monitoring of data pipeline job progress and performance. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Public access to S3 buckets is blocked, encryption for data in transit is required, and server-side encryption using AWS Key Management Service (AWS KMS) secures data at rest. Access to all S3 buckets is logged in a dedicated access log bucket for permission review and maintenance. Built-in data masking and hashing transforms in AWS Glue jobs protect sensitive data, and regular automated execution of data pipelines reduces manual errors or unauthorized access risks. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The inherent durability and availability of Amazon S3, which stores data across multiple Availability Zones, and DynamoDB, which automatically replicates data across three Availability Zones, enhance reliability. Amazon S3 versioning preserves, retrieves, and restores every version of objects, while DynamoDB deletion protection safeguards production environments. Additionally, CodePipeline and infrastructure as code enable easy resource replication across multiple Regions and accounts. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Optimized AWS Glue jobs minimize data processing units (DPU) hours consumed, and efficient Amazon S3 storage for Cleanse and Consume layers enables faster data scans and queries. DynamoDB efficiently stores data lineage, data quality results, job audit data, lookup transform data, and tokenized source data, and provides scalability and low-latency performance. The serverless nature of Athena and AWS Glue provides efficient data access without data movement. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon S3 lifecycle policies automatically transition data to Amazon S3 Glacier storage, and DynamoDB tables can use On-Demand Capacity mode and Infrequent Access storage class as needed. DynamoDB Time to Live (TTL) automatically deletes expired items, and AWS Glue DPU auto scaling and flex capacity right-size compute resources. Fully managed, serverless services like Amazon S3, AWS Glue, and DynamoDB optimize costs by only charging for consumed resources without infrastructure maintenance overhead. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The efficient Parquet file format for data storage in Cleanse and Consume S3 buckets reduces the energy impact of querying data. The serverless design and On-Demand Capacity mode of DynamoDB minimize the carbon footprint compared to on-premises or provisioned database servers. Lambda functions using AWS Graviton processors are more energy-efficient than traditional computer workloads. Fully managed, serverless services help ensure the data lake only consumes resources when needed, minimizing environmental impact. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
