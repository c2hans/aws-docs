---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-inferenceprovidertargetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget InferenceProviderTargetConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-inferenceprovidertargetconfiguration"></a>

The configuration for a provider-based inference target. This configuration explicitly defines the endpoint, model mapping, and operations used to route requests to a large language model (LLM) provider.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-inferenceprovidertargetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-inferenceprovidertargetconfiguration-syntax.json"></a>

```
{
  "[Endpoint](#cfn-bedrockagentcore-gatewaytarget-inferenceprovidertargetconfiguration-endpoint)" : {{String}},
  "[ModelMapping](#cfn-bedrockagentcore-gatewaytarget-inferenceprovidertargetconfiguration-modelmapping)" : {{ModelMapping}},
  "[Operations](#cfn-bedrockagentcore-gatewaytarget-inferenceprovidertargetconfiguration-operations)" : {{[ InferenceOperationConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-inferenceprovidertargetconfiguration-syntax.yaml"></a>

```
  [Endpoint](#cfn-bedrockagentcore-gatewaytarget-inferenceprovidertargetconfiguration-endpoint): {{String}}
  [ModelMapping](#cfn-bedrockagentcore-gatewaytarget-inferenceprovidertargetconfiguration-modelmapping): {{
    ModelMapping}}
  [Operations](#cfn-bedrockagentcore-gatewaytarget-inferenceprovidertargetconfiguration-operations): {{
    - InferenceOperationConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-inferenceprovidertargetconfiguration-properties"></a>

`Endpoint`  <a name="cfn-bedrockagentcore-gatewaytarget-inferenceprovidertargetconfiguration-endpoint"></a>
The HTTPS endpoint of the inference provider that the gateway forwards requests to.
*Required*: Yes
*Type*: String
*Pattern*: `^https://[a-zA-Z0-9\-\.]+(:[0-9]{1,5})?(/.*)?$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelMapping`  <a name="cfn-bedrockagentcore-gatewaytarget-inferenceprovidertargetconfiguration-modelmapping"></a>
The configuration that translates client-facing model IDs to the model IDs expected by the provider.
*Required*: No
*Type*: [ModelMapping](aws-properties-bedrockagentcore-gatewaytarget-modelmapping.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Operations`  <a name="cfn-bedrockagentcore-gatewaytarget-inferenceprovidertargetconfiguration-operations"></a>
A list of per-operation configurations that map request paths to the models supported for each operation.
*Required*: No
*Type*: Array of [InferenceOperationConfiguration](aws-properties-bedrockagentcore-gatewaytarget-inferenceoperationconfiguration.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
