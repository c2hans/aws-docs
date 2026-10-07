---
source_url: https://docs.aws.amazon.com/solutions/rapidly-deploying-generative-ai-for-business-use-cases-on-aws/index.html
---

---
title: 'Guidance for Rapidly Deploying Generative AI for Business Use Cases on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/rapidly-deploying-generative-ai-for-business-use-cases-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Rapidly Deploying Generative AI for Business Use Cases on AWS

## Overview

This Guidance demonstrates how to build and deploy comprehensive generative AI applications on AWS using a complete enterprise architecture. It shows organizations how to integrate security, content delivery, and authentication services with powerful artificial intelligence and serverless computing capabilities. The solution helps teams implement secure, high-performance AI applications by combining robust frontend security controls with flexible backend processing and storage solutions. By incorporating optional components for intelligent search and knowledge retrieval, alongside comprehensive monitoring and scaling capabilities, this guidance enables organizations to create sophisticated AI solutions that meet enterprise requirements for security, performance, and reliability.

## Benefits

### Accelerate AI solution delivery

Deploy production-ready generative AI applications in days instead of months. Leverage pre-configured components with AWS managed services to reduce development cycles while maintaining enterprise-grade security and scalability.

### Enhance knowledge discovery capabilities

Transform how employees access organizational knowledge with intelligent search and retrieval. Combine Amazon Bedrock and Kendra to create context-aware responses that improve decision-making and reduce time spent searching for information.

### Scale AI experiences securely

Build customer-facing AI applications that automatically adjust to demand without performance degradation. Implement comprehensive security controls at every layer while focusing on creating differentiated user experiences rather than infrastructure management.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/rapidly-deploying-generative-ai-for-business-use-cases-on-aws.pdf)

![Architecture diagram](/images/solutions/rapidly-deploying-generative-ai-for-business-use-cases-on-aws/images/rapidly-deploying-generative-ai-for-business-use-cases-on-aws-1.png)

1. **Step 1**: Users access the application through a browser, where AWS Web Application Firewall (AWS WAF) provides security at multiple entry points.
1. **Step 2**: Serve static content through Amazon CloudFront and store in Amazon Simple Storage Service (Amazon S3), while maintaining chat history in Amazon DynamoDB.
1. **Step 3**: Amazon API Gateway handles API requests and integrates with AWS Lambda functions for backend processing.
1. **Step 4**: Manage user authentication through Amazon Cognito, providing secure access control.
1. **Step 5**: [Optional] The RAG (Retrieval Augmented Generation) system can use Amazon Kendra for intelligent search, with documents stored in Amazon S3.
1. **Step 6**: [Optional] Amazon Bedrock can provide fully managed RAG functionality to power the knowledge base component, working with Amazon OpenSearch Service for efficient data retrieval.
1. **Step 7**: Amazon SageMaker AI and Amazon Bedrock process queries, with results handled by AWS Lambda functions.
1. **Step 8**: [Optional] Administrators can monitor the system through the AWS Management Console and Amazon CloudWatch Dashboard.
1. **Step 9**: Amazon Transcribe processes audio content when required.
1. **Step 10**: [Optional] Enable the Search Agent using Amazon Bedrock and AWS Lambda, providing enhanced search capabilities when specified in the deployment parameters.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-samples/generative-ai-use-cases)

[Read usage guidelines](/solutions/guidance-disclaimers/)
