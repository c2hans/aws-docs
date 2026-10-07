---
source_url: https://docs.aws.amazon.com/solutions/building-an-ecommerce-experience-with-commercetools-on-aws/index.html
---

---
title: 'Guidance for Building an Ecommerce Experience with Commercetools on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-an-ecommerce-experience-with-commercetools-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Building an Ecommerce Experience with Commercetools on AWS

## Overview

This Guidance shows how you can build an ecommerce experience around the microservices-based, API-first, cloud-native software as a service, and headless (MACH) approach of commercetools. By integrating AWS services with commercetools, you can extend functionality to address common retail use cases. This integration can help you make quicker decisions related to brand design, helping you provide a consistent and seamless experience for your customers.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-an-ecommerce-experience-with-commercetools-on-aws.pdf)

![Architecture diagram](/images/solutions/building-an-ecommerce-experience-with-commercetools-on-aws/images/building-an-ecommerce-experience-with-commercetools-on-aws-1.png)

1. **Step 1**: Host the static parts of your brand-specific frontend (such as web pages and images) on Amazon Simple Storage Service (Amazon S3), delivered through Amazon CloudFront with low latency.
1. **Step 2**: Your business logic runs in containers using Amazon Elastic Container Service (Amazon ECS) or AWS Lambda to run your code in serverless functions.
1. **Step 3**: Integrate commercetools APIs with your business logic to gain flexibility when composing your shopping experience.
1. **Step 4**: Store additional business data in databases (SQL or NoSQL) or integrate other systems in your IT landscape, such as a content management system (CMS), product information management (PIM) system, or customer relationship management (CRM) system.
1. **Step 5**: Integrate asynchronously with events from commercetools (such as new orders) and use Amazon EventBridge to distribute those events to your applications.
1. **Step 6**: Amazon Simple Queue Service (Amazon SQS) receives events from EventBridge and queues them for processing by downstream services.
1. **Step 7**: By storing commercetools events in an Amazon S3-powered data lake ingested through Amazon Kinesis Data Firehose, you can make events accessible for visualizations, forecasting, and analyzing usage patterns.
1. **Step 8**: Use data such as previous buying behavior to tailor customers' shopping experience with Amazon Personalize.
1. **Step 9**: Use Amazon Connect Customer as your contact center to allow your customers to connect with you through phone or chat. By accessing the same business logic and data in commercetools, you can provide a consistent and unified experience for customers.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

CloudFront, Elastic Load Balancing (ELB), Amazon S3, Amazon ECS, Lambda, Amazon DynamoDB, Amazon Personalize, Kinesis Data Firehose, EventBridge, and Amazon SQS, are all managed services, eliminating operational overhead. Using managed services helps you offload infrastructure and server maintenance to AWS. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

CloudFront improves website security with traffic encryption and access controls. DynamoDB and Amazon S3 encrypt data at rest, and you have the flexibility to select the encryption key. Encrypting data at rest helps ensure that only authorized individuals can access data, preventing data leakage, unauthorized access, and physical theft. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

ELB routes traffic requests from the store’s web and mobile application to healthy containers in Amazon ECS. Amazon ECS auto scales containers across multiple Availability Zones for high availability. Combining ELB with Amazon ECS reduces the chance of application failure for your business logic, meaning that users can browse the web and mobile storefront without encountering downtime errors. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon ECS scales containers running your business logic on demand, helping ensure that only the necessary compute resources are allocated. CloudFront serves requests through the closest edge location of the requester to reduce network latencies. This architecture allows you to sustain peak traffic (often a challenge in ecommerce) while serving requests through the closest edge location of the requester to reduce network latencies. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Where possible, CloudFront eliminates the frequency of data access or microservice invocations through caching, resulting in lower compute costs. Amazon ECS reduces costs with efficient compute resource auto scaling by using AWS Auto Scaling. CloudFront caching enables Amazon ECS automatic application scaling to be cost efficient by provisioning the minimal amount of compute and allowing you to pay only for the resources you use. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon ECS supports AWS Graviton processors, which use up to 60 percent less energy than comparable Amazon Elastic Compute Cloud (Amazon EC2) instances for the same performance. To minimize your workload’s environmental impact, choose the latest Graviton processors for Amazon ECS andclean up unused data, snapshots, and backups at regular intervals. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
