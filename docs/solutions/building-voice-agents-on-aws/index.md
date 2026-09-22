---
source_url: https://docs.aws.amazon.com/solutions/building-voice-agents-on-aws/index.html
---

---
title: 'Guidance for Building Voice Agents on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-voice-agents-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Building Voice Agents on AWS

## Overview

This Guidance demonstrates how to build real-time, conversational voice agents through an automated framework that provisions AI services, streaming infrastructure, and telephony integrations on AWS. You can deploy voice agents using a unified speech-to-speech model such as Amazon Nova Sonic for ultra-low latency, or a cascaded approach that combines speech-to-text, a reasoning model, and text-to-speech for greater flexibility. The framework orchestrates multi-agent collaboration through the Agent-to-Agent protocol, letting specialized sub-agents retrieve knowledge from vector stores or query customer data in real time. With this approach, you can rapidly prototype and scale conversational experiences across phone, web, and mobile channels.

## Benefits

### Accelerate voice agent deployment

Provision AI services, streaming transport, and telephony integrations through an automated framework instead of wiring each component by hand. Your team moves from prototype to production faster and scales conversational experiences across phone, web, and mobile channels without rebuilding the stack.

### Orchestrate multi-agent systems

Connect your main voice agent with specialized sub-agents through the Agent-to-Agent (A2A) protocol for complex task handling. Enable seamless coordination between knowledge base, CRM, and other specialized agents to solve customer inquiries efficiently.

### Scale multi-agent conversations reliably

Run the voice pipeline on serverless containers and coordinate specialized sub-agents through an agent-to-agent protocol with automatic service discovery. You can add capabilities like knowledge retrieval or customer-record lookups as independent agents, keeping the system modular as conversation volume grows.

## How it works

This architecture diagram illustrates how to build and operate Building Voice Agents on AWS. It shows the key components and their interactions. [Download the architecture diagram](downloads/building-voice-agents.pdf)

![Architecture diagram for Building Voice Agents](/images/solutions/building-voice-agents-on-aws/images/building-voice-agents.png)

1. **Step 1**: Caller interact with the voice agent solution via a phone line or web or mobile application.
1. **Step 2**: Daily managed real-time infrastructure on AWS supports both telephony and webRTC streaming. Alternatively, the Pipecat voice agent can connect via WebSockets or other telephony providers using another transport service.
1. **Step 3**: Pipecat voice agent is a Python-based voice agent framework that orchestrates real-time voice pipelines with ultra-low latency, with two key components: streaming network transport, and orchestration of AI services and sub-agents. Pipecat is served on Amazon Elastic Container Service (Amazon ECS). Alternatively, you consider AgentCore which provides enterprise-grade services for deploying and operating AI agents at scale, or Amazon Elastic Kubernetes Service (Amazon EKS).
1. **Step 4**: The solution supports voice agents across two common approaches: (A) a speech-to-speech (S2S) model such as Amazon Nova Sonic, which delivers real-time voice conversations with low latency, or (B) a cascaded models approach that orchestrates speech-to-text (STT) and text-to-speech (TTS) models with a foundation model on Amazon Bedrock, with the option to integrate a reasoning agent on Amazon Bedrock AgentCore. You can configure the solution to use speech models with APIs for prototyping, and Amazon SageMaker with bidirectional streaming in production.
1. **Step 5**: The main voice agent delegates to sub-agents via the Agent-to-Agent (A2A) protocol, using AWS Cloud Map for service discovery. For example, the Knowledge Base Agent retrieves context from Amazon S3 vectors, while the CRM Agent queries Amazon DynamoDB for customer-specific data.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-voice-agents-on-aws)

[Read usage guidelines](/solutions/guidance-disclaimers/)
