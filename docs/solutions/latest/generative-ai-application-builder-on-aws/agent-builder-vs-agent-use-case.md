---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/agent-builder-vs-agent-use-case.html
---

# Agent Builder vs Bedrock Agent use case
<a name="agent-builder-vs-agent-use-case"></a>

This solution provides two distinct approaches for working with AI agents, each suited for different use cases and requirements:

| Feature | Bedrock Agent use case | Agent Builder |
| --- | --- | --- |
|  **Purpose**  | Invoke pre-deployed Amazon Bedrock Agents | Build, deploy, and manage custom agents |
|  **Configuration**  | Agent ID and Alias ID only | Full agent configuration: system prompts, models, MCP servers, memory |
|  **Deployment**  | Simple invocation layer | Complete agent lifecycle on AgentCore Runtime |
|  **Runtime**  | Amazon Bedrock Agents service | Amazon Bedrock AgentCore with Strands SDK |
|  **Tool Integration**  | Configured in Bedrock Agents console | Model Context Protocol (MCP) servers and built in Strands tools |
|  **Memory**  | Managed by Bedrock Agents (up to 30 days) | AgentCore Memory with configurable short-term and long-term retention |
|  **Customization**  | Limited to pre-deployed agent settings | Full control over prompts, models, tools, and behavior |
|  **Best for**  | Quick deployment of existing agents | Custom agent development and production deployments |

**Note**
Both options support real-time streaming, conversation history, and enterprise-grade security.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Generative AI Application Builder on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
