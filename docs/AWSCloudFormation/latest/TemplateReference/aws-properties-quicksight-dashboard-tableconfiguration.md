---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-tableconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard TableConfiguration
<a name="aws-properties-quicksight-dashboard-tableconfiguration"></a>

The configuration for a `TableVisual`.

## Syntax
<a name="aws-properties-quicksight-dashboard-tableconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-tableconfiguration-syntax.json"></a>

```
{
  "[FieldOptions](#cfn-quicksight-dashboard-tableconfiguration-fieldoptions)" : {{TableFieldOptions}},
  "[FieldWells](#cfn-quicksight-dashboard-tableconfiguration-fieldwells)" : {{TableFieldWells}},
  "[Interactions](#cfn-quicksight-dashboard-tableconfiguration-interactions)" : {{VisualInteractionOptions}},
  "[PaginatedReportOptions](#cfn-quicksight-dashboard-tableconfiguration-paginatedreportoptions)" : {{TablePaginatedReportOptions}},
  "[SortConfiguration](#cfn-quicksight-dashboard-tableconfiguration-sortconfiguration)" : {{TableSortConfiguration}},
  "[TableInlineVisualizations](#cfn-quicksight-dashboard-tableconfiguration-tableinlinevisualizations)" : {{[ TableInlineVisualization, ... ]}},
  "[TableOptions](#cfn-quicksight-dashboard-tableconfiguration-tableoptions)" : {{TableOptions}},
  "[TotalOptions](#cfn-quicksight-dashboard-tableconfiguration-totaloptions)" : {{TotalOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-tableconfiguration-syntax.yaml"></a>

```
  [FieldOptions](#cfn-quicksight-dashboard-tableconfiguration-fieldoptions): {{
    TableFieldOptions}}
  [FieldWells](#cfn-quicksight-dashboard-tableconfiguration-fieldwells): {{
    TableFieldWells}}
  [Interactions](#cfn-quicksight-dashboard-tableconfiguration-interactions): {{
    VisualInteractionOptions}}
  [PaginatedReportOptions](#cfn-quicksight-dashboard-tableconfiguration-paginatedreportoptions): {{
    TablePaginatedReportOptions}}
  [SortConfiguration](#cfn-quicksight-dashboard-tableconfiguration-sortconfiguration): {{
    TableSortConfiguration}}
  [TableInlineVisualizations](#cfn-quicksight-dashboard-tableconfiguration-tableinlinevisualizations): {{
    - TableInlineVisualization}}
  [TableOptions](#cfn-quicksight-dashboard-tableconfiguration-tableoptions): {{
    TableOptions}}
  [TotalOptions](#cfn-quicksight-dashboard-tableconfiguration-totaloptions): {{
    TotalOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-tableconfiguration-properties"></a>

`FieldOptions`  <a name="cfn-quicksight-dashboard-tableconfiguration-fieldoptions"></a>
The field options for a table visual.
*Required*: No
*Type*: [TableFieldOptions](aws-properties-quicksight-dashboard-tablefieldoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldWells`  <a name="cfn-quicksight-dashboard-tableconfiguration-fieldwells"></a>
The field wells of the visual.
*Required*: No
*Type*: [TableFieldWells](aws-properties-quicksight-dashboard-tablefieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-dashboard-tableconfiguration-interactions"></a>
The general visual interactions setup for a visual.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-dashboard-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PaginatedReportOptions`  <a name="cfn-quicksight-dashboard-tableconfiguration-paginatedreportoptions"></a>
The paginated report options for a table visual.
*Required*: No
*Type*: [TablePaginatedReportOptions](aws-properties-quicksight-dashboard-tablepaginatedreportoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortConfiguration`  <a name="cfn-quicksight-dashboard-tableconfiguration-sortconfiguration"></a>
The sort configuration for a `TableVisual`.
*Required*: No
*Type*: [TableSortConfiguration](aws-properties-quicksight-dashboard-tablesortconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableInlineVisualizations`  <a name="cfn-quicksight-dashboard-tableconfiguration-tableinlinevisualizations"></a>
A collection of inline visualizations to display within a chart.
*Required*: No
*Type*: Array of [TableInlineVisualization](aws-properties-quicksight-dashboard-tableinlinevisualization.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableOptions`  <a name="cfn-quicksight-dashboard-tableconfiguration-tableoptions"></a>
The table options for a table visual.
*Required*: No
*Type*: [TableOptions](aws-properties-quicksight-dashboard-tableoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalOptions`  <a name="cfn-quicksight-dashboard-tableconfiguration-totaloptions"></a>
The total options for a table visual.
*Required*: No
*Type*: [TotalOptions](aws-properties-quicksight-dashboard-totaloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
