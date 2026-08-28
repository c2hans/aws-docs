---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-dataprepsimpleaggregationfunction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DataPrepSimpleAggregationFunction
<a name="aws-properties-quicksight-dataset-dataprepsimpleaggregationfunction"></a>

A simple aggregation function that performs standard statistical operations on a column.

## Syntax
<a name="aws-properties-quicksight-dataset-dataprepsimpleaggregationfunction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-dataprepsimpleaggregationfunction-syntax.json"></a>

```
{
  "[FunctionType](#cfn-quicksight-dataset-dataprepsimpleaggregationfunction-functiontype)" : {{String}},
  "[InputColumnName](#cfn-quicksight-dataset-dataprepsimpleaggregationfunction-inputcolumnname)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-dataprepsimpleaggregationfunction-syntax.yaml"></a>

```
  [FunctionType](#cfn-quicksight-dataset-dataprepsimpleaggregationfunction-functiontype): {{String}}
  [InputColumnName](#cfn-quicksight-dataset-dataprepsimpleaggregationfunction-inputcolumnname): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-dataprepsimpleaggregationfunction-properties"></a>

`FunctionType`  <a name="cfn-quicksight-dataset-dataprepsimpleaggregationfunction-functiontype"></a>
The type of aggregation function to perform, such as `COUNT`, `SUM`, `AVERAGE`, `MIN`, `MAX`, `MEDIAN`, `VARIANCE`, or `STANDARD_DEVIATION`.
*Required*: Yes
*Type*: String
*Allowed values*: `COUNT | DISTINCT_COUNT | SUM | AVERAGE | MEDIAN | MAX | MIN | VARIANCE | STANDARD_DEVIATION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputColumnName`  <a name="cfn-quicksight-dataset-dataprepsimpleaggregationfunction-inputcolumnname"></a>
The name of the column on which to perform the aggregation function.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
