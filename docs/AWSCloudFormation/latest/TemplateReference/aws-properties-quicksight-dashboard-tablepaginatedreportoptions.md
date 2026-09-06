---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-tablepaginatedreportoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard TablePaginatedReportOptions
<a name="aws-properties-quicksight-dashboard-tablepaginatedreportoptions"></a>

The paginated report options for a table visual.

## Syntax
<a name="aws-properties-quicksight-dashboard-tablepaginatedreportoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-tablepaginatedreportoptions-syntax.json"></a>

```
{
  "[OverflowColumnHeaderVisibility](#cfn-quicksight-dashboard-tablepaginatedreportoptions-overflowcolumnheadervisibility)" : {{String}},
  "[VerticalOverflowVisibility](#cfn-quicksight-dashboard-tablepaginatedreportoptions-verticaloverflowvisibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-tablepaginatedreportoptions-syntax.yaml"></a>

```
  [OverflowColumnHeaderVisibility](#cfn-quicksight-dashboard-tablepaginatedreportoptions-overflowcolumnheadervisibility): {{String}}
  [VerticalOverflowVisibility](#cfn-quicksight-dashboard-tablepaginatedreportoptions-verticaloverflowvisibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-tablepaginatedreportoptions-properties"></a>

`OverflowColumnHeaderVisibility`  <a name="cfn-quicksight-dashboard-tablepaginatedreportoptions-overflowcolumnheadervisibility"></a>
The visibility of repeating header rows on each page.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VerticalOverflowVisibility`  <a name="cfn-quicksight-dashboard-tablepaginatedreportoptions-verticaloverflowvisibility"></a>
The visibility of printing table overflow across pages.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
