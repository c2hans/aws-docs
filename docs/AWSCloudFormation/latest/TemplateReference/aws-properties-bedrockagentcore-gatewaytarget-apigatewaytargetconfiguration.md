---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget ApiGatewayTargetConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration"></a>

The configuration for an Amazon API Gateway target.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration-syntax.json"></a>

```
{
  "[ApiGatewayToolConfiguration](#cfn-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration-apigatewaytoolconfiguration)" : {{ApiGatewayToolConfiguration}},
  "[RestApiId](#cfn-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration-restapiid)" : {{String}},
  "[Stage](#cfn-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration-stage)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration-syntax.yaml"></a>

```
  [ApiGatewayToolConfiguration](#cfn-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration-apigatewaytoolconfiguration): {{
    ApiGatewayToolConfiguration}}
  [RestApiId](#cfn-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration-restapiid): {{String}}
  [Stage](#cfn-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration-stage): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration-properties"></a>

`ApiGatewayToolConfiguration`  <a name="cfn-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration-apigatewaytoolconfiguration"></a>
The configuration for defining REST API tool filters and overrides for the gateway target.
*Required*: Yes
*Type*: [ApiGatewayToolConfiguration](aws-properties-bedrockagentcore-gatewaytarget-apigatewaytoolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RestApiId`  <a name="cfn-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration-restapiid"></a>
The ID of the API Gateway REST API.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Stage`  <a name="cfn-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration-stage"></a>
The ID of the stage of the REST API to add as a target.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
