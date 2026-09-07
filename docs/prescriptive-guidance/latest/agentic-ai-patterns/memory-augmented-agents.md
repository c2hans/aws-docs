---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/memory-augmented-agents.html
---

# Memory-augmented agents
<a name="memory-augmented-agents"></a>

Memory-augmented agents are enhanced with the ability to store, retrieve, and reason using short-term and long-term memory. This allows them to maintain context across multiple tasks, sessions, and interactions, which produces more coherent, personalized, and strategic responses.

Unlike stateless agents, memory-augmented agents adapt by referencing historical data, learn from prior outcomes, and make decisions that align with the user's goals, preferences, and environment.

## Architecture
<a name="architecture.0eee35cd-260e-5f66-a381-8af26bfb0874"></a>

A memory-augmented agent is shown in the following diagram:

![Memory-augmented agents.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/18a2fe3e-c0ed-4b18-8c36-bda63c828c00.png)

## Description
<a name="description.1b0ad68a-a5c6-5b38-9580-ac3fcde4156d"></a>

1. Receives input or event
   + The agent receives a user query or system event. This may be a text, API trigger, or environmental change.

1. Retrieves short-term memory
   + The agent retrieves recent conversational history, task context, or the system state that's relevant to the session or workflow.

1. Retrieves long-term memory
   + The agent queries long-term memory (for example, vector databases and key-value stores) for historical insights, such as the following:
     + User preferences
     + Past decisions and outcomes
     + Learned concepts, summaries, or experiences

1. Reasons through the LLM
   + The memory context is embedded into the LLM prompt, allowing the agent to reason based on both current inputs and prior knowledge.

1. Generates outputs
   + The agent produces a contextually aware response, plan, or action that is personalized according to the task history and user's inputs.

1. Updates memory
   + New information, such as updated goals, success and failure signals, and structured responses, are stored for future tasks.

## Capabilities
<a name="capabilities.6aedf735-0c76-54fc-9313-5741b8caf500"></a>
+ Session continuity across conversations or events
+ Goal persistence over time
+ Contextual awareness based on an evolving state
+ Adaptability informed by prior successes and failures
+ Personalization aligned with user preferences and history

## Common use cases
<a name="common-use-cases.1154b977-c2ca-51ac-9a2f-d5c7cba45375"></a>
+ Conversational copilots that remember user preferences
+ Coding agents that track codebase changes
+ Workflow agents that adapt according to task history
+ Digital twins that evolve from system knowledge
+ Research agents that avoid redundant retrievals

## Implementing memory-augmented agents
<a name="implementing-memory-augmented-agents.156591dc-c29d-5a24-b2fe-5c97a100a254"></a>

Use the following tools and AWS services for memory-augmented agents:

|
|
| Memory layer | AWS service | Purpose |
| --- |--- |--- |
| Short-term | Amazon DynamoDB, Redis, Amazon Bedrock context | Fast retrieval of recent interaction states |
| Long-term (structured) | Amazon Aurora, Amazon DynamoDB, Amazon Neptune | Facts, relationships, and logs |
| Long-term (semantic) | OpenSearch, Pinecone | Embedding-based retrieval (that is, RAG) |
| Storage | Amazon S3 | Storing transcripts, structured memories, and files |
| Orchestration | AWS Lambda or AWS Step Functions | Managing memory injection and update lifecycle |
| Reasoning | Amazon Bedrock | Anthropic Claude or Mistral with memory prompts |

## Implementing memory-injected prompting
<a name="implementing-memory-injected-prompting.3d4c0ddf-bf10-500d-90c6-64c3dd3aee7b"></a>

To integrate memory into agent reasoning, use a combination of structured state and retrieval-augmented context injection:
+ Include the latest agent state and recent dialogue history as structured input when constructing the prompt for the language model, so it can reason with full context.
+ Use retrieval-augmented generation (RAG) to pull relevant documents or facts from long-term memory.
+ Summarize previous plans, context, and interactions for compression and relevance.
+ Inject external memory modules, such as vector stores or structured logs, during inference to guide decision making.

## Summary
<a name="summary.ad068aad-c771-572b-98c0-a387583d5284"></a>

Memory-augmented agents maintain thought continuity by learning from experience and remembering user context. These agents surpass reactive intelligence by using long-term collaboration, personalization, and strategic reasoning. In terms of agentic AI, memory allows agents to behave more like adaptive digital counterparts and less like stateless tools.
