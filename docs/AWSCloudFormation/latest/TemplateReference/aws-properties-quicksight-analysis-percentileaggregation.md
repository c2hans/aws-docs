---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-percentileaggregation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis PercentileAggregation
<a name="aws-properties-quicksight-analysis-percentileaggregation"></a>

An aggregation based on the percentile of values in a dimension or measure.

## Syntax
<a name="aws-properties-quicksight-analysis-percentileaggregation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-percentileaggregation-syntax.json"></a>

```
{
  "[PercentileValue](#cfn-quicksight-analysis-percentileaggregation-percentilevalue)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-percentileaggregation-syntax.yaml"></a>

```
  [PercentileValue](#cfn-quicksight-analysis-percentileaggregation-percentilevalue): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-analysis-percentileaggregation-properties"></a>

`PercentileValue`  <a name="cfn-quicksight-analysis-percentileaggregation-percentilevalue"></a>
The percentile value. This value can be any numeric constant 0–100. A percentile value of 50 computes the median value of the measure.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
