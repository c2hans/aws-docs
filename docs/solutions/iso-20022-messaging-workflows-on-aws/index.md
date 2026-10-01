---
source_url: https://docs.aws.amazon.com/solutions/iso-20022-messaging-workflows-on-aws/index.html
---

---
title: 'Guidance for ISO 20022 Messaging Workflows on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/iso-20022-messaging-workflows-on-aws/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for ISO 20022 Messaging Workflows on AWS

Modernize payment processes with an event-driven architecture

## Overview

This Guidance demonstrates how payment operators can deploy an event-driven architecture to receive, consume, and release ISO 20022 payment messages. Customers can benefit from a multi-Region architecture, tunable consistency, and with the decision-making process managed by API consumers. This allows for the acceptance, rejection, cancellation, and redrive of data processing workflows, with failover across AWS Regions. Payment operators can deploy this Guidance as a proxy in front of their existing payment infrastructure, on-premises, in the cloud, or use it as the foundational building block to modernize payment processes.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/iso-20022-messaging-workflows-on-aws.pdf)

![Architecture diagram](/images/solutions/iso-20022-messaging-workflows-on-aws/images/iso-20022-messaging-workflows-on-aws-1.png)

1. **Step 1**: API consumer calls the regional AUTH endpoint associated with a Region-specific Amazon Cognito client ID and client secret. It receives OAuth 2.0 access token (to be used with all subsequent API requests).
1. **Step 2**: API consumer calls the Regional API endpoint associated with the Transaction Microservice Architecture (MSA), and receives HTTP 200 with response payload. It includes a transaction ID (to be used with all subsequent API requests).
1. **Step 3**: Transaction MSA generates universally unique identifier version 4 (UUID4). It verifies if it's unique within the current partition in Amazon DynamoDB (transaction table). It records in DynamoDB (status = ACCP); otherwise, it retries up to 3 times.
1. **Step 4**: API consumer calls Regional API endpoint associated with Incoming Queue. It passes transaction ID as HTTP header, and ISO 20022 incoming message as HTTP body (this step starts internal event-driven workflow).
1. **Step 5**: Incoming MSA consumes ISO 20022 message from Incoming Queue, and stores it into an Amazon Simple Storage Service (Amazon S3) bucket (incoming path). It records the step in DynamoDB (status = ACTC), and pushes the incoming message to the Processing Queue.
1. **Step 6**: Processing MSA consumes ISO 20022 message from Processing Queue. It runs technical and business validations, including sync calls to other MSA's. Some examples are: Federal Information Processing Standards (FIPS-104-2), Know Your Customer (KYC), Anti-Money Laundering (AML), Fraud, and liquidity records. It records the step in DynamoDB (status = ACSP or RJCT) and pushes an ISO 20022 confirmation or rejection message to the Releasing Queue.
1. **Step 7**: Releasing MSA consumes ISO 20022 message from Releasing Queue, stores it into an Amazon S3 bucket (outgoing path), records step in DynamoDB (status = ACSC or RJCT), and pushes notification to Amazon Simple Notification Service (Amazon SNS).
1. **Step 8**: API consumer calls the Regional API endpoint associated with Outgoing MSA, and receives HTTP 200 with ISO 20022 outgoing message as response payload.
1. **Step 9**: Timeout MSA invokes every 15 seconds to retrieve any transaction that exceeds service level agreement (SLA). It generates rejection ISO 20022 message, stores it in Amazon S3 (outgoing path), and records new step in DynamoDB (status = RJCT).
1. **Step 10**: OPTIONALLY, for on-premises downstream systems leveraging existing messaging capabilities (for example IBM MQ, or Kafka), deploy the same tool in the AWS Cloud and use the native replication between on-premises and the Cloud.
1. **Step 11**: Messaging Queue (MQ) Reader MSA consumes messages from cloud-based MQ and submits them to the Incoming API (see the preceding Steps 1 through 5).
1. **Step 12**: MQ Writer MSA consumes messages from Outgoing API, and pushes them to cloud based MQ (see the preceding Steps 1, 2, and 9).
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-iso20022-messaging-workflows-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses ready to deploy capabilities to monitor and observe your application's state and its business outcomes, it can be integrated through APIs, and deployed through infrastructure as code (IaC) of your choice. Amazon Elastic Container Registry (Amazon ECR) can store app-level code, and AWS Lambda can be deployed using continuous integration and continuous delivery (CI/CD) pipelines of your choice. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance requires encryption in transit and at rest. API and AUTH endpoints have SSL/TSL enabled, and data stores such as Amazon S3, DynamoDB, Amazon Simple Queue Service (Amazon SQS), and Amazon SNS support encryption at rest using AWS Key Management Service (AWS KMS). AWS resources are protected through AWS Identity and Access Management (IAM), while Amazon API Gateway resources are protected through Cognito and 0Autho 2.0. Sensitive information, such as IDs, is stored using AWS Secrets Manager. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance supports reliability testing and implements Amazon S3 as a default backup and restore mechanism. Additionally, the transaction API verifies that each transaction ID is unique, First-In-First-Out (FIFO) queues verify that messages are processed in order and only once, and the Recovering API checks for Region failures and provides self-healing capabilities. AWS CloudWatch and AWS CloudTrail provide ready to deploy logs and default metrics, and you can choose an active-passive or an active-active architecture, depending on your requirements. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses serverless services, such as Lambda, Amazon Elastic Kubernetes Service (Amazon EKS), DynamoDB, and Amazon SQS, making it easier to scale and to monitor traffic and data access patterns. Additionally, you can submit ISO 20022 messages through APIs, observe experiment results through AWS monitoring and observability capabilities, and use the data in the AWS data services to further optimize your systems. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance was built following Event-Driven Architecture (EDA) guidelines and best practices and uses serverless services that scale automatically with demand, so you only pay for the resources you actively use. You can also choose single-region or multi-region rates, depending on your requirements. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

With serverless services, this Guidance makes it easier for you to scale and to maintain consistent high usage of deployed resources, minimizing the need for hardware and verifying that you will use only the minimum resources required. This Guidance also supports data access and storage patterns with services such as Amazon DynamoDB, Amazon SQS, Amazon SNS, and Amazon S3. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
