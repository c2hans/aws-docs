---
source_url: https://docs.aws.amazon.com/solutions/digital-user-onboarding-in-financial-services-on-aws/index.html
---

---
title: 'Guidance for Digital User Onboarding in Financial Services on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/digital-user-onboarding-in-financial-services-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for Digital User Onboarding in Financial Services on AWS

## Overview

This Guidance helps automate and deliver a seamless digital user onboarding process for financial institutions that enable users to open a bank account in a matter of minutes rather than days.

## How it works

Use this reference architecture for building a digital onboarding platform on AWS using AI/ML and cloud-native services.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/digital-user-onboarding-in-financial-services-on-aws.pdf)

![Architecture diagram](/images/solutions/digital-user-onboarding-in-financial-services-on-aws/images/digital-user-onboarding-in-financial-services-on-aws-1.png)

1. **Step 1**: The user begins the onboarding process with the onboarding application. The user provides various documents (including drivers license) as part of the Know Your Customer (KYC) process.
1. **Step 2**: Once the documents are uploaded, they are automatically processed using various artificial intelligence/machine learning (AI/ML) services.
1. **Step 3**: Amazon Rekognition performs user verification and compares the user's selfie with the picture in a valid document.
1. **Step 4**: Amazon Textract extracts text information from all of the uploaded documents (Optical Character Recognition (OCR)).
1. **Step 5**: The user is requested to upload any missing documents or provided status updates using Amazon Simple Email Service (Amazon SES) or Amazon Simple Notification Service (Amazon SNS).
1. **Step 6**: Once all of the documents are uploaded, the identity of the user is verified using Department of Motor Vehicles (DMV) verification, and necessary due diligence is performed (a sanctions list and so on).
1. **Step 7**: API integration to other third-party sources of data is done at this layer: sanctions/ politically exposed person (PEP)/adverse media.
1. **Step 8**: Third-party data is consumed through AWS Data Exchange for checks against the user.
1. **Step 9**: All of the data that the user provided is stored away for long-term retention in Amazon Simple Storage Service Glacier (Amazon S3).
1. **Step 10**: The user is notified of successful account creation once the identity is verified and the due diligence performed.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This architecture is built using native AWS services that integrate with Amazon CloudTrail and Amazon CloudWatch for monitoring, logging, and auditing purposes. With the use of fully managed services, it becomes easy to manage the workload, as AWS takes care of the operational aspects of the services. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

With fully managed services, AWS manages the security aspects of the hosting and management of the services, while customers need only to use the services securely. Managed services also offer better integration with logging and monitoring services such as CloudWatch and CloudTrail, leading to better auditability. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Services such as Amazon Textract and Amazon Rekognition are fully managed services, and inherently reliable, because AWS manages the scalability of the services. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The use of fully managed services makes it easy for customers to try out various patterns that meet their performance requirements. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The use of managed services lets the customer build a platform that scales with the growing business needs. With this option, the customer pays only for what they use, and don’t have to worry about long term investments. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Using native AWS services and serverless technologies (Amazon Textract, Amazon Rekognition, Amazon API Gateway, Amazon S3, Amazon DynamoDB, and so on) helps build a platform that scales with growth in business, so the customer doesn’t need to build and keep over-provisioned resources. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
