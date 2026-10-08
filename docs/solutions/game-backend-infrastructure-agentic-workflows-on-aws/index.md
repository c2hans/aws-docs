---
source_url: https://docs.aws.amazon.com/solutions/game-backend-infrastructure-agentic-workflows-on-aws/index.html
---

---
title: 'Guidance for Game Backend Infrastructure Agentic Workflows on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/game-backend-infrastructure-agentic-workflows-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Game Backend Infrastructure Agentic Workflows on AWS

## Overview

This Guidance helps game developers reduce manual operational overhead and accelerate time-to-market by implementing intelligent agentic workflows that automate backend infrastructure management tasks. A main orchestrator agent coordinates specialized sub-agents that handle infrastructure provisioning, launch preparation, LiveOps scaling, and performance monitoring across services like Amazon GameLift and Amazon Elastic Kubernetes Service. The system uses retrieval-augmented generation with domain-specific knowledge bases to provide context-aware responses, while built-in guardrails ensure secure operations by filtering inputs and outputs for potential vulnerabilities. You can customize agent behaviors, integrate additional monitoring tools, and adapt workflow patterns to match your specific game development and operational requirements.

## Benefits

### Simplify game infrastructure operations

Query your game server fleets, container clusters, and cloud costs through natural language instead of navigating multiple consoles. Reduce mean time to diagnose infrastructure issues affecting player experience.

### Safeguard operations with read-only intelligence

Gain infrastructure insights without risk of accidental changes. Built-in prompt injection detection and PII filtering protect your environment while maintaining a full audit trail.

### Scale expertise with specialized AI agents

Deploy domain-specific agents for Amazon GameLift, Amazon Elastic Kubernetes Service, and cost management that route queries automatically. Extend coverage to new domains using the Model Context Protocol.

## How it works

This architecture diagram shows how to build specialized AI agents with Amazon Bedrock AgentCore for conversational management of game infrastructure running on Amazon GameLift and Amazon Elastic Kubernetes Service. [Download the architecture diagram.](downloads/game-backend-and-infrastructure-agentic-workflows.pdf)

![Architecture diagram for Game Backend Infrastructure Agentic Workflows on AWS](/images/solutions/game-backend-infrastructure-agentic-workflows-on-aws/images/game-backend-and-infrastructure-agentic-workflows.png)

1. **Step 1**: Authenticate with Amazon Cognito User Pool. JWT tokens stored in HttpOnly cookies.
1. **Step 2**: Send query through Next.js frontend on Amazon Elastic Container Service Express Mode. CopilotKit provides the chat UI.
1. **Step 3**: Invoke Amazon Bedrock AgentCore Runtime via AWS SDK with SigV4 authentication.
1. **Step 4**: Route to Orchestrator agent which classifies query intent.
1. **Step 5**: Amazon Bedrock Guardrails filter input/output. Detects prompt injection, blocks PII exposure.
1. **Step 6**: Delegate to Specialist Agent (Amazon GameLift, Amazon Elastic Kubernetes Service, or Cost) based on query.
1. **Step 7**: Query Amazon Bedrock Knowledge Base for domain context. RAG with Titan embeddings.
1. **Step 8**: Invoke MCP Servers (Amazon EKS, Cost) or boto3 (Amazon GameLift) for AWS API integration.
1. **Step 9**: Read-only API calls to AWS Services: Amazon GameLift fleets, Amazon EKS clusters, AWS Cost Explorer.
1. **Step 10**: Amazon CloudWatch Logs and AWS X-Ray traces capture observability data.
1. **Step 11**: KB documents stored in Amazon Simple Storage Service with encryption and access logging.
1. **Step 12**: Container images in Amazon Elastic Container Registry with vulnerability scanning enabled.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-game-backend-and-infrastructure-agentic-workflows)

[Read usage guidelines](/solutions/guidance-disclaimers/)
