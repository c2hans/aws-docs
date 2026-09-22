---
source_url: https://docs.aws.amazon.com/solutions/american-sign-language-3d-avatar-translator-on-aws/index.html
---

---
title: 'Guidance for American Sign Language (ASL) 3D Avatar Translator on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/american-sign-language-3d-avatar-translator-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for American Sign Language (ASL) 3D Avatar Translator on AWS

Translate multiple languages into American Sign Language (ASL) with an avatar-based translator

## Overview

This Guidance demonstrates how to build an application that provides multimodal, high-fidelity translations from over 100 spoken languages into ASL through a realistic avatar. It uses generative artificial intelligence (AI) to transcribe and simplify input phrases from any supported language. Each simplified English phrase is then interpreted, rearranged, and translated directly into ASL. The application also generates a background image from Stable Diffusion to visually portray the input phrase.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/american-sign-language-3d-avatar-translator-on-aws.pdf)

![Architecture diagram](/images/solutions/american-sign-language-3d-avatar-translator-on-aws/images/american-sign-language-3d-avatar-translator-on-aws-1.png)

1. **Step 1**: User authenticates to Amazon Cognito using an Amazon CloudFront-hosted website or web API (through Amazon Cognito-based JWT access token).
1. **Step 2**: User types or speaks an input phrase in a chosen language, which Amazon Transcribe transcribes. Transcription is stored in an Amazon Simple Storage Service (Amazon S3) bucket.
1. **Step 3**: User requests an action (like ASL translate, change avatar, or change background image) through the website or web API (Amazon API Gateway endpoint).
1. **Step 4**: Based on the user-requested action, API Gateway routes its request to a corresponding AWS Lambda function for processing that action.
1. **Step 5**: For ASL Translation requests, a matching Lambda function invokes Amazon Bedrock to form an ASL phrase for the provided input phrase and to obtain a contextual 2D image (to be stored in an S3 bucket).
1. **Step 6**: Amazon Comprehend and Amazon Bedrock perform multi-lingual toxicity checks on the input phrase. Amazon Rekognition performs visual toxicity checks on 2D-generated images. Toxicity check results are returned to respective Lambda functions.
1. **Step 7**: All Lambda functions generate a JSON-based payload to capture a user-requested action for Epic Games Unreal Engine. Each payload is sent to a corresponding Amazon Simple Notification Service (Amazon SNS) topic: Translation and Non-Translation.
1. **Step 8**: Each Amazon SNS-based payload is transmitted to its corresponding Amazon Simple Queue Service (Amazon SQS) queue for later consumption by Unreal Engine.
1. **Step 9**: Using the AWS SDK, the Unreal Engine application polls and dequeues Amazon SQS action-based payloads from its queues. Background images are fetched from an S3 bucket for translation requests.
1. **Step 10**: Based on each payload received, the Unreal Engine application performs a user-requested action and displays resulting video output on that user's system. This output provides an ASL-equivalent interpretation of an input phrase by displaying a MetaHuman 3D avatar animation with ASL-transformed text displayed.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/ai-ml/american-sign-language-3d-avatar-translator-on-aws.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-american-sign-language-3d-avatar-translator-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The AWS Cloud Development Kit (AWS CDK) and AWS CloudFormation stack output provide insights into the current deployment state. Amazon CloudWatch logs enable operational analysis and visibility into the workload. GitLab facilitates source code management, and the AWS CDK deploys changes to the AWS Cloud. Infrastructure can be re-provisioned through AWS CDK in case of failure and can be undeployed or redeployed as a unit using CloudFormation. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Identity and Access Management (IAM) roles and policies, Amazon Cognito -based authentication, and an API Gateway endpoint protect and manage resources. Amazon Cognito restricts access to a specific user pool, with access tokens expiring after one hour. The API Gateway endpoint provides encrypted web API access to specific paths and services, enforcing policies and API authorization. All AWS services use IAM for authentication and authorization, leveraging IAM roles for short-term credentials. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The resilience of serverless services underpins the architecture. Lambda decouples low-level input processing from the Unreal Engine sample application's presentation layer. API Gateway throttles requests, queuing them in Amazon SQS. The Unreal Engine sample application retries failed AWS SDK operations, such as dequeuing from Amazon SQS. Standard CloudWatch logs and metrics store informational messages, error conditions, and enable notifications of errors. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon CloudFront caches web page data at edge locations, scaling based on traffic. API Gateway throttling mechanisms (such as steady-state rate and burst request limits) manage API requests. For Amazon S3, edge locations (such as Transfer Acceleration) decrease latency. Adjusting provisioned throughput from Amazon Bedrock optimizes performance. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Serverless AWS services allow you to run code without provisioning or managing servers, paying only for specific on-demand usage. Costs scale according to the number of ASL translation requests, the amount of words translated into ASL in each request, and the quantity of sentence simplification operations. The serverless architecture avoids persistent AWS resources beyond S3 buckets when the overall solution is inactive. CloudFront's caching reduces requests to the web interface origin server hosted on Amazon S3. As ASL translation requests scale, Amazon SQS queues these requests as needed for later consumption. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Resource utilization scales on demand according to the number of ASL translation requests, the quantity of words translated into ASL in each request, and the amount of sentence simplification operations. The serverless architecture reduces the overall utilization and energy consumption footprint, eliminating the need to provision and manage servers or physical machines. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
