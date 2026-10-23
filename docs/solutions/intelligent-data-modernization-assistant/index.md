---
source_url: https://docs.aws.amazon.com/solutions/intelligent-data-modernization-assistant/index.html
---

---
title: 'Guidance for Intelligent Data Modernization Assistant on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/intelligent-data-modernization-assistant/
source: aws-documentation
generated_on: 2026-10-22
---

# Guidance for Intelligent Data Modernization Assistant on AWS

## Overview

This Guidance demonstrates how to accelerate database migration to AWS with an AI-powered assistant that generates tailored migration patterns and prescriptive strategies. It uses retrieval augmented generation with Amazon Bedrock Knowledge Bases and Amazon Titan embeddings to analyze your database environment and industry requirements, then recommends optimized migration approaches with step-by-step guidance across a wide array of database types. By grounding recommendations in curated migration documents, it helps you avoid common pitfalls around legacy compatibility, security, and cost. Solution architects and consultants interact through a chat interface, reducing migration timelines and project costs while improving outcomes throughout the modernization journey.

## Benefits

### Accelerate migration planning

Generate tailored migration patterns and prescriptive strategies on demand instead of manual assessments, so solution architects move from database analysis to an actionable plan in minutes. This shortens migration timelines and frees experts to focus on execution rather than research.

### Ground strategies in trusted content

Retrieve answers from curated migration documents with Amazon Bedrock Knowledge Bases and Amazon Titan embeddings, so recommendations reflect proven patterns across a wide array of database types. This retrieval augmented approach reduces the risk of incorrect strategies that lead to delays and budget overruns.

### Keep processing private and secure

Run backend functions inside Amazon VPC private subnets with private connectivity to Amazon S3, and secure the API with key-based access. Monitor activity through Amazon CloudWatch, giving teams a controlled, observable environment for handling sensitive database information.

## How it works

This architecture diagram illustrates how to build and operate Intelligent Data Modernization Assistant on AWS. It shows the key components and their interactions. [Download the architecture diagram](downloads/intelligent-data-modernization-assistant.pdf)

![Architecture diagram for Intelligent Data Modernization Assistant](/images/solutions/intelligent-data-modernization-assistant/images/intelligent-data-modernization-assistant.png)

1. **Step 1**: Solution architects and consultants access the Intelligent Data Migration Assistant (IDMA) Chatbot application on AWS Amplify, which serves the React-based frontend UI.
1. **Step 2**: The IDMA Chatbot sends requests through HTTPS to Amazon API Gateway (REST API secured with API Key) for backend processing.
1. **Step 3**: API Gateway routes requests to AWS Lambda functions (bot-handler, database-migration, analytics, modern-strategy) running inside Amazon Virtual Private Cloud (VPC) private subnets based on the API endpoint path.
1. **Step 4**: Lambda functions invoke Amazon Bedrock Knowledge Base using the RAG (Retrieve and Generate) pattern to query curated migration documents and generate AI-powered responses.
1. **Step 5**: Bedrock Knowledge Base uses Amazon Titan Embed v2 (Foundation Model) to convert queries into vector embeddings and performs similarity search against Amazon OpenSearch Serverless to retrieve relevant document context.
1. **Step 6**: A dedicated Lambda (CloudFormation custom resource) creates the KNN vector index schema in OpenSearch Serverless, which Amazon Bedrock Knowledge Base uses to store and query vector embeddings.
1. **Step 7**: Lambda functions access Amazon Simple Storage Service (Amazon S3) bucket via the S3 Gateway Endpoint within the VPC for secure, private connectivity.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-intelligent-data-modernization-assistant-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
