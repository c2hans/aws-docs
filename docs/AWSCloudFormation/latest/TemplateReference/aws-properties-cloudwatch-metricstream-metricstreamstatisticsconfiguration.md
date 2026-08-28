---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-metricstream-metricstreamstatisticsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::MetricStream MetricStreamStatisticsConfiguration
<a name="aws-properties-cloudwatch-metricstream-metricstreamstatisticsconfiguration"></a>

This structure specifies a list of additional statistics to stream, and the metrics to stream those additional statistics for.

All metrics that match the combination of metric name and namespace will be streamed with the additional statistics, no matter their dimensions.

## Syntax
<a name="aws-properties-cloudwatch-metricstream-metricstreamstatisticsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-metricstream-metricstreamstatisticsconfiguration-syntax.json"></a>

```
{
  "[AdditionalStatistics](#cfn-cloudwatch-metricstream-metricstreamstatisticsconfiguration-additionalstatistics)" : {{[ String, ... ]}},
  "[IncludeMetrics](#cfn-cloudwatch-metricstream-metricstreamstatisticsconfiguration-includemetrics)" : {{[ MetricStreamStatisticsMetric, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudwatch-metricstream-metricstreamstatisticsconfiguration-syntax.yaml"></a>

```
  [AdditionalStatistics](#cfn-cloudwatch-metricstream-metricstreamstatisticsconfiguration-additionalstatistics): {{
    - String}}
  [IncludeMetrics](#cfn-cloudwatch-metricstream-metricstreamstatisticsconfiguration-includemetrics): {{
    - MetricStreamStatisticsMetric}}
```

## Properties
<a name="aws-properties-cloudwatch-metricstream-metricstreamstatisticsconfiguration-properties"></a>

`AdditionalStatistics`  <a name="cfn-cloudwatch-metricstream-metricstreamstatisticsconfiguration-additionalstatistics"></a>
The additional statistics to stream for the metrics listed in `IncludeMetrics`.
*Required*: Yes
*Type*: Array of String
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeMetrics`  <a name="cfn-cloudwatch-metricstream-metricstreamstatisticsconfiguration-includemetrics"></a>
An array that defines the metrics that are to have additional statistics streamed.
*Required*: Yes
*Type*: Array of [MetricStreamStatisticsMetric](aws-properties-cloudwatch-metricstream-metricstreamstatisticsmetric.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
