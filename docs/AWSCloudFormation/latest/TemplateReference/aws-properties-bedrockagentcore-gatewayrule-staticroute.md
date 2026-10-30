---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-staticroute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule StaticRoute
<a name="aws-properties-bedrockagentcore-gatewayrule-staticroute"></a>

A static route to a single gateway target.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-staticroute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-staticroute-syntax.json"></a>

```
{
  "[Fallback](#cfn-bedrockagentcore-gatewayrule-staticroute-fallback)" : {{Fallback}},
  "[Model](#cfn-bedrockagentcore-gatewayrule-staticroute-model)" : {{String}},
  "[TargetName](#cfn-bedrockagentcore-gatewayrule-staticroute-targetname)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-staticroute-syntax.yaml"></a>

```
  [Fallback](#cfn-bedrockagentcore-gatewayrule-staticroute-fallback): {{
    Fallback}}
  [Model](#cfn-bedrockagentcore-gatewayrule-staticroute-model): {{String}}
  [TargetName](#cfn-bedrockagentcore-gatewayrule-staticroute-targetname): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-staticroute-properties"></a>

`Fallback`  <a name="cfn-bedrockagentcore-gatewayrule-staticroute-fallback"></a>
The fallback configuration for this route. Supported only for inference targets.
*Required*: No
*Type*: [Fallback](aws-properties-bedrockagentcore-gatewayrule-fallback.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Model`  <a name="cfn-bedrockagentcore-gatewayrule-staticroute-model"></a>
The model ID to send to the target. Supported only for inference targets. If you don't specify a model, the gateway sends the model from the original request.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9\-._/@:]*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetName`  <a name="cfn-bedrockagentcore-gatewayrule-staticroute-targetname"></a>
The name of the target to route requests to.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][-]?){1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
