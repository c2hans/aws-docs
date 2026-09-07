---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/generative-ai-agents.html
---

# Generative AI agents: replacing symbolic logic with LLMs
<a name="generative-ai-agents"></a>

The following diagram illustrates how large language models (LLMs) now serve as a flexible and intelligent cognitive core for software agents. In contrast to traditional symbolic logic systems, which rely on static plan libraries and hand-coded rules, LLMs enable adaptive reasoning, contextual planning, and dynamic tool use, which transform how agents perceive, reason, and act.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/images/guide-img/bf0cde42-baef-4bee-8fff-ca482667d2b6/images/7e2e2c89-16b8-4520-8ecb-f14ea7c73f40.png)

## Key enhancements
<a name="enhancements"></a>

This architecture enhances the traditional agent architecture as follows:
+ LLMs as cognitive engines: Goals, plans, and queries are passed into the model as** **prompt context. The LLM generates reasoning paths (such as chain of thought), decomposes tasks into sub-goals, and decides on next actions.
+ Tool use through prompting: LLMs can be directed through tool use agents or reasoning and acting (ReAct) prompting to call APIs and to search, query, calculate, and interpret outputs.
+ Context-aware planning: Agents generate or revise plans dynamically based on the agent's current goal, input environment, and feedback, without requiring hardcoded plan libraries.
+ Prompt context as memory: Instead of using symbolic knowledge bases, agents encode memory, plans, and goals as prompt tokens that are passed to the model.
+ Learning through few-shot, in-context learning: LLMs adapt behaviors through prompt engineering, which reduces the need for explicit retraining or rigid plan libraries.

## Achieving long-term memory in LLM-based agents
<a name="long-term-memory"></a>

Unlike traditional agents, which stored long-term memory in structured knowledge bases, generative AI agents must work within the context window limitations of LLMs. To extend memory and support persistent intelligence, generative AI agents use several complementary techniques: agent store, Retrieval-Augmented Generation (RAG), in-context learning and prompt chaining, and pretraining.

### Agent store: external long-term memory
<a name="agent-store--external-long-term-memory.7e24fa2c-11e7-520b-be77-2a03e4fc7216"></a>

Agent state, user history, decisions, and outcomes are stored in a long-term agent memory store (such as a vector database, object store, or document store). Relevant memories are retrieved on demand and injected into the LLM prompt context at runtime. This creates a persistent memory loop, where the agent retains continuity across sessions, tasks, or interactions.

### RAG
<a name="rag.363be822-fd3c-5865-a67f-41560ece495f"></a>

RAG enhances LLM performance by combining retrieved knowledge with generative capabilities. When a goal or query is issued, the agent searches a retrieval index (for example, through a semantic search of documents, earlier conversations, or structured knowledge). The retrieved results are appended to the LLM prompt, which grounds the generation in external facts or personalized context. This method extends the agent's effective memory and improves reliability and factual correctness.

### In-context learning and prompt chaining
<a name="in-context-learning-and-prompt-chaining.fbbb51b8-2c49-5722-b6b9-bcccc8e07819"></a>

Agents maintain short-term memory by using in-session token context and structured prompt chaining. Contextual elements, such as the current plan, previous action outcomes, and agent status, are passed between calls to guide behavior.

### Continued pretraining and fine-tuning
<a name="continued-pretraining-and-fine-tuning.d8917cf2-b087-5a8f-9bca-b7d8890d25c9"></a>

For domain-specific agents, LLMs can be continued pretrained on custom collections such as logs, enterprise data, or product documentation. Alternatively, instruction fine-tuning or reinforcement learning from human feedback (RLHF) can embed agent-like behavior directly into the model. This shifts reasoning patterns from prompt-time logic into the model's internal representation, reduces prompt length, and improves efficiency.

## Combined benefits in agentic AI
<a name="benefits"></a>

These techniques, when they're used together, enable generative AI agents to:
+ Maintain contextual awareness over time.
+ Adapt behavior based on user history or preferences.
+ Make decisions by using up-to-date, factual, or private knowledge.
+ Scale to enterprise use cases with persistent, compliant, and explainable behaviors.

By augmenting LLMs with external memory, retrieval layers, and continued training, agents can achieve a level of cognitive continuity and purpose that couldn't be achieved previously through symbolic systems alone.
