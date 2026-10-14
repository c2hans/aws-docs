---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/mcp-server.html
---

# MCP server for AI clients
<a name="mcp-server"></a>

The solution includes an optional Model Context Protocol (MCP) server. This server exposes the deployed solution’s operations as tools to AI coding clients such as Claude Code, Kiro, and the OpenAI Codex CLI. The server is off by default.

To enable the MCP server, set the **EnableMcpServer** parameter to `yes` when you deploy the administrator stack. Use an AWS Region that supports [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/). For how to connect a client after deployment, see [Connect an AI client to the MCP server](connect-an-ai-client-to-the-mcp-server.md).

The solution delivers the MCP server through an Amazon Bedrock AgentCore Gateway. It deploys the gateway as its own nested stack. The MCP server is independent of the Web UI. You can deploy the MCP server with or without the Web UI. Either feature deploys the shared core services: the Amazon Cognito user pool, the solution API, and the user and account mapping table. The MCP Lambda function invokes the solution’s API Lambda function directly rather than over HTTP.

For configuration and operational detail, see the linked topics. The following list summarizes the MCP server’s security controls at a conceptual level:
+  **Token verification before use.** The server verifies the Amazon Cognito access token’s signature. It also confirms that Amazon Cognito issued the token for the server’s own application client before it reads any claim. The server rejects a token that fails either check.
+  **Tier-scoped tool grants.** An AI client can call only the tools that an administrator granted the signed-in user, within that user’s role tier. You can grant account operators and delegated administrators different sets of tools. For how an administrator manages these grants, see [Manage MCP tool access](manage-mcp-tool-access.md).
+  **Metrics and alarms.** The server emits per-tool metrics. When you enable CloudWatch alarms, it also raises an alarm on tool errors. For the dashboard section, see [Monitor the solution's operations with an Amazon CloudWatch dashboard](monitor-the-solutions-operations-with-an-amazon-cloudwatch-dashboard.md).
