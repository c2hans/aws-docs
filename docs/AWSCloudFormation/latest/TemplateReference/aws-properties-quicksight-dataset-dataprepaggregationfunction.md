---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-dataprepaggregationfunction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DataPrepAggregationFunction
<a name="aws-properties-quicksight-dataset-dataprepaggregationfunction"></a>

Defines the type of aggregation function to apply to data during data preparation, supporting simple and list aggregations.

## Syntax
<a name="aws-properties-quicksight-dataset-dataprepaggregationfunction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-dataprepaggregationfunction-syntax.json"></a>

```
{
  "[ListAggregation](#cfn-quicksight-dataset-dataprepaggregationfunction-listaggregation)" : {{DataPrepListAggregationFunction}},
  "[PercentileAggregation](#cfn-quicksight-dataset-dataprepaggregationfunction-percentileaggregation)" : {{DataPrepPercentileAggregationFunction}},
  "[SimpleAggregation](#cfn-quicksight-dataset-dataprepaggregationfunction-simpleaggregation)" : {{DataPrepSimpleAggregationFunction}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-dataprepaggregationfunction-syntax.yaml"></a>

```
  [ListAggregation](#cfn-quicksight-dataset-dataprepaggregationfunction-listaggregation): {{
    DataPrepListAggregationFunction}}
  [PercentileAggregation](#cfn-quicksight-dataset-dataprepaggregationfunction-percentileaggregation): {{
    DataPrepPercentileAggregationFunction}}
  [SimpleAggregation](#cfn-quicksight-dataset-dataprepaggregationfunction-simpleaggregation): {{
    DataPrepSimpleAggregationFunction}}
```

## Properties
<a name="aws-properties-quicksight-dataset-dataprepaggregationfunction-properties"></a>

`ListAggregation`  <a name="cfn-quicksight-dataset-dataprepaggregationfunction-listaggregation"></a>
A list aggregation function that concatenates values from multiple rows into a single delimited string.
*Required*: No
*Type*: [DataPrepListAggregationFunction](aws-properties-quicksight-dataset-datapreplistaggregationfunction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PercentileAggregation`  <a name="cfn-quicksight-dataset-dataprepaggregationfunction-percentileaggregation"></a>
Property description not available.
*Required*: No
*Type*: [DataPrepPercentileAggregationFunction](aws-properties-quicksight-dataset-datapreppercentileaggregationfunction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SimpleAggregation`  <a name="cfn-quicksight-dataset-dataprepaggregationfunction-simpleaggregation"></a>
A simple aggregation function such as `SUM`, `COUNT`, `AVERAGE`, `MIN`, `MAX`, `MEDIAN`, `VARIANCE`, or `STANDARD_DEVIATION`.
*Required*: No
*Type*: [DataPrepSimpleAggregationFunction](aws-properties-quicksight-dataset-dataprepsimpleaggregationfunction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
