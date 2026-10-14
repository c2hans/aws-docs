---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/connect-an-ai-client-to-the-mcp-server.html
---

# Connect an AI client to the MCP server
<a name="connect-an-ai-client-to-the-mcp-server"></a>

If you set **EnableMcpServer** to `yes`, the solution exposes its operations as Model Context Protocol (MCP) tools. It does this through an Amazon Bedrock AgentCore Gateway. You can connect Claude Code, Kiro, or the OpenAI Codex CLI to call those tools. For an overview of the MCP server, see [MCP server for AI clients](mcp-server.md).

**Prerequisites**
Deploy the ASR administrator stack with **EnableMcpServer** set to `yes`. Use an AWS Region that supports Amazon Bedrock AgentCore. Before you connect a client, have your administrator grant your Web UI user the MCP tools you intend to use. For more information, see [Manage MCP tool access](manage-mcp-tool-access.md).

Read these values from the administrator stack’s **Outputs** in the AWS CloudFormation console.

 **McpGatewayUrl**
The HTTPS MCP endpoint your client connects to.

 **McpGatewayClientId**
The public Amazon Cognito OAuth client ID the client authenticates with.

 **McpGatewayScopes**
The OAuth scopes a client requests at login (`openid email profile`).

 **McpCodexCallbackUrl**
The exact OAuth callback URL that the OpenAI Codex CLI requires.

Each client signs in using the OAuth authentication flow with Amazon Cognito, so you authenticate as your own Web UI user. You can call only the tools that an administrator granted you, within your role tier. The MCP server name you set in the client is a local alias that you choose. It is not a deployed ASR resource name.

The Kiro adapter requires Kiro CLI v3 or newer. A client might use a callback URL that is not one of the solution’s defaults. In that case, add the URL with the **AdditionalMcpCallbackUrls** parameter when you deploy or update the administrator stack.

For connection commands for each client, see "Connect an AI client to the ASR MCP server" in the [solution README](https://github.com/aws-solutions/automated-security-response-on-aws/blob/main/README.md) on GitHub.
