---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-tableconditionalformattingoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis TableConditionalFormattingOption
<a name="aws-properties-quicksight-analysis-tableconditionalformattingoption"></a>

Conditional formatting options for a `PivotTableVisual`.

## Syntax
<a name="aws-properties-quicksight-analysis-tableconditionalformattingoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-tableconditionalformattingoption-syntax.json"></a>

```
{
  "[Cell](#cfn-quicksight-analysis-tableconditionalformattingoption-cell)" : {{TableCellConditionalFormatting}},
  "[Row](#cfn-quicksight-analysis-tableconditionalformattingoption-row)" : {{TableRowConditionalFormatting}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-tableconditionalformattingoption-syntax.yaml"></a>

```
  [Cell](#cfn-quicksight-analysis-tableconditionalformattingoption-cell): {{
    TableCellConditionalFormatting}}
  [Row](#cfn-quicksight-analysis-tableconditionalformattingoption-row): {{
    TableRowConditionalFormatting}}
```

## Properties
<a name="aws-properties-quicksight-analysis-tableconditionalformattingoption-properties"></a>

`Cell`  <a name="cfn-quicksight-analysis-tableconditionalformattingoption-cell"></a>
The cell conditional formatting option for a table.
*Required*: No
*Type*: [TableCellConditionalFormatting](aws-properties-quicksight-analysis-tablecellconditionalformatting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Row`  <a name="cfn-quicksight-analysis-tableconditionalformattingoption-row"></a>
The row conditional formatting option for a table.
*Required*: No
*Type*: [TableRowConditionalFormatting](aws-properties-quicksight-analysis-tablerowconditionalformatting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
