---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-gaugechartarcconditionalformatting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GaugeChartArcConditionalFormatting
<a name="aws-properties-quicksight-template-gaugechartarcconditionalformatting"></a>

The options that determine the presentation of the arc of a `GaugeChartVisual`.

## Syntax
<a name="aws-properties-quicksight-template-gaugechartarcconditionalformatting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-gaugechartarcconditionalformatting-syntax.json"></a>

```
{
  "[ForegroundColor](#cfn-quicksight-template-gaugechartarcconditionalformatting-foregroundcolor)" : {{ConditionalFormattingColor}}
}
```

### YAML
<a name="aws-properties-quicksight-template-gaugechartarcconditionalformatting-syntax.yaml"></a>

```
  [ForegroundColor](#cfn-quicksight-template-gaugechartarcconditionalformatting-foregroundcolor): {{
    ConditionalFormattingColor}}
```

## Properties
<a name="aws-properties-quicksight-template-gaugechartarcconditionalformatting-properties"></a>

`ForegroundColor`  <a name="cfn-quicksight-template-gaugechartarcconditionalformatting-foregroundcolor"></a>
The conditional formatting of the arc foreground color.
*Required*: No
*Type*: [ConditionalFormattingColor](aws-properties-quicksight-template-conditionalformattingcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
