---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-tablerowconditionalformatting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard TableRowConditionalFormatting
<a name="aws-properties-quicksight-dashboard-tablerowconditionalformatting"></a>

The conditional formatting of a table row.

## Syntax
<a name="aws-properties-quicksight-dashboard-tablerowconditionalformatting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-tablerowconditionalformatting-syntax.json"></a>

```
{
  "[BackgroundColor](#cfn-quicksight-dashboard-tablerowconditionalformatting-backgroundcolor)" : {{ConditionalFormattingColor}},
  "[TextColor](#cfn-quicksight-dashboard-tablerowconditionalformatting-textcolor)" : {{ConditionalFormattingColor}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-tablerowconditionalformatting-syntax.yaml"></a>

```
  [BackgroundColor](#cfn-quicksight-dashboard-tablerowconditionalformatting-backgroundcolor): {{
    ConditionalFormattingColor}}
  [TextColor](#cfn-quicksight-dashboard-tablerowconditionalformatting-textcolor): {{
    ConditionalFormattingColor}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-tablerowconditionalformatting-properties"></a>

`BackgroundColor`  <a name="cfn-quicksight-dashboard-tablerowconditionalformatting-backgroundcolor"></a>
The conditional formatting color (solid, gradient) of the background for a table row.
*Required*: No
*Type*: [ConditionalFormattingColor](aws-properties-quicksight-dashboard-conditionalformattingcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextColor`  <a name="cfn-quicksight-dashboard-tablerowconditionalformatting-textcolor"></a>
The conditional formatting color (solid, gradient) of the text for a table row.
*Required*: No
*Type*: [ConditionalFormattingColor](aws-properties-quicksight-dashboard-conditionalformattingcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
