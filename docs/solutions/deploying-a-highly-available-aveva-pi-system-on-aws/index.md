---
source_url: https://docs.aws.amazon.com/solutions/deploying-a-highly-available-aveva-pi-system-on-aws/index.html
---

---
title: 'Guidance for Deploying a Highly Available Aveva PI System on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/deploying-a-highly-available-aveva-pi-system-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Deploying a Highly Available Aveva PI System on AWS

## Overview

This Guidance demonstrates how to maintain operational continuity and data accessibility by deploying a highly available Aveva PI System on AWS that seamlessly extracts data into AWS services. Individual site PI Systems connect to a centralized roll-up system through PI Interfaces and PI Connectors, while edge devices communicate via standard industrial protocols and process data locally before transmission. The deployment uses PI Collective servers for redundant data ingestion, stores metadata in Amazon RDS for SQL Server, and enables data export to services like Amazon S3, Amazon Redshift, and Amazon Kinesis for downstream analytics. You gain a robust, scalable platform that consolidates operational data from multiple locations while enabling advanced analytics and business intelligence capabilities across your organization.

## Benefits

### Consolidate multi-site operational data

Aggregate distributed PI Systems from multiple industrial sites into a single, centralized cloud platform. Eliminate data silos and reduce infrastructure management overhead across your operations.

### Ensure near real-time data resilience

Deploy your PI System across multiple Availability Zones with synchronous replication and automated failover. Maintain continuous access to critical operational data without single points of failure.

### Unlock industrial data for analytics

Export operational data to Amazon S3, Amazon Redshift, and Amazon Kinesis through built-in integrators. Enable your data teams to drive advanced analytics and business intelligence from previously siloed plant-floor data.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively build this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](downloads/aveva-pi-system-on-aws.pdf)

![Architecture diagram](/images/solutions/deploying-a-highly-available-aveva-pi-system-on-aws/images/aveva-pi-system-on-aws.png)

1. **Step 1**: Connect PI System from individual sites to the roll-up PI System on AWS using PI Interfaces and PI Connectors. Establish connectivity through AWS Direct Connect or AWS Site-to-Site VPN.
1. **Step 2**: Ingest data from edge devices that communicate via Modbus, OPC UA, or MQTT into AWS IoT Greengrass. Process the data locally using AWS Lambda functions running on Greengrass.
1. **Step 3**: Send data from edge devices to AWS IoT Core in MQTT format through AWS IoT Greengrass. Trigger an AWS IoT Core rule to invoke an AWS Lambda function, passing in the ingested data for processing.
1. **Step 4**: Translate data from the MQTT message into Aveva Message Format (OMF) using a custom AWS Lambda function. Send the translated data to PI Web API, which posts it to the PI System.
1. **Step 5**: Send on-premises PI System data to the PI Connector Relay deployed on Amazon EC2. The relay posts the data to the roll-up PI System hosted on AWS.
1. **Step 6**: Direct PI System traffic from the public subnet through Elastic Load Balancing. Route traffic from PI Connector Relay, PI Web API, PI Vision, and PI Integrator for Business Analytics deployed on Amazon EC2 to the PI Asset Framework (PI AF) in the private subnet.
1. **Step 7**: Store metadata used by PI Vision and PI Asset Framework (PI AF) in a highly available Amazon RDS for SQL Server instance.
1. **Step 8**: Receive data from the PI Connector Relay on both PI Collective servers — the Primary PI Data Archive and the Secondary PI Data Archive deployed on Amazon EC2 — ensuring high availability for data ingestion.
1. **Step 9**: Use Microsoft Active Directory to provide Windows Integrated Security access across PI System components. Authenticate and authorize users through Active Directory for centralized identity management.
1. **Step 10**: Connect PI Analytics to PI Asset Framework (PI AF) and PI Data Archives. Perform KPI calculations and Event Frame computations to derive operational insights from your PI System data.
1. **Step 11**: Export asset data, event view data, and PI Event Frame data from PI System into AWS services — including Amazon S3, Amazon Redshift, Amazon Kinesis, and Amazon Managed Streaming for Apache Kafka (Amazon MSK) — using PI Integrator for Business Analytics.
1. **Step 12**: Alternatively, use the AWS Industrial Data Fabric solution, supported by ISV partners, to ingest PI System data into a broader set of AWS services and third-party platforms such as Snowflake, Databricks, or other applications.
1. **Step 13**: Access the roll-up PI System through PI Vision or PI Integrator for Business Analytics using a web browser or mobile device. Elastic Load Balancer distributes traffic across PI Vision application nodes for high availability.
[Read usage guidelines](/solutions/guidance-disclaimers/)
