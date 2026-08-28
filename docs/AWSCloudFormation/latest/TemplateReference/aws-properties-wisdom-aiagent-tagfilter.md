---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiagent-tagfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIAgent TagFilter
<a name="aws-properties-wisdom-aiagent-tagfilter"></a>

An object that can be used to specify tag conditions.

## Syntax
<a name="aws-properties-wisdom-aiagent-tagfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiagent-tagfilter-syntax.json"></a>

```
{
  "[AndConditions](#cfn-wisdom-aiagent-tagfilter-andconditions)" : {{[ TagCondition, ... ]}},
  "[OrConditions](#cfn-wisdom-aiagent-tagfilter-orconditions)" : {{[ OrCondition, ... ]}},
  "[TagCondition](#cfn-wisdom-aiagent-tagfilter-tagcondition)" : {{TagCondition}}
}
```

### YAML
<a name="aws-properties-wisdom-aiagent-tagfilter-syntax.yaml"></a>

```
  [AndConditions](#cfn-wisdom-aiagent-tagfilter-andconditions): {{
    - TagCondition}}
  [OrConditions](#cfn-wisdom-aiagent-tagfilter-orconditions): {{
    - OrCondition}}
  [TagCondition](#cfn-wisdom-aiagent-tagfilter-tagcondition): {{
    TagCondition}}
```

## Properties
<a name="aws-properties-wisdom-aiagent-tagfilter-properties"></a>

`AndConditions`  <a name="cfn-wisdom-aiagent-tagfilter-andconditions"></a>
A list of conditions which would be applied together with an `AND` condition.
*Required*: No
*Type*: Array of [TagCondition](aws-properties-wisdom-aiagent-tagcondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OrConditions`  <a name="cfn-wisdom-aiagent-tagfilter-orconditions"></a>
A list of conditions which would be applied together with an `OR` condition.
*Required*: No
*Type*: Array of [OrCondition](aws-properties-wisdom-aiagent-orcondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagCondition`  <a name="cfn-wisdom-aiagent-tagfilter-tagcondition"></a>
A leaf node condition which can be used to specify a tag condition.
*Required*: No
*Type*: [TagCondition](aws-properties-wisdom-aiagent-tagcondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
