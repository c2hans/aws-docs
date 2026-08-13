---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-trafficsplitentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule TrafficSplitEntry
<a name="aws-properties-bedrockagentcore-gatewayrule-trafficsplitentry"></a>

An entry in a traffic split configuration, defining a named variant with a weight and configuration bundle reference.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-trafficsplitentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-trafficsplitentry-syntax.json"></a>

```
{
  "[ConfigurationBundle](#cfn-bedrockagentcore-gatewayrule-trafficsplitentry-configurationbundle)" : {{ConfigurationBundleReference}},
  "[Description](#cfn-bedrockagentcore-gatewayrule-trafficsplitentry-description)" : {{String}},
  "[Metadata](#cfn-bedrockagentcore-gatewayrule-trafficsplitentry-metadata)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Name](#cfn-bedrockagentcore-gatewayrule-trafficsplitentry-name)" : {{String}},
  "[Weight](#cfn-bedrockagentcore-gatewayrule-trafficsplitentry-weight)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-trafficsplitentry-syntax.yaml"></a>

```
  [ConfigurationBundle](#cfn-bedrockagentcore-gatewayrule-trafficsplitentry-configurationbundle): {{
    ConfigurationBundleReference}}
  [Description](#cfn-bedrockagentcore-gatewayrule-trafficsplitentry-description): {{String}}
  [Metadata](#cfn-bedrockagentcore-gatewayrule-trafficsplitentry-metadata): {{
    {{Key}}: {{Value}}}}
  [Name](#cfn-bedrockagentcore-gatewayrule-trafficsplitentry-name): {{String}}
  [Weight](#cfn-bedrockagentcore-gatewayrule-trafficsplitentry-weight): {{Number}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-trafficsplitentry-properties"></a>

`ConfigurationBundle`  <a name="cfn-bedrockagentcore-gatewayrule-trafficsplitentry-configurationbundle"></a>
The configuration bundle reference for this variant.
*Required*: Yes
*Type*: [ConfigurationBundleReference](aws-properties-bedrockagentcore-gatewayrule-configurationbundlereference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-bedrockagentcore-gatewayrule-trafficsplitentry-description"></a>
The description of this traffic split variant.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Metadata`  <a name="cfn-bedrockagentcore-gatewayrule-trafficsplitentry-metadata"></a>
Key-value metadata associated with this traffic split variant.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrockagentcore-gatewayrule-trafficsplitentry-name"></a>
The name of this traffic split variant.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]([a-zA-Z0-9-]{0,62}[a-zA-Z0-9])?$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weight`  <a name="cfn-bedrockagentcore-gatewayrule-trafficsplitentry-weight"></a>
The percentage of traffic to route to this variant. Weights across all entries must sum to 100.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `99`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
