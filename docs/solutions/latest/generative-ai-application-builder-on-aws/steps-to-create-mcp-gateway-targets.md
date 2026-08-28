---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/steps-to-create-mcp-gateway-targets.html
---

# Steps to create different MCP Gateway Targets
<a name="steps-to-create-mcp-gateway-targets"></a>

Amazon Bedrock AgentCore Gateway allows you to transform existing AWS services and APIs into MCP tools that can be used by your agents. The Gateway supports multiple target types, enabling you to integrate various backend services seamlessly.

The following target types are supported:
+  **Lambda targets**: Transform AWS Lambda functions into MCP tools. For detailed instructions, refer to the [Amazon Bedrock AgentCore Developer Guide - Add Lambda targets](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-add-target-lambda.html).
+  **OpenAPI targets**: Use OpenAPI specifications to define and expose REST APIs as MCP tools. For detailed instructions, refer to the [Amazon Bedrock AgentCore Developer Guide - OpenAPI schema](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-schema-openapi.html).
+  **Smithy targets**: Build MCP tools using Smithy model definitions for type-safe API integrations. For detailed instructions, refer to the [Amazon Bedrock AgentCore Developer Guide - Building Smithy targets](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-building-smithy-targets.html).
+  **MCP Server targets**: Connect directly to external MCP servers via URL endpoints, allowing you to integrate existing MCP servers. For detailed instructions, refer to the [Amazon Bedrock AgentCore Developer Guide - MCP servers targets](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-MCPservers.html).

For additional examples and tutorials on creating MCP Gateway targets, visit the [Amazon Bedrock AgentCore samples repository](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway/01-transform-lambda-into-mcp-tools).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Generative AI Application Builder on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
