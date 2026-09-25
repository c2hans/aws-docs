---
source_url: https://docs.aws.amazon.com/solutions/identity-verification-on-aws/index.html
---

---
title: 'Guidance for Identity Verification on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/identity-verification-on-aws/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for Identity Verification on AWS

## Overview

This Guidance demonstrates how you can mitigate fraudulent attacks and minimize onboarding friction for legitimate customers through a streamlined facial identity-based authentication user interface.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/guidance-for-identity-verification-on-aws-ra.pdf)

![Architecture diagram](/images/solutions/identity-verification-on-aws/images/identity-verification-on-aws-1.png)

1. **Step 1**: Users access the front-end web portal hosted within the AWS Amplify and submit a selfie image and/or a valid ID card.
1. **Step 2**: AWS Amplify routes the request to endpoints hosted in Amazon API Gateway
1. **Step 3**: Amazon API Gateway invokes AWS Lambda functions to start analysis of submitted image
1. **Step 4**: User registration and verification is built on AWS Step Functions to invoke Amazon Rekognition and Amazon Textract, which uses machine learning (ML) to understand the context of identity documents such as U.S. passports and driver's licenses without the need for templates or configuration.
1. **Step 5**: Analysis of user submitted image is performed by Amazon Rekognition.
1. **Step 6**: When user submits an ID card for registration, user information is extracted using Amazon Textract.
1. **Step 7**: This information is stored in Amazon DynamoDB.
1. **Step 8**: Verification status is returned to the front-end web portal.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-samples/aws-ai-intelligent-document-processing)
[Go to readme](https://github.com/aws-samples/rekognition-identity-verification#readme)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The guidance doesn’t include any code artifacts. You can automate development pipelines using AWS Cloud Development Kit (AWS CDK) v2, AWS CloudFormation, and Terraform to enable fast iteration and consistent deployments. Observability is built in to the recommended services with process level metrics, logs, and dashboards. Extend these mechanisms to your needs, and create alarms in Amazon CloudWatch to inform your on-call team on any issues. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The serverless backend is protected with AWS Identity and Access Management (IAM)-based authentication for secure validation of the user’s guest identity. You can also deploy Amazon Cognito or another trusted identity provider (IdP) to protect client-server communication. You can define a VPC interface endpoint to securely access Amazon Rekognition and Amazon Textract by keeping all the traffic private in your VPC. The backend Amazon Step Functions state machine can be configured to only have access to the services they need by using restricted execution role and trust policies between services. You can extend the security of the backend by introducing AWS WAF, and you can secure your frontend application further with more fine-grained traffic filtering for unwanted traffic. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

By using serverless technologies, all the components are highly available. All components scale automatically because the limits for the Amazon Rekognition and Amazon Textract are configured to your scaling needs. To further increase reliability, consider implementing a disaster recovery plan for your solution by initiating cross-region failover using Amazon Route 53 for the whole infrastructure. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

By using serverless technologies, you only provision the exact resources you use. To maximize the performance of Amazon Rekognition, test with multiple media types. For improved performance for clients, deploy Amazon Rekognition and Amazon Textract in a multi-region architecture and consider implementing Route 53 routing policy to improve the end user experience. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

By using serverless technologies and automatically scaling Amazon Rekognition and Amazon Textract, you only pay for the resources you use. To further optimize cost, perform a content validation before sending to Amazon Rekognition and Amazon Textract. You can get visibility of the cost of the services using AWS Budgets to track your spending and get alerts when you exceed your budget. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By using managed and serverless services, you can minimize the environmental impact of the backend services. A critical component for sustainability is to maximize the usage of the AWS Rekognition and Amazon Textract services, as covered in the Performance Efficiency and Cost Optimization pillars. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
