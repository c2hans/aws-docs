---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-cloudwatchalarmdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster CloudWatchAlarmDefinition
<a name="aws-properties-emr-cluster-cloudwatchalarmdefinition"></a>

`CloudWatchAlarmDefinition` is a subproperty of the `ScalingTrigger `property, which determines when to trigger an automatic scaling activity. Scaling activity begins when you satisfy the defined alarm conditions.

## Syntax
<a name="aws-properties-emr-cluster-cloudwatchalarmdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-cloudwatchalarmdefinition-syntax.json"></a>

```
{
  "[ComparisonOperator](#cfn-emr-cluster-cloudwatchalarmdefinition-comparisonoperator)" : {{String}},
  "[Dimensions](#cfn-emr-cluster-cloudwatchalarmdefinition-dimensions)" : {{[ MetricDimension, ... ]}},
  "[EvaluationPeriods](#cfn-emr-cluster-cloudwatchalarmdefinition-evaluationperiods)" : {{Integer}},
  "[MetricName](#cfn-emr-cluster-cloudwatchalarmdefinition-metricname)" : {{String}},
  "[Namespace](#cfn-emr-cluster-cloudwatchalarmdefinition-namespace)" : {{String}},
  "[Period](#cfn-emr-cluster-cloudwatchalarmdefinition-period)" : {{Integer}},
  "[Statistic](#cfn-emr-cluster-cloudwatchalarmdefinition-statistic)" : {{String}},
  "[Threshold](#cfn-emr-cluster-cloudwatchalarmdefinition-threshold)" : {{Number}},
  "[Unit](#cfn-emr-cluster-cloudwatchalarmdefinition-unit)" : {{String}}
}
```

### YAML
<a name="aws-properties-emr-cluster-cloudwatchalarmdefinition-syntax.yaml"></a>

```
  [ComparisonOperator](#cfn-emr-cluster-cloudwatchalarmdefinition-comparisonoperator): {{String}}
  [Dimensions](#cfn-emr-cluster-cloudwatchalarmdefinition-dimensions): {{
    - MetricDimension}}
  [EvaluationPeriods](#cfn-emr-cluster-cloudwatchalarmdefinition-evaluationperiods): {{Integer}}
  [MetricName](#cfn-emr-cluster-cloudwatchalarmdefinition-metricname): {{String}}
  [Namespace](#cfn-emr-cluster-cloudwatchalarmdefinition-namespace): {{String}}
  [Period](#cfn-emr-cluster-cloudwatchalarmdefinition-period): {{Integer}}
  [Statistic](#cfn-emr-cluster-cloudwatchalarmdefinition-statistic): {{String}}
  [Threshold](#cfn-emr-cluster-cloudwatchalarmdefinition-threshold): {{Number}}
  [Unit](#cfn-emr-cluster-cloudwatchalarmdefinition-unit): {{String}}
```

## Properties
<a name="aws-properties-emr-cluster-cloudwatchalarmdefinition-properties"></a>

`ComparisonOperator`  <a name="cfn-emr-cluster-cloudwatchalarmdefinition-comparisonoperator"></a>
Determines how the metric specified by `MetricName` is compared to the value specified by `Threshold`.
*Required*: Yes
*Type*: String
*Allowed values*: `GREATER_THAN_OR_EQUAL | GREATER_THAN | LESS_THAN | LESS_THAN_OR_EQUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Dimensions`  <a name="cfn-emr-cluster-cloudwatchalarmdefinition-dimensions"></a>
A CloudWatch metric dimension.
*Required*: No
*Type*: Array of [MetricDimension](aws-properties-emr-cluster-metricdimension.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EvaluationPeriods`  <a name="cfn-emr-cluster-cloudwatchalarmdefinition-evaluationperiods"></a>
The number of periods, in five-minute increments, during which the alarm condition must exist before the alarm triggers automatic scaling activity. The default value is `1`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricName`  <a name="cfn-emr-cluster-cloudwatchalarmdefinition-metricname"></a>
The name of the CloudWatch metric that is watched to determine an alarm condition.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Namespace`  <a name="cfn-emr-cluster-cloudwatchalarmdefinition-namespace"></a>
The namespace for the CloudWatch metric. The default is `AWS/ElasticMapReduce`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Period`  <a name="cfn-emr-cluster-cloudwatchalarmdefinition-period"></a>
The period, in seconds, over which the statistic is applied. CloudWatch metrics for Amazon EMR are emitted every five minutes (300 seconds), so if you specify a CloudWatch metric, specify `300`.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Statistic`  <a name="cfn-emr-cluster-cloudwatchalarmdefinition-statistic"></a>
The statistic to apply to the metric associated with the alarm. The default is `AVERAGE`.
*Required*: No
*Type*: String
*Allowed values*: `SAMPLE_COUNT | AVERAGE | SUM | MINIMUM | MAXIMUM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Threshold`  <a name="cfn-emr-cluster-cloudwatchalarmdefinition-threshold"></a>
The value against which the specified statistic is compared.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unit`  <a name="cfn-emr-cluster-cloudwatchalarmdefinition-unit"></a>
The unit of measure associated with the CloudWatch metric being watched. The value specified for `Unit` must correspond to the units specified in the CloudWatch metric.
*Required*: No
*Type*: String
*Allowed values*: `NONE | SECONDS | MICRO_SECONDS | MILLI_SECONDS | BYTES | KILO_BYTES | MEGA_BYTES | GIGA_BYTES | TERA_BYTES | BITS | KILO_BITS | MEGA_BITS | GIGA_BITS | TERA_BITS | PERCENT | COUNT | BYTES_PER_SECOND | KILO_BYTES_PER_SECOND | MEGA_BYTES_PER_SECOND | GIGA_BYTES_PER_SECOND | TERA_BYTES_PER_SECOND | BITS_PER_SECOND | KILO_BITS_PER_SECOND | MEGA_BITS_PER_SECOND | GIGA_BITS_PER_SECOND | TERA_BITS_PER_SECOND | COUNT_PER_SECOND`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
