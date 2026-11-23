---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/bb-ai.html
---

# AI

This section covers AWS CDK Blocks for AI capabilities: conversational agents and semantic search.

## Choosing an AI Block
<a name="_choosing_an_ai_block"></a>

| Block | Best for | Avoid when |
| --- | --- | --- |
|  `Agent`  | Conversational AI with tool calling, streaming, and human-in-the-loop approval | You only need document search without conversation (use KnowledgeBase) |
|  `KnowledgeBase`  | Semantic search over documents, RAG pipelines, context retrieval | You need multi-turn conversation or tool calling (use Agent, optionally with KnowledgeBase as a tool) |

## Agent
<a name="bb-agent"></a>

AI agent with streaming responses, tool calling, human-in-the-loop approval, and conversation persistence. Powered by the Strands Agents SDK. Define a system prompt and a set of tools, then stream messages to the agent. The agent can call your tools, ask for human approval before executing sensitive actions, and persist conversations across sessions.

Locally, Agent uses a canned keyword-based provider that returns predictable responses without calling any real model. No API keys or cloud costs needed. You can alternatively configure an `openai-api` provider pointing to Ollama or any OpenAI-compatible endpoint for testing with real models. On AWS, the agent loop runs on Amazon Bedrock AgentCore Runtime and streams responses to the browser over a `Realtime` WebSocket channel. The default model is `BedrockModels.BALANCED` (model ID `global.anthropic.claude-sonnet-4-6`), called through a global cross-Region inference profile. If your data must stay in specific Regions, set an inference profile limited to those Regions instead. You pay for model tokens in Amazon Bedrock, and for AgentCore Runtime vCPU and memory while a session is active.

Before you can call the default model, your account must submit use case details once in the Amazon Bedrock console. The model is also activated once per account through AWS Marketplace. To activate it, invoke it once, for example from the Amazon Bedrock console playground. Use a principal with the `aws-marketplace:Subscribe`, `aws-marketplace:Unsubscribe`, and `aws-marketplace:ViewSubscriptions` permissions. Until then, or when no configured model is available, the agent reports `AgentErrors.ModelUnavailable`. To filter content, attach an existing Amazon Bedrock guardrail with the `guardrail` model option. Set `untrustedOutput: true` on any tool that returns content you don’t control, such as retrieved documents. The agent then marks that content as untrusted data and tells the model not to follow instructions in it.

For more information, see [bb-agent on GitHub](https://github.com/aws/cdk-blocks/tree/main/packages/bb-agent).

## KnowledgeBase
<a name="bb-knowledge-base"></a>

Semantic document retrieval. Point it at a folder of documents and query with natural language to get the most relevant chunks ranked by relevance. Use it to build RAG (Retrieval-Augmented Generation) pipelines or contextual search features.

Locally, KnowledgeBase builds a text index over your documents in the `.bb-data/` directory, so retrieval works offline. On AWS, it provisions an Amazon Bedrock knowledge base with automatic document ingestion, chunking, and embedding. Vectors are stored in Amazon S3 Vectors. Documents are embedded with Amazon Titan Text Embeddings V2 (1024 dimensions by default) and split with semantic chunking unless you choose another `chunking` strategy. On AWS, the source can also be an `s3://` URI. Local development accepts only a local folder.

For more information, see [bb-knowledge-base on GitHub](https://github.com/aws/cdk-blocks/tree/main/packages/bb-knowledge-base).
