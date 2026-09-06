---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/mcp-hosting-strategy.html
---

# MCP hosting strategy
<a name="mcp-hosting-strategy"></a>

Abstracting the available tools into MCP servers decouples your agent development from the available tools. This introduces the challenges of where you host your MCP server and how tools are organized inside those servers.

## Hosting approaches
<a name="mcp-hosting-strategy-approaches"></a>

There are three options for hosting your MCP servers: running them locally on an end-user machine, hosting them remotely, or hosting them through an MCP gateway. Each option has advantages and tradeoffs.

### Local hosting
<a name="local-hosting.06f822c9-a71e-527a-a675-cb813afe5538"></a>

Local hosting runs the MCP server as a subprocess on your local machine along with the agent that communicates with the server by using JSON-RPC over standard input and output streams. This approach does not require authentication between the client and the server. Tools can interact with local applications and files, use locally stored credentials, and they inherit the network access of the user's local machine. This is the simplest hosting pattern and has several benefits.

Many customers get started with MCP using local servers. They allow engineers to rapidly iterate and solve a variety of problems from their local environment. Consider an MCP server that connects to a Git repository that an engineer's coding assistant us using. Keeping the MCP server local makes a lot of sense because it can use the engineer's unique credentials to access the repository, and it does not add an extra network call to a remote MCP server. The following image shows a locally hosted MCP server being used with a coding agent in an IDE.

![Locally hosted MCP server being used with a coding agent in an IDE.](http://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/images/guide-img/2803ca34-2e01-4597-9d5d-d8b2e530a414/images/eb5a411f-5b63-449d-b6df-9230320ef9ce.png)

For these types of deployments, you must consider how the MCP servers are developed and distributed. Most customers develop an MCP registry where servers can be registered and downloaded by end users. It's very similar to a container registry where a user can search for specific capabilities and find the MCP servers suited to their needs.

There are public MCP registries, such as [Official MCP Registry](https://registry.modelcontextprotocol.io/), and there are privately hosted registries. Organizations typically align their MCP registry strategy with existing policies around open source software distribution, container registries, and internal package management. You should consider factors like security scanning, approval workflows, and compliance requirements.

However, local hosting introduces operational challenges that organizations should consider. First, end-users must discover, download, and configure MCP servers independently. This can add complexity to get started with each individual MCP server they use locally. Second, you cannot control the MCP server lifecycle, meaning that users may continue running outdated versions locally with security vulnerabilities or missing features. This can complicate meeting compliance requirements. Some IDEs and CLI tools, such as [Kiro](https://aws.amazon.com/documentation-overview/kiro/), allow organizations to [manage and control which MCP tools are available](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/mcp-governance.html), ensuring consistency and security across teams.

### Remote hosting
<a name="remote-hosting.c9835526-95b7-5ed0-be74-449d97f97894"></a>

The second option is to host remote MCP servers that are accessed over HTTP or HTTPS. This provides access to any network-connected client. Using remote hosting allows you to centrally control access to MCP resources and capabilities, implement authentication and authorization, and control the versioning and updates of the MCP server logic. Remote hosting still requires the use of an MCP registry so that end-users can discover the MCP servers that they want to use with their agent. The following image shows the remote hosting approach.

![Remote hosting approach.](http://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/images/guide-img/2803ca34-2e01-4597-9d5d-d8b2e530a414/images/b4c20570-0ec0-4d07-b96e-47d16950c1df.png)

From an agent development perspective, the experience is similar whether the MCP server is local or remote. The most significant change is implementing authentication and authorization, including both the agent's access to the MCP server and the server's access to external resources. Remote MCP server implementations must be carefully planned to consider multi-tenant access and privilege management. The [MCP governance strategy](mcp-governance-strategy.md) chapter contains more information about authentication and authorization considerations.

### MCP gateway
<a name="mcp-gateway.932dbbf8-7ab7-5bb4-850f-d1035413add9"></a>

The final option is using an MCP gateway. MCP gateways act as a centralized proxy between MCP clients and servers, and they orchestrate access to the registered MCP servers. Without a gateway, each agent needs to register every remote MCP server that it might want to use. A gateway allows the agent to connect to a single endpoint that manages the authentication, authorization, routing, and protocol translation. New MCP servers and tools can be added dynamically and made immediately available to the agent. The following image shows the MCP gateway approach.

![MCP gateway approach.](http://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/images/guide-img/2803ca34-2e01-4597-9d5d-d8b2e530a414/images/17eabbda-835e-4f62-a258-6899523577a2.png)

Some gateway solutions, such as [Docker MCP Gateway](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/), also manage the lifecycle of the MCP servers, launching servers on-demand as needed. MCP gateways, such as [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html), can also help manage tool discovery by providing [native semantic search capabilities](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-using-mcp-semantic-search.html). This provides agents with a single endpoint to connect with an MCP client and helps optimize their context window usage. The result is simple agents that can choose and use MCP tools effectively. However, it has similar identity-related challenges as the remote MCP server approach.

## Best practices for hosting MCP servers
<a name="mcp-hosting-strategy-best-practices"></a>
+ The spectrum of hosting options are not a one size fits all. Much of the usage of MCP servers today is local.
+ As you start to use remote MCP servers, your main consideration is consistent authentication and authorization to the MCP server and how the MCP server performs authentication and authorization to downstream resources.
+ MCP gateways simplify connectivity and authentication and authorization for hosting multiple remote MCP servers. They also provide capabilities to improve context window management by searching for applicable tools.
