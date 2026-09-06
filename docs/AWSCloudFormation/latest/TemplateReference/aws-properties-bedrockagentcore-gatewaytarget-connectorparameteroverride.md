---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-connectorparameteroverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget ConnectorParameterOverride
<a name="aws-properties-bedrockagentcore-gatewaytarget-connectorparameteroverride"></a>

Specifies a parameter override for a connector tool, allowing you to control parameter visibility and descriptions.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-connectorparameteroverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-connectorparameteroverride-syntax.json"></a>

```
{
  "[Description](#cfn-bedrockagentcore-gatewaytarget-connectorparameteroverride-description)" : {{String}},
  "[Path](#cfn-bedrockagentcore-gatewaytarget-connectorparameteroverride-path)" : {{String}},
  "[Visible](#cfn-bedrockagentcore-gatewaytarget-connectorparameteroverride-visible)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-connectorparameteroverride-syntax.yaml"></a>

```
  [Description](#cfn-bedrockagentcore-gatewaytarget-connectorparameteroverride-description): {{String}}
  [Path](#cfn-bedrockagentcore-gatewaytarget-connectorparameteroverride-path): {{String}}
  [Visible](#cfn-bedrockagentcore-gatewaytarget-connectorparameteroverride-visible): {{Boolean}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-connectorparameteroverride-properties"></a>

`Description`  <a name="cfn-bedrockagentcore-gatewaytarget-connectorparameteroverride-description"></a>
An agent-facing description override for this parameter.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Path`  <a name="cfn-bedrockagentcore-gatewaytarget-connectorparameteroverride-path"></a>
A JSON Pointer path identifying the parameter (for example, `/numberOfResults` or `/filter`).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visible`  <a name="cfn-bedrockagentcore-gatewaytarget-connectorparameteroverride-visible"></a>
Whether this parameter is visible to the agent. If not specified, uses the service default.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
