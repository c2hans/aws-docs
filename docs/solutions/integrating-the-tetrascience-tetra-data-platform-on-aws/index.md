---
source_url: https://docs.aws.amazon.com/solutions/integrating-the-tetrascience-tetra-data-platform-on-aws/index.html
---

---
title: 'Guidance for Integrating the TetraScience Tetra Data Platform on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/integrating-the-tetrascience-tetra-data-platform-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Integrating the TetraScience Tetra Data Platform on AWS

## Overview

This Guidance showcases the versatility of the TetraScience Tetra Data Platform (TDP) and its seamless integration capabilities with other AWS services. TDP is a cloud-native solution that manages scientific data from various sources, such as instruments, contract research organizations, manufacturing facilities, and software systems. TDP centralizes this data into a scientific data lake hosted on AWS. The various ways you can integrate TDP with the rest of your AWS environment include high-performance computing (HPC), data analytics, data lakes, machine learning (ML), and AWS Partner Solutions. Using the multiple interfaces shown throughout this solution, TDP can accelerate the integration of a laboratory data mesh on AWS.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/integrating-the-tetrascience-tetra-data-platform-on-aws.pdf)

![Architecture diagram](/images/solutions/integrating-the-tetrascience-tetra-data-platform-on-aws/images/integrating-the-tetrascience-tetra-data-platform-on-aws-1.png)

1. **Step 1**: The Tetra Data Platform (TDP) connects your instruments and software systems, such as an electronic lab notebook (ELN) and a laboratory inventory management system (LIMS). It also connects with partner organizations, although the individual connector components required for that are not shown here. TDP can also connect with contract research organizations (CROs) and contract manufacturing and development organizations (CDMOs).
1. **Step 2**: The Administrator uses a web application to set monitoring paths and extract metadata, including time, sample, user, and assay data before uploading raw data to TDP. Authentication utilizes AWS Identity and Access Management (IAM) roles and credentials.
1. **Step 3**: TDP collects, enhances, and stores raw data in an Amazon Simple Storage Service (Amazon S3) bucket. Metadata resides in Amazon Relational Database Service (Amazon RDS) and replicates to the Amazon S3 metadata bucket. AWS Key Management Service (AWS KMS) encrypts all data in TDP.
1. **Step 4**: TDP converts raw data into engineered scientific data and stores it in the Tetra Data Amazon S3 bucket.
1. **Step 5**: Engineered scientific data is converted into tables managed by AWS Glue in an open-source Delta Lake format.
1. **Step 6**: The Amazon OpenSearch Service maintains a search index for data.
1. **Step 7**: Scientists log in to the web application to search instruments, experiments, and assay data.
1. **Step 8**: The catalog sharing interface allows Data Administrators to utilize the AWS Glue Data Catalog with AWS Lake Formation for access controls over Tetra Data tables, supporting secure data sharing between Regions and accounts.
1. **Step 9**: The SQL interface through Amazon Redshift Spectrum and Amazon Athena provides interactive querying, analysis, and processing of Tetra Data stored in Amazon S3 and cataloged in AWS Glue. Athena supports Delta Lake tables that are registered with AWS Glue.
1. **Step 10**: Scientists analyze the engineered scientific data (Tetra Data) with high-performance computing, data analytics, data lakes, business intelligence, and machine learning. This consumption flows from Athena, Amazon Redshift, or the table catalog exposed by Lake Formation. TDP also provides software integrations using APIs and webhooks.
1. **Step 11**: Locally, scientists create graphs, author reports, and conduct performance analysis using data packages.
1. **Step 12**: Data Administrators integrate partner solutions and software as a service (SaaS) products into TDP by provisioning API access keys and/or natively supported integrations such as Snowflake.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses Amazon CloudWatch, AWS CloudFormation, and Amazon Simple Notification Service (Amazon SNS) to enhance operational excellence. CloudFormation stacks contain custom alarms configured to automatically invoke actions based on system behavior, while CloudWatch dashboards visualize historical performance data. CloudWatch alarms can invoke notifications through Amazon SNS when thresholds are crossed. Together, these services enable real-time monitoring, alerting, and incident response to ensure the Tetra Data Platform runs smoothly, helping your team provide timely and effective support if unexpected issues arise. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

When configuring this Guidance, we recommend using IAM, AWS KMS, and AWS Secrets Manager to augment your security posture. IAM enforces strict access controls over data and resources through policies and roles, following the principle of least privilege. AWS KMS enables centralized key management and 256-bit encryption using Advanced Encryption Standard (AES) 256 to protect sensitive data stored in Amazon S3. Secrets Manager centrally manages access credentials for external APIs and Amazon RDS databases. Together, these services allow you to build security best practices like encryption, access controls, and secret management directly into the Tetra Data Platform architecture. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The fully-managed AWS services used in this architecture scale automatically as data volumes grow, maintaining 99.99% uptime. Specifically, Amazon S3 provides 99.999999999% (11 nines) durability and 99.99% availability through redundant storage. Amazon RDS deploys in multiple Availability Zones (AZs) with synchronous replication for high availability. OpenSearch Service auto-scales across AZs to sustain zone failure. By building your data lake architecture on the intrinsically reliable infrastructure of AWS, you offload responsibility for availability, backups, scaling, and disaster recovery to AWS. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Athena and OpenSearch Service help make your workloads more efficient. Athena completes queries in parallel, so results return in seconds, while Amazon OpenSearch Serverless, an on-demand auto-scaling configuration for OpenSearch Service, auto-scales resources to maintain fast ingestion and query speeds as data volumes grow. Athena and OpenSearch Service relieve the burden of fine-tuning data pipelines and indexes, ensuring scientists get rapid responses to queries across exponentially growing datasets. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses Amazon S3 and Athena to optimize costs, with Amazon S3 offering inexpensive, scalable object storage while Athena charges only for queries run. Together, these serverless services scale on demand, so you pay only for what you use. Furthermore, automatically tiering data across Amazon S3 storage classes optimizes price performance as access patterns change. Athena also allows tuning query patterns to minimize scanned data and costs. Building on this variable-spend infrastructure means you don't pay for unused capacity. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The centralized data lake of Amazon S3 eliminates redundant copies, while AWS Glue catalogs this data for analysis. Together, these on-demand services scale dynamically to workloads, maximizing resource utilization and minimizing energy demands. Avoiding overprovisioning with serverless architectures optimizes energy consumption to only what's needed for current workloads. Building on this variable-spend infrastructure means you don't leave unused capacity waiting idly. This saves energy for collecting insights rather than maintaining unused servers. AWS empowers innovating sustainably by matching compute costs to each workload's real-time interface patterns. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
