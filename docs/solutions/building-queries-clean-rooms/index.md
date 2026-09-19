---
source_url: https://docs.aws.amazon.com/solutions/building-queries-clean-rooms/index.html
---

---
title: 'Guidance for Building Queries in AWS Clean Rooms'
canonical_url: https://docs.aws.amazon.com/solutions/building-queries-clean-rooms/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Building Queries in AWS Clean Rooms

## Overview

This Guidance demonstrates how to drive insights for media planning, activation, and measurement from AWS Clean Rooms. With sample AWS Clean Rooms queries, you can learn how to use such queries in Amazon Athena and Amazon QuickSight to drive insights for media planning, activation, and measurement.

## How it works

Query, analyze, and collaborate with data in AWS Clean Rooms.

[Download the architecture diagram PDF](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/building-queries-clean-rooms.pdf)

![Architecture diagram](/images/solutions/building-queries-clean-rooms/images/building-queries-clean-rooms-1.png)

1. **Step 1**: AWS Glue is used to produce an AWS Glue Data Catalog for data provided in account A.
1. **Step 2**: AWS Clean Rooms is configured to provide data from account A as part of the collaboration.
1. **Step 3**: AWS Glue is used to produce a Data Catalog for data provided in account B.
1. **Step 4**: AWS Clean Rooms is configured to provide data from account B to the collaboration.
1. **Step 5**: Results of a collaboration within AWS Clean Rooms are stored in an Amazon Simple Storage Service (Amazon S3) bucket within account A.
1. **Step 6**: AWS Glue is used to create a Data Catalog of the query results from AWS Clean Rooms collaboration. Amazon Athena is configured to query results data stored on Amazon S3.
1. **Step 7**: Amazon QuickSight is used to design and share dashboards by utilizing the query results developed in Athena.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: A detailed guide is provided to experiment and use within your AWS account. Each stage of building the Guidance, including deployment, usage, and cleanup, is examined to prepare it for deployment.

[Open implementation guide](https://aws-solutions-library-samples.github.io/advertising-marketing/building-queries-clean-rooms.html)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This solution is built using a multi-tier architecture, where every tier is independently scalable, deployable, and testable. The facets of this multi-tier architecture, which are decoupled from each other, are compute, storage, data management (catalog), and orchestration. Observability is built in. Every service publishes metrics to Amazon CloudWatch, where dashboards and alarms can be configured. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Data at rest is encrypted using SSE-S3 encryption. Data in transit from external system into Amazon S3 is encrypted and transferred over HTTPS. AWS Identity and Access Management (IAM) policies are created using the least privilege access, so every policy is restrictive to the specific resource and operation. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Every service or technology chosen for each architecture layer is serverless and fully managed by AWS, making the overall architecture elastic, highly available, and fault tolerant. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Using serverless technologies, you only provision the exact resources you use. The serverless architecture reduces the amount of underlying infrastructure you need to manage, allowing you to focus on solving your business needs. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The services in this guidance are entirely serverless. Using serverless technologies, you only pay for the resources you consume. As the data ingestion velocity increases and decreases, the costs will align with usage. When AWS Glue is performing data transformations or crawling your data, you only pay for infrastructure during the time the processing is occurring. Similarly, when Athena is querying data, you only pay for the run time for each query and any related storage costs for the results on Amazon S3. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By extensively using serverless services, you maximize overall resource use because compute is only used as needed. The efficient use of serverless resources reduces the overall energy required to operate the workload. You can also use the AWS Billing console carbon footprint tool to calculate and track the environmental impact of the workload over time at the account, region, and service level. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
