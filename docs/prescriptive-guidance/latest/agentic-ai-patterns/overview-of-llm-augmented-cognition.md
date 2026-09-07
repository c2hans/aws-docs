---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/overview-of-llm-augmented-cognition.html
---

# Overview of LLM-augmented cognition
<a name="overview-of-llm-augmented-cognition"></a>

At its core, the cognitive module of a software agent can be viewed as an LLM wrapped in augmentations. The agent can use the following building blocks to reason effectively within its environment:
+ **Prompting** – Framing input using context, instructions, examples, and memory
+ **Retrieval** – Providing up-to-date or domain-specific knowledge to the LLM prompt through vector search or semantic memory, for example, through retrieval-augmented generation (RAG)
+ **Tool use** – Enabling the LLM to invoke APIs or call functions to retrieve or act on information
+ **Memory** – Incorporating persistent or a session-based state into the reasoning loop, either by using structured databases or contextual summaries

These augmentations are composed of workflows that define how the LLM is used over time and across tasks, transforming it from a stateless engine into a dynamic reasoning agent.

![LLM augmentation.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/29d1608e-21a3-4b49-82f1-0bcb102a7875.png)
