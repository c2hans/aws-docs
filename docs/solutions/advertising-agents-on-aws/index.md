---
source_url: https://docs.aws.amazon.com/solutions/advertising-agents-on-aws/index.html
---

---
title: 'Guidance for Advertising Agents on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/advertising-agents-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Advertising Agents on AWS

## Overview

This Guidance helps advertising technology companies and marketing teams streamline complex AdTech workflows—from campaign optimization to brand safety monitoring—by deploying AI-powered multi-agent collaboration systems on Amazon Bedrock. Users interact with orchestrator agents through natural language chat, invoking specialized agents that collaborate to handle tasks like audience strategy, inventory optimization, and ad format selection. The system draws on knowledge bases containing campaign intelligence and performance analytics, then streams integrated responses with interactive visualizations back to users in real time. You can accelerate digital transformation with automated decision-making for programmatic advertising, optimize campaign performance and ad yield, and make data-driven creative decisions while maintaining brand safety standards.

## Benefits

### Automate complex campaign planning workflows

Replace manual media planning processes with collaborative AI agents that deliver integrated campaign strategies, audience insights, and revenue projections through natural language conversations.

### Accelerate advertising decisions with AI collaboration

Deploy specialized orchestrator agents that coordinate audience targeting, inventory optimization, and ad format selection simultaneously, reducing campaign planning cycles from days to minutes.

### Ground campaign strategies in your data

Connect AI agents to your indexed campaign intelligence, performance analytics, and viewer monetization data so every recommendation reflects your actual inventory and audience metrics.

## How it works

This architecture diagram illustrates how to effectively support Advertising Agents on AWS. It shows the key components and their interactions, providing an overview of the architecture's structure and functionality. [Download the architecture diagram](downloads/advertising-agents-on-aws.pdf)

![Architecture diagram for Advertising Agents on AWS](/images/solutions/advertising-agents-on-aws/images/advertising-agents-on-aws-1.png)

1. **Step 1**: Business Users securely authenticate through Amazon Cognito user pools. The AngularJS UI application, hosted in Amazon Simple Storage Service (Amazon S3) and distributed via Amazon CloudFront for low-latency global access, validates these Amazon Cognito tokens to authorize user sessions.
1. **Step 2**: Users asks for Agent help in complex topics like planning a premium product campaign or optimizing inventory yield in natural language using chat interface calling out the agent's name using @<agent> prefix.
1. **Step 3**: The query is passed to one of Intelligent Orchestrator Strands Agent deployed in Amazon Bedrock AgentCore Runtime. Based on the input one of the Orchestrator agents - agent based on the invocation prompt - Media Planner, Inventory Optimizer or Ad Load Optimizer handles the query.
1. **Step 4**: The orchestrator agents uses Amazon Bedrock Knowledge Base indexed with campaign intelligence, performance analytics, content safety, and viewer monetization data. The source of data is Amazon S3.
1. **Step 5**: The orchestrator agents and specialized agents collaboratively work together in natural language conversation, each focusing on areas like audience strategy, inventory optimization, ad format selection, and campaign timing.
1. **Step 6**: On initialization, the Orchestrator agent uses an agent config file packaged in the Agent Core run time to identify other specialized agents that it needs to collaborate with. The specialized agents are then configured using Strands agent as a tool framework. The Orchestrator offers dual interaction modes - users can engage with the orchestration agents for comprehensive response, or directly chat with specialized agents for quick, focused answers.
1. **Step 7**: The agents use visualization template files stored in Amazon S3 to transform complex data to assist rendering of visual elements.
1. **Step 8**: The inter agent conversations and the final response is streamed back to user in real time. The final response contains integrated campaign strategies with interactive visualizations, including audience segments insights and revenue projections.
1. **Step 9**: AWS Identity and Access Management implements fine-grained permissions for service-to-service communication and Amazon Bedrock AgentCore access following a least-privilege access model.
1. **Step 10**: The conversation history between the user and agents are stored in Amazon Bedrock AgentCore Memory.
1. **Step 11**: Amazon Bedrock AgentCore observability features within Amazon CloudWatch collects performance metrics and operational data including session information, conversation traces.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-advertising-agents-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
