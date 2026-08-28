---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-tooloverrideconstantinputvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent ToolOverrideConstantInputValue
<a name="aws-properties-wisdom-aiagent-tooloverrideconstantinputvalue"></a>

A constant input value for tool override.

## Syntax
<a name="aws-properties-wisdom-aiagent-tooloverrideconstantinputvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-tooloverrideconstantinputvalue-syntax.json"></a>

```
{
  "[Type](#cfn-wisdom-aiagent-tooloverrideconstantinputvalue-type)" : {{String}},
  "[Value](#cfn-wisdom-aiagent-tooloverrideconstantinputvalue-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-tooloverrideconstantinputvalue-syntax.yaml"></a>

```
  [Type](#cfn-wisdom-aiagent-tooloverrideconstantinputvalue-type): {{String}}
  [Value](#cfn-wisdom-aiagent-tooloverrideconstantinputvalue-value): {{String}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-tooloverrideconstantinputvalue-properties"></a>

`Type`  <a name="cfn-wisdom-aiagent-tooloverrideconstantinputvalue-type"></a>
Override tool input value with constant values
*Required*: Yes
*Type*: String
*Allowed values*: `STRING | NUMBER | JSON_STRING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-wisdom-aiagent-tooloverrideconstantinputvalue-value"></a>
The constant input override value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
