---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-numericalaggregationfunction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template NumericalAggregationFunction
<a name="aws-properties-quicksight-template-numericalaggregationfunction"></a>

Aggregation for numerical values.

## Syntax
<a name="aws-properties-quicksight-template-numericalaggregationfunction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-numericalaggregationfunction-syntax.json"></a>

```
{
  "[PercentileAggregation](#cfn-quicksight-template-numericalaggregationfunction-percentileaggregation)" : {{PercentileAggregation}},
  "[SimpleNumericalAggregation](#cfn-quicksight-template-numericalaggregationfunction-simplenumericalaggregation)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-numericalaggregationfunction-syntax.yaml"></a>

```
  [PercentileAggregation](#cfn-quicksight-template-numericalaggregationfunction-percentileaggregation): {{
    PercentileAggregation}}
  [SimpleNumericalAggregation](#cfn-quicksight-template-numericalaggregationfunction-simplenumericalaggregation): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-numericalaggregationfunction-properties"></a>

`PercentileAggregation`  <a name="cfn-quicksight-template-numericalaggregationfunction-percentileaggregation"></a>
An aggregation based on the percentile of values in a dimension or measure.
*Required*: No
*Type*: [PercentileAggregation](aws-properties-quicksight-template-percentileaggregation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SimpleNumericalAggregation`  <a name="cfn-quicksight-template-numericalaggregationfunction-simplenumericalaggregation"></a>
Built-in aggregation functions for numerical values.
+ `SUM`: The sum of a dimension or measure.
+ `AVERAGE`: The average of a dimension or measure.
+ `MIN`: The minimum value of a dimension or measure.
+ `MAX`: The maximum value of a dimension or measure.
+ `COUNT`: The count of a dimension or measure.
+ `DISTINCT_COUNT`: The count of distinct values in a dimension or measure.
+ `VAR`: The variance of a dimension or measure.
+ `VARP`: The partitioned variance of a dimension or measure.
+ `STDEV`: The standard deviation of a dimension or measure.
+ `STDEVP`: The partitioned standard deviation of a dimension or measure.
+ `MEDIAN`: The median value of a dimension or measure.
*Required*: No
*Type*: String
*Allowed values*: `SUM | AVERAGE | MIN | MAX | COUNT | DISTINCT_COUNT | VAR | VARP | STDEV | STDEVP | MEDIAN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
