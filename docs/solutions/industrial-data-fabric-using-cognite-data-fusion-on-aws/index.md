---
source_url: https://docs.aws.amazon.com/solutions/industrial-data-fabric-using-cognite-data-fusion-on-aws/index.html
---

---
title: 'Guidance for Industrial Data Fabric Using Cognite Data Fusion® on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/industrial-data-fabric-using-cognite-data-fusion-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Industrial Data Fabric Using Cognite Data Fusion® on AWS

Unifying and connecting industrial data

## Overview

This Guidance shows how to implement an industrial data fabric framework using Cognite Data Fusion with AWS technology. The industrial data fabric approach addresses the challenges industrial organizations face in managing and deriving value from disparate and siloed data sources. Cognite Data Fusion is used to integrate, connect, and unify IT, operational technology (OT), and engineering data into a cohesive and accessible data environment. This consolidation and contextualization of industrial data helps organizations unlock data-driven insights and develop innovative applications that can drive improvements in production efficiency, operational sustainability, and decision-making.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/industrial-data-fabric-using-cognite-data-fusion-on-aws.pdf)

![Architecture diagram](/images/solutions/industrial-data-fabric-using-cognite-data-fusion-on-aws/images/industrial-data-fabric-using-cognite-data-fusion-on-aws-1.png)

1. **Step 1**: Purpose-built extractors ingest data from various industrial sources. Information technology (IT), operational technology (OT), and engineering data such as industrial historians and Programmable Logic Controllers (PLCs) are included. Additionally, this Guidance ingests data from smart sensors or gateways into the AWS customer's data lake through the integration of AWS IoT Greengrass and AWS IoT SiteWise.
1. **Step 2**: In situations where customers already have their data in their AWS data lake, then Cognite Native Extractors for Amazon Simple Storage Service (Amazon S3), Amazon Redshift, Amazon DynamoDB, and Amazon Relational Database Service (Amazon RDS) ingest pre-aggregated data into Cognite Data Fusion.
1. **Step 3**: Data onboarded into Cognite Data Fusion first undergoes a quality and validation check. Customers build a comprehensive and dynamic Industrial Knowledge Graph to deliver near real-time insights using generative AI-powered data pipelines and entity matching to create relationships between siloed industrial data at scale.
1. **Step 4**: Cognite Data Fusion offers a collection of core user experiences (UX) and apps that use the Industrial Knowledge Graph built using contextualized industrial data. These apps include Canvas, AI Copilot, InField, InRobot, Maintain, and Charts designed to maximize production efficiency, ensure safe and sustainable operations, and enable high-quality, AI-powered business decisions.
1. **Step 5**: Customers use AWS Lambda and Amazon API Gateway to ingest and transform data. AWS Glue is used to write data back into Cognite Data Fusion using the Cognite software development kit (SDK). Additional analytics and machine learning capabilities are provided by Amazon Kinesis Data Analytics and Amazon SageMaker, respectively.
1. **Step 6**: AWS IoT TwinMaker, Amazon Managed Grafana, and Amazon QuickSight are used by end users to create applications. Data is consumed from Cognite Data Fusion using Lambda functions.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Cognite Data Fusion uses Amazon CloudWatch as the monitoring service to oversee the performance of various components, including application logs and error log monitoring through the use of AWS CloudTrail and Amazon EventBridge. This comprehensive monitoring approach allows organizations to trace events, analyze and visualize the performance of the technology stack, as well as conduct root cause analysis when errors occur. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance uses several security measures to mitigate cyber attack risks, including the use of Amazon Route 53 with AWS Shield Standard to protect against Distributed Denial of Service (DDoS) attacks. Additionally, it uses AWS Key Management Service (AWS KMS) and AWS Secrets Manager to encrypt and secure sensitive secrets and keys. Furthermore, this Guidance uses AWS Identity and Access Management (IAM) to manage permission policies and scope appropriate permission levels. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Elastic Load Balancing (ELB) automatically distributes incoming application traffic across multiple targets for high availability and fault tolerance. Amazon Elastic Compute Cloud (Amazon EC2) provides reliable and scalable compute capacity, enabling the automatic scaling of infrastructure up or down based on demand, while Amazon Elastic Container Service (Amazon ECS) simplifies the deployment and management of containerized applications, offering a highly reliable and scalable platform. Additionally, Amazon RDS handles database management tasks to ensure reliability and availability. Amazon Simple Queue Service (Amazon SQS) improves the reliability and fault tolerance of microservices and distributed systems. Finally, AWS Backup facilitates the centralization and automation of data backups across AWS services and on-premises resources, enhancing the overall data protection strategy. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon ElastiCache provides sub-millisecond response times, improving the performance of data-intensive applications by caching frequently accessed data in-memory and reducing the load on databases and backend systems. Lambda and AWS Step Functions work together to support performance efficiency. Lambda allows you to run code in response to events or requests without managing servers, while Step Functions orchestrates multiple Lambda functions into optimized serverless workflows. Additionally, Amazon Kinesis Firehose is a fully managed service for real-time data ingestion, enabling low-latency capture, transformation, and loading of streaming data into data stores and analytics services. These AWS services collectively deliver high performance efficiency through serverless compute, in-memory caching, and real-time data processing capabilities that automatically scale. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon EC2 Auto Scaling is a key service for cost efficiency, allowing you to automatically scale compute resources up or down based on demand, optimizing infrastructure costs by only paying for resources used. AWS Cost Explorer provides detailed visibility into AWS spending, enabling identification of cost optimization opportunities and informed resource utilization decisions. Amazon RDS autoscaling extends these benefits to database infrastructure, automatically scaling storage and compute capacity to handle demand changes without manual intervention or over-provisioning. Using these services allows right-sizing infrastructure, eliminating waste, and optimizing costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses Lambda functions for optimal compute resource allocation by stopping and starting resources based on predefined schedules. By efficiently managing compute resources based on demand, the use of Lambda functions minimizes unnecessary energy consumption during idle periods. This enables optimal resource utilization by automatically scaling based on demand, resulting in reduced energy usage compared to traditional server-based models. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
