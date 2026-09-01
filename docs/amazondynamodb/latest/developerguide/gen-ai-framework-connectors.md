---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/gen-ai-framework-connectors.html
---

# AI framework connectors for DynamoDB
<a name="gen-ai-framework-connectors"></a>

AI agents need durable storage for everything they must remember: conversation state that survives a restart, chat history that spans sessions, and long-term memories they can recall in later conversations. Open source connectors, maintained by AWS and by the framework communities, integrate DynamoDB with popular AI agent frameworks so that state lives in a serverless database with single-digit millisecond latency, in your own AWS account.

The following table summarizes the available connectors and what each one stores.

| Framework | Package | What it stores in DynamoDB | Languages |
| --- | --- | --- | --- |
| Strands Agents | `strands-dynamodb-storage` | Session state, long-term memories, transcripts, and oversized tool results, through the SDK's unified storage contract | Python, TypeScript |
| LangChain | `langchain-community`, `langchain-aws` | Chat message history, and documents with embeddings for vector similarity search | Python, JavaScript |
| LangGraph | `langgraph-checkpoint-aws` | Agent checkpoints (short-term conversation state) and long-term, cross-thread memories | Python |

**Topics**
+ [Using DynamoDB as a storage backend for Strands Agents](ddb-strands-storage.md)
+ [Using DynamoDB with LangChain](ddb-langchain.md)
+ [Using DynamoDB as a checkpoint store for LangGraph agents](ddb-langgraph-checkpoint.md)
+ [Semantic long-term memory for LangGraph agents](ddb-langgraph-memory.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
