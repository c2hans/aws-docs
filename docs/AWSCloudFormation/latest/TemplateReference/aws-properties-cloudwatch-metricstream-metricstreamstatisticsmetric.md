---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-metricstream-metricstreamstatisticsmetric.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::MetricStream MetricStreamStatisticsMetric
<a name="aws-properties-cloudwatch-metricstream-metricstreamstatisticsmetric"></a>

A structure that specifies the metric name and namespace for one metric that is going to have additional statistics included in the stream.

## Syntax
<a name="aws-properties-cloudwatch-metricstream-metricstreamstatisticsmetric-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-metricstream-metricstreamstatisticsmetric-syntax.json"></a>

```
{
  "[MetricName](#cfn-cloudwatch-metricstream-metricstreamstatisticsmetric-metricname)" : {{String}},
  "[Namespace](#cfn-cloudwatch-metricstream-metricstreamstatisticsmetric-namespace)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-metricstream-metricstreamstatisticsmetric-syntax.yaml"></a>

```
  [MetricName](#cfn-cloudwatch-metricstream-metricstreamstatisticsmetric-metricname): {{String}}
  [Namespace](#cfn-cloudwatch-metricstream-metricstreamstatisticsmetric-namespace): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-metricstream-metricstreamstatisticsmetric-properties"></a>

`MetricName`  <a name="cfn-cloudwatch-metricstream-metricstreamstatisticsmetric-metricname"></a>
The name of the metric.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Namespace`  <a name="cfn-cloudwatch-metricstream-metricstreamstatisticsmetric-namespace"></a>
The namespace of the metric.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
