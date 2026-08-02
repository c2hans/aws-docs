---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-bodysectiondynamiccategorydimensionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template BodySectionDynamicCategoryDimensionConfiguration
<a name="aws-properties-quicksight-template-bodysectiondynamiccategorydimensionconfiguration"></a>

Describes the **Category** dataset column and constraints for the dynamic values used to repeat the contents of a section.

## Syntax
<a name="aws-properties-quicksight-template-bodysectiondynamiccategorydimensionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-bodysectiondynamiccategorydimensionconfiguration-syntax.json"></a>

```
{
  "[Column](#cfn-quicksight-template-bodysectiondynamiccategorydimensionconfiguration-column)" : {{ColumnIdentifier}},
  "[Limit](#cfn-quicksight-template-bodysectiondynamiccategorydimensionconfiguration-limit)" : {{Number}},
  "[SortByMetrics](#cfn-quicksight-template-bodysectiondynamiccategorydimensionconfiguration-sortbymetrics)" : {{[ ColumnSort, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-bodysectiondynamiccategorydimensionconfiguration-syntax.yaml"></a>

```
  [Column](#cfn-quicksight-template-bodysectiondynamiccategorydimensionconfiguration-column): {{
    ColumnIdentifier}}
  [Limit](#cfn-quicksight-template-bodysectiondynamiccategorydimensionconfiguration-limit): {{Number}}
  [SortByMetrics](#cfn-quicksight-template-bodysectiondynamiccategorydimensionconfiguration-sortbymetrics): {{
    - ColumnSort}}
```

## Properties
<a name="aws-properties-quicksight-template-bodysectiondynamiccategorydimensionconfiguration-properties"></a>

`Column`  <a name="cfn-quicksight-template-bodysectiondynamiccategorydimensionconfiguration-column"></a>
Property description not available.
*Required*: Yes
*Type*: [ColumnIdentifier](aws-properties-quicksight-template-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Limit`  <a name="cfn-quicksight-template-bodysectiondynamiccategorydimensionconfiguration-limit"></a>
Number of values to use from the column for repetition.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortByMetrics`  <a name="cfn-quicksight-template-bodysectiondynamiccategorydimensionconfiguration-sortbymetrics"></a>
Sort criteria on the column values that you use for repetition.
*Required*: No
*Type*: Array of [ColumnSort](aws-properties-quicksight-template-columnsort.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
