---
source_url: https://docs.aws.amazon.com/solutions/industrial-data-fabric-with-ignition-on-aws/index.html
---

---
title: 'Guidance for Industrial Data Fabric with Ignition on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/industrial-data-fabric-with-ignition-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Industrial Data Fabric with Ignition on AWS

## Overview

This Guidance demonstrates how to build a comprehensive industrial data integration solution using Ignition as a central OT/IT connectivity hub. It showcases the unification of plant floor systems, manufacturing execution systems (MES), and enterprise resource planning (ERP) systems through native programmable logic controller (PLC) drivers, open platform communications (OPC) protocols, and database connectors. The Guidance enables bidirectional data exchange across industrial environments using industry-standard protocols such as OPC Unified Architecture (OPC-UA), MQTT Sparkplug, and RESTful interfaces. By leveraging multiple AWS integration paths, including AWS IoT Greengrass, AWS IoT SiteWise, and Amazon Kinesis Data Streams, the Guidance facilitates real-time data processing. Additionally, the Guidance highlights how Ignition Cloud Edition from AWS Marketplace can extend on-premises capabilities, allowing for the creation of enterprise-wide applications and dashboards.

## Benefits

### Unify industrial data across your entire manufacturing ecosystem

Connect and integrate data from PLCs, databases, MES, and ERP systems through comprehensive Ignition integration capabilities, creating a single source of truth that breaks down operational silos and enables data-driven decision making across your organization.

### Accelerate IT/OT convergence with bidirectional data flow

Enable seamless two-way communication between operational technology and AWS services through multiple integration paths including OPC-UA, MQTT, and direct AWS service connections, reducing implementation time and creating new opportunities for operational insights and automation.

### Scale industrial applications from edge to cloud

Deploy a flexible architecture that combines on-premises Ignition for real-time operations with Ignition Cloud Edition on AWS for enterprise-wide applications and dashboards, allowing you to maintain critical local control while leveraging cloud capabilities for analytics and broader business integration.

### Simplify regulatory compliance with comprehensive data traceability

Establish end-to-end data lineage from shop floor to enterprise systems, creating auditable records that streamline compliance reporting and validation for industry regulations while reducing the manual effort required for documentation.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/industrial-data-fabric-with-ignition-on-aws.pdf)

![Architecture diagram](/images/solutions/industrial-data-fabric-with-ignition-on-aws/images/industrial-data-fabric-with-ignition-on-aws-1.png)

1. **Step 1**: Ignition is an integration hub for the entire plant floor for comprehensive system integration. It connects to programmable logic controllers (PLCs) through native drivers and open platform communications (OPC) protocols, interfaces with SQL databases using Java Database Connectivity (JDBC), and supports MongoDB. It exchanges data with manufacturing execution system (MES) systems like Tulip through the Sandalwood Connector and retrieves enterprise resource planning (ERP) data from systems like SAP using web services.
1. **Step 2**: Ignition is a bidirectional platform that exposes data through its OPC-unified architecture (UA) server, writes to SQL databases using JDBC, and publishes to MQTT servers using Sparkplug. It also provides RESTful endpoints for third-party integration.
1. **Step 3**: Ignition connects directly to AWS services through multiple paths: integrating with AWS IoT Greengrass through OPC-UA and MQTT, publishing to MQTT servers, sending OT data to AWS IoT SiteWise through IoT Bridge for SiteWise, and connecting to Amazon Kinesis Data Streams for real-time streaming.
1. **Step 4**: Ignition can also interact with Amazon DynamoDB, a NoSQL database, for storing and retrieving data. Using AWS Injector module Ignition, tag data will flow into DynamoDB using an easy-to-read JSON representation.
1. **Step 5**: Ignition Cloud Edition on AWS Marketplace complements on-premise Ignition, enabling enterprise app and dashboard creation. It connects to Amazon Aurora using JDBC, ingests data from on-premises Ignition, and uses NAT gateways for outbound internet connectivity from private subnets.
1. **Step 6**: Publish data to Amazon Simple Storage Service (Amazon S3) using AWS IoT Core rules or Amazon Data Firehose. Load streaming data into Amazon S3 data lakes, catalog with Amazon Athena, or load into Amazon Redshift for analytics. Develop ML models using Amazon SageMaker AI, and deploy to AWS IoT Greengrass for edge-based processing.
[Read usage guidelines](/solutions/guidance-disclaimers/)
