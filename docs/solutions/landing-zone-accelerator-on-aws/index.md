---
source_url: https://docs.aws.amazon.com//solutions/landing-zone-accelerator-on-aws//index.html
---

---
title: 'Landing Zone Accelerator on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/landing-zone-accelerator-on-aws/
source: aws-documentation
generated_on: 2026-09-25
---

# Landing Zone Accelerator on AWS

Deploy a cloud foundation to support highly-regulated workloads and complex compliance requirements

- **Version**: 1.16.3
- **Released**: 9/2026
- **Author**: AWS
- **Est. deployment time**: 50 mins
- **Estimated cost**: [See details](/solutions/latest/landing-zone-accelerator-on-aws/cost.html)

## Overview

The Landing Zone Accelerator on AWS solution deploys a foundational set of capabilities that is designed to align with AWS best practices and [multiple global compliance frameworks](/solutions/latest/landing-zone-accelerator-on-aws/support-for-regions-and-industries.html). With this AWS solution, you can better manage and govern your multi-account environment that have highly-regulated workloads and complex compliance requirements. When used in coordination with other AWS services, it provides a comprehensive, low-code solution across more than 35 AWS services. **Note: This solution will not, by itself, make you compliant. It provides the foundational infrastructure from which additional complementary solutions can be integrated.**

## Benefits

### Automation

Automatically set up a cloud environment suitable for hosting secure workloads. You can deploy this solution in all AWS Regions. This helps you maintain consistency of your operations and governance across AWS standard Regions, AWS GovCloud (US), and other non-standard partitions in AWS.

### Data security

Deploy this solution in an AWS Region suitable for your data classification, and use Amazon Macie to provide sensitive data detection in Amazon Simple Storage Service (Amazon S3). This solution also helps you deploy, operate, and govern a centrally managed encryption strategy using AWS Key Management System (AWS KMS).

### Foundation for compliance

Leverage a foundational infrastructure for deploying mission-critical workloads across a centrally governed multi-account environment.

## How it works

You can automatically deploy this architecture using the implementation guide and the accompanying AWS CloudFormation template.

[View implementation guide](/solutions/latest/landing-zone-accelerator-on-aws/solution-overview)

![Architecture diagram](/images/solutions/landing-zone-accelerator-on-aws/images/landing-zone-accelerator-on-aws-1.png)

1. **Step 1**: You use AWS CloudFormation to install the solution into your environment. Your environment must meet [prerequisites](/solutions/latest/landing-zone-accelerator-on-aws/prerequisites.html) before deploying the solution. The provided CloudFormation template deploys an AWS CodePipeline that contains the Landing Zone Accelerator on AWS installation engine.
1. **Step 2**: The **Installer** pipeline ( `AWSAccelerator-InstallerStack` ) functions separately from the **Core** pipeline. This way, you can update to future versions of the solution with a single parameter through the AWS CloudFormation console.
1. **Step 3**: An AWS CodeBuild project functions as an orchestration engine to build and run the solution’s AWS CDK application that deploys the Core pipeline ( `AWSAccelerator-PipelineStack` ) and its associated dependencies.
1. **Step 4**: The solution deploys Amazon Simple Notification Service (Amazon SNS) topics that you can subscribe to for alerts on Core pipeline events, which can increase observability of your Core pipeline operations. Additionally, the solution deploys two AWS Key Management Service (AWS KMS) customer-managed keys to manage encryption at rest of Installer and Core pipeline dependencies.
1. **Step 5**: The Core pipeline validates and synthesizes inputs and deploys additional CloudFormation stacks with AWS CDK. An Amazon Simple Storage Service (Amazon S3) bucket ( `aws-accelerator-config` ) stores the configuration files that the solution uses. These configuration files are the primary mechanism for configuring and managing the solution.
1. **Step 6**: An AWS CodeBuild project compiles and validates the solution’s AWS CDK application configuration.
1. **Step 7**: Multiple AWS CodeBuild deployment stages deploy the resources that were defined in the solution configuration files to your multi-account environment. An optional manual review stage can be included, allowing you to view all the changes that these stages will apply.
1. **Step 8**: The solution deploys resources that monitor AWS Control Tower lifecycle events to detect potential drift against a known good state (in other words, when the actual configuration of an infrastructure resource differs from its expected configuration). The solution also deploys resources that can automate the enrollment of new AWS accounts into your multi-account environment. When using AWS Control Tower with this solution, ensure that accounts and organizational units (OUs) within your AWS Control Tower environment are properly enrolled. You can manage this through the AWS Control Tower console. **Note** We provide guidance in [For AWS Organizations based installation (without AWS Control Tower)](/solutions/latest/landing-zone-accelerator-on-aws/prerequisites.html#for-aws-organizations-based-installation-without-aws-control-tower) later in this document if you wish not to use AWS Control Tower.
1. **Step 9**: The solution deploys centralized logging resources in the **Log Archive** account in your multi-account environment. This includes Amazon Kinesis resources to stream and ingest logs, AWS KMS keys to facilitate encryption at rest, and Amazon Simple Storage Service (Amazon S3) buckets as log storage destinations.
1. **Step 10**: The solution provisions the audit account with resources to Amazon CloudWatch log groups to the centralized logging infrastructure in the LogArchive account.
## Deploy with confidence

- **We'll walk you through it**: Get started fast. Read the implementation guide for deployment steps, architecture details, cost information, and customization options.

[Open guide](/solutions/latest/landing-zone-accelerator-on-aws/solution-overview?target=_blank)

- **Let's make it happen**: Ready to deploy? Open the CloudFormation template in the AWS Console to begin setting up the infrastructure you need. You'll be prompted to access your AWS account if you haven't yet logged in.

[Launch in the AWS Console](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?&templateURL=https:%2F%2Fsolutions-reference.s3.amazonaws.com%2Flanding-zone-accelerator-on-aws%2Flatest%2FAWSAccelerator-InstallerStack.template&redirectId=SolutionWeb)

## Deployment options

- **CloudFormation template**: View or modify the CloudFormation template to customize your deployment.

[Download Template](https://s3.amazonaws.com/solutions-reference/landing-zone-accelerator-on-aws/latest/AWSAccelerator-InstallerStack.template)

- **Source Code**: The source code for this AWS Solution is available in GitHub.

[Go to github](https://github.com/awslabs/landing-zone-accelerator-on-aws?refid=sl_card)

## Related content

- **Introduction to Landing Zone Accelerator on AWS | AWS Public Sector**

[Watch the video](https://www.youtube.com/watch?v=UHS_q1oODYM)

- **AWS Summit DC 2022 - Scaling automated governance with Landing Zone Accelerator on AWS**

[Watch the video](https://www.youtube.com/watch?v=HaXzfNfJR7c)

- **AWS re:Inforce 2022 - Build automated compliance using Landing Zone Accelerator on AWS**

[Watch the video](https://www.youtube.com/watch?v=m_KavYgmZ2I)

- **Introducing Landing Zone Accelerator for Healthcare**: The Landing Zone Accelerator for Healthcare is an industry-specific deployment of the Landing Zone Accelerator on AWS solution. It's architected to align with AWS best practices and in conformance with multiple, global compliance frameworks.

[Read the blog](https://aws.amazon.com/blogs/industries/introducing-landing-zone-accelerator-for-healthcare/)

- **What US federal customers need to know about memorandum M-21-31**: In this blog post, learn the services from AWS that have been called out explicitly in the memorandum M-21-31 for logging and retention requirements at the EL1 level, and the resources you can use to set up these services to capture the required log data.

[Read the blog](https://aws.amazon.com/blogs/publicsector/aws-federal-customers-memorandum-m-21-31/)

---

## AWS Support

- [Get support for this AWS Solution](/solutions/latest/landing-zone-accelerator-on-aws/contact-aws-support.html)

## RSS Feed

- [Subscribe now to get updates on the latest release.](https://solutions-reference.s3.us-east-1.amazonaws.com/landing-zone-accelerator-on-aws/latest/rss.xml)
