---
source_url: https://docs.aws.amazon.com/solutions/building-a-banking-core-system-on-aws/index.html
---

---
title: 'Guidance for Building a Core Banking System on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-a-banking-core-system-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Building a Core Banking System on AWS

Transform your customer experience with a modernized banking architecture

## Overview

This Guidance helps financial institutions build a modern core banking system using native AWS services. Banks traditionally have legacy core banking applications, which are monolithic and lack open architecture. With a modern cloud-based core, banks can be more agile and innovate to better serve their financial services customers by adding new functionalities and releasing features quickly.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/guidance-for-core-banking-platform-ra.pdf)

![Architecture diagram](/images/solutions/building-a-banking-core-system-on-aws/images/building-a-banking-core-system-on-aws-1.png)

1. **Step 1**: The API layer interfaces the core platform with the upstream applications by creating and managing accounts.
1. **Step 2**: Real-time transactions come in from the payment networks.
1. **Step 3**: The transaction data virtual private cloud (VPC) registers all transactions and hosts microservices to manage the ledger database.
1. **Step 4**: Data is replicated in real time from Amazon QLDB to a secondary database that performs better with query patterns such as scanning or searching data.
1. **Step 5**: Data from the secondary database is captured in Amazon Managed Streaming for Apache Kafka (Amazon MSK) using Kafka Connect to independently build and scale downstream applications.
1. **Step 6**: Downstream applications and microservices consume from Amazon MSK and scale independently of each other.
1. **Step 7**: Data from Amazon MSK is consumed to perform both real-time and batch data analytics.
1. **Step 8**: Batch files come in from the acquiring banks and are processed by the issuing bank. Transaction values are updated in the ledger database.
1. **Step 9**: The issuing bank's data center is connected to the AWS environment using AWS Direct Connect, which offers reliable connectivity to the network routers and payment hardware security module (HSM) devices.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The platform is built using native AWS services, which integrate natively with Amazon CloudTrail and Amazon CloudWatch for monitoring, logging, and auditing purposes. The applications are built as microservices and scale independently of each other using an event-driven architecture. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The Amazon API Gateway and AWS WAF protects all of the API requests coming into the platform. The various resources are also logically isolated from each other using VPCs. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

All services are scalable to multiple AZs within the region to provide high resiliency. Reliability is also improved by using Amazon MSK to capture data and to build an event-driven platform. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon FSx for Lustre is a shared file system suitable for batch processing requirements where the batch jobs need to finish within a certain timeframe. In addition, real-time transactions need to be written to the database and the response sent within about 200ms. This is achieved by having Direct Connect with the bank’s data center for network connectivity and having as few hops as possible for the transactions to be written to the ledger database. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon QLDB is a serverless database and the customer only pays for what they use. Amazon Elastic Kubernetes Service (Amazon EKS) also allows customers to build a microservices platform and scale the services as needs change. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Leveraging native AWS services and serverless technologies such as Amazon QLDB, API Gateway, Amazon Simple Storage Service (Amazon S3), and Amazon DynamoDB helps build a platform that scales with growth in business and helps the bank avoid building and keeping over-provisioned resources. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
