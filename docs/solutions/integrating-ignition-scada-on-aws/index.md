---
source_url: https://docs.aws.amazon.com/solutions/integrating-ignition-scada-on-aws/index.html
---

---
title: 'Guidance for Integrating Ignition SCADA on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/integrating-ignition-scada-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Integrating Ignition SCADA on AWS

## Overview

This Guidance demonstrates how to host and extend the Ignition Cloud Edition Supervisory Control and Data Acquisition (SCADA) software on AWS. You can use this Guidance as a framework to ingest operational technology (OT) data into a secure, scalable, and fault-tolerant Ignition Cloud Edition environment. The Ignition deployment spans two Availability Zones and uses various AWS services for data storage and data processing. It also can be extended to use artificial intelligence and machine learning (AI/ML) technologies for enterprise-level advanced analytics.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/integrating-ignition-scada-on-aws.pdf)

![Architecture diagram](/images/solutions/integrating-ignition-scada-on-aws/images/integrating-ignition-scada-on-aws-1.png)

1. **Step 1**: Ignition is server software that acts as the hub for comprehensive system integration. Ignition can connect to a variety of Programmable Logic Controllers (PLCs), Open Platform Communications Data Access (OPC-DA), and Open Platform Communications Unified Architecture (OPC-UA) protocols. Ignition supports connectivity to any SQL database through Java Database Connectivity (JDBC).
1. **Step 2**: Ignition is bidirectional and supports a variety of outputs. Ignition can expose data through the built-in OPC-UA server. Ignition can write data to any SQL database using JDBC. Ignition can publish data to a MQTT server using a Sparkplug specification. It can expose REST endpoints for third-party applications.
1. **Step 3**: During data ingestion, Ignition has direct connectors to many AWS services. It enables AWS IoT Greengrass integration through OPC-UA and MQTT, allowing real-time data access. Ignition publishes data directly to the MQTT server. With IoT Bridge for SiteWise available through AWS Marketplace, operational technology (OT) data is delivered to AWS IoT SiteWise seamlessly. It connects to Amazon Kinesis Data Streams for scalable real-time streaming. Ignition can also interact with Amazon DynamoDB, a NoSQL database, for storing and retrieving data.
1. **Step 4**: Ignition Cloud Edition, available on AWS Marketplace, complements the on-premises Ignition platform. It allows building enterprise apps and dashboards. It connects to Amazon Aurora databases using JDBC drivers, whether on-premises or the AWS Cloud. Data can directly be ingested from on-premises Ignition to Ignition Cloud Edition. It utilizes NAT gateways to enable outbound internet connectivity from the private subnets hosting Ignition.
1. **Step 5**: Data is published to Amazon Simple Storage Service (Amazon S3) through AWS IoT Core rules or Amazon Data Firehose through Kinesis Data Streams. It reliably loads streaming data into Amazon S3 data lakes, which can then be cataloged using Amazon Athena. The data can also be loaded into the Amazon Redshift data warehousing service for analytics purposes. Develop machine learning models with Amazon SageMaker, and deploy to IoT Greengrass for simplified edge-based deployment.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The AWS services used for this Guidance provide you with a comprehensive, cloud-native framework to extend your on-premises Ignition deployments. By treating infrastructure as code, using scalable data and analytics services, and enabling edge machine learning capabilities, you can enhance operational visibility, responsiveness, and optimization across your industrial environments. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance, when deployed on AWS, uses several services to enhance your overall security posture. These include AWS Identity and Access Management (IAM) for controlling access, AWS Key Management Service (AWS KMS) for protecting data, an d AWS IoT Core for secure communication. These services work in concert to fortify the deployment with robust access control, data protection, and secure connectivity throughout the Guidance. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Elastic Load Balancing (ELB) routes traffic requests from users' desktop and mobile applications to only the healthy Amazon Elastic Compute Cloud (Amazon EC2) instances, so that traffic is not directed to instances that are nearing overload. This approach reduces the likelihood of application failure, allowing users to seamlessly browse the mobile storefront without encountering downtime errors. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Aurora, configured in a multi-Availability Zone (multi-AZ) deployment, provides a highly available and fault-tolerant database infrastructure so that the Ignition SCADA system can continue operating efficiently. Additionally, the Application Load Balancer is employed to distribute traffic across multiple Ignition frontend instances so that the system can handle increased loads and traffic patterns efficiently. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon S3 is used for data storage, as it offers a range of storage classes, including Standard, Infrequent Access, and Glacier, among others, allowing for the optimization of costs based on the specific data access patterns and durability requirements of the Guidance. The multi-AZ deployment of Aurora is used for its capability to scale the database tier up or down based on demand, thereby avoiding over-provisioning and minimizing costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

SageMaker is a fully managed service for building, training, and deploying machine learning models, allowing you to optimize resource utilization and minimize the environmental impact associated with manual processes and inefficient resource management. Amazon S3 offers different storage classes that are optimized for various data access patterns and durability requirements so you can minimize the resources needed for data storage and reduce the associated environmental impact. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
