---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/meta-tools.html
---

# Meta-tools
<a name="meta-tools"></a>

Meta-tools don't directly interact with external systems. Instead, they enhance agent capabilities by implementing agentic patterns. This section discusses workflow, agent graph, and memory meta-tools.

## Workflow meta-tools
<a name="workflow-meta-tools.2502a690-8753-5460-9de0-7119ffb11b2e"></a>

Workflow meta-tools manage the flow of agent execution:
+ **State management** – Maintain context across multiple agent interactions
+ **Branching logic** – Enable conditional execution paths
+ **Retry mechanisms** – Handle failures with configurable retry strategies

Example frameworks with workflow meta-tools include [LangGraph](https://github.com/langchain-ai/langgraph) and [Strands Agents workflow capabilities](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/).

## Agent graph meta-tools
<a name="agent-graph-meta-tools.761afa87-5320-512e-900a-3a25fd73750b"></a>

Agent graph meta-tools coordinate multiple agents working together:
+ **Task delegation** – Assign subtasks to specialized agents
+ **Result aggregation** – Combine outputs from multiple agents
+ **Conflict resolution** – Resolve disagreements between agents

Frameworks like [AutoGen](https://microsoft.github.io/autogen/docs/Use-Cases/agent_chat) and [CrewAI](https://github.com/crewAIInc/crewAI) specialize in agent graph coordination.

## Memory meta-tools
<a name="memory-meta-tools.4a437473-3b88-5e5b-b296-3b85cd0376fc"></a>

Memory meta-tools provide persistent storage and retrieval:
+ **Conversation history** – Maintain context across sessions
+ **Knowledge bases** – Store and retrieve domain-specific information
+ **Vector stores** – Enable semantic search capabilities

The resource system in Model Context Protocol (MCP) provides a standardized way to implement memory meta-tools that work across different agent frameworks.
