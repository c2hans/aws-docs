---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-filledmapconditionalformatting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis FilledMapConditionalFormatting
<a name="aws-properties-quicksight-analysis-filledmapconditionalformatting"></a>

The conditional formatting of a `FilledMapVisual`.

## Syntax
<a name="aws-properties-quicksight-analysis-filledmapconditionalformatting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-filledmapconditionalformatting-syntax.json"></a>

```
{
  "[ConditionalFormattingOptions](#cfn-quicksight-analysis-filledmapconditionalformatting-conditionalformattingoptions)" : {{[ FilledMapConditionalFormattingOption, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-filledmapconditionalformatting-syntax.yaml"></a>

```
  [ConditionalFormattingOptions](#cfn-quicksight-analysis-filledmapconditionalformatting-conditionalformattingoptions): {{
    - FilledMapConditionalFormattingOption}}
```

## Properties
<a name="aws-properties-quicksight-analysis-filledmapconditionalformatting-properties"></a>

`ConditionalFormattingOptions`  <a name="cfn-quicksight-analysis-filledmapconditionalformatting-conditionalformattingoptions"></a>
Conditional formatting options of a `FilledMapVisual`.
*Required*: Yes
*Type*: Array of [FilledMapConditionalFormattingOption](aws-properties-quicksight-analysis-filledmapconditionalformattingoption.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
