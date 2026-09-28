---
source_url: https://docs.aws.amazon.com/solutions/farm-management-ai-agent-on-aws/index.html
---

---
title: 'Guidance for Farm Management AI Agent on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/farm-management-ai-agent-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Farm Management AI Agent on AWS

## Overview

This guidance demonstrates how to build an AI-powered farm management assistant using Amazon Bedrock AgentCore and Nova models, helping farmers optimize crop health and streamline operations. By combining instant plant disease diagnostics, personalized growing recommendations, and automated supply ordering capabilities, farmers can make data-driven decisions directly from the field. The solution leverages advanced image analysis, contextual reasoning, and automated workflows to deliver expert agricultural knowledge and supply chain efficiency through a simple mobile interface, reducing reliance on manual consultation and enabling faster, more informed crop management decisions.

## Benefits

### Optimize crop management

Deploy specialized AI agents that analyze plant health and provide tailored recommendations. Farmers can upload images to receive immediate diagnostics and growth advice based on plant type, weather conditions, and soil analysis.

### Streamline farming operations

Automate routine agricultural tasks through a multi-agent solution that handles plant diagnostics, growth recommendations, and supply ordering. Focus on implementing expert advice while the system manages the complexity of coordinating multiple specialized AI agents.

### Enhance decision-making capabilities

Access contextual farming insights through specialized tools including image analysis, knowledge retrieval, and real-time web searches. Make informed decisions with AI-powered recommendations that consider your specific agricultural conditions and requirements.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/farm-management-ai-agent-on-aws.pdf)

![Architecture diagram](/images/solutions/farm-management-ai-agent-on-aws/images/farm-management-ai-agent-on-aws-1.png)

1. **Step 1**: User (Farmer) uploads image of a plant to Farmer Assistant App to analyze the plant health and get recommendations to improve its growth. User can also use the app to ask general purpose questions related to farming and order fertilizer from Amazon.com.
1. **Step 2**: The Farmer Assistant App interacts with the Amazon Bedrock AgentCore Runtime as backend entry point, which enables multi-agent orchestration to help the farmer achieve their goals.
1. **Step 3**: Amazon Bedrock AgentCore Runtime hosts three agents (Plant Doctor, Plant Growth Advisor and Automatic Order).
1. **Step 4**: Amazon Bedrock AgentCore Gateway hosts the MCP servers with required tools. AWS Lambda functions host the business logic of tools. The tools include vector database calls, web searches, and browser session for ordering the required material for plants.
1. **Step 5**: AWS Lambda functions implement specialized tools including Plant Detection for analyzing uploaded images, RAG for Fertilizer to provide context-aware recommendations, and Web Search for retrieving current information. Amazon Bedrock AgentCore Browser Tool enables automated fertilizer ordering through browser sessions.
1. **Step 6**: Amazon Bedrock AgentCore Identity is used as oAuth 2.0 server for ingress and egress authentication flows with Amazon Bedrock AgentCore Gateway.
1. **Step 7**: Amazon Bedrock AgentCore Observability powers the agent security and traceability.
1. **Step 8**: The supervisor agent manages all user interactions with the Plant Doctor and the Growth Advisor, and providing confirmation on order placement and tracking link.
1. **Step 9**: Amazon Bedrock AgentCore Memory stores the conversation with the user and refers back to chat history in subsequent chats.
1. **Step 10**: All AI agents leverage Amazon Nova Foundation Models.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/gudiance-for-farm-management-ai-agent-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
