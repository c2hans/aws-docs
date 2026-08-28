---
source_url: https://docs.aws.amazon.com/blocks/latest/devguide/bb-ai.html
---

# AI
<a name="bb-ai"></a>

This section covers Blocks for AI-powered features: conversational agents and semantic search.

## Choosing an AI Block
<a name="_choosing_an_ai_block"></a>

| Block | Best for | Avoid when |
| --- | --- | --- |
|  `Agent`  | Conversational AI with tool calling, streaming, and human-in-the-loop approval | You only need document search without conversation (use KnowledgeBase) |
|  `KnowledgeBase`  | Semantic search over documents, RAG pipelines, context retrieval | You need multi-turn conversation or tool calling (use Agent, optionally with KnowledgeBase as a tool) |

## Agent
<a name="bb-agent"></a>

AI agent with streaming responses, tool calling, human-in-the-loop approval, and conversation persistence. Powered by the Strands Agents SDK. Define a system prompt and a set of tools, then stream messages to the agent. The agent can call your tools, ask for human approval before executing sensitive actions, and persist conversations across sessions.

Locally, Agent uses a canned keyword-based provider that returns predictable responses without calling any real model. No API keys or cloud costs needed. You can alternatively configure an `openai-api` provider pointing to Ollama or any OpenAI-compatible endpoint for testing with real models. On AWS, it connects to Amazon Bedrock.

For more information, see [bb-agent on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/bb-agent).

## KnowledgeBase
<a name="bb-knowledge-base"></a>

Semantic document retrieval. Point it at a folder of documents and query with natural language to get the most relevant chunks ranked by relevance. Use it to build RAG (Retrieval-Augmented Generation) pipelines or contextual search features.

Locally, KnowledgeBase uses in-memory vector search. On AWS, it provisions Amazon Bedrock Knowledge Bases with automatic document ingestion, chunking, and embedding.

For more information, see [bb-knowledge-base on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/bb-knowledge-base).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Blocks. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query blocks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
