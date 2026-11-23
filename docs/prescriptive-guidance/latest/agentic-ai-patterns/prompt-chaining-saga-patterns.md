---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/prompt-chaining-saga-patterns.html
---

# Prompt chaining saga patterns

By reimagining LLM prompt chaining as an event-driven saga, we unlock a new operational model: workflows become distributed, recoverable, and semantically coordinated across autonomous agents. Each prompt-response step is reframed as an atomic task, emitted as an event, consumed by a dedicated agent, and enriched with contextual metadata.

The following diagram is an example of LLM prompt chaining:

![LLM prompt chaining.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/c3b5d8d1-ecbb-4cf2-aebe-9af397821cd9.png)

## Saga choreography
<a name="saga-choreography.f39a1c6d-eea0-54f0-a7aa-ad0df70a9c22"></a>

The saga choreography pattern is an implementation approach in distributed systems that has no central coordinator. Instead, each service or component publishes events that trigger the next workflow action. This pattern is widely used in distributed systems for managing transactions across multiple services. In a saga, the system runs a series of coordinated local transactions. If one fails, the system triggers compensating actions to maintain consistency.

The following diagram is an AWS architectural example of saga choreography:

![Saga choreography.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/301fabfa-a401-488d-abab-754d963d963f.png)

1. Reserve inventory

1. Authorize payment

1. Create shipping order

If step 3 fails, the system invokes compensating actions (for example, cancel a payment or release inventory).

This pattern is especially valuable in event-driven architectures where services are loosely coupled and states must be consistently resolved over time, even in the presence of partial failure.

## Prompt chaining pattern
<a name="prompt-chaining-pattern.55fd947a-ff38-54c8-8516-487fe705e29c"></a>

Prompt chaining resembles the saga pattern in both structure and purpose. It executes a series of reasoning steps that build sequentially while preserving context and allowing for rollbacks and revisions.

## Agent choreography
<a name="agent-choreography.c632a2b8-680e-56b5-81cb-118dea66387f"></a>

1. LLM interprets a complex user query and generates a hypothesis

1. LLM elaborates a plan to solve the task

1. LLM executes a subtask (for example, by using a tool call or retrieving knowledge)

1. LLM refines the output or revisits an earlier step if it deems a result unsatisfactory

If an intermediate result is flawed, the system can do one of the following:
+ Retry the steps using a different approach
+ Revert to a previous prompt and replan
+ Use an evaluator loop (for example, from the evaluator-optimizer pattern) to detect and correct failures

Like the saga pattern, prompt chaining allows for partial progress and rollback mechanisms. This happens through iterative refinement and LLM-directed correction rather than through compensating database transactions.

The following diagram is an AWS architectural example of agent choreography:

![Agent choreography.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/a93aa75d-6850-47ad-86d7-eb8d567b1d0a.png)

1. A user submits a query through an SDK.

1. An Amazon Bedrock agent orchestrates reasoning through the following:
   + Interpretation (LLM)
   + Planning (LLM)
   + Execution through a tool or knowledge base
   + Response construction

1. If a tool fails or returns insufficient data, the agent can dynamically replan or rephrase the task.

1. Memory (for example, a short-term vector store) can preserve its state across steps

## Takeaways
<a name="takeaways.3e88e3ba-9432-5c18-87cc-1563617eba15"></a>

Where the saga pattern manages distributed service calls with compensating logic, prompt chaining manages reasoning tasks with reflective sequencing and adaptive replanning. Both systems allow for incremental progress, decentralized decision points, and failure recovery, and it does all of this through informed reasoning rather than rigid rollback.

Prompt chaining introduces transactional reasoning, which is the cognitive equivalent of sagas. That is, each "thought" is reevaluated, revised, or abandoned as part of a broader goal-directed dialogue.
