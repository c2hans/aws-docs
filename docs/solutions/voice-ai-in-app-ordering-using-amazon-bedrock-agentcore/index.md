---
source_url: https://docs.aws.amazon.com//solutions/voice-ai-in-app-ordering-using-amazon-bedrock-agentcore//index.html
---

---
title: 'Guidance for Voice AI In-App Ordering using Amazon Bedrock AgentCore'
canonical_url: https://docs.aws.amazon.com/solutions/voice-ai-in-app-ordering-using-amazon-bedrock-agentcore/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Voice AI In-App Ordering using Amazon Bedrock AgentCore

## Overview

This Guidance demonstrates how to implement real-time voice ordering across mobile apps, websites, and voice interfaces using Amazon Bedrock AgentCore and Amazon Nova 2 Sonic to process bidirectional voice streams without conversation pauses. The implementation establishes persistent WebSocket connections that enable customers to speak naturally while the AI agent processes requests and retrieves menu data, manages cart operations, and identifies nearby pickup locations through asynchronous tool calls. Authentication happens seamlessly through Amazon Cognito, while AgentCore Gateway transforms backend AWS Lambda functions into agent-ready tools that query Amazon DynamoDB tables and AWS Location Service in real time. You gain a production-ready voice ordering system that delivers natural, uninterrupted conversations while maintaining enterprise-grade security with encrypted data and centralized monitoring across all services.

## Benefits

### Enable hands-free voice ordering

Deploy a near real-time voice ordering experience using managed AI services and persistent WebSocket streaming. Reduce conversational delays so your customers complete orders faster without touching a screen.

### Scale without managing infrastructure

Leverage serverless compute and managed AI runtime that automatically scale with demand. Focus your team on building ordering features while infrastructure scales to zero during off-peak hours.

### Accelerate deployment with one command

Use infrastructure as code to deploy your entire voice AI ordering stack in a single script. Reduce time-to-production and ensure repeatable, consistent environments across development and production.

## How it works

This architecture diagram shows how to build a voice ordering system using Amazon Bedrock AgentCore and Nova 2 Sonic with MCP tool integration on AWS. [Download the architecture diagram.](downloads/omnichannel-voice-ai-ordering-using-amazon-bedrock-agentcore.pdf)

![Architecture diagram for Voice AI In-App Ordering using Amazon Bedrock AgentCore](/images/solutions/voice-ai-in-app-ordering-using-amazon-bedrock-agentcore/images/omnichannel-voice-ai-ordering-using-amazon-bedrock-agentcore.png)

1. **Step 1**: You access the web application hosted on AWS Amplify from a browser or mobile device.
1. **Step 2**: You authenticate with Amazon Cognito using username and password to receive JWT tokens and temporary AWS credentials.
1. **Step 3**: The frontend opens a SigV4-signed WebSocket connection to Amazon Bedrock AgentCore Runtime to begin the voice ordering session, establishing a persistent bidirectional channel for real-time voice streaming.
1. **Step 4**: The runtime validates the token via Amazon Cognito and initializes Amazon Nova 2 Sonic through Amazon Bedrock, a fully managed service with built-in security, privacy, and responsible AI.
1. **Step 5**: You speak your order into the device microphone. The agent processes voice through Amazon Nova 2 Sonic and invokes tool functions via AWS Lambda to manage your cart and retrieve menu items.
1. **Step 6**: AgentCore Gateway converts AWS Lambda functions and APIs into MCP-compatible, agent-ready tools, routing tool invocations to Amazon API Gateway and the underlying AWS Lambda functions.
1. **Step 7**: AWS Lambda functions query Amazon DynamoDB tables and AWS Location Service for menu data, cart management, and store proximity.
1. **Step 8**: Amazon Nova 2 Sonic generates a contextual voice response and streams it back to you over the WebSocket connection through AgentCore Runtime.
1. **Step 9**: AWS CDK deploys the solution with a single script, uploading application code to Amazon Simple Storage Service and triggering AWS CodeBuild to build container images stored in AWS ECR for the AgentCore runtime.
1. **Step 10**: Amazon CloudWatch provides centralized monitoring, logging, and alerting across all services. All data at rest is encrypted using AWS KMS.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-samples/sample-omnichannel-ordering-with-amazon-bedrock-agentcore-and-nova-sonic)

## Related content

- **Omnichannel ordering with Amazon Bedrock AgentCore and Amazon Nova 2 Sonic**: Learn how to build a voice ordering system using Amazon Bedrock AgentCore and Nova 2 Sonic with MCP tool integration.

[Read the blog](https://aws.amazon.com/blogs/machine-learning/omnichannel-ordering-with-amazon-bedrock-agentcore-and-amazon-nova-2-sonic/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
