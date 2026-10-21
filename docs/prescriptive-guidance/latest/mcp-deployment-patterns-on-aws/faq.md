---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/faq.html
---

# Local MCP Servers
<a name="faq"></a>

**Overview**

Local MCP servers run directly on a developer's workstation or laptop, operating as standard processes that communicate with MCP client applications through local protocols. This deployment model provides the fastest path to integrating AI tools with local resources and development environments, making it ideal for personal productivity, experimentation, and early-stage development.

The local deployment pattern avoids external network hops. With the stdio transport, the MCP client launches the server as a subprocess and exchanges messages through its standard input and output streams. Alternatively, when both sides support Streamable HTTP, the client can connect to an MCP server through a loopback interface, the server runs independently and can serve multiple local clients, enabling shared or stateful services when concurrency, state and client isolation are managed appropriately. AI applications like Kiro, Claude Desktop/Code, Cursor, or custom development tools connect to local MCP servers through client-specific configuration or installation mechanisms. Stdio configurations typically specify the server command, arguments, and environment variables, whereas Streamable HTTP configurations specify a local endpoint URL.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/images/guide-img/596b5834-b415-44f3-9601-59b1ced57c6b/images/c42148ec-ff35-4172-afda-251cb0be02dd.png)

[AWS Documentation MCP server](https://awslabs.github.io/mcp/servers/aws-documentation-mcp-server)

Local MCP servers require minimal configuration, typically defined in the MCP client settings file. For example, provides tools to access AWS documentation, search for content, and get recommendations.

## Common use cases for MCP servers deployed locally
<a name="common-use-cases-for-mcp-servers-deployed-locally"></a>
+ File system access for code analysis: Most coding agents include native file- system tools. A local file-system MCP server adds value when users need consistent, scoped file operations across multiple MCP clients or want to restrict access to approved directories through a common interface.
+ Git repository integration: Developers build MCP servers that expose Git operations, allowing AI assistants to review commit history, analyze branch differences, and suggest merging conflict resolutions. This enables conversational interactions for version control tasks without leaving the AI interface.
+ Local development tools: Coding agents with shell access can run build commands and automated tests directly. A local MCP server can add value by exposing the same structured tool interface to compatible MCP clients. Tool schemas define inputs and structured results, while the server enforces access controls and permitted operations. For example, a server can expose a run\_tests tool for approved packages or read-only queries against a development database.
+ Personal Productivity Applications: Calendar integration enables AI assistants to check availability and schedule meetings. Note-taking applications like Obsidian or Notion expose their local databases through MCP, allowing AI to search notes, create entries, and maintain knowledge bases.

### Security and compliance considerations for local deployment
<a name="security-and-compliance-considerations-for-local-deployment.9254b86b-43cd-5557-9a27-85cbc0688e09"></a>

Local MCP servers can improve developer productivity by giving compatible AI applications low-latency access to approved tools and data on a developer workstation. This model is appropriate for individual development workflows when the organization can trust the server source and control the permissions granted to it.

A local MCP server can run with the user's operating system privileges and may access local files, credentials, network resources, and development tools. Organizations should manage this risk through existing endpoint and software-governance controls. Allow only approved server packages and distribution channels, require explicit approval for installation and tool execution, apply least-privilege file-system and network access, sandbox server processes where supported, centrally manage configurations and versions, and capture audit events required by policy.
