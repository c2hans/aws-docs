---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-pivottableconditionalformattingoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis PivotTableConditionalFormattingOption
<a name="aws-properties-quicksight-analysis-pivottableconditionalformattingoption"></a>

Conditional formatting options for a `PivotTableVisual`.

## Syntax
<a name="aws-properties-quicksight-analysis-pivottableconditionalformattingoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-pivottableconditionalformattingoption-syntax.json"></a>

```
{
  "[Cell](#cfn-quicksight-analysis-pivottableconditionalformattingoption-cell)" : {{PivotTableCellConditionalFormatting}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-pivottableconditionalformattingoption-syntax.yaml"></a>

```
  [Cell](#cfn-quicksight-analysis-pivottableconditionalformattingoption-cell): {{
    PivotTableCellConditionalFormatting}}
```

## Properties
<a name="aws-properties-quicksight-analysis-pivottableconditionalformattingoption-properties"></a>

`Cell`  <a name="cfn-quicksight-analysis-pivottableconditionalformattingoption-cell"></a>
The cell conditional formatting option for a pivot table.
*Required*: No
*Type*: [PivotTableCellConditionalFormatting](aws-properties-quicksight-analysis-pivottablecellconditionalformatting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
