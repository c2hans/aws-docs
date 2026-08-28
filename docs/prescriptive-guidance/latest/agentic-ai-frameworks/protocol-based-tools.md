---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/protocol-based-tools.html
---

# Protocol-based tools
<a name="protocol-based-tools"></a>

When considering protocol-based tools, the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) provides the most comprehensive and flexible foundation for tool integration. As stated in the [AWS Open Source blog post on agent interoperability](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-1-inter-agent-communication-on-mcp/), AWS has embraced MCP as a strategic protocol, actively contributing to its development.

The following table describes options for MCP tool deployment.

|
|
| Deployment model | Description | Ideal for | Implementation |
| --- |--- |--- |--- |
| Local stdio-based | Tools run in the same process as the agent | Development, testing, and simple tools | Quick to implement with no network overhead |
| Local server-sent events (SSE)-based (legacy) | Tools run locally but communicate over HTTP | More complex local tools with separation of concerns | Better isolation but still low latency |
| Remote HTTP Streamable | Tools run on remote servers | Production environments and shared tools | Scalable and centrally managed |

The official MCP SDKs are available for building MCP tools:
+ [Python SDK](https://github.com/modelcontextprotocol/python-sdk) – Comprehensive implementation with full protocol support
+ [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) – JavaScript/TypeScript implementation for web applications
+ [Java SDK](https://github.com/modelcontextprotocol/java-sdk) – Java implementation for enterprise applications

These SDKs provide the building blocks for creating MCP-compatible tools in your preferred language, with consistent implementations of the protocol specification.

In addition, AWS has implemented MCP in the [Strands Agents SDK](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/). The Strands Agents SDK provides a straightforward way to create and use MCP-compatible tools. Comprehensive documentation is available in the [Strands Agents GitHub repository](https://github.com/strands-agents). For simpler use cases or when working outside of the Strands Agents framework, the official MCP SDKs offer direct implementations of the protocol in multiple languages.

## Security features of MCP tools
<a name="security-features-of-mcp-tools.4b302df1-cae8-5cb2-9659-0a2292c948c9"></a>

Security features of MCP tools include the following:
+ **OAuth 2.0/2.1 authentication** – Industry-standard authentication
+ **Permission scoping** – Fine-grained access control for tools
+ **Tool capability discovery** – Dynamic discovery of available tools
+ **Structured error handling** – Consistent error patterns

## Getting started with MCP tools
<a name="getting-started-with-mcp-tools.ee46a782-5e95-5586-987a-2f3cb0008a43"></a>

To implement MCP for tool integration, take the following actions:

1. Explore the [Strands Agents SDK ](https://strandsagents.com/)for a production-ready MCP implementation.

1. Review the [MCP technical documentation](https://modelcontextprotocol.io/) to understand core concepts.

1. Use the practical examples described in this [AWS Open Source Blog](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/) post.

1. Start with simple local tools before progressing to remote tools.

1. Join the [MCP community](https://github.com/modelcontextprotocol/modelcontextprotocol) to influence the protocol's evolution.

## Explore AgentCore Gateway
<a name="explore-9999999999999999brac--gateway.21dd769b-7c4e-5e6b-93d1-3acf2955ae10"></a>

[Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) provides an easy and secure way for developers to build, deploy, discover, and connect to MCP tools, and other target endpoints at scale. With AgentCore Gateway, developers can convert APIs, AWS Lambda functions, and existing services into MCP-compatible tools. Then, with just a few lines of code, they can make these tools available to agents through AgentCore Gateway endpoints. AgentCore Gateway supports OpenAPI, Smithy, and Lambda as input types, and is the only solution that provides both comprehensive ingress authentication and egress authentication in a fully-managed service.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
