---
source_url: https://docs.aws.amazon.com/solutions/unified-commerce-on-aws/index.html
---

# Guidance for Unified Commerce on AWS

## Overview

This Guidance uses the MACH principles of Microservices, API-first, Cloud-native SaaS, and Headless applications to seamlessly integrate multiple systems on AWS. Unified Commerce encompasses all customer-facing touch-points to deliver a unified experience regardless of channel and breaks down the silos of a multi-channel approach. By deploying this Guidance, you can put marketing and operations together to improve your customer satisfaction with a coherent brand engagement that will increase advocacy.

## How it works

This architecture diagram shows the seamless integration of multiple systems to provide a personalized and consistent retail experience to customers—regardless of the touchpoint or fulfillment method—by using AWS services for different layers and to orchestrate between multiple applications and software-as-a-service (SaaS) offerings.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/unified-commerce-on-aws.pdf)

![Architecture diagram](/images/solutions/unified-commerce-on-aws/images/unified-commerce-on-aws-1.png)

1. **Step 1**: Frontend applications, or heads, use a common set of microservices and other applications that are abstracted behind an API layer such as AWS AppSync, creating headless applications.
1. **Step 2**: Common microservices such as Amazon DynamoDB and Amazon Neptune provide application logic and data to power the frontend experience applications. They usually provide services that differentiate the retailer's offer from that of their competitors.
1. **Step 3**: Software-as-a-service (SaaS) applications are used where possible to provide mature evergreen application logic, especially where the service is undifferentiating for the retailer.
1. **Step 4**: Traditional commercial off-the-shelf (COTS) applications can also be deployed in AWS services such as Amazon Elastic Compute Search (Amazon EC2) and Amazon Relational Database Service (Amazon RDS) to provide application services that are not available as SaaS or have not yet been decomposed into microservices.
1. **Step 5**: Existing systems of record or location-based systems, such as on-premises warehouse management systems and enterprise resource planning (ERP) or finance software, are also integrated behind the aggregation API.
1. **Step 6**: All microservices and applications produce events that are published to Amazon EventBridge custom event buses and consumed by decoupled applications by using rules.
1. **Step 7**: Application data and events are streamed into a data platform such as Amazon Simple Storage Service (Amazon S3) or Amazon Athena for real-time and historical analysis and reporting.
1. **Step 8**: Personalization for dynamic content and marketing offers is based on real-time events and pushed to the customer on their chosen engagement channels.
1. **Step 9**: Machine learning uses the data layer as source for generating forecasts and intelligent insight.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The proposed architecture is capable of running at scale as it leverages managed services where possible. The traditional COTS applications would leverage Amazon EC2 instance metrics with Amazon CloudWatch alarms and logs. Auto Scaling groups and managed Amazon RDS can recover from failure. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The architecture uses managed services where possible, so a large portion of security responsibility falls to AWS, following best practices of security including Amazon S3 encrypted data, IAM roles scoped down, and Amazon DynamoDB encryption at rest. Strong identity is enforced for Consumers through Amazon Cognito, and for operators through IAM roles. CloudWatch Logs and AWS CloudTrail provide traceability, and can be used with organization-wide capabilities, such as Amazon GuardDuty, AWS Security Hub, and a central SIEM. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Using managed services, reliability is achieved by default. Redundancy in storage on Amazon S3 and DynamoDB, scaling of Amazon SageMaker instances, Amazon Redshift, Athena, Amazon SageMaker Canvas, Amazon Pinpoint, Amazon Personalize, AWS AppSync, and EventBridge are also highly available by design. In case of any issues, the data can be replayed from raw events on Amazon S3 using the same pipeline. Events can also be replayed by using the EventBridge archive and reply functionality. The container architecture scales horizontally on a choice of either Amazon Elastic Container Service (Amazon ECS) or Amazon Elastic Kubernetes Service (Amazon EKS) running on AWS Fargate and dynamically adapts to capacity demands. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Scaling is based on the use of AWS Serverless services like AWS Lambda, DynamoDB, SageMaker endpoints, and Amazon Redshift, where possible. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The use of managed and serverless services ensures the minimum cost for the architecture, because they’re designed to charge only when in use. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The proposed architecture uses managed and serverless services where possible to have a sustainable approach, only running when needed. The AWS customer carbon footprint tool can be used to obtain total impact figures. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
