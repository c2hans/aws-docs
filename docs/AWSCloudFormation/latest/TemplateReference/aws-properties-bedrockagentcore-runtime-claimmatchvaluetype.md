---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-claimmatchvaluetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime ClaimMatchValueType
<a name="aws-properties-bedrockagentcore-runtime-claimmatchvaluetype"></a>

The value or values to match for.
+ Include a `matchValueString` with the `EQUALS` operator to specify a string that matches the claim field value.
+ Include a `matchValueArray` to specify an array of string values. You can use the following operators:
  + Use `CONTAINS` to yield a match if the claim field value is in the array.
  + Use `CONTAINS_ANY` to yield a match if the claim field value contains any of the strings in the array.

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-claimmatchvaluetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-claimmatchvaluetype-syntax.json"></a>

```
{
  "[MatchValueString](#cfn-bedrockagentcore-runtime-claimmatchvaluetype-matchvaluestring)" : {{String}},
  "[MatchValueStringList](#cfn-bedrockagentcore-runtime-claimmatchvaluetype-matchvaluestringlist)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-claimmatchvaluetype-syntax.yaml"></a>

```
  [MatchValueString](#cfn-bedrockagentcore-runtime-claimmatchvaluetype-matchvaluestring): {{
    String}}
  [MatchValueStringList](#cfn-bedrockagentcore-runtime-claimmatchvaluetype-matchvaluestringlist): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-claimmatchvaluetype-properties"></a>

`MatchValueString`  <a name="cfn-bedrockagentcore-runtime-claimmatchvaluetype-matchvaluestring"></a>
The string value to match for.
*Required*: No
*Type*: String
*Pattern*: `[A-Za-z0-9_.-]+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchValueStringList`  <a name="cfn-bedrockagentcore-runtime-claimmatchvaluetype-matchvaluestringlist"></a>
An array of strings to check for a match.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
