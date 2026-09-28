---
source_url: https://docs.aws.amazon.com/solutions/generative-ai-assistant-on-aws/index.html
---

---
title: 'Guidance for Generative AI Assistant on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/generative-ai-assistant-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Generative AI Assistant on AWS

## Overview

This Guidance shows how to unlock instant insights with a generative AI assistant that transforms content consumption across diverse sources, including web documents, PDFs, media files, and YouTube videos. Using Amazon Bedrock large language models (LLMs) and other AWS services, you can upload documents or share URLs and then receive instant, comprehensive summaries without sifting through extensive content. The interactive chat interface enables real-time conversations with the AI assistant, allowing you to ask questions and explore topics in depth. Every interaction and chat session remains saved for future reference, enhancing your productivity through efficient information management.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/generative-ai-assistant-on-aws.pdf)

![Architecture diagram](/images/solutions/generative-ai-assistant-on-aws/images/generative-ai-assistant-on-aws-1.png)

1. **Step 1**: Users access a web application based on React that is served by AWS Amplify. User inputs can be a query with a web link or a PDF document to summarize.
1. **Step 2**: Amazon Cognito user pool authenticates users.
1. **Step 3**: When a user inputs a message, the application sends a POST request to the Amazon API Gateway REST API.
1. **Step 4**: API Gateway then routes the message to the AWS Lambda function.
1. **Step 5**: User conversations are stored in Amazon DynamoDB. Users can create separate threads for discussing separate topics in the Amplify web application.
1. **Step 6**: The user input and conversation history is sent to Amazon Bedrock for large language model (LLM) response generation. Users can choose between Amazon Nova Micro or Anthropic Claude Sonnet foundation models.
1. **Step 7**: When the response comes back from Amazon Bedrock, the Lambda function stores it in a DynamoDB table as conversational memory.
1. **Step 8**: The Lambda function then sends back a response to the user with the same channel through API Gateway.
1. **Step 9**: The Amplify frontend web application shows the responses.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-generative-ai-assistant-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Amplify streamlines the development and deployment workflow by providing a robust continuous integration, continuous deployment (CI/CD) pipeline to help ensure consistent and automated deployments. Amazon Bedrock enables straightforward integration with multiple foundation models. For example, this Guidance implements Anthropic's LLM through Amazon Bedrock to process input documents and web URLs, generating summaries and enabling chat functionality. Additionally, DynamoDB provides auto-scaling capabilities that eliminate the operational overhead of database management. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amplify provides secure hosting with built-in SSL/TLS encryption, while implementing identity management through Amazon Cognito for robust authentication and authorization. With Amazon Bedrock, you gain full control over the data you use to customize the foundation models for your generative AI applications. This service encrypts all data both in transit and at rest, while helping ensure your data remains isolated and protected. When you fine-tune foundation models, Amazon Bedrock creates a private copy of that model, preventing data sharing with model providers or base model improvements. Through AWS Identity and Access Management (IAM), you can maintain precise control over resource access, managing user permissions and sign-in capabilities for related resources. Additionally, DynamoDB helps ensure data security through encryption at rest. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon CloudWatch monitors all services configured in this Guidance, collecting metrics and presenting them through intuitive dashboards that offer visibility into application health and operational status. CloudWatch provides advanced analysis capabilities to simplify the debugging process for distributed systems, providing detailed insights into application performance and underlying service behavior. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amplify delivers a high-performance frontend experience through global content delivery network (CDN) distribution and automatic performance optimization. Amazon Bedrock streamlines access to high-performing foundation models from industry leaders including AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, and Amazon through a unified API interface. The Claude 3 Sonnet model delivers optimal balance between intelligence and processing speed, supporting an extensive context window of 200,000 text tokens and maintaining a maximum token limit of 4,096. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amplify uses a pay-as-you-go model, helping to align costs with actual usage. Amplify also provides built-in hosting optimizations to reduce bandwidth costs. Amazon Bedrock charges for model inference and customization operations. The service offers two distinct pricing plans for inference. The first plan, On-Demand and Batch, enables foundation model usage on a pay-as-you-go basis without time-based commitments. The second plan, Provisioned Throughput, lets you provision specific throughput levels to meet application performance needs in exchange for time-based commitments. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The unified API approach of Amazon Bedrock enables efficient access to high-performing foundation models, allowing you to select optimal models for your sustainability initiatives. This consolidated access point streamlines resource utilization while maintaining performance standards for sustainability-focused applications. This Guidance also uses Amplify automated scaling to help ensure compute resources are used only when needed, reducing idle capacity. DynamoDB has an on-demand capacity mode that scales resources to match actual usage patterns. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
