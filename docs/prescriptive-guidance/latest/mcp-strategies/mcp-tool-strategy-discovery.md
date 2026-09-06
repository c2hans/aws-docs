---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/mcp-tool-strategy-discovery.html
---

# Tool discovery
<a name="mcp-tool-strategy-discovery"></a>

There are three approaches for discovering and registering tools in your agent with MCP servers: static definition, dynamic discovery, and search function.

## Static definition
<a name="mcp-tool-strategy-discovery-static"></a>

First, you can statically define the available tools directly in the agent code. In this approach you define a remote tool (a client-side reference object in a framework like Strands Agent SDK) for each tool provided by the MCP server that is accessed by an MCP client. The following example uses streamable HTTP transport:

```
from mcp.client.streamable_http import streamablehttp_client
from strands import Agent
from strands.tools.mcp import MCPClient

streamable_http_mcp_client = MCPClient(
    lambda: streamablehttp_client("https://mcp1:8000/mcp")
)

reverse_text = RemoteTool(
    name="reverseText",
    client=streamable_http_mcp_client
)

agent = Agent(tools=[reverse_text])
```

Individual tool registration helps you to be very selective about the tools you make available to the LLM, which minimizes the amount of context window used. The tradeoff is that it requires knowing the names of the available tools and can be brittle if the available tools change in the MCP server.

## Dynamic discovery
<a name="mcp-tool-strategy-discovery-dynamic"></a>

The next approach is using dynamic discovery and registering all the available tools with the agent. This approach consumes context linearly as more tools are added to the MCP server. The following is an example of this approach:

```
from mcp.client.streamable_http import streamablehttp_client
from strands import Agent
from strands.tools.mcp import MCPClient

streamable_http_mcp_client = MCPClient(
    lambda: streamablehttp_client("https://mcp1:8000/mcp")
)

with streamable_http_mcp_client:
    tools = streamable_http_mcp_client.list_tools_sync()
    agent = Agent(tools=tools)
```

Consider a scenario where a typical tool definition consumes approximately 250–500 tokens (including name, description, and schema). Registering 20 tools would consume 5,000–10,000 tokens of your context window. When you have a small number of MCP servers and you have control over the number of tools, this option is the simplest to implement. However, if the list of tools is expected to grow, it can create silent context management issues in your agents. An alternative variation of this approach is to use a tool filter parameter when calling `list_tools`, such as what the [Strands Agents SDK provides](https://strandsagents.com/docs/user-guide/concepts/tools/mcp-tools/#client-configuration), to reduce the number of tools that are registered with the agent.

## Search function
<a name="mcp-tool-strategy-discovery-search"></a>

The third option is to use a search function to find relevant tools during runtime. You list all available tools from your MCP server and then perform a semantic search over those tools based on the user prompt. Then, the resulting tools are registered with your agent. [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) provides a [native semantic search capability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-using-mcp-semantic-search.html) that can make this kind of solution easier to implement.

## Best practices for MCP tool discovery
<a name="mcp-tool-strategy-discovery-best-practices"></a>
+ **Context window preservation** – Pick a tool discovery and registration approach that conserves as much of your context window as possible.
+ **Use tool filtering or semantic search capabilities** – Dynamically provide the LLM with a scoped-down set of tools to choose from, which improves its accuracy and effectiveness at choosing the right tool. Tool filtering can operate on tool names (exact matching or patterns), tool descriptions (semantic matching), or domain or category tags. Semantic search is particularly effective for matching user intent against tool descriptions. Both approaches reduce context window use.
