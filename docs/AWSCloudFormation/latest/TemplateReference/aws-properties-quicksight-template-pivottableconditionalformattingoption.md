---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-pivottableconditionalformattingoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template PivotTableConditionalFormattingOption
<a name="aws-properties-quicksight-template-pivottableconditionalformattingoption"></a>

Conditional formatting options for a `PivotTableVisual`.

## Syntax
<a name="aws-properties-quicksight-template-pivottableconditionalformattingoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-pivottableconditionalformattingoption-syntax.json"></a>

```
{
  "[Cell](#cfn-quicksight-template-pivottableconditionalformattingoption-cell)" : {{PivotTableCellConditionalFormatting}}
}
```

### YAML
<a name="aws-properties-quicksight-template-pivottableconditionalformattingoption-syntax.yaml"></a>

```
  [Cell](#cfn-quicksight-template-pivottableconditionalformattingoption-cell): {{
    PivotTableCellConditionalFormatting}}
```

## Properties
<a name="aws-properties-quicksight-template-pivottableconditionalformattingoption-properties"></a>

`Cell`  <a name="cfn-quicksight-template-pivottableconditionalformattingoption-cell"></a>
The cell conditional formatting option for a pivot table.
*Required*: No
*Type*: [PivotTableCellConditionalFormatting](aws-properties-quicksight-template-pivottablecellconditionalformatting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
