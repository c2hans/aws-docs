---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-conditionalformattingicon.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template ConditionalFormattingIcon
<a name="aws-properties-quicksight-template-conditionalformattingicon"></a>

The formatting configuration for the icon.

## Syntax
<a name="aws-properties-quicksight-template-conditionalformattingicon-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-conditionalformattingicon-syntax.json"></a>

```
{
  "[CustomCondition](#cfn-quicksight-template-conditionalformattingicon-customcondition)" : {{ConditionalFormattingCustomIconCondition}},
  "[IconSet](#cfn-quicksight-template-conditionalformattingicon-iconset)" : {{ConditionalFormattingIconSet}}
}
```

### YAML
<a name="aws-properties-quicksight-template-conditionalformattingicon-syntax.yaml"></a>

```
  [CustomCondition](#cfn-quicksight-template-conditionalformattingicon-customcondition): {{
    ConditionalFormattingCustomIconCondition}}
  [IconSet](#cfn-quicksight-template-conditionalformattingicon-iconset): {{
    ConditionalFormattingIconSet}}
```

## Properties
<a name="aws-properties-quicksight-template-conditionalformattingicon-properties"></a>

`CustomCondition`  <a name="cfn-quicksight-template-conditionalformattingicon-customcondition"></a>
Determines the custom condition for an icon set.
*Required*: No
*Type*: [ConditionalFormattingCustomIconCondition](aws-properties-quicksight-template-conditionalformattingcustomiconcondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IconSet`  <a name="cfn-quicksight-template-conditionalformattingicon-iconset"></a>
Formatting configuration for icon set.
*Required*: No
*Type*: [ConditionalFormattingIconSet](aws-properties-quicksight-template-conditionalformattingiconset.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
