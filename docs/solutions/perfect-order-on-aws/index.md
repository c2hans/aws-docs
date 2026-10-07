---
source_url: https://docs.aws.amazon.com/solutions/perfect-order-on-aws/index.html
---

---
title: 'Guidance for Perfect Order on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/perfect-order-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Perfect Order on AWS

## Overview

This Guidance demonstrates how you can configure an optimized order process that delivers what your consumers want and when they want it, also referred to as a "perfect order." An important part of the perfect order is the "last mile." This means delivering the product right to the consumer's front door. Getting the last mile right takes careful planning across the whole supply chain, which this architecture is built for. From the upstream order to the delivery, you can use this architecture to design a perfect order process that makes sure products are ready to ship on time, through optimized routes, with fleets tracked, and consumers notified.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/perfect-order-on-aws.pdf)

![Architecture diagram](/images/solutions/perfect-order-on-aws/images/perfect-order-on-aws-1.png)

1. **Step 1**: Upstream systems, which can be an ecommerce website or mobile app, produce the order. These orders are pushed to Amazon Simple Queue Service (Amazon SQS) which invokes an AWS Lambda function. These orders are pushed to Amazon DynamoDB, which then invokes an event by Amazon EventBridge.
1. **Step 2**: Order and customer details are pulled by AWS Fargate into the routing block. This data is used for planning an optimized fleet route using Amazon Location Service. Data is persisted in Amazon Neptune, a graph analytics database (DB).
1. **Step 3**: Lambda, in the fleet navigation block, extracts the route information and publishes to the fleet driver using AWS AppSync. AWS IoT Core receives the driver's location and sends it to GeoServices for analysis using Amazon Kinesis.
1. **Step 4**: Vehicle data is pushed to GeoServices where it is persisted in DynamoDB Streams. Lambda is invoked for analysis.
1. **Step 5**: A geofencing application is core for the analysis of a vehicle's state. A geofencing admin sets geofences for the route. Lambda uses the geofence to locate the vehicle.
1. **Step 6**: A Lambda function checks the Amazon Location Service for the estimated time of arrival (ETA) and predicts the scheduled delivery. Analyzed data is pushed by Amazon Simple Notification Service (Amazon SNS) alerts to both the driver and the end user for any delays and archives storage.
1. **Step 7**: Using AWS Lake Formation, the analytics outcome, along with other fleet data, are archived using Lambda into Amazon Simple Storage Service (Amazon S3) and a data lake.
1. **Step 8**: The data from the delivery status (outlined in step 6) is received in Amazon SQS. The data is pulled by Lambda to send proactive notifications to the consumer about the delivery status.
1. **Step 9**: Data managed by Lake Formation is used to build smart insights and reports using AWS Glue, Amazon Athena, and Amazon QuickSight.
1. **Step 10**: The data lake can be used for delivery predictions, driver profiling, and route profiling using Amazon SageMaker. The outcomes can be exposed using the Lambda API.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

We recommend integrating and deploying changes using AWS and DevOps practices when configuring this Guidance. For example, AWS CodeBuild and AWS CodeDeploy can be used to manage versions and deployment strategies. We also recommend using an AWS Cloud Development Kit (AWS CDK) which helps manage deployment through code in a controlled environment across accounts. This infrastructure as code approach helps with versioning, testing, and deployment automation. By leveraging AWS, DevOps tools, and CDK, you can deploy changes easily, rollback failed deployments, and provision resources reliably and repeatably across environments. This enables a robust continuous integration and continuous delivery (CI/CD) pipeline for safe, efficient updates to the architecture. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Several AWS services were used in this architecture to make sure communication and data are secure. For core communication between services, we used Amazon Cognito and AWS Identity and Access Management (IAM). This allows you to authenticate and authorize access for both people and machines. All service-to-service communication is authenticated with Amazon Cognito and authorized using IAM roles. For storing data, we used DynamoDB, Neptune, Amazon S3, and Lake Formation. These services encrypt data both when stored and when moved between services. By building in security with AWS from the start, you can ensure sensitive information is protected. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance follows AWS best practices for a serverless architecture. The core processing service is Lambda, provisioned using concurrency limits. To enable decoupled services, Amazon SQS and Amazon SNS are used. For observability, AWS metrics and logging services like Amazon CloudWatch, AWS X-Ray, and AWS CloudTrail are used. All backend logs and metrics from transactions and services are streamed to CloudWatch. By adhering to AWS serverless architectures, such as using Lambda for processing, and implementing AWS observability services, you can build a robust and scalable serverless system that is cost-effective, high-performing, and secure. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The AWS serverless services used throughout this Guidance scale continuously and usage is metered in milliseconds, optimizing costs. Since AWS manages the services, overall resource consumption is reduced too. The serverless architecture enables automatic scaling, resilience, cost optimization, and high performance. The on-demand nature of serverless computing allows you to only pay for exactly what you need while AWS handles provisioning and managing resources behind the scenes. This is ideal for workloads that are event-driven, inconsistent, or unpredictable. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses serverless services, the building blocks of AWS. Since AWS manages the infrastructure behind the services in this architecture, you avoid having to setup and maintain servers yourselves. This saves you money on operations and administration. You only pay for what you use. There are no charges when the services are idle. Using these ready-to-go components, optimized for fast processing and sharing, means your costs stay low and your productivity stays high. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This architecture promotes sustainability in a few key ways. First, it utilizes AWS serverless services that scale up and down based on demand, meaning the services only use the resources required at any given time. You don't have to overprovision idle or wasted capacity. Second, the AWS infrastructure is designed for optimal energy efficiency and sustainability. AWS data centers use advanced cooling systems and renewable energy sources to reduce environmental impact. By running your architecture on AWS, you benefit from its carbon-efficient operations. Third, the serverless model means you aren't purchasing and maintaining our own hardware. AWS manages the physical servers and resources on your behalf. This avoids manufacturing new hardware unnecessarily and extends the useful lifecycle of existing equipment. Finally, the automation enabled by AWS lets you easily delete and recreate resources when needed. This supports rebuilding fresh, optimized environments while minimizing persistent resource usage. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
