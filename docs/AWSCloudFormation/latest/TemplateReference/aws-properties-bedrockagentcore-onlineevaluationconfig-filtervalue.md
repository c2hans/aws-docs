---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-onlineevaluationconfig-filtervalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OnlineEvaluationConfig FilterValue
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-filtervalue"></a>

 The value to compare against using the specified operator. Can be a string, double, or boolean value.

## Syntax
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-filtervalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-filtervalue-syntax.json"></a>

```
{
  "[BooleanValue](#cfn-bedrockagentcore-onlineevaluationconfig-filtervalue-booleanvalue)" : {{Boolean}},
  "[DoubleValue](#cfn-bedrockagentcore-onlineevaluationconfig-filtervalue-doublevalue)" : {{Number}},
  "[StringValue](#cfn-bedrockagentcore-onlineevaluationconfig-filtervalue-stringvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-filtervalue-syntax.yaml"></a>

```
  [BooleanValue](#cfn-bedrockagentcore-onlineevaluationconfig-filtervalue-booleanvalue): {{
    Boolean}}
  [DoubleValue](#cfn-bedrockagentcore-onlineevaluationconfig-filtervalue-doublevalue): {{Number}}
  [StringValue](#cfn-bedrockagentcore-onlineevaluationconfig-filtervalue-stringvalue): {{
    String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-onlineevaluationconfig-filtervalue-properties"></a>

`BooleanValue`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-filtervalue-booleanvalue"></a>
 The boolean value for true/false filtering conditions.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DoubleValue`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-filtervalue-doublevalue"></a>
 The numeric value for numerical filtering and comparisons.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringValue`  <a name="cfn-bedrockagentcore-onlineevaluationconfig-filtervalue-stringvalue"></a>
 The string value for text-based filtering.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
