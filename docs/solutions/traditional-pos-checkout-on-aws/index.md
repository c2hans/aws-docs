---
source_url: https://docs.aws.amazon.com/solutions/traditional-pos-checkout-on-aws/index.html
---

---
title: 'Guidance for Traditional POS Checkout on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/traditional-pos-checkout-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Traditional POS Checkout on AWS

## Overview

This Guidance demonstrates how retailers can set up a point of sale (POS) system in the AWS Cloud. Data captured by in-store card readers and POS terminals is securely transmitted to backend applications for processing and settlement. Key business processes such as checkout, order processing, inventory management, and back office functions are all integrated from the corporate data center to the Cloud. The security and confidentiality of the captured data is ensured through monitoring, security, and protection measures.

## How it works

This diagram shows how to build a cloud-based point of sale (POS) system for retailers and merchants on AWS.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/traditional-pos-checkout-on-aws.pdf)

![Architecture diagram](/images/solutions/traditional-pos-checkout-on-aws/images/traditional-pos-checkout-on-aws-1.png)

1. **Step 1**: In-store card readers and point of sale (POS) terminals capture the transaction. Amazon One, a contactless identity service that scans a customer's palm, acts as an authentication mechanism.
1. **Step 2**: AWS Outposts Family delivers AWS infrastructure and services to on-premises or edge locations. Lambda@Edge integrates with the payment gateways and other third-parties. Amazon ECS Anywhere runs containers with applications at the edge that require low-latency support.
1. **Step 3**: AWS Direct Connect and AWS Site-to-Site VPN securely connect retail stores and the corporate data center to the AWS Cloud.
1. **Step 4**: Amazon API Gateway, Amazon EventBridge, and AWS AppSync act as an integration layer, cascading the store transaction to the backend applications for processing and settlement.
1. **Step 5**: AWS Lambda, AWS Step Functions, and Amazon Elastic Container Service (Amazon ECS) support the application layer. This includes custom functions for key business processes like checkout, order processing, inventory management, and back office functions.
1. **Step 6**: Amazon Aurora is used for transactional data, while Amazon DynamoDB handles unstructured data, and Amazon Simple Storage Service (Amazon S3) is used as a data lake.
1. **Step 7**: Amazon CloudWatch, AWS Identity and Access Management (IAM), Amazon Fraud Detector, and AWS Key Management Service (AWS KMS) monitor, secure, and protect data.
1. **Step 8**: The corporate data center is connected to the AWS Cloud and integrated with systems and data sources supporting the POS.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Outposts, Lambda, and Amazon ECS Anywhere provide low-latency edge capabilities for the retail store, ensuring a superior customer experience, quickly. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Both Direct Connect and Site-to-Site VPN provide secure connections between the retail store and the AWS Cloud. And, by using IAM and AWS KMS for securing and encrypting the data, you can continually adjust permissions on the journey to least privilege. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The availability and reliability of managed services such as Aurora, DynamoDB, and Step Functions are essential for ensuring the stability and scalability of your infrastructure. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

DynamoDB, Amazon S3, and Aurora are used as core components of this Guidance to power performance-intensive workloads. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Serverless services such as Lambda, Step Functions, and EventBridge are used extensively throughout this Guidance to help you build and operate cost-aware workloads that achieve business outcomes, while minimizing costs. Maximizing your return on this investment. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

AWS services enable you to maximize the benefits of your resources while reducing your carbon footprint. The services selected in this Guidance help you scale both up and down according to demand. The serverless components also automate the process of infrastructure management, reducing energy while gaining efficiencies. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
