---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-bodysectiondynamiccategorydimensionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis BodySectionDynamicCategoryDimensionConfiguration
<a name="aws-properties-quicksight-analysis-bodysectiondynamiccategorydimensionconfiguration"></a>

Describes the **Category** dataset column and constraints for the dynamic values used to repeat the contents of a section.

## Syntax
<a name="aws-properties-quicksight-analysis-bodysectiondynamiccategorydimensionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-bodysectiondynamiccategorydimensionconfiguration-syntax.json"></a>

```
{
  "[Column](#cfn-quicksight-analysis-bodysectiondynamiccategorydimensionconfiguration-column)" : {{ColumnIdentifier}},
  "[Limit](#cfn-quicksight-analysis-bodysectiondynamiccategorydimensionconfiguration-limit)" : {{Number}},
  "[SortByMetrics](#cfn-quicksight-analysis-bodysectiondynamiccategorydimensionconfiguration-sortbymetrics)" : {{[ ColumnSort, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-bodysectiondynamiccategorydimensionconfiguration-syntax.yaml"></a>

```
  [Column](#cfn-quicksight-analysis-bodysectiondynamiccategorydimensionconfiguration-column): {{
    ColumnIdentifier}}
  [Limit](#cfn-quicksight-analysis-bodysectiondynamiccategorydimensionconfiguration-limit): {{Number}}
  [SortByMetrics](#cfn-quicksight-analysis-bodysectiondynamiccategorydimensionconfiguration-sortbymetrics): {{
    - ColumnSort}}
```

## Properties
<a name="aws-properties-quicksight-analysis-bodysectiondynamiccategorydimensionconfiguration-properties"></a>

`Column`  <a name="cfn-quicksight-analysis-bodysectiondynamiccategorydimensionconfiguration-column"></a>
Property description not available.
*Required*: Yes
*Type*: [ColumnIdentifier](aws-properties-quicksight-analysis-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Limit`  <a name="cfn-quicksight-analysis-bodysectiondynamiccategorydimensionconfiguration-limit"></a>
Number of values to use from the column for repetition.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortByMetrics`  <a name="cfn-quicksight-analysis-bodysectiondynamiccategorydimensionconfiguration-sortbymetrics"></a>
Sort criteria on the column values that you use for repetition.
*Required*: No
*Type*: Array of [ColumnSort](aws-properties-quicksight-analysis-columnsort.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
