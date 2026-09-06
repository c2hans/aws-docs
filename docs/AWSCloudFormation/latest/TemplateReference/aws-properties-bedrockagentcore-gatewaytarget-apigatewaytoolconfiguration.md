---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-apigatewaytoolconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget ApiGatewayToolConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-apigatewaytoolconfiguration"></a>

The configuration for defining REST API tool filters and overrides for the gateway target.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-apigatewaytoolconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-apigatewaytoolconfiguration-syntax.json"></a>

```
{
  "[ToolFilters](#cfn-bedrockagentcore-gatewaytarget-apigatewaytoolconfiguration-toolfilters)" : {{[ ApiGatewayToolFilter, ... ]}},
  "[ToolOverrides](#cfn-bedrockagentcore-gatewaytarget-apigatewaytoolconfiguration-tooloverrides)" : {{[ ApiGatewayToolOverride, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-apigatewaytoolconfiguration-syntax.yaml"></a>

```
  [ToolFilters](#cfn-bedrockagentcore-gatewaytarget-apigatewaytoolconfiguration-toolfilters): {{
    - ApiGatewayToolFilter}}
  [ToolOverrides](#cfn-bedrockagentcore-gatewaytarget-apigatewaytoolconfiguration-tooloverrides): {{
    - ApiGatewayToolOverride}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-apigatewaytoolconfiguration-properties"></a>

`ToolFilters`  <a name="cfn-bedrockagentcore-gatewaytarget-apigatewaytoolconfiguration-toolfilters"></a>
A list of path and method patterns to expose as tools using metadata from the REST API's OpenAPI specification.
*Required*: Yes
*Type*: Array of [ApiGatewayToolFilter](aws-properties-bedrockagentcore-gatewaytarget-apigatewaytoolfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ToolOverrides`  <a name="cfn-bedrockagentcore-gatewaytarget-apigatewaytoolconfiguration-tooloverrides"></a>
A list of explicit tool definitions with optional custom names and descriptions.
*Required*: No
*Type*: Array of [ApiGatewayToolOverride](aws-properties-bedrockagentcore-gatewaytarget-apigatewaytooloverride.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
