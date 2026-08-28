---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-advanced.html
---

# Advanced features and topics for Amazon Bedrock AgentCore Memory
<a name="memory-advanced"></a>

This chapter describes how to front Amazon Bedrock AgentCore Memory with an AgentCore Gateway to add OAuth authentication for end users and fine-grained access control (FGAC). With these features, you can enforce per-user Memory isolation at the infrastructure layer — without distributing AWS credentials to end users — and restrict Memory so that it can be reached only through your gateway.

**Topics**
+ [Access AgentCore Memory through a gateway](memory-gateway-connector.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
