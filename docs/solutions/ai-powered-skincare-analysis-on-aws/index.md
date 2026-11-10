---
source_url: https://docs.aws.amazon.com/solutions/ai-powered-skincare-analysis-on-aws/index.html
---

---
title: 'Guidance for AI-Powered Skincare Analysis on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/ai-powered-skincare-analysis-on-aws/
source: aws-documentation
generated_on: 2026-11-09
---

# Guidance for AI-Powered Skincare Analysis on AWS

## Overview

This Guidance helps you analyze a customer's skin from a few photos and generate a personalized skincare routine. Consumers struggle to choose products that suit their skin, and brands can't offer one-to-one consultations at scale. With this Guidance, you deploy a multi-agent application on Amazon Bedrock AgentCore Runtime. Its agents analyze the photos with foundation models in Amazon Bedrock, plan routine steps, and select ingredients. Server code matches products from your catalog with Amazon OpenSearch Service and Amazon DynamoDB. Results stream back to the browser as each agent completes, so customers see progress instead of waiting. Amazon Bedrock Guardrails screens every model call, and the application doesn't store photos.

## Benefits

### Personalize skincare routines at scale

Generate a personalized skincare routine from one to three skin photos, with agents that analyze the skin, plan steps, and pick ingredients in parallel. Results stream to the browser as each agent completes, so you offer consultation-style advice without staffing one-to-one sessions.

### Recommend products from your catalog

Match each routine step to products from your own catalog, ranked by exact ingredient matches and rechecked against authoritative records. Server code selects the products instead of the model, which reduces the risk of recommending items you don't carry.

### Protect customers and their photos

Screen every model call with Amazon Bedrock Guardrails and structured-output checks, and process skin photos without storing them. A web application firewall, user authentication, per-user limits, and a private network for the agents help reduce exposure to abuse and unauthorized access.

## How it works

This architecture diagram illustrates how to build and operate AI-Powered Skincare Analysis on AWS. It shows the key components and their interactions. [Download the architecture diagram](downloads/ai-powered-skincare-analysis.pdf)

![Architecture diagram for AI-Powered Skincare Analysis](/images/solutions/ai-powered-skincare-analysis-on-aws/images/ai-powered-skincare-analysis.png)

1. **Step 1**: An admin-created Amazon Cognito user signs in and uploads one to three skin photos, up to 1 MiB each. Amazon CloudFront serves the React app from a private Amazon S3 bucket behind AWS WAF.
1. **Step 2**: Amazon API Gateway validates the Amazon Cognito ID token, a JSON Web Token (JWT), on the analyze and ingredient-lookup routes. A second AWS WAF web ACL admits only Amazon CloudFront traffic.
1. **Step 3**: Amazon API Gateway invokes a streaming AWS Lambda proxy. It enforces per-user limits in Amazon DynamoDB and invokes Amazon Bedrock AgentCore Runtime, which only this role can call. It stores no photos.
1. **Step 4**: In a private virtual private cloud (VPC), Amazon Bedrock AgentCore Runtime runs the agents. A skin-analysis agent reads the photos with an Amazon Bedrock model; a planning agent selects two to eight steps.
1. **Step 5**: For each step in parallel, an ingredient agent picks preferred ingredients. Server code ranks exact matches in Amazon OpenSearch Service and rechecks authoritative records in Amazon DynamoDB, choosing up to three products.
1. **Step 6**: Agents explain the server-selected products. Amazon Bedrock Guardrails and structured-output checks screen every model call. A compile node assembles the routine, which streams back as server-sent events (SSE).
1. **Step 7**: A publisher writes products to Amazon DynamoDB with outbox events. A DynamoDB stream and Amazon EventBridge schedules drive a catalog worker AWS Lambda that projects records into Amazon OpenSearch Service.
1. **Step 8**: AWS CodeBuild builds the agent image from Amazon S3 and pushes it to Amazon ECR for the runtime. Amazon CloudWatch collects Amazon API Gateway, AWS WAF, build, and runtime logs.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-ai-powered-skincare-analysis-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
