---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-mcptargetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget McpTargetConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-mcptargetconfiguration"></a>

The Model Context Protocol (MCP) configuration for a target. This structure defines how the gateway uses MCP to communicate with the target.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-mcptargetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-mcptargetconfiguration-syntax.json"></a>

```
{
  "[ApiGateway](#cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-apigateway)" : {{ApiGatewayTargetConfiguration}},
  "[Connector](#cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-connector)" : {{ConnectorTargetConfiguration}},
  "[Lambda](#cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-lambda)" : {{McpLambdaTargetConfiguration}},
  "[McpServer](#cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-mcpserver)" : {{McpServerTargetConfiguration}},
  "[OpenApiSchema](#cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-openapischema)" : {{ApiSchemaConfiguration}},
  "[SmithyModel](#cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-smithymodel)" : {{ApiSchemaConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-mcptargetconfiguration-syntax.yaml"></a>

```
  [ApiGateway](#cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-apigateway): {{
    ApiGatewayTargetConfiguration}}
  [Connector](#cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-connector): {{
    ConnectorTargetConfiguration}}
  [Lambda](#cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-lambda): {{
    McpLambdaTargetConfiguration}}
  [McpServer](#cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-mcpserver): {{
    McpServerTargetConfiguration}}
  [OpenApiSchema](#cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-openapischema): {{
    ApiSchemaConfiguration}}
  [SmithyModel](#cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-smithymodel): {{
    ApiSchemaConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-mcptargetconfiguration-properties"></a>

`ApiGateway`  <a name="cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-apigateway"></a>
The configuration for an Amazon API Gateway target.
*Required*: No
*Type*: [ApiGatewayTargetConfiguration](aws-properties-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Connector`  <a name="cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-connector"></a>
The connector integration configuration for the Model Context Protocol target. This configuration defines how the gateway uses a pre-built connector to communicate with the target.
*Required*: No
*Type*: [ConnectorTargetConfiguration](aws-properties-bedrockagentcore-gatewaytarget-connectortargetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Lambda`  <a name="cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-lambda"></a>
The Lambda configuration for the Model Context Protocol target. This configuration defines how the gateway uses a Lambda function to communicate with the target.
*Required*: No
*Type*: [McpLambdaTargetConfiguration](aws-properties-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`McpServer`  <a name="cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-mcpserver"></a>
The configuration for an MCP server target.
*Required*: No
*Type*: [McpServerTargetConfiguration](aws-properties-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OpenApiSchema`  <a name="cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-openapischema"></a>
The OpenAPI schema for the Model Context Protocol target. This schema defines the API structure of the target.
*Required*: No
*Type*: [ApiSchemaConfiguration](aws-properties-bedrockagentcore-gatewaytarget-apischemaconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmithyModel`  <a name="cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-smithymodel"></a>
The Smithy model for the Model Context Protocol target. This model defines the API structure of the target using the Smithy specification.
*Required*: No
*Type*: [ApiSchemaConfiguration](aws-properties-bedrockagentcore-gatewaytarget-apischemaconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
