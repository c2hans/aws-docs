---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-anomalydetector-metriccharacteristics.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::AnomalyDetector MetricCharacteristics
<a name="aws-properties-cloudwatch-anomalydetector-metriccharacteristics"></a>

This object includes parameters that you can use to provide information to CloudWatch to help it build more accurate anomaly detection models.

## Syntax
<a name="aws-properties-cloudwatch-anomalydetector-metriccharacteristics-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-anomalydetector-metriccharacteristics-syntax.json"></a>

```
{
  "[PeriodicSpikes](#cfn-cloudwatch-anomalydetector-metriccharacteristics-periodicspikes)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cloudwatch-anomalydetector-metriccharacteristics-syntax.yaml"></a>

```
  [PeriodicSpikes](#cfn-cloudwatch-anomalydetector-metriccharacteristics-periodicspikes): {{Boolean}}
```

## Properties
<a name="aws-properties-cloudwatch-anomalydetector-metriccharacteristics-properties"></a>

`PeriodicSpikes`  <a name="cfn-cloudwatch-anomalydetector-metriccharacteristics-periodicspikes"></a>
Set this parameter to true if values for this metric consistently include spikes that should not be considered to be anomalies. With this set to true, CloudWatch will expect to see spikes that occurred consistently during the model training period, and won't flag future similar spikes as anomalies.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
