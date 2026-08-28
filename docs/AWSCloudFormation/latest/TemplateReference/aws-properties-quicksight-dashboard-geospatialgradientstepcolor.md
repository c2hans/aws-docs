---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-geospatialgradientstepcolor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GeospatialGradientStepColor
<a name="aws-properties-quicksight-dashboard-geospatialgradientstepcolor"></a>

The gradient step color for a single step.

## Syntax
<a name="aws-properties-quicksight-dashboard-geospatialgradientstepcolor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-geospatialgradientstepcolor-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-dashboard-geospatialgradientstepcolor-color)" : {{String}},
  "[DataValue](#cfn-quicksight-dashboard-geospatialgradientstepcolor-datavalue)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-geospatialgradientstepcolor-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-dashboard-geospatialgradientstepcolor-color): {{String}}
  [DataValue](#cfn-quicksight-dashboard-geospatialgradientstepcolor-datavalue): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-geospatialgradientstepcolor-properties"></a>

`Color`  <a name="cfn-quicksight-dashboard-geospatialgradientstepcolor-color"></a>
The color and opacity values for the gradient step color.
*Required*: Yes
*Type*: String
*Pattern*: `^#[A-F0-9]{6}(?:[A-F0-9]{2})?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataValue`  <a name="cfn-quicksight-dashboard-geospatialgradientstepcolor-datavalue"></a>
The data value for the gradient step color.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
