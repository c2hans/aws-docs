---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gateway-mcpgatewayconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Gateway MCPGatewayConfiguration
<a name="aws-properties-bedrockagentcore-gateway-mcpgatewayconfiguration"></a>

The configuration for a Model Context Protocol (MCP) gateway. This structure defines how the gateway implements the MCP protocol.

## Syntax
<a name="aws-properties-bedrockagentcore-gateway-mcpgatewayconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gateway-mcpgatewayconfiguration-syntax.json"></a>

```
{
  "[Instructions](#cfn-bedrockagentcore-gateway-mcpgatewayconfiguration-instructions)" : {{String}},
  "[SearchType](#cfn-bedrockagentcore-gateway-mcpgatewayconfiguration-searchtype)" : {{String}},
  "[SessionConfiguration](#cfn-bedrockagentcore-gateway-mcpgatewayconfiguration-sessionconfiguration)" : {{SessionConfiguration}},
  "[StreamingConfiguration](#cfn-bedrockagentcore-gateway-mcpgatewayconfiguration-streamingconfiguration)" : {{StreamingConfiguration}},
  "[SupportedVersions](#cfn-bedrockagentcore-gateway-mcpgatewayconfiguration-supportedversions)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gateway-mcpgatewayconfiguration-syntax.yaml"></a>

```
  [Instructions](#cfn-bedrockagentcore-gateway-mcpgatewayconfiguration-instructions): {{String}}
  [SearchType](#cfn-bedrockagentcore-gateway-mcpgatewayconfiguration-searchtype): {{String}}
  [SessionConfiguration](#cfn-bedrockagentcore-gateway-mcpgatewayconfiguration-sessionconfiguration): {{
    SessionConfiguration}}
  [StreamingConfiguration](#cfn-bedrockagentcore-gateway-mcpgatewayconfiguration-streamingconfiguration): {{
    StreamingConfiguration}}
  [SupportedVersions](#cfn-bedrockagentcore-gateway-mcpgatewayconfiguration-supportedversions): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gateway-mcpgatewayconfiguration-properties"></a>

`Instructions`  <a name="cfn-bedrockagentcore-gateway-mcpgatewayconfiguration-instructions"></a>
The instructions for using the Model Context Protocol gateway. These instructions provide guidance on how to interact with the gateway.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SearchType`  <a name="cfn-bedrockagentcore-gateway-mcpgatewayconfiguration-searchtype"></a>
The search type for the Model Context Protocol gateway. This field specifies how the gateway handles search operations.
*Required*: No
*Type*: String
*Allowed values*: `SEMANTIC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SessionConfiguration`  <a name="cfn-bedrockagentcore-gateway-mcpgatewayconfiguration-sessionconfiguration"></a>
The session configuration for the MCP gateway. This configuration controls session behavior, including session timeout settings.
*Required*: No
*Type*: [SessionConfiguration](aws-properties-bedrockagentcore-gateway-sessionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamingConfiguration`  <a name="cfn-bedrockagentcore-gateway-mcpgatewayconfiguration-streamingconfiguration"></a>
The streaming configuration for the MCP gateway. This configuration controls whether response streaming is enabled for the gateway.
*Required*: No
*Type*: [StreamingConfiguration](aws-properties-bedrockagentcore-gateway-streamingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SupportedVersions`  <a name="cfn-bedrockagentcore-gateway-mcpgatewayconfiguration-supportedversions"></a>
The supported versions of the Model Context Protocol. This field specifies which versions of the protocol the gateway can use.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
