---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentmanager-claimmatchvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentManager ClaimMatchValue
<a name="aws-properties-bedrockagentcore-paymentmanager-claimmatchvalue"></a>

<a name="aws-properties-bedrockagentcore-paymentmanager-claimmatchvalue-description"></a>The `ClaimMatchValue` property type specifies Property description not available. for an [AWS::BedrockAgentCore::PaymentManager](aws-resource-bedrockagentcore-paymentmanager.md).

## Syntax
<a name="aws-properties-bedrockagentcore-paymentmanager-claimmatchvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentmanager-claimmatchvalue-syntax.json"></a>

```
{
  "[MatchValueString](#cfn-bedrockagentcore-paymentmanager-claimmatchvalue-matchvaluestring)" : {{String}},
  "[MatchValueStringList](#cfn-bedrockagentcore-paymentmanager-claimmatchvalue-matchvaluestringlist)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentmanager-claimmatchvalue-syntax.yaml"></a>

```
  [MatchValueString](#cfn-bedrockagentcore-paymentmanager-claimmatchvalue-matchvaluestring): {{
    String}}
  [MatchValueStringList](#cfn-bedrockagentcore-paymentmanager-claimmatchvalue-matchvaluestringlist): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentmanager-claimmatchvalue-properties"></a>

`MatchValueString`  <a name="cfn-bedrockagentcore-paymentmanager-claimmatchvalue-matchvaluestring"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9_.:/-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MatchValueStringList`  <a name="cfn-bedrockagentcore-paymentmanager-claimmatchvalue-matchvaluestringlist"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Maximum*: `255`
*Minimum*: `1 | 1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
