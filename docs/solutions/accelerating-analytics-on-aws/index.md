---
source_url: https://docs.aws.amazon.com/solutions/accelerating-analytics-on-aws/index.html
---

---
title: 'Guidance for Accelerating Analytics on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/accelerating-analytics-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Accelerating Analytics on AWS

## Overview

This Guidance deploys a configurable, end-to-end set of AWS data and analytics services to visualize your data. Previously, integrating multiple data and analytics components required manually deploying and configuring each service, often a time-consuming process needing engineers to instrument. This Guidance is especially helpful to quickly iterate, publish, and test analytics projects on the way to wider-scale implementations. With Accelerating Analytics on AWS, you can launch a single [AWS CloudFormation template](https://aws.amazon.com/cloudformation/resources/templates/) that deploys and configures multiple, integrated AWS data and analytics services to quickly scale users’ access to data and insights more quickly and with less resources.

## How it works

This Guidance helps you quickly deploy a data analytics stack using AWS services. In this diagram, an administrator creates a storage bucket and uploads files that can be processed for data analysis and visualization.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/accelerating-analytics-on-aws.pdf)

![Architecture diagram](/images/solutions/accelerating-analytics-on-aws/images/accelerating-analytics-on-aws-1.png)

1. **Step 1**: An administrator creates a new Amazon Simple Storage Service (Amazon S3) data bucket, and uploads flat files that will be visualized in Amazon QuickSight.
1. **Step 2**: AWS Lake Formation registers the Amazon S3 data bucket as a resource, and allows access to an AWS Identity and Access Management (IAM) role used by QuickSight.
1. **Step 3**: An AWS Glue crawler crawls the Amazon S3 data bucket to obtain metadata of the user data. The crawler runs everyday on a schedule to update the Table metadata if new data is available in the bucket.
1. **Step 4**: The crawler updates the metadata in an AWS Glue Data Catalog as a Database and Table, with permissions managed by Lake Formation.
1. **Step 5**: Amazon Athena queries the Table using SQL queries issued by QuickSight when visuals are loaded.
1. **Step 6**: A QuickSight subscription is created if it does not exist. A new QuickSight Dataset and Analysis is created using the IAM role to issue queries to Athena and access the data in the Amazon S3 bucket.
1. **Step 7**: You can access QuickSight analysis and start creating visuals to gain insight about your data.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The AWS services used in this Guidance support logging information in Amazon CloudWatch or AWS CloudTrail that can be tracked and reviewed for additional customization. This enables a fast and easy way to review errors and respond to incidents appropriately. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The AWS Glue database and table created in this Guidance are secured using Lake Formation, and access is granted only to the IAM role used by Quicksight. This allows for secure authentication and authorization for people and machine access. The resources provisioned in this Guidance are private by default, and can only be modified with IAM identity-based policies. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Since AWS services used in this Guidance are serverless, use AWS managed endpoints and DNS, the implementation can depend on the high availability and resiliency to failures that are inherent in AWS services. AWS CloudFormation automates deployment and provisioning of resources. Upon failure of one resource, the implementation rolls back all other provisioned resources, ensuring you have a reliable application-level architecture. Additionally, CloudFormation logs resource provisioning and errors that can be accessed using CloudTrail and CloudWatch. QuickSight sends an email to notify account administrators when significant events occur. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The services selected for this Guidance are purpose-built to handle advanced analytics. For example, QuickSight is an AWS managed serverless business intelligence (BI) service that integrates with Athena to query data in Amazon S3. A QuickSight analysis, where you analyze and visualize your data, is created when this Guidance is deployed, helping you gain insights from your data. Based on Athena tables, also created by this Guidance, you can experiment and create additional tables to query data in Amazon S3 or other supported data sources. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance uses managed services that deploy a pay-as-you-go approach, removing the need to maintain overhead and reduce cost. AWS services used in this Guidance are also provisioned in the same AWS Region to reduce data transfer charges, whereas QuickSight does not accrue any data transfer charges. All services in this Guidance are serverless and do not require running for an extended period of time. To ensure this Guidance scales to continually match the demand with the minimum resources, it deploys an Amazon S3 bucket that contains only customer provisioned data. The AWS Glue crawler runs once per day to check for new data, and Athena is invoked only when using QuickSight. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance invokes Athena only when users interact with the corresponding data sets in QuickSight, ensuring limited provisioning of resources. Additionally, Amazon S3 and Athena automatically scale to accommodate data that you provide. Architecture patterns that maintain consistently high utilization of deployed resources are implemented with this Guidance. For example, the AWS Glue crawler is only invoked once every day to crawl customer data in Amazon S3 buckets and to update the Glue Catalog. Finally, this Guidance uses serverless AWS services that do not require continuous hardware provisioning, making it a more sustainable architecture. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
