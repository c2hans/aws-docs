---
source_url: https://docs.aws.amazon.com/solutions/connecting-data-clean-rooms/index.html
---

---
title: 'Guidance for Connecting Data to AWS Clean Rooms'
canonical_url: https://docs.aws.amazon.com/solutions/connecting-data-clean-rooms/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Connecting Data to AWS Clean Rooms

## Overview

This Guidance demonstrates how to provision data for collaboration using AWS Clean Rooms. Data connectors capture data sources through data ingestion and data preparation. The data is then imported into AWS and made available for collaboration.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/connecting-data-clean-rooms.pdf)

![Architecture diagram](/images/solutions/connecting-data-clean-rooms/images/connecting-data-clean-rooms-1.png)

1. **Step 1**: Data stored in external applications needs to be ingested into Amazon Simple Storage Service (Amazon S3). Either export data directly from a SaaS application that supports a native Amazon S3 connector. Use an AWS Glue extract, transform, and load (ETL) service to pull data from relational databases.
1. **Step 2**: Create a rule in Amazon EventBridge to schedule the data processing in AWS Step Functions. The function includes data ingestion and downstream processing steps.
1. **Step 3**: Use the AWS Lambda function to decrypt the files from the source Amazon S3 bucket using AWS Key Management Service (AWS KMS) and place them in a different prefix for AWS Glue DataBrew to pick up and process.
1. **Step 4**: Use AWS Glue DataBrew recipe to transform the data from the decrypted source Amazon S3 location. Use this step to normalize, and secure Personal Identifiable Information (PII) data using the SHA256 hashing algorithm.
1. **Step 5**: The output of the AWS Glue DataBrew recipe is written to the target Amazon S3 bucket:prefix location in parquet format.
1. **Step 6**: An AWS Glue Crawler job is initiated to refresh the table definition and its associated meta-data.
1. **Step 7**: After the AWS Glue Crawler job concludes, a Lambda function moves the source data files to an archive prefix location as part of clean-up activity.
1. **Step 8**: An event is published to Amazon Simple Notification Service (Amazon SNS) to inform the user that the new data files are now available for consumption within AWS Clean Rooms.
1. **Step 9**: The user can use the latest data within the AWS Clean Rooms service to collaborate with other data producers.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: A detailed guide is provided to experiment and use within your AWS account. Each stage of building the Guidance, including deployment, usage, and cleanup, is examined to prepare it for deployment.

[Open implementation guide](https://aws-solutions-library-samples.github.io/advertising-marketing/connecting-data-clean-rooms.html)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Every service has built-in observability, with metrics published to CloudWatch, where dashboards and alarms are then configured. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

IAM policies are created using the least-privilege access, so every policy is restricted to the specific resource and operation. Secrets, keys, and configuration items are centrally managed and secured using the AWS KMS service. The data at rest in the Amazon S3 bucket is encrypted using AWS KMS keys. File transfers into Amazon S3 are secured using Pretty Good Privacy (PGP) encryption and tunnel level TLS 1.2 encryption for API calls. Data transfer through API calls are encrypted using TLS 1.2. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Every service or technology for each architecture layer is fully managed by AWS, making the overall architecture elastic, highly available, and fault-tolerant. Incremental data processing is not included in the solution. This solution is built using a multi-tier architecture, where every tier is independently scalable, deployable, and testable. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Using serverless technologies, you only provision the exact resources you use. The serverless architecture reduces the amount of underlying infrastructure you need to manage, allowing you to focus on solving your business needs. All components of the solution are collocated in a single region and uses a serverless stack, which avoids the need for you to make infrastructure location decisions apart from the region choice. You can use automated deployments to deploy the solution components into any region quickly, providing data residence and reduced latency. Experiments and tests can be performed against different load levels, configurations, and services. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance utilizes managed services for cost optimization. As the data ingestion velocity increases and decreases, the costs align with usage. When AWS Glue is performing data transformations, you only pay for infrastructure while the processing is occurring. In addition, through a tenant solution model and resource tagging, you can automate cost usage alerts and measure costs specific to each tenant, application module, and service. IAM policies are created using the least-privilege access, such that every policy is restricted to the specific resource and operation. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By using serverless services, you maximize overall resource utilization and reduces the amount of energy required to operate the workload. You can also use the AWS Customer Carbon Footprint Tool to calculate and track the environmental impact of the workload over time at any account, region, or service level. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
