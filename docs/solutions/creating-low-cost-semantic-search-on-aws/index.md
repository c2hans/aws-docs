---
source_url: https://docs.aws.amazon.com/solutions/creating-low-cost-semantic-search-on-aws/index.html
---

---
title: 'Guidance for Creating Low-Cost Semantic Search on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/creating-low-cost-semantic-search-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Creating Low-Cost Semantic Search on AWS

## Overview

This Guidance demonstrates how you can implement cost-effective retrieval-augmented generation (RAG) solutions for your AI needs. It provides practical tools and methodologies for creating accessible, small-scale RAG implementations that remain effective without the high costs typically associated with vector database solutions. Making advanced AI techniques more accessible, this approach will enable your small business to personalize generative AI applications and use AI capabilities within budget constraints.

## Benefits

### Deploy AI-powered search while saving on costs

Implement a retrieval-augmented generation solution capabilities using DynamoDB as a cost-effective vector store, eliminating the need for expensive dedicated vector databases while maintaining performance for small to medium workloads.

### Enhance decision-making with contextual AI

Empower your applications with intelligent document understanding and semantic search capabilities. Improve user experiences by providing relevant, context-aware responses based on your organization's specific knowledge base.

### Accelerate AI adoption for small businesses

Quickly implement advanced AI techniques using pre-built workflows and managed services. Focus on creating value from your data while AWS handles the underlying infrastructure and AI model management.

## How it works

### Document ingestion and vectorization flow

This architecture diagram shows how to effectively create a low-cost vector store using Amazon DynamoDB. It shows the key components and their interactions, providing an overview of the architecture’s structure and functionality. This diagram illustrates document ingestion and vectorization flow.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/creating-low-cost-semantic-search-on-aws.pdf)Step 1A user accesses the document upload portal through Amazon CloudFront, while AWS WAF protects against malicious traffic and common web exploits.Step 2Amazon Simple Storage Service (Amazon S3) serves the web portal's static files (HTML, CSS, and JavaScript). Amazon Cognito simultaneously handles user authentication and access management.Step 3Amazon API Gateway securely receives document uploads from the user and routes them to Amazon S3 for encrypted storage.Step 4When a new document is uploaded to Amazon S3, it automatically invokes an AWS Step Functions workflow to begin the data ingestion process.Step 5Depending on the document type, a user has two options for document processing: Amazon Textract for text extraction and parsing or Amazon Bedrock for advanced document understanding. Once processed, the documents are stored in Amazon S3. Subsequently, an AWS Lambda function performs two key operations:Step 5aText Chunking: This operation segments the text into smaller chunks, with a user-configurable default size.Step 5bEmbedding Generation: This operation creates vector embeddings for each chunk by using Amazon Titan Embeddings through the Amazon Bedrock API.Step 6The system stores document vectors in Amazon DynamoDB tables with separate tables for different chunk sizes to optimize retrieval performance.### Inference flow

This architecture diagram shows how to effectively create a low-cost vector store using Amazon DynamoDB. It shows the key components and their interactions, providing an overview of the architecture’s structure and functionality. This diagram illustrates inference flow.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/creating-low-cost-semantic-search-on-aws.pdf)Step 1A user accesses the management portal through CloudFront, which enables them to do the following:Step 1aAdjust document processing settings (such as chunk sizes and processing models).Step 1bEvaluate and test the chat interface's performance.Step 2API Gateway routes the user's prompt to a Lambda function for processing.Step 3The inference processes the user's prompt by converting it to vectors using an Amazon Titan Embeddings model. This model stores the conversation history in DynamoDB for context retention. Simultaneously, a Lambda function performs the following:Step 3aIt retrieves all vectors associated with the Amazon Cognito user from DynamoDB.Step 3bIt performs a context similarity search using inverse cosine similarity.Step 3cIt uses the most relevant text chunks as context for the generative AI model.Step 4Amazon Bedrock uses Claude 3 Haiku to process the user's prompt alongside contextually relevant vectors. It then generates and delivers the response to the user through the chat interface.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-low-cost-semantic-search-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
