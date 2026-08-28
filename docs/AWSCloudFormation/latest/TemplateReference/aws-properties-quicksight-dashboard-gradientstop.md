---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-gradientstop.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GradientStop
<a name="aws-properties-quicksight-dashboard-gradientstop"></a>

Determines the gradient stop configuration.

## Syntax
<a name="aws-properties-quicksight-dashboard-gradientstop-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-gradientstop-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-dashboard-gradientstop-color)" : {{String}},
  "[DataValue](#cfn-quicksight-dashboard-gradientstop-datavalue)" : {{Number}},
  "[GradientOffset](#cfn-quicksight-dashboard-gradientstop-gradientoffset)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-gradientstop-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-dashboard-gradientstop-color): {{String}}
  [DataValue](#cfn-quicksight-dashboard-gradientstop-datavalue): {{Number}}
  [GradientOffset](#cfn-quicksight-dashboard-gradientstop-gradientoffset): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-gradientstop-properties"></a>

`Color`  <a name="cfn-quicksight-dashboard-gradientstop-color"></a>
Determines the color.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataValue`  <a name="cfn-quicksight-dashboard-gradientstop-datavalue"></a>
Determines the data value.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GradientOffset`  <a name="cfn-quicksight-dashboard-gradientstop-gradientoffset"></a>
Determines gradient offset value.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
