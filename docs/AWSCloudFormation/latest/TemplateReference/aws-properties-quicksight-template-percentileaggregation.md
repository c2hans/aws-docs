---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-percentileaggregation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template PercentileAggregation
<a name="aws-properties-quicksight-template-percentileaggregation"></a>

An aggregation based on the percentile of values in a dimension or measure.

## Syntax
<a name="aws-properties-quicksight-template-percentileaggregation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-percentileaggregation-syntax.json"></a>

```
{
  "[PercentileValue](#cfn-quicksight-template-percentileaggregation-percentilevalue)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-template-percentileaggregation-syntax.yaml"></a>

```
  [PercentileValue](#cfn-quicksight-template-percentileaggregation-percentilevalue): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-template-percentileaggregation-properties"></a>

`PercentileValue`  <a name="cfn-quicksight-template-percentileaggregation-percentilevalue"></a>
The percentile value. This value can be any numeric constant 0–100. A percentile value of 50 computes the median value of the measure.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
