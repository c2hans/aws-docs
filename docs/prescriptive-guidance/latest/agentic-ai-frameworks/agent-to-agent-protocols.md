---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/agent-to-agent-protocols.html
---

# Agent-to-agent protocols
<a name="agent-to-agent-protocols"></a>

The following table provides an overview of agentic protocols that enable multiple agents to collaborate, delegate tasks, and share information.

|
|
| Protocol | Ideal for | Considerations |
| --- |--- |--- |
| [MCP inter-agent communication](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-1-inter-agent-communication-on-mcp/) | Organizations seeking flexible agent collaboration patterns | + An extension to the Model Context Protocol (MCP) proposed by AWS that builds on its existing foundation for agent-to-agent communication<br />+ Enables seamless agent collaboration with OAuth-based security |
| [A2A protocol](https://github.com/a2aproject/A2A) | Cross-platform agent ecosystems | + Backed by Google<br />+ Newer standard with more limited adoption compared to MCP |

## Deciding among protocol options
<a name="deciding-among-protocol-options.38a4e70b-e8c9-5317-967c-d93f902ed4b3"></a>

When implementing agent-to-agent communication, match your specific communication requirements with the appropriate protocol capabilities. Different interaction patterns require different protocol features. The following table outlines common communication patterns and recommends the most suitable protocol choices for each scenario.

|
|
| Pattern | Description | Ideal protocol choice |
| --- |--- |--- |
| Simple request and response | One-off interactions between agents | MCP with stateless flows |
| Stateful dialogues | Ongoing conversations with context | MCP with session management |
| Multi-agent collaboration | Complex interactions between multiple agents | MCP inter-agent or AutoGen |
| Team-based workflows | Hierarchical agent teams with defined roles | MCP inter-agent, CrewAI, or AutoGen |

Beyond communication patterns, several technical and organizational factors can influence your protocol selection. The following table outlines key considerations that can help you evaluate which protocol aligns most closely with your specific implementation requirements.

|
|
| Consideration | Description | Example |
| --- |--- |--- |
| Security model | Authentication and authorization requirements | OAuth 2.0 in MCP |
| Deployment environment | Where agents will run and communicate | Distributed or single machine |
| Ecosystem compatibility | Integration with existing agent frameworks | LangChain or Strands Agents |
| Scalability needs | Expected growth in agent interactions | Streaming capabilities of MCP |
