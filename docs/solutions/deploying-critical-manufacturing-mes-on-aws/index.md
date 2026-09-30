---
source_url: https://docs.aws.amazon.com/solutions/deploying-critical-manufacturing-mes-on-aws/index.html
---

---
title: 'Guidance for Deploying Critical Manufacturing MES on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/deploying-critical-manufacturing-mes-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Deploying Critical Manufacturing MES on AWS

## Overview

This Guidance shows how manufacturers can modernize their operations by implementing a cloud-based Manufacturing Execution System (MES) that combines enterprise-grade reliability with operational flexibility. The Guidance helps organizations achieve digital transformation through a highly available, secure architecture that seamlessly connects shop floor operations with enterprise systems. It demonstrates how manufacturers can leverage cloud technology to enhance production efficiency, ensure data integrity, and scale operations while maintaining robust security and compliance. This approach enables real-time visibility into manufacturing operations, supports quick adaptation to changing business needs, and provides the foundation for smart manufacturing initiatives.

## Benefits

### Accelerate manufacturing digital transformation

Deploy a comprehensive manufacturing execution system that connects shop floor operations with enterprise systems. Gain the agility to quickly adapt to changing market demands while maintaining operational continuity.

### Enhance operational reliability and security

Enable continuous manufacturing operations with multi-Availability Zone high availability and automated data protection. Maintain security and compliance with encrypted data storage and comprehensive audit logging.

### Streamline factory-to-cloud integration

Seamlessly connect on-premises industrial assets and enterprise applications through secure, reliable networking options. Simplify management of hybrid infrastructure while maintaining local manufacturing capabilities.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/deploying-critical-manufacturing-mes-on-aws.pdf)

![Architecture diagram](/images/solutions/deploying-critical-manufacturing-mes-on-aws/images/deploying-critical-manufacturing-mes-on-aws-1.png)

1. **Step 1**: Critical Manufacturing MES helps manufacturers digitalize their operations effectively and easily adapt to changes in demand, opportunities, or requirements. It can be deployed on AWS on an Amazon Elastic Kubernetes Service (Amazon EKS) cluster in a private subnet in multiple Availability Zones (AZs) for high availability configuration. The cluster contains multiple pods and services for multiple MES functions.
1. **Step 2**: The SQL Server is used as a relational database for MES and is deployed on Amazon Elastic Compute Cloud (Amazon EC2) instances in multiple AZs in an Always-On availability group for high availability.
1. **Step 3**: Amazon MQ for Rabbit MQ is used by MES as a message broker and Amazon Managed Streaming for Apache Kafka (Amazon MSK) is used by MES for Kafka-based event streaming.
1. **Step 4**: Amazon Elastic File Systems (Amazon EFS) is used as a file storage backend for Amazon EKS cluster volumes and for file share among containers.
1. **Step 5**: Amazon Simple Storage Service (Amazon S3) is used for persistent storage of files. Pods in the EKS cluster connect to Amazon S3 over a virtual private cloud (VPC) endpoint to keep the traffic private.
1. **Step 6**: Critical Manufacturing MES uses ClickHouse for data persistence of analytical data processing. ClickHouse Cloud is available as a software as a service (SaaS) offering on AWS Marketplace.
1. **Step 7**: Critical Manufacturing Cloud provides additional services, such as container image registry and application monitoring.
1. **Step 8**: A NAT gateway in the public subnet allows application and database servers to reach the internet.
1. **Step 9**: The Network Load Balancer (NLB) serves as an entry point to access the Critical Manufacturing MES application.
1. **Step 10**: Amazon Route 53 is used for routing to the NLB.
1. **Step 11**: MES can integrate directly with enterprise applications, such as enterprise resource planning (ERP) hosted on AWS.
1. **Step 12**: AWS Backup centralizes and automates data protection for all EC2 instances, Amazon EFS, and Amazon S3.
1. **Step 13**: Amazon CloudWatch monitors the health of the workload and the infrastructure. AWS CloudTrail collects audit logs for these workloads. AWS Systems Manager manages and accesses Amazon EC2 servers in the private subnet. AWS Key Management Service (AWS KMS) manages data encryptions keys.
1. **Step 14**: The network connectivity to the on-premises manufacturing and enterprise network is enabled by connecting the customer gateway and the VPN gateway through AWS Site-to-Site VPN or AWS Direct Connect.
1. **Step 15**: On the shop floor, MES can connect with variety of programmable logic controllers (PLCs), IoT devices, and other industrial assets using native industrial protocols through a locally hosted automation manager. Any local printers can also be connected using the locally installed printing service provided by Critical Manufacturing. On-premises users access the MES application through web or thick client.
[Read usage guidelines](/solutions/guidance-disclaimers/)
