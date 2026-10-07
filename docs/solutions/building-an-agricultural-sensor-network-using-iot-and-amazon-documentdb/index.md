---
source_url: https://docs.aws.amazon.com/solutions/building-an-agricultural-sensor-network-using-iot-and-amazon-documentdb/index.html
---

---
title: 'Guidance for Building an Agricultural Sensor Network using IoT and Amazon DocumentDB'
canonical_url: https://docs.aws.amazon.com/solutions/building-an-agricultural-sensor-network-using-iot-and-amazon-documentdb/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Building an Agricultural Sensor Network using IoT and Amazon DocumentDB

## Overview

This Guidance demonstrates how to build an application that helps farmers improve productivity by capturing data from their agricultural operations. With AWS services, Internet of Things (IoT) devices, such as soil sensors and weather stations, are installed to measure temperature, rainfall, soil moisture, and crop conditions for data-driven decision-making in farming.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/building-an-agricultural-sensor-network-using-iot-and-amazon-documentdb.pdf)

![Architecture diagram](/images/solutions/building-an-agricultural-sensor-network-using-iot-and-amazon-documentdb/images/building-an-agricultural-sensor-network-using-iot-and-amazon-documentdb-1.png)

1. **Step 1**: Sensors on the farm sends JSON data to AWS IoT Core.
1. **Step 2**: AWS IoT rule forwards data to Amazon Managed Streaming for Apache Kafka (Amazon MSK) based on rule conditions that are setup.
1. **Step 3**: JSON data from the sensors is stored in Amazon DocumentDB (with MongoDB compatibility) leveraging Amazon MSK serverless and containerized Kafka connector that is setup on AWS Fargate.
1. **Step 4**: Smart farms containerized microservices process the sensor and third-party data received, and generate recommendations to farmers. Smart farm's microservices can run on either Amazon Elastic Container Service (Amazon ECS), Fargate, or Amazon Elastic Kubernetes Service (Amazon EKS)
1. **Step 5**: Farmers would be notified through Amazon Simple Notification Service (Amazon SNS).
1. **Step 6**: Amazon EventBridge triggers AWS Lambda function periodically to collect data such as weather updates and soil tests results from third-parties.
1. **Step 7**: Agriculture officers, insurance companies, or farmers can access smart farm application for additional information using Amazon API Gateway (this is an optional user action).
1. **Step 8**: Smart Farm's organization admins can generate reports or perform on-demand analysis on the data stored in Amazon DocumentDB using Amazon Athena, Amazon QuickSight, or any other reporting (this is an optional user action).
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

To improve operational efficiency, use Amazon CloudWatch for monitoring, and enable logging to CloudWatch for each AWS Service. You can configure logging for all of AWS IoT Core or only specific groups. For API Gateway, you can enable API logging to CloudWatch. To identify queries that may need tuning, you can use Amazon DocumentDB Performance insights or use Amazon DocumentDB profiler to define a slow query and log its execution details to CloudWatch logs. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS IoT Core provides fine-grained access controls for managing topic permissions. Every device or sensor needs a credential to interact with AWS IoT, and all traffic to and from AWS IoT is encrypted via Transport Layer Security (TLS). Use AWS Identity and Access Management (IAM) roles to provide only the needed permissions to Lambda to access Amazon MSK and API Gateway. Amazon DocumentDB allows for encryption at rest, as well as TLS for data in transit. To further protect resources in production, use Amazon Cognito to protect the API Gateway for public user authentication and authorization. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Serverless technologies implemented in this Guidance are highly available and scalable depending on traffic. Amazon DocumentDB is a fully managed document database service that is deployed as a highly available 3 node cluster spanning across three Availability Zones and allows you to scale vertically and horizontally. Backup in Amazon DocumentDB is enabled by default and cannot be disabled, and the database can be restored to any second during the retention period, up to the last five minutes. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance comprises managed services, integrated monitoring, alerting, reporting, and event-driven workloads. The services selected for this Guidance have high availability, resiliency, efficiency, and remove undifferentiated heavy lifting. Amazon DocumentDB allows for flexibility within document storage due to the expected changes in IoT hardware, sensors, and schemas that are common within agricultural implementations of IoT. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

To avoid over provisioning of resources, this Guidance incorporates serverless technologies for on-demand data ingestion, processing storage, and to optimize costs through pay-as-you-go pricing. With Amazon DocumentDB, you only pay for the capacity you use for storage and backup; it offers per second billing for compute with no extra cost for encryption and monitoring. As Amazon DocumentDB supports flexible data model (also called 'schemaless'), it reduces engineering effort required to support new IoT devices. New IoT device models often bring varying sensor values and can require changes to schemas. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The serverless services used in this Guidance ensure that just the right amount of resources are utilized to handle the workload. And the use of managed services (such as Amazon DocumentDB) are aimed at reducing carbon footprint using AWS Graviton Processors compared to the footprint of continually operating on-premises servers. The scaling features of Amazon DocumentDB allows for scaling vertically and horizontally to reduce unnecessary resources. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
