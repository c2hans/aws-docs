---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-inferenceconnectorsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget InferenceConnectorSource
<a name="aws-properties-bedrockagentcore-gatewaytarget-inferenceconnectorsource"></a>

The source identifying the inference connector.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-inferenceconnectorsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-inferenceconnectorsource-syntax.json"></a>

```
{
  "[ConnectorId](#cfn-bedrockagentcore-gatewaytarget-inferenceconnectorsource-connectorid)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-inferenceconnectorsource-syntax.yaml"></a>

```
  [ConnectorId](#cfn-bedrockagentcore-gatewaytarget-inferenceconnectorsource-connectorid): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-inferenceconnectorsource-properties"></a>

`ConnectorId`  <a name="cfn-bedrockagentcore-gatewaytarget-inferenceconnectorsource-connectorid"></a>
The identifier for the inference connector (for example, `bedrock-mantle`, `openai`, or `anthropic`).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
