---
source_url: https://docs.aws.amazon.com/solutions/creating-a-customized-coding-companion-with-amazon-q-developer/index.html
---

---
title: 'Guidance for Creating a Customized Coding Companion with Amazon Q Developer'
canonical_url: https://docs.aws.amazon.com/solutions/creating-a-customized-coding-companion-with-amazon-q-developer/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Creating a Customized Coding Companion with Amazon Q Developer

## Overview

This Guidance demonstrates how to aggregate public, open-source code repositories into a central location to customize Amazon Q Developer. It provides a blueprint to create a new repository that is preconfigured with source code and a workflow to deploy into an AWS account. Each repository is checked for open-source providers (such as GitHub) for a new release. If a new release is available, a subsequent task is launched within a customer-managed virtual private cloud (VPC). It uses an image of the repository, downloads, and extracts the release archive into a storage bucket. The task updates the repository and a notification is sent. An Amazon Q customization can be trained using the repository archives, allowing developers to use AI-generated code suited to their coding language and style.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/creating-a-customized-coding-companion-with-amazon-q-developer.pdf)

![Architecture diagram](/images/solutions/creating-a-customized-coding-companion-with-amazon-q-developer/images/creating-a-customized-coding-companion-with-amazon-q-developer-1.png)

1. **Step 1**: Initialize a new project in Amazon CodeCatalyst with this blueprint to create a new Git repository. It is preconfigured with the source code and a workflow to deploy to an AWS account environment.
1. **Step 2**: All changes in the Git repository invoke a workflow which builds and deploys all infrastructure-as-code (IaC) related to the architecture, using an AWS Cloud Development Kit (AWS CDK), which includes a command line interface (CLI) tool for working with your AWS CDK apps and stacks.
1. **Step 3**: An AWS Lambda trigger function examines which repositories should be included in the archival process, and updates metadata in the Amazon DynamoDB repository table.
1. **Step 4**: An Amazon EventBridge rule invokes an AWS Step Functions state machine to process on a regular interval.
1. **Step 5**: A Lambda function scans the repository table in DynamoDB for enabled repositories, and starts a parallel process for each repository using a Map state.
1. **Step 6**: For each repository in the Map state, a Lambda function checks open-source providers (such as GitHub) for a new release. If a new release is available, a subsequent AWS Fargate task is launched within a customer-managed virtual private cloud (VPC). It uses an image from Amazon Elastic Container Registry (Amazon ECR), downloads, and extracts the release archive in an Amazon Simple Storage Service (Amazon S3) bucket. The task updates the repository table in DynamoDB. A message is also published to an Amazon Simple Notification Service (Amazon SNS) topic.
1. **Step 7**: An Amazon Q Developer customization can be trained using the repository archives in Amazon S3, allowing developers to use AI-generated code suited to their coding language and style.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-creating-a-customized-coding-companion-with-amazon-q-developer)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The goal of operational excellence is to get new features and bug fixes into your hands quickly and reliably. EventBridge, Step Functions, Amazon SNS, and Lambda do this byhelping you automate the process of downloading or extracting repository releases when available, and alerting you when a new version of an Amazon Q customization can be trained. An EventBridge rule and a Step Functions workflow automatically check for new repository versions on a schedule, whereas the Lambda functions synchronize repository metadata. Finally, messages are published to an Amazon SNS topic for operational notifications. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) is used to define roles and permission policies for resources deployed in this solution, and Amazon S3 is configured with policies to restrict access to outside entities. Roles and policies defined within IAM and Amazon S3 are critical for implementing least-privilege access, and limiting access to only what is needed. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Step Functions has features like automated retries, error handling, and fault tolerance for minimizing failures. It also can help limit re-processing that can degrade performance. These capabilities minimize the likelihood and impact of disruptions, enhancing the overall resiliency of workflow orchestration. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The Map state feature in Step Functions allows you to process steps concurrently instead of sequentially, significantly increasing throughput and performance for workloads that can be done in parallel. This enables faster processing time by doing multiple tasks at once, and as the list of repositories scales, the time it takes to process all repositories remains static. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

By using Fargate and Lambda to complete on-demand tasks, you can achieve significant cost efficiencies compared to self-managed Amazon Elastic Compute Cloud(Amazon EC2) deployments that accrue costs when idle. Fargate enables a serverless model with auto-scaling to reduce over-provisioning and minimize idle resources. With Lambda, you only pay for compute time when your functions execute. No need to provision and pay for Amazon EC2 instances that may be underutilized. With these serverless options, you can save significantly compared to traditional servers or virtual machines. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Both Fargate and Lambda are serverless, auto-scaling services that right-size usage to workload needs. This eliminates over-provisioning and idle resources, which reduces energy usage. The serverless auto-scaling nature, ephemeral infrastructure, and managed provider sustainability efforts of Lambda and Fargate help you to reduce waste, maximize utilization, and minimize the overall environmental footprint of your workloads. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
