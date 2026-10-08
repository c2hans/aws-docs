---
source_url: https://docs.aws.amazon.com/solutions/product-360-on-aws/index.html
---

---
title: 'Guidance for Product 360 on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/product-360-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Product 360 on AWS

## Overview

This Guidance helps you increase customer engagement through a Product 360 framework. Product 360 is a data analytics framework that provides insights by aggregating relevant information from data sources for a comprehensive view of products. This comprehensive view enhances sales motions based on product usage patterns and guides product strategy and roadmap development. This Guidance is also combined with artificial intelligence and machine learning (AI/ML)-augmented recommendations to support data-driven decision-making for future products.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/product-360-on-aws.pdf)

![Architecture diagram](/images/solutions/product-360-on-aws/images/product-360-on-aws-1.png)

1. **Step 1**: Sources for Product 360 include product, customer relationship management (CRM), sales transaction, pricing, customer interaction, and clickstream data.
1. **Step 2**: AWS Database Migration Service (AWS DMS) ingests data from database and analytical sources, and Amazon AppFlow ingests data from software-as-a-service (SaaS) services.
1. **Step 3**: Ingested data is sent in its original, immutable format to an Amazon Simple Storage Service (Amazon S3) raw zone bucket.
1. **Step 4**: Data processing and pipeline orchestration is conducted using purpose-built data processing components and transformation libraries through AWS Step Functions and Amazon EMR. Amazon DynamoDB stores pipeline configuration and schema information about data sources.
1. **Step 5**: Amazon EventBridge initiates Step Functions, which invokes Amazon EMR to transform raw data into an efficient data format (Parquet). This data is moved to a clean zone S3 bucket.
1. **Step 6**: EventBridge initiates Step Functions again, which invokes Amazon EMR to use Apache Spark-based batch and streaming pipelines to create Apache Iceberg-based data in the curated zone S3 bucket from the clean zone S3 bucket.
1. **Step 7**: The analytics layer uses Amazon QuickSight and Amazon Athena to natively integrate with the curated zone for analytics, dashboards, ad-hoc reporting, and ML.
1. **Step 8**: Amazon Forecast forecasts product demand, and an S3 bucket stores forecast output. Athena and QuickSight query and visualize the forecast output.
1. **Step 9**: Using AWS Lake Formation, Product 360 users will get fine-grained access to data assets in the curated zone and forecast S3 buckets for consumption.
1. **Step 10**: AWS Glue Data Catalog stores technical metadata for all data assets in S3 buckets, which is used for querying the data assets from Athena and QuickSight.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS services used in this Guidance are provisioned in the same AWS Region to reduce data transfer charges. Additionally, services such as QuickSight do not accrue any data transfer charges. Additionally, most services in this Guidance are either serverless or are available with a serverless option, such as Amazon EMR Serverless. Serverless services do not need to run for extended periods of time. You can take advantage of sustained usage through reserved instances for Amazon EMR. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Lake Formation applies central audited governance, fine-grained access controls, and data classification tagging. This helps you secure data at the object-, database-, table-, column-, and row-level. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Serverless services such as AWS Glue and DynamoDB scale horizontally, automatically responding to the velocity of data ingestion and processing. This scaling enables the architecture to adapt to changes imposed upon it. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The component-oriented architecture allows you to build independent layers using infrastructure as code (IaC). By separating the ingestion, processing, storage, unified governance, cataloging, and consumption, you can more easily test and deploy modules. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The serverless architecture reduces the amount of underlying infrastructure that needs to be managed, allowing you to focus on differentiated work, such as onboarding new customers and building new feature enhancements. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon Forecast summarizes large data sets into meaningful insights. This reduces data volumes and processing, helping ensure that you only use the minimum resources required. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
