---
source_url: https://docs.aws.amazon.com/solutions/establishing-an-initial-foundation-using-aws-organizations/index.html
---

---
title: 'Guidance for Establishing an Initial Foundation Using AWS Organizations'
canonical_url: https://docs.aws.amazon.com/solutions/establishing-an-initial-foundation-using-aws-organizations/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for Establishing an Initial Foundation Using AWS Organizations

## Overview

This Guidance demonstrates how to build an initial cloud foundation on AWS that is secure, resilient, scalable, and automated across multiple accounts using AWS Organizations. You can add and group accounts, apply policies, and integrate with AWS services, all from a central location.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/establishing-an-initial-foundation-using-aws-oganizations.pdf)

![Architecture diagram](/images/solutions/establishing-an-initial-foundation-using-aws-organizations/images/establishing-an-initial-foundation-using-aws-organizations-1.png)

1. **Step 0**: Before you begin, identify a method to name your AWS accounts and determine the Regions you want to manage and operate in AWS.
1. **Step 1**: Create an AWS account with the AWS Management Console. Use a planned naming convention for root user email and account alias. Secure root user account and configure billing and tax information.
1. **Step 2**: Create and configure AWS IAM Identity Center and standard management account roles for administrative management. Apply security configurations to IAM Identity Center settings.
1. **Step 3**: Activate AWS Cost Explorer and create and configure AWS Cost & Usage Reports.
1. **Step 4**: Plan and deploy your foundational Organization Unit (OU) structure and accounts from AWS Organizations.
1. **Step 5**: Set up AWS CloudTrail to deploy CloudTrail to all AWS member accounts to deliver logs to a Log Archive Amazon Simple Storage Service (Amazon S3) bucket. Secure your log data using an AWS Key Management Service (AWS KMS) customer managed key.
1. **Step 6**: Deploy AWS Config to all accounts within the organization. Configure delivery of resource changes to a Log Archive S3 Bucket. Secure the log storage using an AWS KMS customer managed key.
1. **Step 7**: Create and publish a Tagging dictionary and enable Cost Allocation Tags.
1. **Step 8**: Deploy additional foundational security hardening configurations to your environment, using services such as Amazon CloudWatch.
[Read usage guidelines](/solutions/guidance-disclaimers/)
