---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/routing-dynamic-dispatch-patterns.html
---

# Routing dynamic dispatch patterns

In modern agentic systems, where tasks range from document parsing to autonomous software generation, the ability to dynamically route requests to the most capable large language model (LLM) or agent becomes critical. Static routing logic, often embedded within orchestration scripts or API layers, lacks the adaptability required for real-time, multi-model, multi-capability environments. To address this, LLM routing workflows can be transformed into an event-driven architecture that leverages a dynamic dispatch pattern, turning LLM calls into intelligently routed, context-aware events.

The following diagram is an example of LLM routing:

![LLM routing.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/e7be6841-1c50-45c2-a277-a0a5f7d0c81b.png)

## Dynamic dispatch
<a name="dynamic-dispatch.fac554ee-5dbc-5571-a207-ca58f1d78328"></a>

In traditional distributed systems, the dynamic dispatch pattern selects and invokes specific services at runtime based on incoming event attributes, such as event type, source, and payload. This is commonly implemented using Amazon EventBridge, which can evaluate and route incoming events to appropriate targets (for example, AWS Lambda functions AWS Step Functions, or Amazon Elastic Container Service tasks).

The following diagram is an AWS architectural example of dynamic dispatch:

![Dynamic dispatch.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/4cb6cd7a-818b-4b50-98a4-c06a4aa2c17e.png)

1. An application emits an event (for example, {"type": "orderCreated", "priority": "high"}).

1. Amazon EventBridge evaluates the event against its routing rules.

1. Based on an event's attributes, the system dynamically dispatches to the following:
   + `HighPriorityOrderProcessor` (service A)
   + `StandardOrderProcessor` (service B)
   + `UpdateOrderProcessor` (service C)

This pattern supports loose coupling, domain-based specialization, and runtime extensibility. This allows systems to respond intelligently to changing requirements and event semantics.

## LLM-based routing
<a name="llm-based-routing.2ce4683c-06d2-5309-928f-d146d49c23a9"></a>

In agentic systems, routing also performs dynamic task delegation – but instead of Amazon EventBridge rules or metadata filters, the LLM classifies and interprets the user's intent through natural language. The result is a flexible, semantic, and adaptive form of dispatching.

## Agent router
<a name="agent-router.753e7369-cd80-52b3-8932-50252365f86a"></a>

This architecture enables rich intent-based dispatching without predefined schemas or event types, which is ideal for unstructured input and complex queries.

1. A user submits the request "Can you help me review my contract terms?"

1. The LLM interprets this as a legal document task.

1. The agent routes the task to one or more of the following:
   + Contract review prompt template
   + Legal reasoning subagent
   + Document parsing tool

The following diagram is an AWS architectural example of an agent router:

![Agent router.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/8072c685-a78d-4d31-9723-34bde78f8791.png)

1. A user submits a natural language request through an SDK.

1. An Amazon Bedrock agent uses an LLM to classify the task (for example, legal, technical, or scheduling).

1. The agent dynamically routes the task through an action group to invoke the required agent:
   + Domain-specific agent
   + Specialized tool chain
   + Custom prompt configuration

1. The selected handler processes the task and returns a tailored response.

## Takeaways
<a name="takeaways.5443c201-4515-5fb7-b02e-c399c18b69ca"></a>

Where traditional dynamic dispatch uses Amazon Bedrock rules for routing based on structured event attributes, agentic routing uses LLMs to semantically classify and route tasks based on meaning and intent. This expands the system's flexibility by enabling the following:
+ Broader input understanding
+ Intelligent fallback and tool selection
+ Natural extensibility through new agent roles or prompt styles

Agentic routing replaces rigid rules with dynamic cognitive dispatching, which allows systems to evolve with language rather than code.
