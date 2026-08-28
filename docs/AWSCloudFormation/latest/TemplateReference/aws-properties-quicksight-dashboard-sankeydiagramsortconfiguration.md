---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-sankeydiagramsortconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard SankeyDiagramSortConfiguration
<a name="aws-properties-quicksight-dashboard-sankeydiagramsortconfiguration"></a>

The sort configuration of a sankey diagram.

## Syntax
<a name="aws-properties-quicksight-dashboard-sankeydiagramsortconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-sankeydiagramsortconfiguration-syntax.json"></a>

```
{
  "[DestinationItemsLimit](#cfn-quicksight-dashboard-sankeydiagramsortconfiguration-destinationitemslimit)" : {{ItemsLimitConfiguration}},
  "[SourceItemsLimit](#cfn-quicksight-dashboard-sankeydiagramsortconfiguration-sourceitemslimit)" : {{ItemsLimitConfiguration}},
  "[WeightSort](#cfn-quicksight-dashboard-sankeydiagramsortconfiguration-weightsort)" : {{[ FieldSortOptions, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-sankeydiagramsortconfiguration-syntax.yaml"></a>

```
  [DestinationItemsLimit](#cfn-quicksight-dashboard-sankeydiagramsortconfiguration-destinationitemslimit): {{
    ItemsLimitConfiguration}}
  [SourceItemsLimit](#cfn-quicksight-dashboard-sankeydiagramsortconfiguration-sourceitemslimit): {{
    ItemsLimitConfiguration}}
  [WeightSort](#cfn-quicksight-dashboard-sankeydiagramsortconfiguration-weightsort): {{
    - FieldSortOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-sankeydiagramsortconfiguration-properties"></a>

`DestinationItemsLimit`  <a name="cfn-quicksight-dashboard-sankeydiagramsortconfiguration-destinationitemslimit"></a>
The limit on the number of destination nodes that are displayed in a sankey diagram.
*Required*: No
*Type*: [ItemsLimitConfiguration](aws-properties-quicksight-dashboard-itemslimitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceItemsLimit`  <a name="cfn-quicksight-dashboard-sankeydiagramsortconfiguration-sourceitemslimit"></a>
The limit on the number of source nodes that are displayed in a sankey diagram.
*Required*: No
*Type*: [ItemsLimitConfiguration](aws-properties-quicksight-dashboard-itemslimitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WeightSort`  <a name="cfn-quicksight-dashboard-sankeydiagramsortconfiguration-weightsort"></a>
The sort configuration of the weight fields.
*Required*: No
*Type*: Array of [FieldSortOptions](aws-properties-quicksight-dashboard-fieldsortoptions.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
