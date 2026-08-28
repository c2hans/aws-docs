---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-tooloverrideinputvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent ToolOverrideInputValue
<a name="aws-properties-wisdom-aiagent-tooloverrideinputvalue"></a>

An input value override for tools.

## Syntax
<a name="aws-properties-wisdom-aiagent-tooloverrideinputvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-tooloverrideinputvalue-syntax.json"></a>

```
{
  "[JsonPath](#cfn-wisdom-aiagent-tooloverrideinputvalue-jsonpath)" : {{String}},
  "[Value](#cfn-wisdom-aiagent-tooloverrideinputvalue-value)" : {{ToolOverrideInputValueConfiguration}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-tooloverrideinputvalue-syntax.yaml"></a>

```
  [JsonPath](#cfn-wisdom-aiagent-tooloverrideinputvalue-jsonpath): {{String}}
  [Value](#cfn-wisdom-aiagent-tooloverrideinputvalue-value): {{
    ToolOverrideInputValueConfiguration}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-tooloverrideinputvalue-properties"></a>

`JsonPath`  <a name="cfn-wisdom-aiagent-tooloverrideinputvalue-jsonpath"></a>
The JSON path for the input value override.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-wisdom-aiagent-tooloverrideinputvalue-value"></a>
The override input value.
*Required*: Yes
*Type*: [ToolOverrideInputValueConfiguration](aws-properties-wisdom-aiagent-tooloverrideinputvalueconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
