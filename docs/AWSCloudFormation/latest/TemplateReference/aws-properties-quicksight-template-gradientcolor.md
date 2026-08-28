---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-gradientcolor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GradientColor
<a name="aws-properties-quicksight-template-gradientcolor"></a>

Determines the gradient color settings.

## Syntax
<a name="aws-properties-quicksight-template-gradientcolor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-gradientcolor-syntax.json"></a>

```
{
  "[Stops](#cfn-quicksight-template-gradientcolor-stops)" : {{[ GradientStop, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-gradientcolor-syntax.yaml"></a>

```
  [Stops](#cfn-quicksight-template-gradientcolor-stops): {{
    - GradientStop}}
```

## Properties
<a name="aws-properties-quicksight-template-gradientcolor-properties"></a>

`Stops`  <a name="cfn-quicksight-template-gradientcolor-stops"></a>
The list of gradient color stops.
*Required*: No
*Type*: Array of [GradientStop](aws-properties-quicksight-template-gradientstop.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
