---
source_url: https://docs.aws.amazon.com/solutions/optimizing-data-architecture-for-sustainability-on-aws/index.html
---

---
title: 'Guidance for Optimizing Data Architecture for Sustainability on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/optimizing-data-architecture-for-sustainability-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Optimizing Data Architecture for Sustainability on AWS

## Overview

This Guidance demonstrates how you can optimize a data architecture for sustainability on AWS that helps to maximize efficiency and reduce waste. Included are curated data services and best practices that help you identify the right solution for your workloads, so you can build a more efficient, end-to-end modern data architecture in the cloud. With a comprehensive set of data and analytics capabilities, this Guidance helps you design a data strategy that grows with your business.

## How it works

These steps provide an overview of this architecture. For diagrams highlighting different aspects of this architecture, open the tabs below.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/optimizing-data-architecture-for-sustainability-on-aws.pdf)

![Architecture diagram](/images/solutions/optimizing-data-architecture-for-sustainability-on-aws/images/optimizing-data-architecture-for-sustainability-on-aws-1.png)

1. **Step 1**: Organizations ingest data from streaming sources like sensors, devices, social media, or web applications, and in batches from database and file systems.
1. **Step 2**: Streaming event data from data streams is stored for longer retention. Data from databases and file systems are stored in a colder storage layer for transformation and consumption.
1. **Step 3**: A stream analytics system analyzes, filters, and transforms incoming data streams in real-time. The batch data processing layer transforms raw data by cleaning, combining, and aggregating the data for analytical purposes.
1. **Step 4**: Streaming data is sent to downstream systems for consumers to query and visualize in real-time. Batch data is modeled and served for consumption for business intelligence.
1. **Step 5**: Data consumers use query and visualization tools to analyze the data.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

To swiftly respond to incidents and events, customize Amazon CloudWatch metrics, alarms, and dashboards. This service allows you to monitor the operational health of the Guidance and notify operators of faults. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Resources deployed by this Guidance are protected by AWS Identity and Access Management (IAM) policies and principles. For example, authentication to services like Aurora, TimeStream, AWS IoT SiteWise, Amazon S3, and Amazon Redshift are managed by IAM. With IAM identity-based policies, administrators can set what actions users can perform, on which resources, and under what conditions. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon S3, Aurora, DynamoDB, and Amazon Redshift are built for data storage, backup, and recovery. We recommend using AWS Backup to back up TimeStream tables. And AWS IoT SiteWise uses the highly available and durable Amazon S3 for backups. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses purpose-built services for each layer of its data architecture. For storage, it selects services based on access patterns (transactional, analytical), and frequency of access (hot, cold, archival). For data ingestion, it selects services based on data velocity (data streaming services, batch data ingestions). And for data processing, it selects services based on consumption patterns (real-time, batch). For query and visualization, it selects services based on personas (business insights consumers, data analysts, data engineers, and data scientists). You can use proxy metrics—metrics that best quantify the effect of any changes you make with the associated resources. Examples of proxy metrics include CPU Utilization, Memory Utilization, and Storage Utilization that you can use to measure and optimize this Guidance based on changes you make. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses serverless services that reduce compute costs on data ingestion and data processing by provisioning the appropriate resources and disposing resources when processes are not running. For storage, this Guidance recommends using serverless services such as Aurora for hot data storage, as well as cost-effective and scalable services for colder layers like Amazon S3. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses technologies based on data access and storage patterns. For frequently accessed data, it guides you to use hot storage layers supported by Aurora, TimeStream, DynamoDB, and AWS IoT SiteWise. For lower frequency or batch consumption, it guides you to use services for colder storage layers, like Amazon S3. For specialized access patterns, like aggregations on normalized tables, it uses Amazon Redshift. This Guidance recommends you select serverless services to reduce the chances of overprovisioning your resources. In addition, Lambda functions powered by Graviton2 are designed to deliver up to 19 percent better performance at 20 percent lower cost, leading to the additional benefit of improved environmental sustainability as a result of potential increased performance. We also recommend you review the delivery SLA to choose the appropriate patterns that reduce the consumption of resources when the resources are not needed. For example, moving to a batch ingestion pattern from real-time streaming patterns when real-time consumption is not required. Finally, it helps you to implement automation to terminate resources when not in use. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Optimize Data Pattern using Amazon Redshift Data Sharing**: This workshop helps you optimize data patterns for sustainability, specifically focused on removing unneeded or redundant data, and minimizing data movement across networks.

[Optimize Data Pattern using Amazon Redshift Data Sharing](https://catalog.workshops.aws/well-architected-sustainability/en-US/3-data/optimize-data-pattern-using-redshift-data-sharing)

[Read usage guidelines](/solutions/guidance-disclaimers/)
