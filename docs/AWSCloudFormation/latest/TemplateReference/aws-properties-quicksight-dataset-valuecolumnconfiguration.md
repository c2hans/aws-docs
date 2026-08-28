---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-valuecolumnconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet ValueColumnConfiguration
<a name="aws-properties-quicksight-dataset-valuecolumnconfiguration"></a>

Configuration for how to handle value columns in pivot operations, including aggregation settings.

## Syntax
<a name="aws-properties-quicksight-dataset-valuecolumnconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-valuecolumnconfiguration-syntax.json"></a>

```
{
  "[AggregationFunction](#cfn-quicksight-dataset-valuecolumnconfiguration-aggregationfunction)" : {{DataPrepAggregationFunction}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-valuecolumnconfiguration-syntax.yaml"></a>

```
  [AggregationFunction](#cfn-quicksight-dataset-valuecolumnconfiguration-aggregationfunction): {{
    DataPrepAggregationFunction}}
```

## Properties
<a name="aws-properties-quicksight-dataset-valuecolumnconfiguration-properties"></a>

`AggregationFunction`  <a name="cfn-quicksight-dataset-valuecolumnconfiguration-aggregationfunction"></a>
The aggregation function to apply when multiple values map to the same pivoted cell.
*Required*: No
*Type*: [DataPrepAggregationFunction](aws-properties-quicksight-dataset-dataprepaggregationfunction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
