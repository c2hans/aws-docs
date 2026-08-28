---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gateway-claimmatchvaluetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Gateway ClaimMatchValueType
<a name="aws-properties-bedrockagentcore-gateway-claimmatchvaluetype"></a>

The value or values to match for.
+ Include a `matchValueString` with the `EQUALS` operator to specify a string that matches the claim field value.
+ Include a `matchValueArray` to specify an array of string values. You can use the following operators:
  + Use `CONTAINS` to yield a match if the claim field value is in the array.
  + Use `CONTAINS_ANY` to yield a match if the claim field value contains any of the strings in the array.

## Syntax
<a name="aws-properties-bedrockagentcore-gateway-claimmatchvaluetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gateway-claimmatchvaluetype-syntax.json"></a>

```
{
  "[MatchValueString](#cfn-bedrockagentcore-gateway-claimmatchvaluetype-matchvaluestring)" : {{String}},
  "[MatchValueStringList](#cfn-bedrockagentcore-gateway-claimmatchvaluetype-matchvaluestringlist)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gateway-claimmatchvaluetype-syntax.yaml"></a>

```
  [MatchValueString](#cfn-bedrockagentcore-gateway-claimmatchvaluetype-matchvaluestring): {{
    String}}
  [MatchValueStringList](#cfn-bedrockagentcore-gateway-claimmatchvaluetype-matchvaluestringlist): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gateway-claimmatchvaluetype-properties"></a>

`MatchValueString`  <a name="cfn-bedrockagentcore-gateway-claimmatchvaluetype-matchvaluestring"></a>
The string value to match for.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9_.:/-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchValueStringList`  <a name="cfn-bedrockagentcore-gateway-claimmatchvaluetype-matchvaluestringlist"></a>
An array of strings to check for a match.
*Required*: No
*Type*: Array of String
*Maximum*: `255`
*Minimum*: `1 | 1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
