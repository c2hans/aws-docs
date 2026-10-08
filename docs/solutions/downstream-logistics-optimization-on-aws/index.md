---
source_url: https://docs.aws.amazon.com/solutions/downstream-logistics-optimization-on-aws/index.html
---

---
title: 'Guidance for Downstream Logistics Optimization on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/downstream-logistics-optimization-on-aws/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Downstream Logistics Optimization on AWS

## Overview

This Guidance helps oil and gas facility operators deploy AWS services and Independent Software Vendor (ISV) Partner applications to optimize asset tracking, fleet management, driving directions, and other location-centric business processes. You can increase efficiency and mitigate supply chain risks of feed, products, and intermediates through waterborne cargoes, pipelines, railcars, and trucks. This Guidance aims to improve logistics operational agility, lower operating expenses, and reduce field risk.

## How it works

This architecture diagram uses an industrial data lake and location-based data to increase asset utilization.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/downstream-logistics-optimization-on-aws.pdf)

![Architecture diagram](/images/solutions/downstream-logistics-optimization-on-aws/images/downstream-logistics-optimization-on-aws-1.png)

1. **Step 1**: An industrial data lake built with Amazon Simple Storage Service (Amazon S3), AWS Glue, and Amazon Timestream stores timeseries data. Scheduled AWS Glue crawlers and the AWS Glue Data Catalog organize data sources and relationships.
1. **Step 2**: Amazon Location Service ingests partner and operational technology (OT) vehicle, vessel, tank level, and other logistics data. Amazon Location optimizes asset tracking, geofence alerts, and driving directions as conditions and asset locations change.
1. **Step 3**: Paper and digital documents contain valuable operational data that use Amazon S3 to call an AWS Lambda function that analyzes and structures document text using Amazon Textract. The industrial data lake stores results.
1. **Step 4**: Enterprise information technology (IT) systems contain asset functional locations, product movement records, and critical contextual information for product supply and demand.
1. **Step 5**: Data analytics capabilities from Amazon Athena provide contextualized datasets of OT data joined with enterprise systems of record and static documents. You can apply, reuse, and share queries and views in Athena.
1. **Step 6**: Amazon QuickSight, Amazon Managed Grafana, or AWS Partner business intelligence (BI) applications provide visualization and reporting based on customer preference. Amazon Managed Grafana provides real-time monitoring, and QuickSight focuses on business key performance indicators (KPIs).
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Lambda application code emits information about logic and outcomes directly into Amazon CloudWatch. Logs and insights from CloudWatch use the instrumented logic to create operational dashboards for monitoring and alerts. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

All services in this Guidance, including Amazon S3, Timestream, and Amazon Aurora, have server-side encryption using encryption keys stored in AWS Key Management Service (AWS KMS). [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance is event-driven, providing a modular, microservices approach for AWS services, including Amazon Location. Data processing pathways are loosely coupled, and you can remove these pathways or replace them with ISV AWS Partner software with minimal impact on the overall architecture. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon Location provides fleet tracking, optimized routing, and geofencing capabilities that are crucial for logistics-dependent business processes. If asset locations are better aligned with AWS IoT Core, you can instead send the data as MQTT messages, providing different configurations to match business and technical requirements. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Lambda participates in Compute Savings Plans, which allows 1- or 3-year terms of discounted rates for the amount of Lambda usage. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon S3 Lifecycle configuration supports transfers of data objects to a more sustainable storage class tier based on pre-defined rules. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
