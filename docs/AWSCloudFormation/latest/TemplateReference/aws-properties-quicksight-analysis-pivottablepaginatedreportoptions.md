---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-pivottablepaginatedreportoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis PivotTablePaginatedReportOptions
<a name="aws-properties-quicksight-analysis-pivottablepaginatedreportoptions"></a>

The paginated report options for a pivot table visual.

## Syntax
<a name="aws-properties-quicksight-analysis-pivottablepaginatedreportoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-pivottablepaginatedreportoptions-syntax.json"></a>

```
{
  "[OverflowColumnHeaderVisibility](#cfn-quicksight-analysis-pivottablepaginatedreportoptions-overflowcolumnheadervisibility)" : {{String}},
  "[VerticalOverflowVisibility](#cfn-quicksight-analysis-pivottablepaginatedreportoptions-verticaloverflowvisibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-pivottablepaginatedreportoptions-syntax.yaml"></a>

```
  [OverflowColumnHeaderVisibility](#cfn-quicksight-analysis-pivottablepaginatedreportoptions-overflowcolumnheadervisibility): {{String}}
  [VerticalOverflowVisibility](#cfn-quicksight-analysis-pivottablepaginatedreportoptions-verticaloverflowvisibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-pivottablepaginatedreportoptions-properties"></a>

`OverflowColumnHeaderVisibility`  <a name="cfn-quicksight-analysis-pivottablepaginatedreportoptions-overflowcolumnheadervisibility"></a>
The visibility of the repeating header rows on each page.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VerticalOverflowVisibility`  <a name="cfn-quicksight-analysis-pivottablepaginatedreportoptions-verticaloverflowvisibility"></a>
The visibility of the printing table overflow across pages.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
