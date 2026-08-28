---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-kpiprogressbarconditionalformatting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard KPIProgressBarConditionalFormatting
<a name="aws-properties-quicksight-dashboard-kpiprogressbarconditionalformatting"></a>

The conditional formatting for the progress bar of a KPI visual.

## Syntax
<a name="aws-properties-quicksight-dashboard-kpiprogressbarconditionalformatting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-kpiprogressbarconditionalformatting-syntax.json"></a>

```
{
  "[ForegroundColor](#cfn-quicksight-dashboard-kpiprogressbarconditionalformatting-foregroundcolor)" : {{ConditionalFormattingColor}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-kpiprogressbarconditionalformatting-syntax.yaml"></a>

```
  [ForegroundColor](#cfn-quicksight-dashboard-kpiprogressbarconditionalformatting-foregroundcolor): {{
    ConditionalFormattingColor}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-kpiprogressbarconditionalformatting-properties"></a>

`ForegroundColor`  <a name="cfn-quicksight-dashboard-kpiprogressbarconditionalformatting-foregroundcolor"></a>
The conditional formatting of the progress bar's foreground color.
*Required*: No
*Type*: [ConditionalFormattingColor](aws-properties-quicksight-dashboard-conditionalformattingcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
