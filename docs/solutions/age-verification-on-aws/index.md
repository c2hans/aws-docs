---
source_url: https://docs.aws.amazon.com/solutions/age-verification-on-aws/index.html
---

---
title: 'Guidance for Age Verification on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/age-verification-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Age Verification on AWS

## Overview

This Guidance helps customers streamline the age verification process when selling age-restricted items. Customers completing age verification for the first time upload a copy of their ID and an image of themselves using their device's built-in camera. AWS services verify that the image taken from the camera matches the ID provided and that the customer meets the minimum age requirement to purchase age-restricted products.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/age-verification-on-aws.pdf)

![Architecture diagram](/images/solutions/age-verification-on-aws/images/age-verification-on-aws-1.png)

1. **Step 1**: Customers access the front end age verification application through AWS Amplify to either register as a new age-verified customer, or to verify their age as an existing user.
1. **Step 2**: Amplify routes the requests to AWS AppSync endpoints.
1. **Step 3**: AWS AppSync uses a service integration to run the relevant AWS Step Functions express state machine.
1. **Step 4**: Customers completing age verification for the first time upload a copy of their ID (such as a driver's license or passport) and an image of themselves (collectively referred to as "ID forms") using their device's built-in camera.
1. **Step 5**: ID forms are routed through AWS Lambda to the Know Your Customer (KYC) Partner platform for ID certification and self image cross-verification. Successfully verified customers have their ID forms pushed to Amazon Simple Storage Service (Amazon S3). Their metadata is pushed to Amazon DynamoDB. Validated self images are indexed in Amazon Rekognition for use in future verification processes.
1. **Step 6**: Exceptions are routed to a queue through AWS AppSync and are verified by a manual approver using the Amplify admin user interface (UI).
1. **Step 7**: Existing customers use their device's built-in camera to provide a facial fingerprint. Amazon Rekognition cross-checks the self image against a collection of verified users using the Amazon Rekognition SearchFacesByImage capability.
1. **Step 8**: If a match is found, the customer is verified. If no match is found, the customer is routed to the new user workflow.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance does not include code artifacts, enabling you to automate development pipelines using AWS Cloud Development Kit (AWS CDK) v2, AWS CloudFormation, and Terraform for fast iteration and consistent deployments. Observability is built-in to the recommended services with process level metrics, logs, and dashboards. Extend these mechanisms to meet your needs, and create alarms in Amazon CloudWatch to inform your on-call team of any issues. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a private connection between Amazon VPC and Amazon Rekognition and keep all the traffic private. By using a restricted execution role and trust policies between services, you can configure the backend Step Functions state machine to limit the access to just the services you need. Extend the security of the backend with AWS WAF, a web application firewall. Secure your frontend application further with fine-grained traffic filtering for unwanted traffic. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The Serverless technologies make all components in this Guidance highly available. All components scale automatically because the Amazon Rekognition limits are configured based on your needs. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Serverless technologies allow you to provision only the exact resources you use. You can test with multiple media types to maximize the performance of Amazon Rekognition. For improved performance for clients, deploy Amazon Rekognition in a multi-region architecture and consider implementing the Amazon Route 53 routing policy to further improve the end-user experience. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The cost of this Guidance is minimized by using serverless technologies and because Amazon Rekognition automatically scales based on demand, ensuring only the minimum resources are required. Storage in Amazon S3 follows a consumption-based pricing model where you pay only for resources you use. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By using managed and serverless services, you can minimize the environmental impact of the backend services. A critical component for sustainability is to maximize the usage of the AWS services such as Amazon Rekognition, as covered in the Performance Efficiency and Cost Optimization pillars. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
