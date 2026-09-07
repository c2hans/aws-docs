---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/agentic-workflow-patterns.html
---

# Agentic workflow patterns
<a name="agentic-workflow-patterns"></a>

Agentic workflow patterns integrate modular software agents with structured large language model (LLM) workflows, enabling autonomous reasoning and action. While inspired by traditional serverless and event-driven architectures, these patterns shift core logic from static code to LLM-augmented agents, providing enhanced adaptability and contextual decision-making. This evolution transforms conventional cloud architectures from deterministic systems to ones capable of dynamic interpretation and intelligent augmentation, while maintaining fundamental principles of scalability and responsiveness.

## From event-driven to cognition-augmented systems
<a name="from-event-driven-to-cognition-augmented-systems.8e5df640-2e22-56db-87bb-c99ef64b1e31"></a>

Modern cloud architectures, particularly those built on serverless and event-driven principles, have traditionally relied on patterns like routing, fan-out, and enrichment to create responsive, scalable systems. Agentic AI systems build upon these foundations while reframing them around LLM-augmented reasoning and cognitive flexibility. This approach allows for more sophisticated problem-solving and automation capabilities, potentially revolutionizing how complex tasks are handled in cloud environments.

## Event-driven architecture
<a name="event-driven-architecture.fd02525f-41f9-5d41-be74-6396b56c1e15"></a>

The following diagram shows a typical distributed system:

![Event-driven architecture with data enrichment.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/f817137b-0873-4d4b-9787-237b854cc7b3.png)

1. A user submits a request to Amazon API Gateway.

1. Amazon API Gateway routes the request to an AWS Lambda function.

1. AWS Lambda performs data enrichment by querying an Amazon Aurora database

1. Amazon API Gateway returns the enriched payload to the caller.

This structure is both reliable and scalable, but it's fundamentally static. Business rules and logic paths must be explicitly coded, and adapting to changing contexts or incomplete information is limited.

## Cognition-augmented workflows
<a name="cognition-augmented-workflows.8fa0747f-e373-5b72-8f73-1169ac2f5a78"></a>

Agentic architectures add cognitive augmentation to an event-driven system. The following diagram shows an agentic equivalent:

![Cognition-augmented workflow.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/b113f13d-0e76-48cc-a43d-a54008182569.png)

1. A user submits a query through an SDK or API call.

1. An Amazon Bedrock agent receives the query.

1. The agent interprets the query by invoking an LLM

1. The agent performs semantic enrichment by searching the Amazon Bedrock knowledge base or other external data sources.

1. The LLM synthesizes a context-rich, goal-aligned response.

1. The system returns a synthesized response to the user.

In this flow, the LLM uses logic, understands intent, retrieves and combines relevant context, and then decides how best to respond. This pattern mirrors the traditional enrichment pattern, where messages are augmented with external data before being routed further. In agentic systems, however, this enrichment is not a static lookup. Instead, the enrichment is dynamic, semantically guided, and driven by purpose.

## Core insights
<a name="core-insights.f8a21ccd-3bc8-59d6-8781-5aac742d6a1f"></a>

Each LLM workflow can be mapped to an agentic workflow pattern, which mirrors and evolves traditional event-driven architecture styles. A basic building block of agentic workflows is the ability to augment an LLM's context with data, tools and memory. This creates a reasoning loop that's informed, adaptive, and aligned with user intent. Where traditional systems enrich messages with lookup data, agentic systems enable software to act less like scripts and more like intelligent collaborators.
