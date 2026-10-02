---
source_url: https://docs.aws.amazon.com//solutions/cost-analysis-and-optimization-with-amazon-bedrock-agentcore-on-aws//index.html
---

---
title: 'Guidance for Cost Analysis and Optimization with Amazon Bedrock AgentCore on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/cost-analysis-and-optimization-with-amazon-bedrock-agentcore-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Cost Analysis and Optimization with Amazon Bedrock AgentCore on AWS

## Overview

This Guidance shows how to simplify AWS cost management across multiple accounts by building a conversational AI agent that consolidates billing data from multiple sources into a single natural language interface. Finance teams can ask questions like "What are my top compute cost drivers this month?" and the agent queries AWS Cost Explorer for historical spending, AWS Budgets for budget status, and AWS Compute Optimizer for rightsizing recommendations, then synthesizes the data into an immediate conversational response. The agent maintains conversation context across interactions, enabling follow-up questions without repeating information. You can eliminate manual cost report generation, accelerate budget analysis, identify optimization opportunities faster, and empower non-technical finance teams to access complex billing data through simple conversations.

## Benefits

### Consolidate cost insights through conversation

Query AWS Cost Explorer, Budgets, and Compute Optimizer through a single natural language chat interface. Eliminate manual navigation across multiple consoles to analyze your cloud spend.

### Democratize FinOps across your organization

Enable non-technical stakeholders to access cost analysis and optimization recommendations without specialized cloud billing expertise. Reduce dependency on dedicated FinOps engineers for routine cost inquiries.

### Accelerate analysis with multi-turn context

Conduct complex cost investigations across follow-up questions without repeating prior context. Resolve multi-step FinOps queries in minutes instead of hours of manual cross-referencing.

## How it works

This architecture diagram shows how to build a conversational FinOps agent that consolidates AWS cost data using Amazon Bedrock AgentCore, MCP servers, and natural language. [Download the architecture diagram.](downloads/cost-analysis-and-optimization-with-amazon-bedrock-agentcore-on-aws.pdf)

![Architecture diagram for Cost Analysis and Optimization with Amazon Bedrock AgentCore on AWS](/images/solutions/cost-analysis-and-optimization-with-amazon-bedrock-agentcore-on-aws/images/cost-analysis-and-optimization-with-amazon-bedrock-agentcore-on-aws.png)

1. **Step 1**: Administrative users use AWS CDK to deploy the guidance with a single script, uploading application code to Amazon S3 bucket and triggering AWS CodeBuild to build container images stored in Amazon Elastic Container Registry (ECR) for the Amazon Bedrock AgentCore runtime.
1. **Step 2**: Users access the web application hosted on AWS Management Portal for vCenter, which serves the frontend interface.
1. **Step 3**: Users authenticate with Amazon Cognito. Amazon Cognito validates your credentials and returns temporary AWS credentials from the Identity Pool.
1. **Step 4**: The frontend sends the user's question to the Amazon Bedrock AgentCore Runtime — a secure, serverless environment that hosts and runs the agent with session isolation — using the temporary AWS credentials to call InvokeAgentRuntime via IAM SigV4 authentication.
1. **Step 5**: The Strands agent — an open-source agent framework supported natively by AgentCore Runtime — sends the user's question with 24 tool definitions to Claude Sonnet 4.5 on Amazon Bedrock, a fully managed service providing secure access to foundation models. The model selects the appropriate cost analysis tool.
1. **Step 6**: Amazon Bedrock AgentCore Memory — a fully managed service for session and long-term memory — maintains conversation context across interactions, enabling the agent to understand follow-up questions and provide coherent multi-turn cost analysis without users repeating context.
1. **Step 7**: The agent routes the tool call to AgentCore Gateway using IAM SigV4 authentication via InvokeGateway.
1. **Step 8**: AgentCore Identity — a secure identity and credential management service purpose-built for AI agents — retrieves an OAuth 2.0 access token from the registered Amazon Cognito M2M credential provider (using the client credentials grant) and attaches it to the outbound MCP request, enabling the agent to securely access the billing tools.
1. **Step 9**: The Gateway sends the Model Context Protocol (MCP) tool call request with the OAuth token to the Billing MCP Runtime.
1. **Step 10**: The Billing MCP Runtime queries the appropriate AWS cost services: AWS Cost Explorer for historical cost and usage data, AWS Budgets for budget status and alerts, AWS Compute Optimizer for rightsizing recommendations, and AWS Cost & Pricing APIs for current service pricing — providing comprehensive FinOps coverage through a single conversational interface.
1. **Step 11**: Cost data flows back through the chain. The agent sends it to Amazon Bedrock, where Claude generates a natural language summary of your costs.
1. **Step 12**: The formatted response displays the cost breakdown in the user's chat interface.
1. **Step 13**: Amazon CloudWatch provides centralized monitoring, logging, and alerting across all guidance services for complete observability.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-samples/sample-finops-agent-amazon-bedrock-agentcore)

## Related content

- **Build a FinOps agent using Amazon Bedrock AgentCore**: Learn how to build a conversational FinOps agent using Amazon Bedrock AgentCore.

[Read the blog](https://aws.amazon.com/blogs/machine-learning/build-a-finops-agent-using-amazon-bedrock-agentcore/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
