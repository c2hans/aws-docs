---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-anomalydetector-metricmathanomalydetector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::AnomalyDetector MetricMathAnomalyDetector
<a name="aws-properties-cloudwatch-anomalydetector-metricmathanomalydetector"></a>

Indicates the CloudWatch math expression that provides the time series the anomaly detector uses as input. The designated math expression must return a single time series.

## Syntax
<a name="aws-properties-cloudwatch-anomalydetector-metricmathanomalydetector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-anomalydetector-metricmathanomalydetector-syntax.json"></a>

```
{
  "[MetricDataQueries](#cfn-cloudwatch-anomalydetector-metricmathanomalydetector-metricdataqueries)" : {{[ MetricDataQuery, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudwatch-anomalydetector-metricmathanomalydetector-syntax.yaml"></a>

```
  [MetricDataQueries](#cfn-cloudwatch-anomalydetector-metricmathanomalydetector-metricdataqueries): {{
    - MetricDataQuery}}
```

## Properties
<a name="aws-properties-cloudwatch-anomalydetector-metricmathanomalydetector-properties"></a>

`MetricDataQueries`  <a name="cfn-cloudwatch-anomalydetector-metricmathanomalydetector-metricdataqueries"></a>
An array of metric data query structures that enables you to create an anomaly detector based on the result of a metric math expression. Each item in `MetricDataQueries` gets a metric or performs a math expression. One item in `MetricDataQueries` is the expression that provides the time series that the anomaly detector uses as input. Designate the expression by setting `ReturnData` to `true` for this object in the array. For all other expressions and metrics, set `ReturnData` to `false`. The designated expression must return a single time series.
*Required*: No
*Type*: Array of [MetricDataQuery](aws-properties-cloudwatch-anomalydetector-metricdataquery.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
