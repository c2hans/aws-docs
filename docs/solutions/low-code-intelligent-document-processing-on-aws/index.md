---
source_url: https://docs.aws.amazon.com/solutions/low-code-intelligent-document-processing-on-aws/index.html
---

---
title: 'Guidance for Low Code Intelligent Document Processing on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/low-code-intelligent-document-processing-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Low Code Intelligent Document Processing on AWS

## Overview

This Guidance provides best practices for building and deploying an intelligent document processing (IDP) architecture that scales with workload demands. The code provided automates the creation of machine learning (ML) resources which will reduce developer friction associated with the time-consuming and error-prone tasks of standing up a high-quality IDP environment. This will reduce the time it takes to deliver a proof-of-concept for IDP workflows and help ensure adherence to architectural best practices.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/low-code-intelligent-document-processing-on-aws.pdf)

![Architecture diagram](/images/solutions/low-code-intelligent-document-processing-on-aws/images/low-code-intelligent-document-processing-on-aws-1.png)

1. **Step 1**: Document processing workflows are developed using the AWS Cloud Development Kit (AWS CDK).
1. **Step 2**: AWS CDK generates a stack in AWS CloudFormation that deploys templates for the resources required to execute the workflows.
1. **Step 3**: The CloudFormation template creates an Amazon Simple Storage Service (Amazon S3) bucket where documents are uploaded for processing.
1. **Step 4**: Document uploads trigger an AWS Step Functions workflow to orchestrate document processing functions. Depending on your specific use case, you can choose one or more workflows available in the sample code.
1. **Step 5**: The Step Functions workflow begins with Amazon Textract extracting the text from the document.
1. **Step 6**: An AWS Lambda function processes the output of Amazon Textract and generates a CSV file and key/value pairs of extracted text.
1. **Step 7**: Amazon Comprehend uses the extracted text to classify documents by type. The sample code includes custom classifiers.
1. **Step 8**: Depending on the deployed workflow, Amazon DynamoDB or Amazon Aurora persists the data.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-low-code-intelligent-document-processing-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance comes with a Git repository that contains all the artifacts required to deploy the architecture. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon S3 encrypts your data by default using Amazon S3-managed encryption keys. You may also use AWS Key Management Service (AWS KMS), a managed service that allows you to use your own cryptographic keys to protect your data. Data shared between services in your account never leaves your account. You can use the Amazon Comprehend console or APIs to detect personally identifiable information (PII) in English text documents. With PII detection, you have the choice of locating the PII entities or redacting the PII entities in the text. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The Guidance recommends and has separate AWS CDK components for each Lambda function that can be used as microservices. The serverless, event-driven architecture in addition to retry and exponential back off features make this architecture scalable. The Lambda functions included in the sample code have logging enabled, set with the default mode of "DEBUG.” You can view these logs in Amazon CloudWatch, through which you can also monitor and set alarms for specific log events. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The Guidance deploys a serverless event-driven architecture that scales according to traffic patterns. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance and the associated workshop use AWS Cloud9 to create instances to install Docker and deploy the AWS CDK stacks. We recommend using the cost-saving setting that prompts the environment to auto-hibernate after thirty minutes of no activity. The Step Functions workflow is initiated only when the document is uploaded to a particular Amazon S3 location. The workshop contains an estimate on total cost of execution and has a clean-up section to destroy the deployed stack. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance allows you to maximize your utilization and right-size your implementation by using Step Functions, which only runs when your documents are being processed. This allows you to use resources only when needed and conserve energy consumption of the underlying infrastructure. By using managed services like AWS Textract and Amazon Comprehend, you can operate at scale and share the underlying resources, which allows you to further maximize resource usage. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
