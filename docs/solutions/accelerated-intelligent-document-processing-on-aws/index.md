---
source_url: https://docs.aws.amazon.com/solutions/accelerated-intelligent-document-processing-on-aws/index.html
---

---
title: 'Guidance for Accelerated Intelligent Document Processing on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/accelerated-intelligent-document-processing-on-aws/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Accelerated Intelligent Document Processing on AWS

## Overview

This Guidance demonstrates a scalable, serverless approach for automated document processing and information extraction using AWS services, such as Amazon Bedrock Data Automation and Amazon Bedrock foundational models. It combines generative AI and optical character recognition (OCR) to process documents at scale. With this Guidance, organizations gain capabilities such as document classification, information extraction, summarization, and question answering. This helps to streamline document workflows while reducing manual processing time and costs. **Latest features:** Stay current with the latest features and releases for this Guidance in the [CHANGELOG](https://github.com/aws-solutions-library-samples/accelerated-intelligent-document-processing-on-aws/blob/main/CHANGELOG.md) .

## Benefits

### Automate complex document processing workflows

Deploy a scalable, serverless architecture that processes documents intelligently using generative AI models, reducing manual data extraction while maintaining accuracy through automated evaluation against baselines.

### Monitor processing in real time

Track document status through a secure dashboard with real-time updates using AppSync and DynamoDB. Gain immediate visibility into processing metrics while maintaining authentication controls through Amazon Cognito.

### Scale document processing effortlessly

Handle varying document volumes with managed concurrency through DynamoDB and SQS queues. The serverless architecture automatically adjusts resources based on demand, eliminating infrastructure management overhead.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/accelerated-intelligent-document-processing-on-aws.pdf)

![Architecture diagram](/images/solutions/accelerated-intelligent-document-processing-on-aws/images/accelerated-intelligent-document-processing-on-aws-1.png)

1. **Step 1**: Client applications submit PDF documents through either the web interface or directly to the Amazon Simple Storage Service (Amazon S3) input bucket. Amazon EventBridge detects these uploads and invokes the document processing workflow.
1. **Step 2**: AWS Lambda (Queue-Sender function) records document events in the AWS AppSync API for tracking and sends them to an Amazon Simple Queue Service (Amazon SQS) queue for message processing.
1. **Step 3**: The Lambda (Queue-Processor function) retrieves messages from the Amazon SQS queue in batches. It manages workflow concurrency using an Amazon DynamoDB counter and initiates AWS Step Functions implementations for document processing.
1. **Step 4**: The Step Functions workflow orchestrates document processing using Lambda functions. For this pattern, a Lambda function invokes Amazon Bedrock Data Automation processing to perform AI-powered document analysis tasks. Then, Lambda (Process-Results function) handles the output.
1. **Step 5**: Upon workflow completion, Lambda (Evaluation function) automatically compares processing outputs against predefined baseline documents. These are known correct outputs in the Amazon S3 evaluation-baseline bucket. Final results and evaluation reports are stored as JSON files in the Amazon S3 output bucket.
1. **Step 6**: The AWS AppSync API maintains document status in the DynamoDB tracking table and enables real-time status updates through the web interface. The tracker function updates processing metrics and status.
1. **Step 7**: The web interface (GenAI IDP Web UI) is hosted in the Amazon S3 web-app bucket and distributed through Amazon CloudFront. It uses Amazon Cognito for user authentication, enabling you to monitor document processing through a secure dashboard.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/accelerated-intelligent-document-processing-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
