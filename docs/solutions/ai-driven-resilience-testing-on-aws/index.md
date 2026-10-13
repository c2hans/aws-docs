---
source_url: https://docs.aws.amazon.com/solutions/ai-driven-resilience-testing-on-aws/index.html
---

---
title: 'Guidance for AI-Driven Resilience Testing on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/ai-driven-resilience-testing-on-aws/
source: aws-documentation
generated_on: 2026-10-13
---

# Guidance for AI-Driven Resilience Testing on AWS

## Overview

This Guidance shows how you can automate the journey from operational findings to chaos engineering validation. It deploys an FIS Recommender MCP server that integrates with AWS DevOps Agent to analyze operational findings and recommend tailored AWS Fault Injection Service experiments, generating complete, ready-to-deploy experiment templates. The solution maps findings across scenarios spanning network, database, compute, containers, AWS Lambda, caching, API throttling, and availability to specific fault injection actions with calibrated durations, targets, and Amazon CloudWatch stop conditions. You deploy the MCP server through Amazon Bedrock AgentCore or AWS Lambda and connect it to Kiro and other MCP clients, using Amazon Cognito for authentication.

## Benefits

### Automate chaos experiment creation

Automatically convert AWS DevOps Agent findings into targeted AWS Fault Injection Service experiment templates through the FIS Recommender MCP. This removes manual experiment authoring, so your teams move from resilience findings to ready-to-run chaos tests in minutes.

### Target experiments to real findings

Generate experiment templates grounded in the specific weaknesses AWS DevOps Agent surfaces, rather than generic fault scenarios. This focuses testing on the failure modes most relevant to your workloads.

### Deploy securely without managing servers

Run the FIS Recommender on Amazon Bedrock AgentCore serverless runtime with Amazon Cognito OAuth authentication and scoped IAM execution roles. This scales automatically to demand and keeps agent access controlled.

## How it works

This diagram shows how AWS DevOps Agent findings flow through the FIS Recommender MCP on Amazon Bedrock AgentCore to automatically generate targeted AWS Fault Injection Service experiment templates through direct MCP or Lambda-based paths. [Download the architecture diagram](downloads/ai-driven-resilience-testing-on-aws.pdf)

![Architecture diagram for AI-Driven Resilience Testing on AWS](/images/solutions/ai-driven-resilience-testing-on-aws/images/ai-driven-resilience-testing-on-aws.png)

1. **Step 1**: User triggers the FIS Recommender MCP through one of two paths. - Path A (Lambda-based): AWS DevOps Agent findings flow using Amazon API Gateway or Amazon EventBridge to AWS Lambda, triggering the FIS Recommender MCP. Amazon Cognito handles auth. - Path B (Direct MCP): FIS Recommender MCP integrated directly in any MCP client (AWS DevOps Agent skill, Kiro, Claude) using OAuth with Amazon Cognito auth.
1. **Step 2**: (Path A) Investigation events flow to Amazon EventBridge or Amazon API Gateway for event-driven processing and routing to AWS Lambda.
1. **Step 3**: (Path A) AWS Lambda invokes the Amazon Bedrock AgentCore Gateway with MCP tool parameters to route the request to the FIS Recommender MCP server.
1. **Step 4**: Amazon Bedrock AgentCore Gateway on Amazon Bedrock AgentCore routes the request to the FIS Recommender to generate targeted experiment templates.
1. **Step 5**: Amazon Bedrock AgentCore Runtime pulls the agent's container image from Amazon Elastic Container Registry (Amazon ECR), where it was built with Docker and pushed.
1. **Step 6**: Amazon Bedrock AgentCore Runtime executes the FIS recommendation logic and automatically generates targeted AWS Fault Injection Service (AWS FIS) experiment templates.
1. **Step 7**: AWS Fault Injection Service (AWS FIS) creates the chaos experiment templates based on the recommendations, ready for execution.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-ai-driven-resilience-testing-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
