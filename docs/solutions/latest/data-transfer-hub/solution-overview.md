---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-hub/solution-overview.html
---

# Framework for secure, scalable, and trackable data transfer for Amazon Simple Storage Service (Amazon S3) objects and Amazon Elastic Container Registry (Amazon ECR) images
<a name="solution-overview"></a>

Publication date: *December 2021 ([last update](revisions.md): November 2024)*

 The Data Transfer Hub Guidance provides secure, scalable, and trackable data transfer for Amazon Simple Storage Service (Amazon S3) objects and Amazon Elastic Container Registry (Amazon ECR) images. This data transfer helps you easily create and manage different types (Amazon S3 object and Amazon ECR image) of transfer tasks between AWS [partitions](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/partitions.html) (for example, aws, aws-cn, aws-us-gov), and from other cloud providers to AWS at your own discretion.

If you have enabled the Direct Connect service in a specific AWS Region and a specific AWS China Region and have purchased a compliant cross-border dedicated line provided by a qualified operator to connect the AWS Region and their own VPC in the AWS China Region, you can use Data Transfer Hub's console to create a data transfer task and choose to use a dedicated line for data transfer at your own discretion.

 This implementation guide describes an overview of the Data Transfer Hub Guidance, its reference architecture and components, considerations for planning the deployment, and configuration steps for deploying Data Transfer Hub in the AWS Cloud. It also includes some tutorials with prescriptive guidance for using Data Transfer Hub.

 Use this navigation table to quickly find answers to these questions:

|  If you want to …  |  Read…  |
| --- | --- |
|  Know the cost for running this Guidance  |  [Cost](cost.md)  |
|  Understand the security considerations for this Guidance  |  [Security](security-1.md)  |
|  Know how to plan for quotas for this Guidance  |  [Quotas](quotas.md)  |
|  Know which AWS Regions are supported for this Guidance  |  [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions)  |
|  View or download the AWS CloudFormation template included in this Guidance to automatically deploy the infrastructure resources (the “stack”) for this Guidance  |  [AWS CloudFormation template](aws-cloudformation-template.md)  |

 This guide is intended for IT architects, developers, DevOps, data analysts, and marketing technology professionals who have practical experience architecting in the AWS Cloud.

You will be responsible for your compliance with all applicable laws in respect of your data transfer tasks.
