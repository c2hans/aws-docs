---
source_url: https://docs.aws.amazon.com/solutions/establishing-an-initial-foundation-using-control-tower-on-aws/index.html
---

---
title: 'Guidance for Establishing an Initial Foundation using Control Tower on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/establishing-an-initial-foundation-using-control-tower-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Establishing an Initial Foundation using Control Tower on AWS

## Overview

This Guidance demonstrates how to build an initial cloud foundation on AWS that is secure, resilient, scalable, and automated across multiple accounts. It helps customers quickly and securely deploy workloads across a centrally governed environment.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram PDF](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/establishing-an-initial-foundation-using-control-tower-on-aws.pdf)

![Architecture diagram](/images/solutions/establishing-an-initial-foundation-using-control-tower-on-aws/images/establishing-an-initial-foundation-using-control-tower-on-aws-1.png)

1. **Step 1**: (CFLZ1-P2) Create an AWS account using a planned naming convention for root user email and account alias, secure root user account, and configure billing and tax information.
1. **Step 2**: (CFLZ1-P4) Create and configure AWS IAM Identity Center and standard management account roles for administrative management. Apply security configurations to IAM Identity Center settings.
1. **Step 3**: (CFLZ1-P3) Activate AWS Cost Explorer and create and configure AWS Cost & Usage Report.
1. **Step 4**: (CFLZ1-P5) Plan and deploy AWS Control Tower from identified parameters and secure your log data through AWS Key Management Service (AWS KMS) encryption. Apply an additional AWS Control Tower setting for landing zone. Set up AWS CloudTrail to deploy CloudTrail to all AWS member accounts, delivering logs to Log Archive S3 Bucket.
1. **Step 5**: (CFLZ1-P6) Build foundational Organizational unit structure on top of your Control Tower deployment.
1. **Step 6**: (CFLZ1-P7) Establish and deploy AWS Tag Policies. Activate cost allocation tags.
1. **Step 7**: (CFLZ1-P8) Deploy additional foundational security hardening configurations to your environment to include CloudWatch monitoring and AWS Config to management account, apply additional service control policies through AWS Organizations.
[Read usage guidelines](/solutions/guidance-disclaimers/)
