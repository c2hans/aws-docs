---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/agentic-memory-architecture.html
---

# Solution architecture
<a name="agentic-memory-architecture"></a>

The following architecture implements persistent memory for agentic AI applications using ElastiCache for Valkey as the vector storage component.

**Key components:**
+ **Amazon Bedrock AgentCore Runtime** – Provides the hosting environment for deploying and running agents. It provides access to the LLM and embedding models required for the architecture.
+ **Agent framework (for example, Strands Agents)** – Manages LLM invocations, tool execution, and user conversations. Strands Agents supports multiple LLMs, including models from Amazon Bedrock, Anthropic, Google Gemini, and OpenAI.
+ **Mem0** – The memory orchestration layer that sits between AI agents and storage systems. Mem0 manages the memory lifecycle, from extracting information from agent interactions to storing and retrieving it.
+ **Amazon ElastiCache for Valkey** – The managed in-memory data store that serves as the vector storage component. ElastiCache uses Valkey's vector similarity search capabilities to store high-dimensional vector embeddings, enabling semantic memory retrieval.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
