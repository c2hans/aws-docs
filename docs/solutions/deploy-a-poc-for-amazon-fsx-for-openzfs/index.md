---
source_url: https://docs.aws.amazon.com/solutions/deploy-a-poc-for-amazon-fsx-for-openzfs/index.html
---

---
title: 'Deploy a PoC for Amazon FSx for OpenZFS'
canonical_url: https://docs.aws.amazon.com/solutions/deploy-a-poc-for-amazon-fsx-for-openzfs/
source: aws-documentation
generated_on: 2026-09-25
---

# Deploy a PoC for Amazon FSx for OpenZFS

## Overview

This Guidance demonstrates how to set up and test Amazon FSx for OpenZFS in a controlled environment before implementing it in production workloads. The deployment process uses AWS CloudFormation to create essential components including a VPC, an EC2 compute node, and an FSx for OpenZFS file system. The environment can be configured with optional high-availability features for enhanced reliability. You can validate your workload requirements and performance expectations before full-scale implementation.

## Benefits

### Accelerate workload testing

Deploy a ready-to-use proof-of-concept environment for Amazon FSx for OpenZFS in minutes using AWS CloudFormation. This automated deployment allows you to quickly evaluate performance and functionality with your specific workloads without extensive manual configuration.

### Simplify storage evaluation

Test Amazon FSx for OpenZFS capabilities through a pre-configured environment with integrated compute resources and secure access methods. Focus on validating your storage requirements while the template handles infrastructure setup, including VPC configuration and Systems Manager integration.

### Enable high-availability testing

Evaluate both standard and high-availability configurations of Amazon FSx for OpenZFS within the same proof-of-concept environment. This flexibility helps you determine the appropriate resilience level for your production workloads while understanding performance characteristics under different deployment scenarios.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/Deploy%20a%20PoC%20for%20Amazon%20FSx%20for%20OpenZFS.pdf)

![Architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/images/architecture-diagrams/Deploy a PoC for Amazon FSx for OpenZFS.ba307e739eb8a5afd2cd74012ffa8d43f0e20fa8.png)

1. **Step 1**: The user logs into the AWS Management Console and deploys the Proof-of-Concept (PoC) template provided in this Guidance, using AWS CloudFormation to create a new stack.
1. **Step 2**: AWS CloudFormation deploys an Amazon Virtual Private Cloud (VPC).
1. **Step 3**: AWS CloudFormation deploys an Amazon Elastic Compute Cloud Instance (Amazon EC2) compute node. This compute node will be used as part of this Guidance to conduct functional and performance testing with the deployed Amazon FSx for OpenZFS file system.
1. **Step 4**: AWS CloudFormation configures the Amazon EC2 instance with AWS Systems Manager, allowing for Session Manager to be utilized for secure access to the Amazon EC2 instance.
1. **Step 5**: AWS CloudFormation deploys an Amazon FSx for OpenZFS file system.
1. **Step 6**: Optionally, AWS CloudFormation deploys an Amazon FSx for OpenZFS file system in a high-availability configuration.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-deploying-a-poc-on-amazon-fsx-for-openzfs/tree/main)

[Read usage guidelines](/solutions/guidance-disclaimers/)
