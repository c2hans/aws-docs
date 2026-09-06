---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/faq.html
---

# Local MCP Servers
<a name="faq"></a>

**Overview**

Local MCP servers run directly on a developer's workstation or laptop, operating as standard processes that communicate with MCP client applications through local protocols. This deployment model provides the fastest path to integrating AI tools with local resources and development environments, making it ideal for personal productivity, experimentation, and early-stage development.

The local architecture eliminates network latency entirely, as communication occurs through standard input/output (stdio) streams or inter-process communication (IPC) mechanisms. AI applications like Kiro, Claude Desktop/Code, Cursor, or custom development tools connect to local MCP servers through configuration files that specify the server's executable path and startup parameters.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-deployment-patterns-on-aws/images/guide-img/596b5834-b415-44f3-9601-59b1ced57c6b/images/c42148ec-ff35-4172-afda-251cb0be02dd.png)

[AWS Documentation MCP server](https://awslabs.github.io/mcp/servers/aws-documentation-mcp-server)

Local MCP servers require minimal configuration, typically defined in the MCP client settings file. For example, provides tools to access AWS documentation, search for content, and get recommendations.

For test the MCP servers, developers can use the [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) which is an official tool from Anthropic that provides an interactive web-based interface for exploring MCP server capabilities, testing protocol compliance, and troubleshooting integration issues.

## Common use cases for MCP servers deployed locally
<a name="common-use-cases-for-mcp-servers-deployed-locally"></a>
+ File system access for code analysis: AI-powered code editors use MCP servers to analyze project files, provide context-aware suggestions, and perform automated refactoring. The MCP server grants read and write access to specific directories, enabling intelligent code completion based on project structure, automated documentation generation from code comments, and refactoring operations that maintain consistency across multiple files
+ Git repository integration: Developers build MCP servers that expose Git operations, allowing AI assistants to review commit history, analyze branch differences, and suggest merging conflict resolutions. This enables conversational interactions for version control tasks without leaving the AI interface.
+ Local development tools: Integration with local build tools and test runners enables conversational commands like "run the unit tests" or "build the Docker image." Local database access for development instances provides AI with query capabilities for testing and data exploration during development.
+ Personal Productivity Applications: Calendar integration enables AI assistants to check availability and schedule meetings. Note-taking applications like Obsidian or Notion expose their local databases through MCP, allowing AI to search notes, create entries, and maintain knowledge bases.

### Limitations of local deployment
<a name="limitations-of-local-deployment.31e3efeb-5b84-5950-8632-3e0aea2c3526"></a>

While local MCP servers are convenient for individual developers, they have inherent limitations that make them unsuitable for team collaboration and production workloads and face significant limitations:
+ Security and Compliance risks: Sensitive credentials and API keys stored on individual workstations increase exposure risk through lost devices, malware, or inadequate access controls. Audit logging fragments across multiple machines, making compliance verification difficult. Organizations cannot enforce centralized security policies or access controls.
+ Environment inconsistency: Each developer must install and configure MCP servers independently, leading to environment drift and version inconsistencies across team members. Sharing capabilities require duplicating deployment on each workstation, complicating maintenance, and updates.
+ Limited scalability: Consumer laptops lack compute resources, memory, and storage for enterprise-scale data processing. Local servers cannot handle concurrent requests from multiple users or applications, restricting use to single-user scenarios.
+ Reliability concerns: Workstation reboots, network disconnections, and hardware failures impact availability. No built-in redundancy or failover capabilities exist. Service availability depends entirely on the developer's workstation being powered on and connected.
+ These limitations drive the need for remote deployment models on cloud infrastructure for team collaboration and production workloads.
