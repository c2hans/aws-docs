---
source_url: https://docs.aws.amazon.com/solutions/integrating-third-party-saas-data-using-amazon-appflow/index.html
---

---
title: 'Guidance for Integrating Third-Party SaaS Data using Amazon AppFlow'
canonical_url: https://docs.aws.amazon.com/solutions/integrating-third-party-saas-data-using-amazon-appflow/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for Integrating Third-Party SaaS Data using Amazon AppFlow

## Overview

This Guidance demonstrates how to ingest third-party Software as a Service (SaaS) data into Amazon S3 to build a serverless business intelligence pipeline. SaaS applications remove the burden of having to build a solution from the ground up. The challenge with SaaS applications is that the data exists in external data stores, making it difficult to analyze the data that comes from other sources. Importing data into Amazon S3 removes data silos and centralizes the data to transform and enrich the datasets. By deploying this Guidance, you can gain better insights from your SaaS data, remove barriers when integrating the data, and leverage a serverless architecture that provides on-demand resources and a pay-as-you-go pricing model.

## How it works

This architecture diagram shows how to integrate data from third-party software as a service (SaaS) providers into their data lake on AWS.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/integrating-third-party-saas-data-using-amazon-appflow.pdf)

![Architecture diagram](/images/solutions/integrating-third-party-saas-data-using-amazon-appflow/images/integrating-third-party-saas-data-using-amazon-appflow-1.png)

1. **Step 1**: Amazon AppFlow is invoked to run either on-demand, or on a schedule, to pull data from software as a service (SaaS) applications such as SAP, Salesforce, ServiceNow and other SaaS applications.
1. **Step 2**: Amazon AppFlow stores the raw data pulled from SaaS applications in Amazon Simple Storage Service (Amazon S3).
1. **Step 3**: Amazon AppFlow integrates with AWS Glue Data Catalog to catalog and store metadata.
1. **Step 4**: Using AWS Glue or AWS Glue DataBrew, the raw data is transformed and enriched using a low-code serverless data integration pipeline.
1. **Step 5**: AWS Glue reads Data Catalog to access raw data, and also makes a new table of the enriched and transformed data.
1. **Step 6**: Transformed data is stored in an Amazon S3 bucket (Curated_Data) that can be analyzed further using business intelligence (BI) services or tools.
1. **Step 7**: Amazon Athena integrates with Data Catalog to query curated data from the Amazon S3 bucket.
1. **Step 8**: Data is loaded into Amazon QuickSight SPICE cache for developing responsive dashboards.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-integrating-3rd-party-saas-data-with-amazon-appflow-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance focuses on deploying a decoupled architecture that is modular and can change based on business requirements. By using Amazon S3 as a data lake, you can integrate your SaaS data into BI tools like QuickSight. Future business requirements may change to use machine learning, and by using a data lake, the data can be easily integrated into AWS artificial intelligence and machine learning (AI/ML) services, such as Amazon SageMaker. You can also use Amazon Redshift as a data warehouse to provide live data querying capabilities using Open Data Connectivity (ODBC) or Java Database Connectivity (JDBC). [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

A number of design decisions were factored into securing people and machine access in this Guidance. One, credentials that Amazon AppFlow uses to authenticate with the SaaS applications are secured using AWS Secrets Manager. Credentials are encrypted and cannot be viewed by users or roles without explicit permissions in AWS Identity and Access Management (IAM). Data stored in Amazon S3 can be encrypted when it is written, and access to data is granted with IAM. Two, with a serverless architecture, AWS manages the network security of the underlying infrastructure. You only need to focus on granting permissions to the users of services using IAM. Third, all public access to Amazon S3 is blocked by default. Only users or roles with sufficient IAM permissions are able to perform actions in the bucket. Amazon S3 automatically applies server-side encryption for each new object, unless you specify a different encryption option. Data that moves from one service to another is encrypted in transit by default. Services that access Amazon S3, like AWS Glue, Athena, or QuickSight, all need explicit access in IAM to read or write data. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance implements a highly available network topology by using a serverless architecture that is deployed in a single Region and runs across multiple Availability Zones (AZs). This removes the single source of failure that could come from a rare, but possible, AZ failure. Additionally, application reliability is achieved by decoupling the application into individual components that focus on a single task. Having data from the SaaS application land in Amazon S3 allows you to ingest data without having to transform it in-transit. This makes it resilient to schema changes and other errors that may occur when ingesting or transforming the data in-transit. Once raw data is in Amazon S3, you can transform the dataset using AWS Glue or DataBrew without altering the source dataset, and have the transformed dataset land in an Amazon S3 curated data bucket. The curated dataset is used by Athena to load the data into the QuickSight SPICE cache. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Decoupling each service allows each component to work independently of each other. Each service is purpose built to perform a specific task. Services like AppFlow, Amazon S3, and Athena can scale up and down to meet demand without having to anticipate changes in demand. AWS Glue and AWS Glue DataBrew data processing units (DPUS) can be increased perform task faster, or process larger datasets. Optimizations of the data to increase performance can be done based on how the data is being queried. Query access patterns will determine if there is a need to use columnar storage, such as parquet, or partitioning the data based on query filters. This optimization will accelerate query performances in Athena. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance focuses on making a serverless BI pipeline. By using a serverless architecture, you only pay for what you use. Services like Amazon AppFlow, AWS Glue, and Athena only incur charges for times that those services are invoked and used. Services like Amazon S3 incur charges for the amount of data that is actually used. And, using a serverless architecture allows the architecture to scale up and down to meet demand without having to over provision resources. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Because deploying this Guidance results in a serverless BI pipeline, resources are on-demand and do not sit idle when not in use. This limits the overall hardware used in the AWS Cloud so you can maximize efficiency and minimize waste. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
