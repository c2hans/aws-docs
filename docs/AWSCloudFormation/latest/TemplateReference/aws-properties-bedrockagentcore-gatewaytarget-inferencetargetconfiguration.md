---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-inferencetargetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget InferenceTargetConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-inferencetargetconfiguration"></a>

The configuration for an inference target. An inference target routes requests to a large language model (LLM) provider, either through a built-in connector or an explicitly configured provider.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-inferencetargetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-inferencetargetconfiguration-syntax.json"></a>

```
{
  "[Connector](#cfn-bedrockagentcore-gatewaytarget-inferencetargetconfiguration-connector)" : {{InferenceConnectorTargetConfiguration}},
  "[Provider](#cfn-bedrockagentcore-gatewaytarget-inferencetargetconfiguration-provider)" : {{InferenceProviderTargetConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-inferencetargetconfiguration-syntax.yaml"></a>

```
  [Connector](#cfn-bedrockagentcore-gatewaytarget-inferencetargetconfiguration-connector): {{
    InferenceConnectorTargetConfiguration}}
  [Provider](#cfn-bedrockagentcore-gatewaytarget-inferencetargetconfiguration-provider): {{
    InferenceProviderTargetConfiguration}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-inferencetargetconfiguration-properties"></a>

`Connector`  <a name="cfn-bedrockagentcore-gatewaytarget-inferencetargetconfiguration-connector"></a>
The connector-based inference configuration. Use this option to route requests to an LLM provider through a built-in connector that includes predefined provider rules.
*Required*: No
*Type*: [InferenceConnectorTargetConfiguration](aws-properties-bedrockagentcore-gatewaytarget-inferenceconnectortargetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Provider`  <a name="cfn-bedrockagentcore-gatewaytarget-inferencetargetconfiguration-provider"></a>
The provider-based inference configuration. Use this option to explicitly configure the endpoint, model mapping, and operations for an LLM provider.
*Required*: No
*Type*: [InferenceProviderTargetConfiguration](aws-properties-bedrockagentcore-gatewaytarget-inferenceprovidertargetconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
