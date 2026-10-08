---
source_url: https://docs.aws.amazon.com/solutions/generating-support-case-insights-on-aws/index.html
---

---
title: 'Guidance for Generating Support Case Insights on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/generating-support-case-insights-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Generating Support Case Insights on AWS

## Overview

This Guidance demonstrates how to address the challenge of inaccurate numerical analysis in traditional RAG-based analytics by combining semantic search with structured data querying to deliver deterministic, reliable insights for AWS Support cases. The implementation uses AI Agents built on the Strands Agents SDK, running on a serverless architecture, to process user queries through a REST API or web interface, automatically collecting and analyzing support case data from multiple AWS accounts. Amazon Bedrock Knowledge Bases provides managed RAG capabilities while Amazon Athena handles precise aggregations, creating a comprehensive approach to support case insights without complex custom integrations. You gain more accurate and actionable insights from support cases data, improving your operational decision-making and incident response capabilities.

## Benefits

### Accelerate support issue resolution

Reduce time spent analyzing AWS Support cases by using AI-powered search to surface relevant patterns and actionable insights from your case history in near real-time.

### Automate your support data pipeline

Eliminate manual case review with scheduled, serverless data collection and processing that continuously keeps your knowledge base current across all linked AWS accounts.

### Query support cases conversationally

Empower your teams to ask natural language questions and receive accurate, contextual answers drawn from your organization's AWS Support history using retrieval-augmented generation.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/generating-support-case-insights-on-aws.pdf)

![Architecture diagram](/images/solutions/generating-support-case-insights-on-aws/images/generating-support-case-insights-on-aws-1.png)

1. **Step 1**: Submit a query through the client UI to explore insights from their AWS Support cases.
1. **Step 2**: Amazon API Gateway authenticates the request and forwards it to an AWS Lambda function for processing.
1. **Step 3**: The AWS Lambda function implements AI agents using the Strands Agents SDK (an open-source framework for building autonomous AI agents), case-aggregation workflows, and the Amazon Bedrock Knowledge Bases to retrieve and interpret information related to the submitted query.
1. **Step 4**: Amazon Bedrock, a fully managed service, provides secure LLM inference with built-in privacy controls and responsible AI features to generate final responses based on support case data.
1. **Step 5**: Strands Agents Case Aggregation tool query Amazon Athena to get the case metadata.
1. **Step 6**: Strands Agents Knowledge Base tool query Amazon Bedrock Knowledge Base and return response. Amazon Bedrock Knowledge Bases provides fully managed Retrieval Augmented Generation (RAG) capabilities, automatically retrieving relevant support case information to enhance the accuracy and relevance of AI-generated responses without requiring custom integrations or data flow management.
1. **Step 7**: Amazon EventBridge triggers a Lambda function on a scheduled interval to collect the latest support cases from AWS accounts.
1. **Step 8**: AWS Lambda function trigger AWS Support API.
1. **Step 9**: AWS Support API collect support cases from the linked AWS accounts.
1. **Step 10**: AWS Lambda function store the retrieved support cases data in Amazon S3.
1. **Step 11**: The data pipeline Lambda function processes new support case data in Amazon S3, converts it into vector embeddings, and refreshes the Amazon Bedrock Knowledge Bases on a scheduled cadence or when triggered by Amazon S3 events to ensure up-to-date information retrieval.
1. **Step 12**: The data pipeline updates the support case metadata on a scheduled cadence or when triggered by Amazon S3 events.
1. **Step 13**: The support cases and metadata source to refresh the knowledge base and metadata are stored in Amazon S3 bucket.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-generating-support-case-insights-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
