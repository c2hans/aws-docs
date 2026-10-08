---
source_url: https://docs.aws.amazon.com/solutions/deploy-a-poc-for-aws-backup/index.html
---

---
title: 'Deploy a PoC for AWS Backup'
canonical_url: https://docs.aws.amazon.com/solutions/deploy-a-poc-for-aws-backup/
source: aws-documentation
generated_on: 2026-10-08
---

# Deploy a PoC for AWS Backup

## Overview

This Guidance provides instructions and templates that enable users to quickly and easily deploy a proof-of-concept (PoC) deployment of AWS Backup. Customers can leverage this Guidance and the best practices provided, along with the CloudFormation template and deployment steps to perform their own PoC evaluation of AWS Backup for their scenario, allowing users to understand the service and its capabilities.

## Benefits

### Accelerate backup implementation

Deploy a complete AWS Backup environment in minutes using the provided CloudFormation template. Quickly test backup capabilities across EC2, Aurora, and S3 resources without extensive configuration or specialized knowledge.

### Simplify compliance verification

Validate backup compliance requirements with pre-configured AWS Backup Audit Manager reports delivered to S3. Gain immediate visibility into your backup posture through automated reporting that helps demonstrate adherence to organizational policies.

### Enhance data protection strategy

Test comprehensive backup capabilities including tag-based selection and KMS encryption in an isolated environment. Experience AWS Backup's centralized approach to protecting your critical workloads before implementing in production.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/deploy-a-poc-for-aws-backup.pdf)

![Architecture diagram](/images/solutions/deploy-a-poc-for-aws-backup/images/deploy-a-poc-for-aws-backup-1.png)

1. **Step 1**: The user logs into the AWS Management Console and deploys the Proof-of-Concept (PoC) template provided in this Guidance, using AWS CloudFormation to create a new stack.
1. **Step 2**: AWS CloudFormation deploys an Amazon Virtual Private Cloud (Amazon VPC) with one public and one private subnet, and the required VPC endpoints for private access.
1. **Step 3**: AWS CloudFormation deploys an Amazon Elastic Compute Cloud (Amazon EC2) Instance, an Amazon Elastic Block Store (Amazon EBS) volume, an Amazon Aurora MySQL database cluster (single writer), and an Amazon Simple Storage Service (Amazon S3) bucket.
1. **Step 4**: AWS CloudFormation creates two AWS Backup vaults encrypted with AWS Key Management Service (AWS KMS) Customer managed key, and an AWS Backup plan with a tag-based selection.
1. **Step 5**: AWS CloudFormation configures an AWS Backup Audit Manager report plan to deliver compliance reports to Amazon S3.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/deploy-a-poc-of-aws-backup)

[Read usage guidelines](/solutions/guidance-disclaimers/)
