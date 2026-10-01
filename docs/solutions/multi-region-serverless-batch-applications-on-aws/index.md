---
source_url: https://docs.aws.amazon.com/solutions/multi-region-serverless-batch-applications-on-aws/index.html
---

---
title: 'Guidance for Multi-Region Serverless Batch Applications on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/multi-region-serverless-batch-applications-on-aws/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Multi-Region Serverless Batch Applications on AWS

## Overview

This Guidance helps customers design a resilient batch process application using AWS services. The batch application is deployed across two AWS Regions for automated failover and failback from one Region to another and leverages Amazon Simple Storage Service (Amazon S3) Multi-Region Access Points (MRAPs). With this architecture, you can obtain insights from your applications that help you make decisions on when to failover batch applications from a primary to a standby Region. While single-Region architectures are sufficient to support most customer's resilience requirements, the multi-Region architecture in this Guidance is ideal for customers with more demanding needs for resiliency.

## How it works

### Primary Region

This architecture shows the multi-Region, event-driven workload when running in the primary Region.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/multi-region-serverless-batch-applications-on-aws-primary-region.pdf)Step 1Add the file to an Amazon Simple Storage Service (Amazon S3) bucket using the MRAP. MRAP routes the file to one of the S3 buckets, which will replicate the object to the other bucket.Step 2Amazon S3 invokes the AWS Lambda function putObject in both Regions.Step 3The Lambda function will resolve the TXT record in an Amazon Route53 private hosted zone to determine if it is the active Region. If it is, the workflow will continue. If it is not, the function will exit and not take further action. The function in the active Region writes metadata on the file to the Amazon DynamoDB batch state table, including that the processing has started, and starts the first AWS Step Functions workflow.Step 4The main orchestrator Step Functions workflow orchestrates file processing by splitting the file into small chunks and then passing it to chunk file processor Step Functions workflow.Step 5The chunk file processor Step Functions workflow is responsible for processing each row from the chunk file.Step 6The merged file is written to Amazon S3, which replicates it to the standby Region's bucket.Step 7A pre-signed URL is generated using the MRAP so the user can retrieve the file from the closest S3 bucket. The routing logic is abstracted from the client.Step 8Amazon Simple Email Service (Amazon SES) mails the pre-signed URL to recipients so they can retrieve the file from one of the S3 buckets through the MRAP.### Standby Region

This architecture shows the multi-Region, event-driven workload when failing over to the standby Region.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/multi-region-serverless-batch-applications-on-aws-primary-region.pdf)Step 1Add the file to an Amazon Simple Storage Service (Amazon S3) bucket using the MRAP. MRAP routes the file to one of the S3 buckets, which will replicate the object to the other bucket.Step 2Amazon S3 invokes the AWS Lambda function putObject in both Regions.Step 3The Lambda function will resolve the TXT record in an Amazon Route53 private hosted zone to determine if it is the active Region. If it is, the workflow will continue. If it is not, the function will exit and not take further action. The function in the active Region writes metadata on the file to the Amazon DynamoDB batch state table, including that the processing has started, and starts the first AWS Step Functions workflow.Step 4The main orchestrator Step Functions workflow orchestrates file processing by splitting the file into small chunks and then passing it to chunk file processor Step Functions workflow.Step 5The chunk file processor Step Functions workflow is responsible for processing each row from the chunk file.Step 6The merged file is written to Amazon S3, which replicates it to the standby Region's bucket.Step 7A pre-signed URL is generated using the MRAP so the user can retrieve the file from the closest S3 bucket. The routing logic is abstracted from the client.Step 8Amazon Simple Email Service (Amazon SES) mails the pre-signed URL to recipients so they can retrieve the file from one of the S3 buckets through the MRAP.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-multi-region-serverless-batch-applications-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

You can deploy this Guidance with infrastructure as code (IaC) to make any modifications. We also provide a dashboard that helps you understand performance and make iterations to the Guidance so you can achieve your desired performance characteristics. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

We implemented least privilege access on Identity and Access Management (IAM) roles attached to the Lambda functions, so these roles only have permission to access the resources they need. You can use a pre-signed Amazon S3 URL to access S3 buckets. In this Guidance, these URLs come with a set expiration time of sixty minutes to protect resources from unrestricted access. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance replicates data across Regions to allow for full redundancy in the standby Region. This multi-Region approach allows you to failover to another Region in disaster recovery scenarios. Within the Region, you can use retry logic and decoupled processing. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

We chose the services in this Guidance based on their abilities to reduce cost and complexity and enhance performance. You can test the Guidance with the provided example files and modify processes based on your specific use case. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses serverless services that allow you to pay only for the resources you consume during batch processing. With these services, your costs are directly associated to the number of processed items for each batch job. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The serverless and managed services scale to meet changes in demand. AWS handles the provisioning of the underlying resources. This helps you avoid provisioning unneeded resources. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
