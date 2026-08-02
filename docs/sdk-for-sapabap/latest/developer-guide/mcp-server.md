---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/mcp-server.html
---

# Using the AWS SDK for SAP ABAP Knowledge MCP Server
<a name="mcp-server"></a>

The AWS SDK for SAP ABAP Knowledge MCP Server is a specialized knowledge resource that enables AI coding assistants to generate accurate ABAP code for AWS integrations. By connecting your AI-enabled IDE to this server, you can describe what you want to build in natural language and receive syntactically correct ABAP code that properly invokes the AWS SDK for SAP ABAP.

The MCP server uses the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/), an open standard for connecting AI assistants to external knowledge sources. The server is updated daily in sync with AWS SDK for SAP ABAP releases, so your IDE always has access to current, accurate SDK information.

The AWS SDK for SAP ABAP Knowledge MCP Server is available at no additional cost. You only pay for the AWS resources and services that you consume in your SAP applications with the AWS SDK for SAP ABAP.

**Topics**
+ [Benefits](#mcp-server-benefits)
+ [Setting up the MCP server](#mcp-server-setup)
+ [What the MCP server can do](#mcp-server-capabilities)
+ [Important considerations](#mcp-server-limitations)

## Benefits
<a name="mcp-server-benefits"></a>

The AWS SDK for SAP ABAP Knowledge MCP Server provides the following benefits for ABAP developers.
+ **Accurate code generation** – Your AI coding assistant gains deep knowledge of AWS SDK for SAP ABAP-specific patterns, method signatures, data types, and exception handling. This eliminates common errors and significantly reduces compilation errors and debugging time.
+ **Instant SDK discovery** – The MCP server exposes the complete AWS SDK for SAP ABAP knowledge base, covering 200\+ AWS services. You can discover available services, operations, and data types without manually searching documentation.
+ **Always up to date** – The knowledge base is updated daily in sync with SDK releases. New services and updated method signatures are immediately available to your IDE.
+ **Zero installation** – Setup requires only pasting a URL into your IDE's MCP configuration. No local software installation, no dependency management, and no IT approval process is required.

## Setting up the MCP server
<a name="mcp-server-setup"></a>

To connect your IDE to the AWS SDK for SAP ABAP Knowledge MCP Server, add the following configuration to your IDE's MCP settings. The configuration format and file location may vary by IDE; refer to your IDE's MCP documentation for details.

The following example shows the configuration for Kiro. Add this to your workspace MCP config file `.kiro/settings/mcp.json` or your user-level config file `~/.kiro/settings/mcp.json`:

```
{
  "mcpServers": {
    "abap-sdk-knowledge": {
      "url": "https://sdk-for-sap-abap-knowledge-mcp.global.api.aws/mcp",
      "disabled": false,
      "autoApprove": ["*"]
    }
  }
}
```

The `autoApprove` setting allows your IDE to use the MCP server's tools without prompting for approval on each request. This is safe because the MCP server is read-only and does not modify any data or execute code.

After saving the configuration, your IDE will connect to the MCP server automatically. No restart is required in most IDEs. You can verify the connection by asking your AI assistant a question about the AWS SDK for SAP ABAP, such as *"What AWS services are available in the AWS SDK for SAP ABAP?"*

If your IDE does not connect to the MCP server, verify that your IDE supports the Model Context Protocol and that the configuration file syntax matches your IDE's requirements.

**Note**
The MCP server endpoint uses HTTPS and does not require authentication. Your IDE communicates with the server only when you ask your AI assistant questions related to AWS SDK for SAP ABAP usage. Your proprietary business logic and SAP application code remain within your development environment.

## What the MCP server can do
<a name="mcp-server-capabilities"></a>

Once connected, your AI coding assistant can use the following capabilities provided by the MCP server.
+ **Service discovery** – List and search all AWS services available in the AWS SDK for SAP ABAP, including service metadata and factory class names.
+ **Operation details** – Retrieve ABAP method signatures, input parameters, return types, and exception types for any SDK operation.
+ **Data type definitions** – Look up ABAP structure definitions for SDK data types, including field names and types.
+ **Code examples** – Retrieve working ABAP code examples for specific operations, covering common use cases for each service.
+ **Session and client creation** – Generate boilerplate ABAP code for creating SDK sessions, initializing service clients, and calling operations with correct exception handling.

For example, you can prompt your AI assistant with requests such as the following.
+ *"Write ABAP code to read a message from an SQS queue."*
+ *"Generate ABAP code to invoke an Amazon Bedrock model for text generation."*
+ *"Show me how to upload a file to Amazon S3 from ABAP."*

The AI assistant uses the MCP server's knowledge to generate syntactically correct ABAP code that follows AWS SDK for SAP ABAP conventions, including proper session creation, client initialization, and exception handling patterns.

## Important considerations
<a name="mcp-server-limitations"></a>

Keep the following in mind when using the AWS SDK for SAP ABAP Knowledge MCP Server.
+ The MCP server provides read-only access to SDK knowledge. It does not execute ABAP code or connect to SAP systems.
+ The MCP server covers only the AWS SDK for SAP ABAP. It does not provide general ABAP programming assistance unrelated to AWS SDK for SAP ABAP usage.
+ The MCP server does not support custom or third-party ABAP libraries.
+ The MCP server delivers documentation based on the latest version of the SDK, which may not match the version installed in your SAP system.
+ Generated code examples are starting points. Review and test all generated code before using it in production.
+ The quality and format of generated code may vary depending on your IDE's AI assistant capabilities.

Separately from the AWS SDK for SAP ABAP Knowledge MCP Server described on this page, AWS also offers the [AWS Knowledge MCP Server](https://awslabs.github.io/mcp/servers/aws-documentation-mcp-server/), which provides broad AWS service information, architectural guidance, and troubleshooting across all AWS services. The two servers complement each other and are especially effective when used together.
