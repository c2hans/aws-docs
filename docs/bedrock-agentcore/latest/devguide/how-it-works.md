---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/how-it-works.html
---

# How it works
<a name="how-it-works"></a>

AgentCore Memory provides a set of APIs that let your AI agents seamlessly store, retrieve, and utilize both short-term and long-term memory. The architecture is designed to separate the immediate context of a conversation from the persistent knowledge that should be retained over time.

**Topics**
+ [Memory terminology](memory-terminology.md)
+ [Memory types](memory-types.md)
+ [Memory strategies](memory-strategies.md)
+ [Memory organization in AgentCore Memory](memory-organization.md)
+ [Memory record streaming](memory-record-streaming.md)
+ [Cross-account memory access](memory-cross-account-access.md)
+ [Compare long-term memory with Retrieval-Augmented Generation](memory-ltm-rag.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
