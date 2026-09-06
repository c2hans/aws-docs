---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gateway-gatewayprotocolconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Gateway GatewayProtocolConfiguration
<a name="aws-properties-bedrockagentcore-gateway-gatewayprotocolconfiguration"></a>

The configuration for a gateway protocol. This structure defines how the gateway communicates with external services.

## Syntax
<a name="aws-properties-bedrockagentcore-gateway-gatewayprotocolconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gateway-gatewayprotocolconfiguration-syntax.json"></a>

```
{
  "[Mcp](#cfn-bedrockagentcore-gateway-gatewayprotocolconfiguration-mcp)" : {{MCPGatewayConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gateway-gatewayprotocolconfiguration-syntax.yaml"></a>

```
  [Mcp](#cfn-bedrockagentcore-gateway-gatewayprotocolconfiguration-mcp): {{
    MCPGatewayConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gateway-gatewayprotocolconfiguration-properties"></a>

`Mcp`  <a name="cfn-bedrockagentcore-gateway-gatewayprotocolconfiguration-mcp"></a>
The configuration for the Model Context Protocol (MCP). This protocol enables communication between Amazon Bedrock Agent and external tools.
*Required*: Yes
*Type*: [MCPGatewayConfiguration](aws-properties-bedrockagentcore-gateway-mcpgatewayconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
