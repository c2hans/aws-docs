---
source_url: https://docs.aws.amazon.com/solutions/core-banking-data-lake-on-aws/index.html
---

---
title: 'Guidance for Core Banking Data Lake on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/core-banking-data-lake-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Core Banking Data Lake on AWS

## Overview

This Guidance shows how credit unions can securely replicate and transform their Centralized Online Real-time Environment (core) banking data on AWS, unlocking actionable insights into key performance indicators such as new, lost, and returning members, deposit and loan growth, debit card usage, account openings, mortgage portfolios, member demographics, and bill pay adoption rates. By leveraging AWS as a robust data lake, and facilitating data transformation and visualization, credit unions can gain a deeper understanding of their members, drive revenue growth, and enhance data-driven decision-making.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/core-banking-data-lake-on-aws.pdf)

![Architecture diagram](/images/solutions/core-banking-data-lake-on-aws/images/core-banking-data-lake-on-aws-1.png)

1. **Step 1**: AWS Direct Connect provides transparent and resilient connectivity by connecting core banking data from customer data centers to the AWS Cloud.
1. **Step 2**: AWS Database Migration Service (AWS DMS) migrates and replicates data from the on-premises core database to the AWS Cloud.
1. **Step 3**: Amazon Simple Storage Service (Amazon S3) migrates and replicates data. The source database remains fully operational during the migration, minimizing downtime to applications that rely on the database.
1. **Step 4**: An Amazon EMR Serverless cluster is created with Apache Spark, an open-source, distributed processing system used for big data workloads to transform your data.
1. **Step 5**: AWS Lake Formation centrally governs, secures, and shares your data, while allowing you to easily manage permissions. AWS Glue crawlers scan data in your data lake, classify it, extract schema information from it, and store the metadata automatically in the AWS Glue Data Catalog.
1. **Step 6**: Amazon Redshift uses SQL and machine learning (ML) features built into the service to analyze structured and semi-structured data across your data lake at scale.
1. **Step 7**: Visualize your data using Amazon QuickSight, a fast, easy-to-use, serverless business analytics service that makes it easier to build visualizations, perform ad-hoc analysis, and quickly get business insights from your data, anytime, on any device.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon CloudWatch provides comprehensive visibility into system performance and health, enabling you to configure CloudWatch alarms that invoke automated actions for proactive issue resolution. CloudTrail maintains a detailed audit trail of API calls and configuration changes, enhancing compliance and security efforts. AWS Glue automates data management processes, offering automated schema discovery, classification, and catalog management, even for large datasets. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS DMS offers data protection during transit through its encryption capabilities, and Amazon S3 simplifies security by automatically encrypting all new objects at rest. IAM policies adhere to the principle of least privilege, scoping permissions to the minimum required. Additionally, Lake Formation defines granular security policies, restricting access at the database, table, column, row, and cell levels. AWS Key Management Service (AWS KMS) centrally manages encryption keys used across AWS services. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon S3 provides highly durable and redundant storage, replicating data across multiple Availability Zones. Amazon S3 versioning preserves, restores, and retrieves previous object versions. To further improve reliability, Amazon Redshift enhances data warehouse resilience through automatic backups, failure remediation, and multi-AZ deployment options. Amazon EMR provides configuration options to help you control automatic termination of clusters once steps are completed and to terminate clusters due to errors or issues before processing. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon EMR optimizes data processing by enabling right-sizing of clusters, dynamic scaling, and preconfigured environments. Amazon Redshift unlocks performance potential through features like partitioning, columnar compression, and query tuning so you can optimize data processing and reduce storage and I/O requirements. With Lake Formation, you can streamline data lake management by simplifying the process of identifying and moving data into a centralized repository, whether that data is structured or unstructured. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon S3 Intelligent-Tiering and lifecycle policies automate cost savings by seamlessly moving data to the most cost-effective storage tiers. Amazon EMR optimizes costs through auto-scaling and Amazon Elastic Compute Cloud (Amazon EC2) Spot instance utilization. Additionally, Amazon Redshift offers reserved sodes for steady-state workloads and Amazon Redshift Serverless for cost-effective scaling of unpredictable workloads. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The energy-efficient infrastructure of Amazon S3 and the resource optimization capabilities of managed services like Amazon Redshift, Amazon EMR, AWS DMS, QuickSight, and Lake Formation reduce environmental impact and lower overall IT footprint and carbon emissions compared to running on-premises with physical servers and hardware. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Transforming the Member Experience Using Amazon Redshift with Together Credit Union**: This case study demonstrates how Together Credit Union in financial services unlocked near real-time business intelligence using a data lake built on AWS.

[Read the case study](https://aws.amazon.com/solutions/case-studies/together-credit-union-centralized-data-lake-case-study/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
