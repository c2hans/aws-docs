---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-targettrafficsplitentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule TargetTrafficSplitEntry
<a name="aws-properties-bedrockagentcore-gatewayrule-targettrafficsplitentry"></a>

An entry in a target traffic split configuration.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-targettrafficsplitentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-targettrafficsplitentry-syntax.json"></a>

```
{
  "[Description](#cfn-bedrockagentcore-gatewayrule-targettrafficsplitentry-description)" : {{String}},
  "[Fallback](#cfn-bedrockagentcore-gatewayrule-targettrafficsplitentry-fallback)" : {{Fallback}},
  "[Metadata](#cfn-bedrockagentcore-gatewayrule-targettrafficsplitentry-metadata)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Model](#cfn-bedrockagentcore-gatewayrule-targettrafficsplitentry-model)" : {{String}},
  "[Name](#cfn-bedrockagentcore-gatewayrule-targettrafficsplitentry-name)" : {{String}},
  "[TargetName](#cfn-bedrockagentcore-gatewayrule-targettrafficsplitentry-targetname)" : {{String}},
  "[Weight](#cfn-bedrockagentcore-gatewayrule-targettrafficsplitentry-weight)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-targettrafficsplitentry-syntax.yaml"></a>

```
  [Description](#cfn-bedrockagentcore-gatewayrule-targettrafficsplitentry-description): {{String}}
  [Fallback](#cfn-bedrockagentcore-gatewayrule-targettrafficsplitentry-fallback): {{
    Fallback}}
  [Metadata](#cfn-bedrockagentcore-gatewayrule-targettrafficsplitentry-metadata): {{
    {{Key}}: {{Value}}}}
  [Model](#cfn-bedrockagentcore-gatewayrule-targettrafficsplitentry-model): {{String}}
  [Name](#cfn-bedrockagentcore-gatewayrule-targettrafficsplitentry-name): {{String}}
  [TargetName](#cfn-bedrockagentcore-gatewayrule-targettrafficsplitentry-targetname): {{String}}
  [Weight](#cfn-bedrockagentcore-gatewayrule-targettrafficsplitentry-weight): {{Number}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-targettrafficsplitentry-properties"></a>

`Description`  <a name="cfn-bedrockagentcore-gatewayrule-targettrafficsplitentry-description"></a>
The description of this traffic split variant.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Fallback`  <a name="cfn-bedrockagentcore-gatewayrule-targettrafficsplitentry-fallback"></a>
The fallback configuration for this variant. Supported only for inference targets.
*Required*: No
*Type*: [Fallback](aws-properties-bedrockagentcore-gatewayrule-fallback.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Metadata`  <a name="cfn-bedrockagentcore-gatewayrule-targettrafficsplitentry-metadata"></a>
Key-value metadata associated with this traffic split variant.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Model`  <a name="cfn-bedrockagentcore-gatewayrule-targettrafficsplitentry-model"></a>
The model ID to send to the target for this variant. Supported only for inference targets. If you don't specify a model, the gateway sends the model from the original request.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9\-._/@:]*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrockagentcore-gatewayrule-targettrafficsplitentry-name"></a>
The name of this traffic split variant.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]([a-zA-Z0-9-]{0,62}[a-zA-Z0-9])?$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetName`  <a name="cfn-bedrockagentcore-gatewayrule-targettrafficsplitentry-targetname"></a>
The name of the target to route traffic to.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][-]?){1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weight`  <a name="cfn-bedrockagentcore-gatewayrule-targettrafficsplitentry-weight"></a>
The percentage of traffic to route to this variant.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `99`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
