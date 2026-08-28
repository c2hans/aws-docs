---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-targets-mcp.html
---

# MCP targets
<a name="gateway-targets-mcp"></a>

MCP targets operate in aggregation mode — the gateway acts as an MCP server whose capabilities combine those of all its MCP targets. Clients see a single consolidated `tools/list` response that includes tools from all attached MCP targets. MCP targets support capability synchronization, semantic tool search, and three-legged OAuth (3LO) at the target level.

The following topics describe the MCP target types that you can add to your gateway.

**Topics**
+ [AWS Lambda function targets](gateway-add-target-lambda.md)
+ [Amazon API Gateway REST API stages as targets](gateway-target-api-gateway.md)
+ [OpenAPI schema targets](gateway-schema-openapi.md)
+ [Smithy model targets](gateway-building-smithy-targets.md)
+ [MCP servers targets](gateway-target-MCPservers.md)
+ [Built-in templates from integration providers as targets](gateway-target-integrations.md)
+ [Built-in connectors as targets](gateway-target-connectors.md)
+ [Understand how AgentCore Gateway tools are named](gateway-tool-naming.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
