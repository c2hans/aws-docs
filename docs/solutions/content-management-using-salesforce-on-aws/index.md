---
source_url: https://docs.aws.amazon.com/solutions/content-management-using-salesforce-on-aws/index.html
---

---
title: 'Guidance for Content Management Using Salesforce on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/content-management-using-salesforce-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Content Management Using Salesforce on AWS

AI-powered content creation for deeper customer engagement with Salesforce on AWS

## Overview

This Guidance demonstrates how to utilize advanced artificial intelligence (AI) capabilities within your existing Salesforce environment to gain more valuable insights about your customers. It allows you to seamlessly integrate the user-friendly interface of Salesforce with the powerful data storage and processing capabilities of AWS. With this Guidance, you can securely upload any type of document to store on AWS. AWS AI services will then automatically process those documents, converting audio and video to text, creating readable documents from images, extracting key details while redacting personal data, and analyzing visuals. By combining the strength of Salesforce with the advanced AI services of AWS, you can uncover deeper insights into your customers' needs, behaviors, and preferences—all within your existing Salesforce workflows.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/content-management-using-salesforce-on-aws.pdf)

![Architecture diagram](/images/solutions/content-management-using-salesforce-on-aws/images/content-management-using-salesforce-on-aws-1.png)

1. **Step 1**: The Salesforce Lightning Web Component (LWC) runs on the client side. The AWS Lambda function grants Salesforce users read or write permission to Amazon Simple Storage Service (Amazon S3) by exchanging a JSON Web Token (JWT) for AWS Security Token Service (AWS STS) credentials.
1. **Step 2**: The LWC allows Salesforce users to upload media files to an Amazon S3 bucket (Media input).
1. **Step 3**: When a media file is uploaded to an Amazon S3 bucket, an Amazon Simple Notification Service (Amazon SNS) event is invoked. It filters the file's suffix and sends the relevant Amazon SNS topic based on the media type.
1. **Step 4**: For video files, an Amazon SNS topic invokes a Lambda function that runs an Amazon Rekognition video job.
1. **Step 5**: The Lambda function passes the video file to Amazon Rekognition to tag objects within the video asynchronously. Once Amazon Rekognition finishes running, it publishes a notification to the Amazon SNS topic.
1. **Step 6**: Once Amazon Rekognition finishes running, it publishes a notification to the Amazon SNS topic.
1. **Step 7**: Amazon SNS invokes a Lambda function to store the results of the video in the Amazon S3 bucket (Output).
1. **Step 8**: An Amazon SNS topic runs two parallel Lambda functions for image files. Lambda (Image recognition) performs object tagging through Amazon Rekognition. The Lambda function (Metadata extraction) extracts metadata, including location and device details. Both outputs are saved in an Amazon S3 bucket (Output).
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-content-management-using-salesforce-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance implements a modular, agile, and decoupled architecture that aligns with AWS operational best practices. For example, by using Amazon SNS topics, the Guidance can be decoupled, and you can add Lambda functions as needed. Additionally, AWS artificial intelligence (AI) services like Amazon Transcribe and Amazon Rekognition remove the need for you to manage machine learning (ML) models and infrastructure. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

One of the core advantages of serverless architectures is that AWS manages the underlying infrastructure, including network security. This alleviates the burden of securing the network layer, allowing you to focus on securing your application and data. However, you are responsible for managing access control through AWS Identity and Access Management (IAM). By default, data stored in Amazon S3 is encrypted with Amazon S3 managed keys (SSE-S3), but it can also be encrypted using AWS KMS (SSE-KMS) or customer-provided encryption keys (SSE-C). Access to Amazon S3 is denied by default, and all public access is blocked. Amazon S3 access is authorized through IAM, allowing you to define access scope and permitted actions for services or users. Furthermore, this Guidance uses AWS STS in conjunction with a JSON Web Token (JWT) authorizer. This approach enhances security by eliminating the need to store hard-coded AWS access keys in Salesforce, which could potentially be compromised. Instead, Salesforce obtains temporary, limited-privilege IAM credentials from AWS STS, which are used to securely access and interact with Amazon S3. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance implements a highly available network topology by using a serverless architecture that is deployed in a single Region and runs across multiple Availability Zones (AZs). This eliminates the risk caused by a rare, but possible, AZ failure. Application reliability is achieved by decoupling the application into individual components that focus on a single task, and Amazon SNS is essential for decoupling this architecture. If a subscribed endpoint is unavailable temporarily, Amazon SNS will retry delivering the message according to the retry policy. For messages that can't be delivered, Amazon SNS can target messages with a dead-letter queue (DLQ) to prevent message loss. Finally, Amazon CloudWatch monitors Lambda functions, and you can review reports on metrics such as the number of requests, invocation duration, and errors. This helps track the performance and health of the Lambda functions. If a function invocation fails due to an error, it will be automatically retried at least three times. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Decoupling individual services allows each component to work independently and run in parallel. Using a serverless architecture, each Lambda function is provisioned with the right amount of RAM and CPU to perform its task. And using Amazon SNS allows for asynchronous invocation of resources, so once a job is complete, it is not waiting for a synchronous response. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

By using a serverless architecture, you only pay for what you use. Services like Lambda, Amazon SNS, or Amazon Rekognition only incur charges for the times that those services are invoked and used. Services like Amazon S3 incur charges for the amount of data that is actually used. And using serverless services allows the architecture to scale up and down to meet demand without having to overprovision resources. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Through right-sized, transient resources that avoid excess idling, this Guidance minimizes energy consumption and hardware waste. For example, rather than pre-provisioning servers that continually run even when unutilized, Lambda functions are invoked on-demand only when needed. Each function is individually configured with the optimal amount of memory and CPU capacity required to complete its designated task, avoiding over-provisioning of resources. By dynamically allocating just the right compute power when workloads arrive and terminating those resources after use, Lambda eliminates resource waste from idle servers. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
