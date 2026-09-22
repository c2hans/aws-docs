---
source_url: https://docs.aws.amazon.com/solutions/industrial-data-fabric-with-snowflake-and-highbyte-on-aws/index.html
---

---
title: 'Guidance for Industrial Data Fabric with Snowflake and HighByte on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/industrial-data-fabric-with-snowflake-and-highbyte-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Industrial Data Fabric with Snowflake and HighByte on AWS

## Overview

The Guidance demonstrates how to create an enterprise-governed model in HighByte, ingest real-time, historical, and transactional data at scale from edge and cloud data sources into Snowflake, and interface with applications using REST APIs. It addresses challenges faced by operations leaders at manufacturing and industrial companies with disconnected, siloed data sources by enabling a scalable, unified, and integrated mechanism to harness data as an asset. By providing economical, secure, and easy access to high-quality datasets, the Guidance helps you build the foundation for digital industrial transformation and optimize operations across quality, maintenance, materials management, and process optimization.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/industrial-data-fabric-with-snowflake-and-highbyte-on-aws.pdf)

![Architecture diagram](/images/solutions/industrial-data-fabric-with-snowflake-and-highbyte-on-aws/images/industrial-data-fabric-snowflake-highbyte-aws.png)

1. **Step 1**: Define enterprise-standardized and contextualized data models using Central HighByte Intelligence Hub, and push the models to on-premises remote hubs.
1. **Step 2**: Ingest operational technology (OT) data using HighByte from industrial data sources, including machine data sources such as programmable logic controller (PLC), supervisory control and data acquisition (SCADA), and message queuing telemetry transport (MQTT). This may also include other sources, such as manufacturing execution system (MES), enterprise asset management (EAM), quality management system (QMS), historians, databases, files, and more.
1. **Step 3**: A direct, low-latency connection from HighByte to Snowpipe Streaming then connects to Snowflake tables to efficiently insert data.
1. **Step 4**: Publish to Snowpipe Streaming through Amazon Managed Streaming for Apache Kafka (Amazon MSK). Host a Kafka connector for Snowpipe Streaming on Amazon MSK Connect.
1. **Step 5**: Query data from Snowflake using direct table access with HighByte Intelligence Hub and the Snowflake SQL connector.
1. **Step 6**: Connect to Amazon Simple Storage Service (Amazon S3) using a HighByte S3 connector. Move large or historical datasets into S3 buckets for Snowflake Snowpipe services to automatically retrieve.
1. **Step 7**: Transform data using Snowpark to leverage the power of Java or Python. Data can then be aggregated and prepared using SQL for analytics.
1. **Step 8**: Create real-time dashboards in Amazon Managed Grafana using a native connector for Snowflake.
1. **Step 9**: Create Streamlit apps running on Amazon Elastic Compute Cloud (Amazon EC2) to display real-time dashboards from the raw data zone and historical analysis from the analytics zone in Snowflake using the Python or Snowpark connector.
1. **Step 10**: Analyze and visualize data using Amazon QuickSight with a native connector to Snowflake.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Serverless offerings such as Amazon S3, Amazon MSK, and Amazon Managed Grafana offload the burden of managing underlying infrastructure. This allows the focus to remain on core functionality and continuous improvement of your workloads. These AWS services provide scalability, elasticity, high availability, and durability, automatically scaling up or down based on demand. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Certificate-based encryption enhances the security of this Guidance by authenticating communicating parties and helping to ensure confidentiality, integrity, and non-repudiation of data. This automated approach eliminates manual key exchange, establishing a trusted, encrypted channel for data transfer between systems like HighByte Intelligence Hub and Snowflake, safeguarding sensitive information. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Services like Amazon S3, Amazon MSK, and Amazon Managed Grafana are fully managed by AWS, handling infrastructure, software updates, patches, and ongoing maintenance. These scalable services automatically adjust resources to meet fluctuating demand, helping to ensure consistent performance and availability during high traffic periods. Additionally, built-in disaster recovery and backup capabilities provide data durability and recovery from failures or outages, further enhancing reliability. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The Guidance leverages purpose-built storage services and features like Amazon S3 cross-region replication (CRR) to reduce latency, increase throughput, and support scalability for data-driven workloads. By using geographically distributed storage across AWS Regions, the Guidance can provide lower-latency data access and match specific access patterns. These scalable services allow seamless capacity adjustments to handle fluctuating traffic and data demands for consistent performance. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses purpose-built storage services such as Amazon S3 and Amazon MSK to reduce latency and increase throughput while optimizing costs. By using managed services, it offloads infrastructure provisioning, configuration, and maintenance burdens, allowing focus on core application functionality. Services such as Amazon S3 and Amazon MSK are optimized for specific low-cost durable storage and high-throughput streaming, respectively. Additionally, managed services reduce operational costs through features like automatic scaling and software updates, minimizing operational overhead. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Scalable cloud services like Amazon S3 align with sustainability goals through on-demand usage and efficiency, paying only for consumed resources. Cloud providers' economies of scale and optimized infrastructure often result in lower carbon emissions per unit of computing power. Cloud infrastructure reduces hardware waste by eliminating constant provisioning and replacement of physical hardware. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
