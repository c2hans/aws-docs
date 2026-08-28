---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-sankeydiagramsortconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template SankeyDiagramSortConfiguration
<a name="aws-properties-quicksight-template-sankeydiagramsortconfiguration"></a>

The sort configuration of a sankey diagram.

## Syntax
<a name="aws-properties-quicksight-template-sankeydiagramsortconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-sankeydiagramsortconfiguration-syntax.json"></a>

```
{
  "[DestinationItemsLimit](#cfn-quicksight-template-sankeydiagramsortconfiguration-destinationitemslimit)" : {{ItemsLimitConfiguration}},
  "[SourceItemsLimit](#cfn-quicksight-template-sankeydiagramsortconfiguration-sourceitemslimit)" : {{ItemsLimitConfiguration}},
  "[WeightSort](#cfn-quicksight-template-sankeydiagramsortconfiguration-weightsort)" : {{[ FieldSortOptions, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-sankeydiagramsortconfiguration-syntax.yaml"></a>

```
  [DestinationItemsLimit](#cfn-quicksight-template-sankeydiagramsortconfiguration-destinationitemslimit): {{
    ItemsLimitConfiguration}}
  [SourceItemsLimit](#cfn-quicksight-template-sankeydiagramsortconfiguration-sourceitemslimit): {{
    ItemsLimitConfiguration}}
  [WeightSort](#cfn-quicksight-template-sankeydiagramsortconfiguration-weightsort): {{
    - FieldSortOptions}}
```

## Properties
<a name="aws-properties-quicksight-template-sankeydiagramsortconfiguration-properties"></a>

`DestinationItemsLimit`  <a name="cfn-quicksight-template-sankeydiagramsortconfiguration-destinationitemslimit"></a>
The limit on the number of destination nodes that are displayed in a sankey diagram.
*Required*: No
*Type*: [ItemsLimitConfiguration](aws-properties-quicksight-template-itemslimitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceItemsLimit`  <a name="cfn-quicksight-template-sankeydiagramsortconfiguration-sourceitemslimit"></a>
The limit on the number of source nodes that are displayed in a sankey diagram.
*Required*: No
*Type*: [ItemsLimitConfiguration](aws-properties-quicksight-template-itemslimitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WeightSort`  <a name="cfn-quicksight-template-sankeydiagramsortconfiguration-weightsort"></a>
The sort configuration of the weight fields.
*Required*: No
*Type*: Array of [FieldSortOptions](aws-properties-quicksight-template-fieldsortoptions.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
