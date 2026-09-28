---
source_url: https://docs.aws.amazon.com/solutions/building-airline-order-management-systems-on-aws/index.html
---

---
title: 'Guidance for Building Airline Order Management Systems on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-airline-order-management-systems-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Building Airline Order Management Systems on AWS

## Overview

This Guidance demonstrates how airlines can build an International Air Transport Association (IATA) ONE Order compliant order management system (OMS). The Guidance enhances airline retailing and servicing by unifying customer data and streamlining order management processes. By leveraging native AWS services, the Guidance implements best practices in security, scalability, and availability while supporting IATA-recommended order lifecycle events through native event publishing and change data stream mechanisms. Airlines can use this Guidance to modernize their operations and improve customer service flexibility through a cloud-native approach.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/building-airline-order-management-systems-on-aws.pdf)

![Architecture diagram](/images/solutions/building-airline-order-management-systems-on-aws/images/building-airline-order-management-systems-on-aws-1.png)

1. **Step 1**: Deploy the order services as containers on Amazon Elastic Container Service (Amazon ECS) using AWS Fargate, and expose the endpoints using Amazon API Gateway with traffic routed through Elastic Load Balancing (ELB).
1. **Step 2**: Emit order lifecycle events (create/update) to Amazon DynamoDB for persistent storage.
1. **Step 3**: Capture order changes in real time using DynamoDB Streams and ingest them into Amazon OpenSearch Service using zero-extract, transform, load (ETL) integration for search and aggregation.
1. **Step 4**: Export order data from DynamoDB to Amazon Simple Storage Service (Amazon S3) using AWS Glue for reporting and historical analysis.
1. **Step 5**: Transform order events with AWS Lambda and stream them to passenger service system (PSS), passenger revenue accounting (PRA), finance, fulfillment, and delivery using Amazon Managed Streaming for Apache Kafka (Amazon MSK).
1. **Step 6**: Process and transform the PSS messages, such as passenger name record (PNR), electronic ticket (ETKT), electronic miscellaneous document (EMD), or departure control system (DCS) changes, with Lambda. Update the DynamoDB order store.
1. **Step 7**: Ingest ServiceStatusChangeNotif (SSCN) and ServiceDeliveryNotif (SDN) messages from fulfillment and delivery companies using Amazon MSK. Process them with Lambda, and update the order store.
1. **Step 8**: Visualize real-time order data with dashboards and metrics using Amazon Managed Grafana.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amazon Managed Grafana empowers you to monitor and optimize applications through comprehensive visualization capabilities and real-time metrics. You can leverage interactive dashboards and alerting features to track system performance without managing underlying infrastructure. The service streamlines operational workflows by eliminating maintenance overhead while providing automatic version upgrades and built-in security controls. You can focus resources on analyzing data and making informed decisions rather than maintaining monitoring systems, leading to improved operational efficiency and faster troubleshooting capabilities. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Built-in protection mechanisms within API Gateway create multiple layers of security for your API endpoints. The service automatically encrypts data in transit using SSL/TLS protocols while implementing request throttling to prevent potential abuse. You can maintain precise control through API keys for client identification and resource policies for granular access management. Robust logging capabilities enable continuous security monitoring and support compliance requirements, eliminating the need for additional security service configuration. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

ELB continuously monitors container health and intelligently routes traffic while Amazon ECS on Fargate handles automatic scaling and container management without infrastructure overhead. The combination of these services helps ensure high availability by detecting and replacing failed containers, maintaining consistent performance during traffic spikes and eliminating single points of failure. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

DynamoDB stands at the core of performance optimization, delivering consistent single-digit millisecond response times regardless of scale. The database service leverages built-in DynamoDB Accelerator (DAX) caching and automatic scaling to handle millions of requests per second effortlessly. Global tables enable multi-Region deployment for reduced latency, while the serverless architecture eliminates traditional database management overhead. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon S3 offers diverse storage classes that help you optimize costs without sacrificing performance. S3 Intelligent-Tiering automatically moves objects between access tiers based on usage patterns, eliminating manual data management tasks. The implementation of S3 Lifecycle policies further reduces expenses by automatically transitioning objects to lower-cost storage tiers or removing unnecessary data. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda uses an event-driven computing model to help maximize resource efficiency through precise scaling. Lambda only consumes compute resources when needed. The elimination of “always-on” servers significantly reduces energy consumption compared to traditional hosting models. Lambda can align resource allocation to workload requirements to minimize waste while maintaining optimal performance. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
