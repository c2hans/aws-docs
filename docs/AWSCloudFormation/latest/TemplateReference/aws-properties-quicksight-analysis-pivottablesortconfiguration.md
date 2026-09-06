---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-pivottablesortconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis PivotTableSortConfiguration
<a name="aws-properties-quicksight-analysis-pivottablesortconfiguration"></a>

The sort configuration for a `PivotTableVisual`.

## Syntax
<a name="aws-properties-quicksight-analysis-pivottablesortconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-pivottablesortconfiguration-syntax.json"></a>

```
{
  "[FieldSortOptions](#cfn-quicksight-analysis-pivottablesortconfiguration-fieldsortoptions)" : {{[ PivotFieldSortOptions, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-pivottablesortconfiguration-syntax.yaml"></a>

```
  [FieldSortOptions](#cfn-quicksight-analysis-pivottablesortconfiguration-fieldsortoptions): {{
    - PivotFieldSortOptions}}
```

## Properties
<a name="aws-properties-quicksight-analysis-pivottablesortconfiguration-properties"></a>

`FieldSortOptions`  <a name="cfn-quicksight-analysis-pivottablesortconfiguration-fieldsortoptions"></a>
The field sort options for a pivot table sort configuration.
*Required*: No
*Type*: [Array](aws-properties-quicksight-analysis-fieldsortoptions.md) of [PivotFieldSortOptions](aws-properties-quicksight-analysis-pivotfieldsortoptions.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
