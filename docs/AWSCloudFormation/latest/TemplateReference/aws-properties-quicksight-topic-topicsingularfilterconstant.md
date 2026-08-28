---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-topic-topicsingularfilterconstant.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Topic TopicSingularFilterConstant
<a name="aws-properties-quicksight-topic-topicsingularfilterconstant"></a>

A structure that represents a singular filter constant, used in filters to specify a single value to match against.

## Syntax
<a name="aws-properties-quicksight-topic-topicsingularfilterconstant-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-topic-topicsingularfilterconstant-syntax.json"></a>

```
{
  "[ConstantType](#cfn-quicksight-topic-topicsingularfilterconstant-constanttype)" : {{String}},
  "[SingularConstant](#cfn-quicksight-topic-topicsingularfilterconstant-singularconstant)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-topic-topicsingularfilterconstant-syntax.yaml"></a>

```
  [ConstantType](#cfn-quicksight-topic-topicsingularfilterconstant-constanttype): {{String}}
  [SingularConstant](#cfn-quicksight-topic-topicsingularfilterconstant-singularconstant): {{String}}
```

## Properties
<a name="aws-properties-quicksight-topic-topicsingularfilterconstant-properties"></a>

`ConstantType`  <a name="cfn-quicksight-topic-topicsingularfilterconstant-constanttype"></a>
The type of the singular filter constant. Valid values for this structure are `SINGULAR`.
*Required*: No
*Type*: String
*Allowed values*: `SINGULAR | RANGE | COLLECTIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SingularConstant`  <a name="cfn-quicksight-topic-topicsingularfilterconstant-singularconstant"></a>
The value of the singular filter constant.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
