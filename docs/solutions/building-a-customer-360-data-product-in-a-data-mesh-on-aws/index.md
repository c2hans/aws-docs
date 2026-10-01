---
source_url: https://docs.aws.amazon.com/solutions/building-a-customer-360-data-product-in-a-data-mesh-on-aws/index.html
---

---
title: 'Guidance for Building a Customer 360 Data Product in a Data Mesh on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-a-customer-360-data-product-in-a-data-mesh-on-aws/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Building a Customer 360 Data Product in a Data Mesh on AWS

## Overview

This Guidance shows how to implement a Customer 360 Data Product using a data mesh for a decentralized cloud architecture. With a data mesh framework, you can combine and link data with centrally governed guidelines, helping business teams build and share core data products with their wider organization.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/building-a-customer-360-data-product-in-a-data-mesh-on-aws.pdf)

![Architecture diagram](/images/solutions/building-a-customer-360-data-product-in-a-data-mesh-on-aws/images/building-a-customer-360-data-product-in-a-data-mesh-on-aws-1.png)

1. **Step 1**: The data required for building a customer 360 product for your enterprise is distributed in source systems, such as a Customer Data Platform (CDP), Point of Sale (POS), Unified Communication as a Service (UCaaS), ecommerce, and many other data sources.
1. **Step 2**: Ingest data from source systems into AWS using AWS services like Amazon AppFlow. Event-driven and near real-time ingestion can be achieved using Amazon Kinesis and Amazon EventBridge.
1. **Step 3**: Core data products owned by business teams can be built using AWS services. For example, a campaign performance data product is owned by the marketing team and combines data from multiple campaign sources. These sources can include audio ads, paid ads, pay-per-click, influencer campaigns, and more. Amazon EMR can be used to process these interactive analytics. AWS Entity Resolution can be used to deduplicate and unify customer master data. This curated data can be published through output ports such as files using Amazon Simple Storage Service (Amazon S3) and AWS Glue Data Catalog or APIs published using AWS Lambda.
1. **Step 4**: An agent performance data product owned by a support team is built using data from customer chatbot conversations, support call recordings, and cases. It is ingested through AppFlow and processed using Amazon Comprehend. These customer insights can be published through output ports as files using Amazon S3.
1. **Step 5**: A sales analytics data product owned by a sales team is built on source data like order, payments and product data. This data is stored in Amazon Redshift data warehouse for analysis and can be accessed using SQL or by using APIs built through Lambda.
1. **Step 6**: Composite Data Products, such as Customer 360 and Customer Journey Analytics, can be built using Amazon Redshift and Amazon Neptune by combining multiple core data products.
1. **Step 7**: Data products are secured, published, and governed using AWS services such as AWS Lake Formation and Data Catalog. Metadata changes in data products can be automatically captured using AWS Glue Crawlers. Shared capabilities such as data quality, deduplication, and monitoring can be implemented using AWS Glue Data Quality and Amazon CloudWatch.
1. **Step 8**: Existing business applications, such as core data products and ecommerce using an AWS Cloud Development Kit, can consume data products using SQL or API endpoints.
1. **Step 9**: Users, such as data scientists, can consume data products to build a machine learning (ML) model using Amazon SageMaker for customer insights like next best offer or customer intent prediction. Business analysts can build self-service dashboards using Amazon QuickSight.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

A customer 360 data product in a data mesh helps you to collect, transform, govern, and analyze customer data, all from a central location. You can build customer profiles, as well as analyze customer journeys and interactions to create a personalized user experience. The decentralized nature of a data mesh distinguishes it from traditional data warehouses and data lakes. Data products are owned by department leaders and shared across organizations using a data product library leveraging Data Catalog. Central governance is established using Lake Formation features, such as tag-based security, access policies, and approval workflows. Changes in data products are captured automatically using AWS Glue Data Crawlers to keep metadata consistent across the data mesh. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

When configuring this Guidance, all the data in Amazon S3 is encrypted at rest using AWS Key Management Service (AWS KMS). Also, SageMaker can only access the data through virtual private cloud (VPC) endpoints, meaning the data does not travel through the public internet. Finally, AWS Identity and Access Management (IAM) and Lake Formation are used to control access to the data. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

When configuring this Guidance, data is stored in Amazon S3, an object storage service that offers 99.999999999% durability, making it a reliable way to store the data since it provides high reliability and fault tolerance while also being cost-effective. Amazon Athena, QuickSight, and AWS Glue are serverless and help you to query and visualize the data at scale without you needing to worry about provisioning infrastructure. Also, SageMaker offers a broad set of machine learning (ML) services, putting ML at the hands of every developer and data scientist. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda is a serverless compute service that automatically scales up and down depending on the demand. While AWS Glue, Athena, and QuickSight are used to query and visualize the results to help you monitor performance and maintain efficiency as your business needs evolve. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Unlike a centralized data warehouse that replicates and combines data from various sources, data is managed, federated, and decentralized in a data mesh. Configuring a data mesh helps to minimize both data movement and redundant storage. It does this in a number of ways. First, Lambda is used to process data and exposes the data mesh as APIs. Due to the on-demand nature of Lambda, resources are consumed only for the usage duration. Also, AWS Glue jobs are used to extract, transfer, and load (ETL) a batch of users rather than individual records. Moreover, Athena and QuickSight are used to query and visualize the insights in a cost-efficient way. Finally, SageMaker batch inference jobs are used to create predictive insights. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda, AWS Glue, Athena, and QuickSight are all serverless services that work on-demand, maximizing the performance and utilization of resources. In addition, SageMaker batch inference jobs are processed using the appropriate size of instance to ensure an optimal utilization of the resources while being cost-efficient. By extensively using serverless services, you maximize overall resource utilization as compute is only used as needed. The efficient use of serverless resources reduces the overall energy required to operate the workload. You can also use the AWS Billing Conductor carbon footprint tool to calculate and track the environmental impact of the workload over time at an account, Region, and service level. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
