---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-textconditionalformat.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard TextConditionalFormat
<a name="aws-properties-quicksight-dashboard-textconditionalformat"></a>

The conditional formatting for the text.

## Syntax
<a name="aws-properties-quicksight-dashboard-textconditionalformat-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-textconditionalformat-syntax.json"></a>

```
{
  "[BackgroundColor](#cfn-quicksight-dashboard-textconditionalformat-backgroundcolor)" : {{ConditionalFormattingColor}},
  "[Icon](#cfn-quicksight-dashboard-textconditionalformat-icon)" : {{ConditionalFormattingIcon}},
  "[TextColor](#cfn-quicksight-dashboard-textconditionalformat-textcolor)" : {{ConditionalFormattingColor}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-textconditionalformat-syntax.yaml"></a>

```
  [BackgroundColor](#cfn-quicksight-dashboard-textconditionalformat-backgroundcolor): {{
    ConditionalFormattingColor}}
  [Icon](#cfn-quicksight-dashboard-textconditionalformat-icon): {{
    ConditionalFormattingIcon}}
  [TextColor](#cfn-quicksight-dashboard-textconditionalformat-textcolor): {{
    ConditionalFormattingColor}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-textconditionalformat-properties"></a>

`BackgroundColor`  <a name="cfn-quicksight-dashboard-textconditionalformat-backgroundcolor"></a>
The conditional formatting for the text background color.
*Required*: No
*Type*: [ConditionalFormattingColor](aws-properties-quicksight-dashboard-conditionalformattingcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Icon`  <a name="cfn-quicksight-dashboard-textconditionalformat-icon"></a>
The conditional formatting for the icon.
*Required*: No
*Type*: [ConditionalFormattingIcon](aws-properties-quicksight-dashboard-conditionalformattingicon.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextColor`  <a name="cfn-quicksight-dashboard-textconditionalformat-textcolor"></a>
The conditional formatting for the text color.
*Required*: No
*Type*: [ConditionalFormattingColor](aws-properties-quicksight-dashboard-conditionalformattingcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
