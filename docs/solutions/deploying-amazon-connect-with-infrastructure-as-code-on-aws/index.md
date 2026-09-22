---
source_url: https://docs.aws.amazon.com/solutions/deploying-amazon-connect-with-infrastructure-as-code-on-aws/index.html
---

---
title: 'Guidance for Deploying Amazon Connect Customer Customer with Infrastructure as Code on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/deploying-amazon-connect-with-infrastructure-as-code-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Deploying Amazon Connect Customer Customer with Infrastructure as Code on AWS

## Overview

This Guidance helps organizations rapidly scale and standardize their contact center operations by implementing Connect Customer through infrastructure as code. It streamlines the provisioning of Connect Customer instances and integrated services, eliminating manual configuration errors and reducing operational overhead. The Guidance encompasses omnichannel communication capabilities, AI-enhanced agent support, and robust analytics features, all built on AWS security best practices.

## Benefits

### Accelerate contact center modernization

Deploy an enterprise-grade contact center in hours instead of months using automated infrastructure provisioning. Focus on delivering exceptional customer experiences while AWS manages the underlying infrastructure and scales automatically to match your business demands.

### Enhance security and compliance controls

Implement comprehensive security measures with built-in encryption and access controls that protect sensitive customer communications. Maintain detailed audit trails and meet regulatory requirements through centralized security management.

### Optimize agent productivity efficiently

Empower agents with an intuitive workspace that streamlines customer call handling. Enable seamless call management while automatically capturing interaction data for continuous improvement.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/deploying-amazon-connect-with-infrastructure-as-code-on-aws.pdf)

![Architecture diagram](/images/solutions/deploying-amazon-connect-with-infrastructure-as-code-on-aws/images/deploying-amazon-connect-with-infrastructure-as-code-on-aws-1.png)

1. **Step 1**: A customer calls the Amazon Connect Customer contact center phone number.
1. **Step 2**: A contact center agent gets the call on the agent workspace and answers the call.
1. **Step 3**: An Amazon Simple Storage Service (Amazon S3) bucket stores the call recordings.
1. **Step 4**: For management, Amazon Connect Customer sends the performance logs to Amazon CloudWatch and audit logs to AWS CloudTrail.
1. **Step 5**: An AWS Key Management Service (AWS KMS) key encrypts the data in the S3 bucket.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-deploying-amazon-connect-with-infrastructure-as-code-on-aws#)

[Read usage guidelines](/solutions/guidance-disclaimers/)
