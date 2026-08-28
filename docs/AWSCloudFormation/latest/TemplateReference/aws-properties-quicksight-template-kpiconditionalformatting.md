---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-kpiconditionalformatting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template KPIConditionalFormatting
<a name="aws-properties-quicksight-template-kpiconditionalformatting"></a>

The conditional formatting of a KPI visual.

## Syntax
<a name="aws-properties-quicksight-template-kpiconditionalformatting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-kpiconditionalformatting-syntax.json"></a>

```
{
  "[ConditionalFormattingOptions](#cfn-quicksight-template-kpiconditionalformatting-conditionalformattingoptions)" : {{[ KPIConditionalFormattingOption, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-kpiconditionalformatting-syntax.yaml"></a>

```
  [ConditionalFormattingOptions](#cfn-quicksight-template-kpiconditionalformatting-conditionalformattingoptions): {{
    - KPIConditionalFormattingOption}}
```

## Properties
<a name="aws-properties-quicksight-template-kpiconditionalformatting-properties"></a>

`ConditionalFormattingOptions`  <a name="cfn-quicksight-template-kpiconditionalformatting-conditionalformattingoptions"></a>
The conditional formatting options of a KPI visual.
*Required*: No
*Type*: Array of [KPIConditionalFormattingOption](aws-properties-quicksight-template-kpiconditionalformattingoption.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
