---
source_url: https://docs.aws.amazon.com/solutions/customer-data-analytics-on-aws/index.html
---

# Guidance for Customer Data Analytics on AWS

## Overview

This Guidance helps you improve customer retention by performing data collection and analysis on customer demographics, behavior, and preferences. You can achieve data optimization by building a modern customer data platform and a data analytics pipeline that generates actionable data insights about your customers. With a modern data architecture on AWS, you can use purpose-built data services to rapidly build scalable data lakes, ensure compliance, and easily share data across organizational boundaries.

## How it works

This architecture helps you build modern customer data analytics pipelines and derive insights from the data you collect.

[Download the architecture diagram PDF](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/customer-data-analytics-on-aws.pdf)

![Architecture diagram](/images/solutions/customer-data-analytics-on-aws/images/customer-data-analytics-on-aws-1.png)

1. **Step 1**: Data is collected from multiple data sources across the enterprise, including software-as-a-service (SaaS) applications, edge devices, logs, streaming media, and social networks. Online web activity comes from web sites, social media platforms, emails, and online campaigns. Offline sources include purchase history and subscriptions – primarily customer relationship management (CRM) and 3rd party data.
1. **Step 2**: Based on the type of data source, you can ingest the data into a data lake in AWS by using AWS Database Migration Service (AWS DMS), AWS DataSync, Amazon Kinesis, Amazon Managed Streaming for Apache Kafka (Amazon MSK), or Amazon AppFlow.
1. **Step 3**: AWS Data Exchange can be used to integrate third-party data into the data lake.
1. **Step 4**: Build a scalable data lake by using AWS Lake Formation, and use Amazon Simple Storage Service (Amazon S3) for data lake storage.
1. **Step 5**: You can also use AWS Lake Formation to enable unified governance, which helps you centrally manage security, access control (table, row, or column level security), and audit trails. It also enables automatic schema discovery and conversion to required formats.
1. **Step 6**: AWS Glue extracts, transforms, catalogs, and ingests data across multiple data stores. Use AWS Glue DataBrew for visual data preparation and AWS Lambda for enrichment and validation.
1. **Step 7**: Amazon QuickSight provides machine learning (ML) powered business intelligence. Amazon Redshift is used as a cloud data warehouse. Amazon SageMaker and AWS ML services can be used to build, train, and deploy ML models, and add intelligence to your applications. Amazon Redshift Spectrum and Amazon Athena have interactive querying, analyzing, and processing capabilities. Amazon Managed Service for Apache Flink is used to transform and analyze streaming data in real time.
1. **Step 8**: Store unified customer profile information in Amazon OpenSearch Service (elastic search).
1. **Step 9**: Build a single customer profile view with the help of identity resolution data coming from Amazon Neptune.
1. **Step 10**: With Amazon API Gateway, you can expose developed APIs as microservices.
1. **Step 11**: Activate the unified customer data and send it to internal and external parties.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The Customer Data Analytics Platform (CDAP) reference architecture is fully serverless. Your solution can be deployed with infrastructure as code and automation for fast iteration and consistent deployments. Use Amazon CloudWatch for application and Infrastructure monitoring. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Use Lake Formation for unified governance to centrally manage security, access control (at the table, row, column security level), and audit trails. It also enables automatic schema discovery and conversion to required formats. API Gateway enforces policies that control security aspects such as authentication, authorization, or traffic management. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Serverless architecture enables the solution to be automatically scalable, available, and deployed across all Availability Zones. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

By using serverless technologies, you only provision the exact resources you need. To maximize the performance of the CDAP solution, test with multiple instance types. Use API Gateway Edge endpoints for geographically dispersed customers. Use Regional for regional customers (and when using other AWS services within the same Region). [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

By using serverless technologies and automatically scaling, you only pay for the resources you use. Serverless services don’t cost anything while they’re idle. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Minimize your environmental impact. Data lake uses processes to automatically move infrequently accessed data to cold storage with Amazon S3 Lifecycle configurations. By extensively using managed services and dynamic scaling, this architecture minimizes the environmental impact of the backend services. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
