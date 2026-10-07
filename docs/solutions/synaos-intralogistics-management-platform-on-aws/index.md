---
source_url: https://docs.aws.amazon.com/solutions/synaos-intralogistics-management-platform-on-aws/index.html
---

---
title: 'Guidance for SYNAOS Intralogistics Management Platform on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/synaos-intralogistics-management-platform-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for SYNAOS Intralogistics Management Platform on AWS

## Overview

This Guidance demonstrates how to revolutionize manufacturing and logistics operations using SYNAOS Intralogistics Platform on AWS, a cloud-native solution that orchestrates and optimizes end-to-end material flow management across all vehicle types and resources including manual forklifts, AGVs, AMRs, mixed fleets, and human operators. By intelligently coordinating diverse operational resources through demand-driven job assignment, the solution helps manufacturers and logistics companies achieve unprecedented operational efficiency and flexibility. Through the innovative "Material Need" approach and advanced optimization algorithms, the solution enables dynamic resource allocation and real-time decision making across entire intralogistics ecosystems. This future-ready platform helps organizations maximize asset utilization, reduce operational costs, and achieve scalable growth through intelligent automation and data-driven insights.

## Benefits

### Unified Mixed Fleet Management

Eliminate disparate middleware systems by integrating AGVs, AMRs, forklifts, and human operators onto a single platform running on Amazon EKS across multiple availability zones for high availability and scalability. SYNAOS's vendor-independent VDA 5050 native architecture ensures interoperability with any manufacturer while protecting against vendor lock-in. Control vehicles from multiple manufacturers, manage automated and manual operations from one system, and flexibly adjust operations based on demand and seasonal requirements.

### Material Need-Centric Optimization

Transform operations by putting material demand at the center and orchestrates all intralogistics processes accordingly. SYNAOS creates intelligent Intralogistics Jobs that assign tasks to the most suitable resources using smart resource allocation and optimization that analyzes vehicle availability, location, load capacity, and order priorities. The platform's traffic management system proactively prevents bottlenecks, coordinates automated and manual processes and enables manual intervention capabilities for maximum operational flexibility.

### Enterprise Integration and Comprehensive Connectivity

Seamlessly integrate with existing MES, WMS, and ERP systems through Amazon API Gateway while leveraging Amazon Aurora for high-performance, scalable database operations. Connect a wide range of shopfloor assets including gates, traffic lights, conveyors, sensors, and automated storage systems into the unified SYNAOS platform. Leverage comprehensive analytics with Amazon S3 data storage, Amazon SageMaker for ML insights, and Amazon QuickSight for efficiency reporting, with intuitive apps for forklift drivers and clear dashboards for supervisors and shopfloor managers to monitor all transport processes.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/synaos-intralogistics-management-platform-on-aws.pdf)

![Architecture diagram](/images/solutions/synaos-intralogistics-management-platform-on-aws/images/synaos-intralogistics-management-platform-on-aws-1.png)

1. **Step 1**: The SYNAOS Intralogistics Management Platform (IMP) core services run in Amazon Elastic Kubernetes Service (Amazon EKS) across multiple availability zones with Amazon Aurora database for high availability. Self-managed Apache Kafka handles real-time event streaming and message distribution between services. AWS Secrets Manager stores credentials, IoT certificates, and API keys securely.
1. **Step 2**: AWS IoT Greengrass on the shopfloor connects local MQTT devices to AWS IoT Core in the cloud. Devices and assets communicate through MQTT.
1. **Step 3**: IMP receives transport demands from Manufacturing Execution Systems (MES), Warehouse Management Systems (WMS), or Enterprise Resource Planning (ERP) systems via Amazon API Gateway. Sensors and push buttons on the shopfloor also trigger transport demands.
1. **Step 4**: IMP core services process messages from mobile robots (AGVs, AMRs), handling stations, and traffic lights to determine optimal transport solutions. IMP sends commands to vehicles to execute transport jobs based on near real-time demands and shopfloor status.
1. **Step 5**: SYNAOS real-time localization system tracks manually operated forklifts and transport vehicles. Drivers receive transport jobs via the mobile SYNAOS Worker App. Plant operations staff monitor all transport processes through the SYNAOS IMP Control Center. The Control Center provides manual intervention capabilities to resolve shopfloor issues.
1. **Step 6**: Data analysts analyze historical intralogistics data from Amazon Simple Storage Service (Amazon S3) using Amazon SageMaker for ML insights, Amazon Redshift for complex queries, and Amazon QuickSight for efficiency reports and optimization opportunities.
[Read usage guidelines](/solutions/guidance-disclaimers/)
