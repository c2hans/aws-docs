---
source_url: https://docs.aws.amazon.com/solutions/distributed-order-management-on-aws/index.html
---

---
title: 'Guidance for Distributed Order Management on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/distributed-order-management-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Distributed Order Management on AWS

## Overview

This Guidance helps you build an order management system (OMS) on AWS using cloud-native services. By building OMS on the cloud, you can incorporate an event-based workflow to help streamline orders, from order entry to fulfillment. This Guidance also helps you manage and analyze data within your OMS so you can generate insights to improve your customer experience.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/distributed-order-management-on-aws.pdf)

![Architecture diagram](/images/solutions/distributed-order-management-on-aws/images/distributed-order-management-on-aws-1.png)

1. **Step 1**: Enterprise applications feed data into OMS. This includes facility attribute data (such as store and warehouse data), product data, and inventory data. eCommerce order data is also sent to OMS for allocation and release.
1. **Step 2**: The integration layer consists of multiple AWS services that support file transfer for external file feeds, APIs, event-driven patterns, and streaming for inventory and master data.
1. **Step 3**: The extract, transform, load (ETL) layer consists of AWS Lambda functions that consume and publish data to Amazon Kinesis Data Streams and Amazon EventBridge. AWS Glue loads and transforms data for batch transactions.
1. **Step 4**: The data layer consists of Amazon Aurora for transactional data and Amazon DynamoDB, which serves requests at low latency.
1. **Step 5**: The OMS exposes a graphical user interface (GUI) that associates will use to create and modify orders, which in turn calls the necessary APIs from the API layer.
1. **Step 6**: The API layer consists of Lambda functions. The presentation layer of OMS and other applications, such as eCommerce, front-end, and customer care, invoke these functions.
1. **Step 7**: The allocation engine consists of Lambda functions and AWS Step Functions. These services execute the optimal allocation logic, publish eCommerce orders to EventBridge, and identify the appropriate facility to fulfill the order.
1. **Step 8**: EventBridge sends the orders to fulfillment applications. Associates pick and pack the items and send shipment confirmations to OMS.
1. **Step 9**: Data moved by the integration layer is sent to the analytics layer. Amazon Redshift generates insights on order processing efficiency.
1. **Step 10**: Third-party applications provide functionality based on specific tasks and interact with OMS through the integration layer.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This architecture follows a microservices approach, meaning that services are decoupled from one another. This allows you to make small, frequent, and reversible changes to the architecture. Additionally, if one component of the architecture fails, it will not affect other components. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Data is encrypted at rest in DynamoDB and Aurora. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This architecture uses stateless compute, meaning that data is not stored on servers so that servers can perform other functions. It also uses a decoupled architecture so that the function of one service is not altered by the function of another. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This architecture uses DynamoDB, which delivers response times that can be measured in single-digit milliseconds for most cases. If you need response times in microseconds, you can use DynamoDB Accelerator (DAX). [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This architecture is an internal application, so data transfer charges between Availability Zones within an AWS Region will be lower compared to an external application. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This architecture uses serverless services, which helps ensure that applications only use the exact amount of resources needed. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
