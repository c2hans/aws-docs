---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/agentic-memory-overview.html
---

# Overview of agentic memory
<a name="agentic-memory-overview"></a>

An agentic AI application is a system that takes actions and makes decisions based on input. These agents use external tools, APIs, and multi-step reasoning to complete complex tasks. Without persistent memory, agents forget everything between conversations, making it impossible to deliver personalized experiences or complete multi-step tasks effectively.

Agentic memory handles the persistence, encoding, storage, retrieval, and summarization of knowledge gained through user interactions. This memory system is a critical part of the context management component of an agentic AI application, enabling agents to learn from past conversations and apply that knowledge to future interactions.

Consider the following examples where agentic memory provides value:
+ **Customer support agents** – An agent remembers a customer's previous issues, preferences, and account details across support sessions, avoiding repetitive information gathering and delivering faster resolutions.
+ **Research agents** – An agent that researches GitHub repositories remembers previously discovered project metrics, avoiding redundant web searches and reducing token usage and response time.
+ **Personal assistant agents** – An agent retains a user's scheduling preferences, communication style, and recurring tasks to provide increasingly personalized assistance over time.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
