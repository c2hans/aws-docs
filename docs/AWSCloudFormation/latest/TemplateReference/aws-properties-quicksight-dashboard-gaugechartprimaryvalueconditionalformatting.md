---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-gaugechartprimaryvalueconditionalformatting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GaugeChartPrimaryValueConditionalFormatting
<a name="aws-properties-quicksight-dashboard-gaugechartprimaryvalueconditionalformatting"></a>

The conditional formatting for the primary value of a `GaugeChartVisual`.

## Syntax
<a name="aws-properties-quicksight-dashboard-gaugechartprimaryvalueconditionalformatting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-gaugechartprimaryvalueconditionalformatting-syntax.json"></a>

```
{
  "[Icon](#cfn-quicksight-dashboard-gaugechartprimaryvalueconditionalformatting-icon)" : {{ConditionalFormattingIcon}},
  "[TextColor](#cfn-quicksight-dashboard-gaugechartprimaryvalueconditionalformatting-textcolor)" : {{ConditionalFormattingColor}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-gaugechartprimaryvalueconditionalformatting-syntax.yaml"></a>

```
  [Icon](#cfn-quicksight-dashboard-gaugechartprimaryvalueconditionalformatting-icon): {{
    ConditionalFormattingIcon}}
  [TextColor](#cfn-quicksight-dashboard-gaugechartprimaryvalueconditionalformatting-textcolor): {{
    ConditionalFormattingColor}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-gaugechartprimaryvalueconditionalformatting-properties"></a>

`Icon`  <a name="cfn-quicksight-dashboard-gaugechartprimaryvalueconditionalformatting-icon"></a>
The conditional formatting of the primary value icon.
*Required*: No
*Type*: [ConditionalFormattingIcon](aws-properties-quicksight-dashboard-conditionalformattingicon.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextColor`  <a name="cfn-quicksight-dashboard-gaugechartprimaryvalueconditionalformatting-textcolor"></a>
The conditional formatting of the primary value text color.
*Required*: No
*Type*: [ConditionalFormattingColor](aws-properties-quicksight-dashboard-conditionalformattingcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
