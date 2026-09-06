---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/getting-started-with-mcp.html
---

# Getting started with MCP
<a name="getting-started-with-mcp"></a>

AWS actively supports the Model Context Protocol (MCP) through contributions to the protocol's development and implementation. AWS is collaborating with leading open-source agent frameworks, including LangGraph, CrewAI, and LlamaIndex, to shape the future of inter-agent communication on the protocol.

To implement the MCP in your agent architecture, take the following actions:

1. Explore MCP implementations in frameworks like the Strands Agents SDK.

1. Review the [Model Context Protocol](https://modelcontextprotocol.io/introduction) technical documentation.

1. Read [Open Protocols for Agent Interoperability Part 1: Inter-Agent Communication on MCP](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-1-inter-agent-communication-on-mcp/) (AWS Blog) to learn about agent interoperability.

1. Join the [MCP community](https://github.com/orgs/modelcontextprotocol/discussions) to influence the protocol's evolution.

MCP provides a communication layer that enables agents to interact with external data and services and can also be used to enable agents to interact with other agents. The protocol's [Streamable HTTP transport](https://modelcontextprotocol.io/docs/concepts/transports#streamable-http) implementation gives developers a comprehensive set of interaction patterns without having to reinvent the wheel. These patterns support both stateless request/response flows and stateful session management with persistent IDs.

By adopting open protocols like MCP, you position your organization to build agent systems that remain flexible, interoperable, and adaptable as AI technology evolves.

For information about agent-to-tool protocol implementation, see Tool integration strategy later in this guide.
