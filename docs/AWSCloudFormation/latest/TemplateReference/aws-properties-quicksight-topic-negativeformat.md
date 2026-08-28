---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-topic-negativeformat.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Topic NegativeFormat
<a name="aws-properties-quicksight-topic-negativeformat"></a>

A structure that represents a negative format.

## Syntax
<a name="aws-properties-quicksight-topic-negativeformat-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-topic-negativeformat-syntax.json"></a>

```
{
  "[Prefix](#cfn-quicksight-topic-negativeformat-prefix)" : {{String}},
  "[Suffix](#cfn-quicksight-topic-negativeformat-suffix)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-topic-negativeformat-syntax.yaml"></a>

```
  [Prefix](#cfn-quicksight-topic-negativeformat-prefix): {{String}}
  [Suffix](#cfn-quicksight-topic-negativeformat-suffix): {{String}}
```

## Properties
<a name="aws-properties-quicksight-topic-negativeformat-properties"></a>

`Prefix`  <a name="cfn-quicksight-topic-negativeformat-prefix"></a>
The prefix for a negative format.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Suffix`  <a name="cfn-quicksight-topic-negativeformat-suffix"></a>
The suffix for a negative format.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
