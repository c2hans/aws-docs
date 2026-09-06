---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/govern-architect-agentic-ai/introduction.html
---

# Governing and architecting the diversity of agentic AI at scale
<a name="introduction"></a>

*Jocelyn Pinault, Massimiliano Angelino, Sebastien Grazzini, Florent Lacroute, and Lior Perez, Amazon Web Services*

This guidance addresses a critical challenge for any organization deploying AI at scale: how to govern and architect the growing diversity of agentic AI across an entire organization, not just within individual workloads or projects. As organizations deploy an increasing variety of AI agents, from simple chatbots to autonomous customer-facing systems, they need cohesive strategies that span use cases, teams, and business units.

## Intended audience
<a name="intended-audience"></a>

This guidance is designed for CIOs, CTOs, VP AI, Enterprise architects, AI governance leaders, platform engineers, and technical decision-makers who need to scale agentic AI across their organizations while maintaining control and compliance.

## Objectives
<a name="objectives"></a>

Understanding how to govern and architect agentic AI at scale requires a structured approach that moves from conceptual clarity to practical implementation.

**Use case typologies** examines the full spectrum of use case typologies, from simple chatbots and personal AI Assistants to autonomous team agents and customer-facing applications, Each category demands different governance rigor and architectural patterns.

**Agentic AI governance** explores governance frameworks covering agent/tool/MCP registry management, LLM model management, platform standards, multi-level access controls, and audit requirements. It presents three governance models centralized, federated, and hybrid and addresses citizen developer enablement.

**Agentic AI architecture in the enterprise** presents distinct layers covering applications (GenAI solutions such as Quick Suite and Kiro, and business system integrations), agents (Bedrock AgentCore services for runtime and orchestration), and core services (model access, tools, and knowledge bases).

This structure reflects an important reality governance and architectural requirements evolve with organizational maturity. While foundational elements such as security apply universally, other elements, such as compliance rigor, reliability standards, and output precision, intensify as deployments move from internal productivity tools to customer-facing applications. Use this guidance based on your enterprise's maturity stage:
+ Early stage, when you are exploring chatbots and personal assistants – focus on use case typologies and foundational governance. Do not attempt to build the entire reference architecture in the first iteration. Instead, focus on one or two pilot use cases and build only the necessary components for it. Then, add capability iteratively as new use cases are onboarded.
+ Growing maturity, when you are deploying team agents and business applications – emphasize agentic AI governance models and architectural patterns
+ Advanced maturity, when you are building customer-facing applications – prioritize enterprise agentic AI architecture, with providing advanced controls for agent permissions, referring to governance and audit requirements.

## About this content series
<a name="about-this-content-series"></a>

This guide is part of a series about agentic AI on AWS. For more information and to view the other guides in this series, see [Agentic AI](https://aws.amazon.com/prescriptive-guidance/agentic-ai/) on the AWS Prescriptive Guidance website.
