---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-inferenceoperationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget InferenceOperationConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-inferenceoperationconfiguration"></a>

The configuration for a specific inference operation, including its request path and the models that the operation supports.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-inferenceoperationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-inferenceoperationconfiguration-syntax.json"></a>

```
{
  "[Models](#cfn-bedrockagentcore-gatewaytarget-inferenceoperationconfiguration-models)" : {{[ ModelEntry, ... ]}},
  "[Path](#cfn-bedrockagentcore-gatewaytarget-inferenceoperationconfiguration-path)" : {{String}},
  "[ProviderPath](#cfn-bedrockagentcore-gatewaytarget-inferenceoperationconfiguration-providerpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-inferenceoperationconfiguration-syntax.yaml"></a>

```
  [Models](#cfn-bedrockagentcore-gatewaytarget-inferenceoperationconfiguration-models): {{
    - ModelEntry}}
  [Path](#cfn-bedrockagentcore-gatewaytarget-inferenceoperationconfiguration-path): {{String}}
  [ProviderPath](#cfn-bedrockagentcore-gatewaytarget-inferenceoperationconfiguration-providerpath): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-inferenceoperationconfiguration-properties"></a>

`Models`  <a name="cfn-bedrockagentcore-gatewaytarget-inferenceoperationconfiguration-models"></a>
The list of models supported for this operation.
*Required*: No
*Type*: Array of [ModelEntry](aws-properties-bedrockagentcore-gatewaytarget-modelentry.md)
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Path`  <a name="cfn-bedrockagentcore-gatewaytarget-inferenceoperationconfiguration-path"></a>
The request path for this operation (for example, `/v1/messages` or `/v1/responses`).
*Required*: Yes
*Type*: String
*Pattern*: `^/[a-zA-Z0-9\-\._/]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderPath`  <a name="cfn-bedrockagentcore-gatewaytarget-inferenceoperationconfiguration-providerpath"></a>
The provider path to forward requests to, if it differs from the request path. For example, `/anthropic/v1/messages` when the provider expects a different path than the client-facing `/v1/messages`.
*Required*: No
*Type*: String
*Pattern*: `^/[a-zA-Z0-9\-\._/]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
