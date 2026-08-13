---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/tool-categories.html
---

# Tool categories
<a name="tool-categories"></a>

Building agent systems involves three main categories of tools.

## Protocol-based tools
<a name="protocol-based-tools.a47e2084-3d34-5fb6-8448-b190d904dfcb"></a>

[Protocol-based tools](protocol-based-tools.md) use standardized protocols for agent-to-tool communication:
+ [**MCP tools**](https://modelcontextprotocol.io/specification/2025-06-18/server/tools) – Open standard tools that work across frameworks with both local and remote execution options.
+ [**OpenAI function calling**](https://platform.openai.com/docs/guides/function-calling) – Proprietary tools that are specific to OpenAI models.
+ [**Anthropic tool use**](https://docs.claude.com/en/docs/agents-and-tools/tool-use/implement-tool-use#tool-use-system-prompt) – A variation on OpenAI function calling for proprietary tools specific to Anthropic Claude models.

## Framework-native tools
<a name="framework-native-tools.eef27b25-1e30-5ee5-ad9f-98fda4e2d9a2"></a>

[Framework-native tools](framework-native-tools.md) are built directly into specific agent frameworks:
+ **Strands Agents tools** – Lightweight, quick-to-implement tools that are specific to the Strands Agents framework.
+ **LangChain tools** – Python-based tools that are tightly integrated with the LangChain ecosystem.
+ **LlamaIndex tools** – Tools that are optimized for data retrieval and processing within LlamaIndex.

## Meta-tools
<a name="meta-tools.a320701c-8355-511f-ad67-baa4215aefdc"></a>

[Meta-tools](meta-tools.md) enhance agent workflows without directly taking external actions:
+ **Workflow tools** – Manage agent execution flow, branching logic, and state management.
+ **Agent graph tools** – Coordinate multiple agents in complex workflows.
+ **Memory tools** – Provide persistent storage and retrieval of information across agent sessions.
+ **Reflection tools** – Enable agents to analyze and improve their own performance.
