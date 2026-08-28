---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-datacolor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis DataColor
<a name="aws-properties-quicksight-analysis-datacolor"></a>

Determines the color that is applied to a particular data value.

## Syntax
<a name="aws-properties-quicksight-analysis-datacolor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-datacolor-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-analysis-datacolor-color)" : {{String}},
  "[DataValue](#cfn-quicksight-analysis-datacolor-datavalue)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-datacolor-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-analysis-datacolor-color): {{String}}
  [DataValue](#cfn-quicksight-analysis-datacolor-datavalue): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-analysis-datacolor-properties"></a>

`Color`  <a name="cfn-quicksight-analysis-datacolor-color"></a>
The color that is applied to the data value.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataValue`  <a name="cfn-quicksight-analysis-datacolor-datavalue"></a>
The data value that the color is applied to.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
