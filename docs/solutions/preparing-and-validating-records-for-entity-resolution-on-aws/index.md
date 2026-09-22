---
source_url: https://docs.aws.amazon.com/solutions/preparing-and-validating-records-for-entity-resolution-on-aws/index.html
---

---
title: 'Guidance for Preparing and Validating Records for Entity Resolution on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/preparing-and-validating-records-for-entity-resolution-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Preparing and Validating Records for Entity Resolution on AWS

## Overview

This Guidance demonstrates how to prepare and validate Personally Identifiable Information (PII) data, including physical address, phone, and email, for use with AWS Entity Resolution. PII is processed to fix or remove incorrect, corrupted, duplicated, and incomplete data. The data is then standardized and validated for use with AWS Entity Resolution, delivering higher data quality, accurate identity resolution, as well as improved accuracy in customer analytics, segmentation, and targeting.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/preparing-and-validating-records-for-entity-resolution-on-aws.pdf)

![Architecture diagram](/images/solutions/preparing-and-validating-records-for-entity-resolution-on-aws/images/preparing-and-validating-records-for-entity-resolution-on-aws-1.png)

1. **Step 1**: Create a rule in Amazon EventBridge to schedule the data processing in AWS Step Functions. The Step Functions state machine includes data cleaning and validation steps.
1. **Step 2**: Use AWS Glue DataBrew recipe to transform the data from the source Amazon Simple Storage Service (Amazon S3) location. Use this step to normalize data, which will give better outcomes with data validation API.
1. **Step 3**: Use AWS Glue to read the output of the DataBrew job, enabling the invocation of the respective personally identifiable information (PII) entity validation services in small batches.
1. **Step 4**: AWS Glue writes the validated data to the target curated Amazon S3 bucket for AWS Entity Resolution to consume.
1. **Step 5**: An AWS Glue crawler job is initiated to "refresh" the table definition or metadata of the curated Amazon S3 storage location, and stores it in the AWS Glue Data Catalog.
1. **Step 6**: An event is published to Amazon Simple Notification Service (Amazon SNS) to inform the user that the new curated data files are now available for consumption.
1. **Step 7**: Security, Configuration, and Observability: This Guidance uses the following AWS services to promote security and access control: AWS Identity and Access Management (IAM): Least-privilege access to specific resources and operations. AWS Key Management Service (AWS KMS): Provides encryption for data at rest and data in transit, using Pretty Good Privacy (PGP) encryption of data files. AWS Secrets Manager: Provides hashing keys for PII data. Amazon CloudWatch: Monitors logs and metrics across all services used in this Guidance.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: A detailed guide is provided to experiment and use within your AWS account. Each stage of building the Guidance, including deployment, usage, and cleanup, is examined to prepare it for deployment. The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open guide](https://aws-solutions-library-samples.github.io/advertising-marketing/preparing-and-validating-records-for-entity-resolution-on-aws.html)
[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-preparing-and-validating-records-for-entity-resolution-on-aws/)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance has observability built-in, with every service publishing metrics to CloudWatch, where dashboards and alarms can be configured. CloudWatch Events deliver a near real-time stream of system events that describe changes in resources. CloudWatch logs help you to monitor, store, and access log files for various resources to notify you when certain thresholds are met. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

IAM policies are created using the least-privilege access so that every policy is restricted to the specific resource and operation. To protect resources in this Guidance, secrets and configuration items are centrally managed and secured using AWS KMS. Data at rest in Amazon S3 is also encrypted using AWS KMS. AWS Glue supports using resource policies to control access to Data Catalog resources. These resources include databases, tables, connections, and user-defined functions, along with the Data Catalog APIs that interact with these resources. You can turn on encryption of Data Catalog objects in the Data Catalog, and encrypt connection passwords using AWS KMS. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance provides ways to process data in chunks, which reduces the risk of exceeding API limits, memory constraints, and time limits. Every service and technology chosen for each architecture layer of this Guidance is serverless and fully managed by AWS, making the overall architecture elastic, highly available, and fault-tolerant. It also implements a resilience to failures with dead-letter queues (DLQ) that allow for investigation of AWS Lambda failures. And Implementing EventBridge Message bus allows for redrive or replay of the events. You can use Step Functions to set up retries, backoff rates, max attempts, intervals, and timeouts for any failed AWS Glue job. Also, AWS Glue is subject to Region-specific service quota that may affect reliability. You can contact AWS Support to request a quota increase based on your needs. With Amazon S3, you have offers industry-leading durability, availability, performance, security, and virtually unlimited scalability at very low costs. Finally, to implement data backup and recovery for this Guidance, you should back up data, applications, and configurations to meet the requirements for recovery time objectives (RTO) and recovery point objectives (RPO). RTO or RPO may vary based on your business impact analysis, and should be planned for recovery accordingly. For example, if your RTO and RPO is 5 minutes, an active or active Disaster Recovery (DR) strategy is required. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Using serverless technologies, you only provision the exact resources you use. The serverless architecture reduces the amount of underlying infrastructure you need to manage, allowing you to focus on solving your business needs. You can use automated deployments to deploy the components of this Guidance into any Region quickly - providing data residence and reduced latency. You can experiment and test each Guidance component, enabling you to perform comparative testing against varying load levels, configurations, and services. For example, AWS Auto Scaling is available for AWS Glue extract, transform, and load (ETL) jobs. With AWS Auto Scaling enabled, AWS Glue automatically adds and removes workers from the cluster depending on the parallelism at each stage of the job run. Amazon S3 automatically scales to high request rates. There are no limits to the number of prefixes in a bucket, and you can increase read or write performance by using parallelization. All components of this Guidance are collocated in a single Region. If the components are deployed in multiple Availability Zones, and you use a serverless stack, it avoids the need for you to make infrastructure location decisions apart from the Region or Availability Zone choice. You can use automated deployments to deploy this Guidance into any Region quickly - providing data residence and reduced latency. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Using serverless technologies and managed services, you only pay for the resources you consume, and this Guidance doesn’t have any AWS data egress charges. Depending on your business continuity goals, this Guidance could be a single Availability Zone (AZ) deployment, which would avoid cross AZ data transfer costs. When AWS Glue is performing data transformations, you only pay for infrastructure during the time the processing is occurring. For the AWS Glue Data Catalog, you pay a simple monthly fee for storing and accessing the metadata. With Amazon S3, you pay for storing objects in buckets. With EventBridge free tier, you can schedule rules to initiate data processing using a Step Functions workflow, where you are charged based on the number of state transitions. In addition, through a tenant isolation model and resource tagging, you can automate cost usage alerts and measure costs specific to each tenant, application module, and service. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By extensively using serverless services, you maximize overall resource utilization - as compute is only used as needed. The efficient use of serverless resources reduces the overall energy required to operate the workload. Serverless services used in this Guidance ( AWS Glue, Amazon S3 ) automatically optimize the resource utilization in response to demand. You can extend this Guidance by using an Amazon S3 Lifecycle configuration to define policies and move objects to different storage classes based on access patterns. All of the services used in this architecture are managed services that allocate hardware according to the workload demand. Use the provisioned capacity option in the service configurations, where it's available, when the workload is predictable. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
