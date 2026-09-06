---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentmanager-claimmatchvaluetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentManager ClaimMatchValueType
<a name="aws-properties-bedrockagentcore-paymentmanager-claimmatchvaluetype"></a>

The value or values to match against an authorizing claim.

## Syntax
<a name="aws-properties-bedrockagentcore-paymentmanager-claimmatchvaluetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentmanager-claimmatchvaluetype-syntax.json"></a>

```
{
  "[MatchValueString](#cfn-bedrockagentcore-paymentmanager-claimmatchvaluetype-matchvaluestring)" : {{String}},
  "[MatchValueStringList](#cfn-bedrockagentcore-paymentmanager-claimmatchvaluetype-matchvaluestringlist)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentmanager-claimmatchvaluetype-syntax.yaml"></a>

```
  [MatchValueString](#cfn-bedrockagentcore-paymentmanager-claimmatchvaluetype-matchvaluestring): {{
    String}}
  [MatchValueStringList](#cfn-bedrockagentcore-paymentmanager-claimmatchvaluetype-matchvaluestringlist): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentmanager-claimmatchvaluetype-properties"></a>

`MatchValueString`  <a name="cfn-bedrockagentcore-paymentmanager-claimmatchvaluetype-matchvaluestring"></a>
A single string value to match against the claim.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9_.-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MatchValueStringList`  <a name="cfn-bedrockagentcore-paymentmanager-claimmatchvaluetype-matchvaluestringlist"></a>
An array of string values to match against the claim.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
