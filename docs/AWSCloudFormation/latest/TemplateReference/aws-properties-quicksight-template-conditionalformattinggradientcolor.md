---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-conditionalformattinggradientcolor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template ConditionalFormattingGradientColor
<a name="aws-properties-quicksight-template-conditionalformattinggradientcolor"></a>

Formatting configuration for gradient color.

## Syntax
<a name="aws-properties-quicksight-template-conditionalformattinggradientcolor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-conditionalformattinggradientcolor-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-template-conditionalformattinggradientcolor-color)" : {{GradientColor}},
  "[Expression](#cfn-quicksight-template-conditionalformattinggradientcolor-expression)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-conditionalformattinggradientcolor-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-template-conditionalformattinggradientcolor-color): {{
    GradientColor}}
  [Expression](#cfn-quicksight-template-conditionalformattinggradientcolor-expression): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-conditionalformattinggradientcolor-properties"></a>

`Color`  <a name="cfn-quicksight-template-conditionalformattinggradientcolor-color"></a>
Determines the color.
*Required*: Yes
*Type*: [GradientColor](aws-properties-quicksight-template-gradientcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Expression`  <a name="cfn-quicksight-template-conditionalformattinggradientcolor-expression"></a>
The expression that determines the formatting configuration for gradient color.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
