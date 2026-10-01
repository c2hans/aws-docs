---
source_url: https://docs.aws.amazon.com/solutions/self-healing-code-on-aws/index.html
---

---
title: 'Guidance for Self-Healing Code on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/self-healing-code-on-aws/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Self-Healing Code on AWS

## Overview

This Guidance helps software companies set up a system to detect error logs, generate bug fixes, and create pull requests. Any company that creates software inevitably has to balance addressing bugs while also competing with product and feature development pressure. Bugs can distract developers' focus, degrade the user experience, and cause misleading metrics. This Guidance helps software companies implement an automated system that detects and fixes bugs to enhance application reliability and improve the overall customer experience.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/self-healing-code-on-aws.pdf)

![Architecture diagram](/images/solutions/self-healing-code-on-aws/images/self-healing-code-on-aws-1.png)

1. **Step 1**: The AWS Lambda Error Logs Processor function receives application error logs through an Amazon CloudWatch logs subscription and filter, which matches only Python stack traces. All Lambda functions assume an AWS Identity and Access Management (IAM) role scoped with minimum permissions to access the required resources.
1. **Step 2**: The stack trace in the application error log is md5-hashed for uniqueness and stored in an Amazon DynamoDB table to track its processing state. Each item in the table represents a deduplicated error message.
1. **Step 3**: The Lambda Event Processor function obtains events from the DynamoDB stream and sends them to Amazon Simple Queue Service (Amazon SQS) for batch processing.
1. **Step 4**: Amazon SQS enqueues messages to enable batch processing and concurrency control for the Lambda Code Optimizer function.
1. **Step 5**: The Lambda Code Optimizer function builds a prompt that includes source code and the relevant error message. The SSH key to access the Git repository is retrieved from Parameter Store, a capability of AWS Systems Manager. It invokes Amazon Bedrock with the prompt, which returns modified source code as a response. Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models (FMs) through a single API, along with a broad set of capabilities you need to build generative AI applications.
1. **Step 6**: The Lambda Code Optimizer function commits the modified source code into a new Git branch. The Git branch and its corresponding pull request are pushed to the source control system through the GitHub API.
1. **Step 7**: Git users review the pull request for testing and integration.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: A detailed guide is provided to experiment and use within your AWS account. Each stage of building the Guidance, including deployment, usage, and cleanup, is examined to prepare it for deployment. The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open implementation guide](https://aws-solutions-library-samples.github.io/ai-ml/self-healing-code-on-aws.html)
[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-self-healing-code-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

The CloudWatch logs subscription pre-filters application error logs and automatically invokes a Lambda function for further processing to remediate the error. CloudWatch and Lambda can help with the automatic detection and triaging of application errors. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Secrets are stored in Parameter Store with encryption enabled and can only be read by users or roles with explicit permissions. By storing secrets in Parameter Store, you can create fine-grained permissions per parameter. All IAM policies are scoped down to minimum permissions required for the services and integrations. Encryption on the parameters also aids in obscuring the values of the secrets in the AWS console. Scoped IAM policies help ensure that the blast radius of each IAM role is scoped to its bare minimum. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Lambda, DynamoDB, and Amazon SQS are managed services which offer automatic scalability and reliability across multiple Availability Zones (AZs). Lambda offers serverless computing for code focus and provides a stateless compute layer. DynamoDB is a fully managed NoSQL database with backups and replication and offers native backup and restore capabilities. Amazon SQS helps ensure message delivery in distributed systems through loose coupling between services, which reduces chances for system failure. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Lambda is highly scalable and can enable parallel processing of items. DynamoDB has a stateless API layer and shared storage layer which allows virtually limitless storage and throughput. DynamoDB Streams also allows efficient event-driven processing of item updates for downstream constructs. Amazon Bedrock handles all infrastructure management and scaling of models. The combination of DynamoDB, DynamoDB Streams, Amazon Bedrock, and Lambda allows you to efficiently scale your database, react to data changes in near real time, and process events on-demand without the overhead of server management. This is particularly important for this system, where the rate of invocations can be inconsistent or erratic. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Lambda, DynamoDB, Amazon SQS, and Amazon Bedrock are all serverless services which are charged on usage, rather than incurring static costs. This system will potentially have an inconsistent rate of invocations, with frequent periods of no activity. Serverless services allow efficient use of on-demand resources and only generate costs during invocation of the system. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

CloudWatch, Lambda, DynamoDB, Amazon SQS, and Amazon Bedrock are all serverless services which do not require statically provisioned servers and do not consume resources during periods of inactivity. Serverless services allow efficient use of on-demand resources, which get de-provisioned automatically when no longer used to reduce your overall resource footprint. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
