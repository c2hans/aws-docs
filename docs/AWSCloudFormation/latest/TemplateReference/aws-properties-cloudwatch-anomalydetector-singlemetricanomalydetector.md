---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::AnomalyDetector SingleMetricAnomalyDetector
<a name="aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector"></a>

Designates the CloudWatch metric and statistic that provides the time series the anomaly detector uses as input. If you have enabled unified cross-account observability, and this account is a monitoring account, the metric can be in the same account or a source account.

## Syntax
<a name="aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector-syntax.json"></a>

```
{
  "[AccountId](#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-accountid)" : {{String}},
  "[Dimensions](#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-dimensions)" : {{[ Dimension, ... ]}},
  "[MetricName](#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-metricname)" : {{String}},
  "[Namespace](#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-namespace)" : {{String}},
  "[Stat](#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-stat)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector-syntax.yaml"></a>

```
  [AccountId](#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-accountid): {{String}}
  [Dimensions](#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-dimensions): {{
    - Dimension}}
  [MetricName](#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-metricname): {{String}}
  [Namespace](#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-namespace): {{String}}
  [Stat](#cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-stat): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector-properties"></a>

`AccountId`  <a name="cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-accountid"></a>
If the CloudWatch metric that provides the time series that the anomaly detector uses as input is in another account, specify that account ID here. If you omit this parameter, the current account is used.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Dimensions`  <a name="cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-dimensions"></a>
The metric dimensions to create the anomaly detection model for.
*Required*: No
*Type*: Array of [Dimension](aws-properties-cloudwatch-anomalydetector-dimension.md)
*Maximum*: `30`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MetricName`  <a name="cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-metricname"></a>
The name of the metric to create the anomaly detection model for.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Namespace`  <a name="cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-namespace"></a>
The namespace of the metric to create the anomaly detection model for.
*Required*: No
*Type*: String
*Pattern*: `[^:].*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Stat`  <a name="cfn-cloudwatch-anomalydetector-singlemetricanomalydetector-stat"></a>
The statistic to use for the metric and anomaly detection model.
*Required*: No
*Type*: String
*Pattern*: `(SampleCount|Average|Sum|Minimum|Maximum|IQM|(p|tc|tm|ts|wm)(\d{1,2}(\.\d{0,10})?|100)|[ou]\d+(\.\d*)?)(_E|_L|_H)?|(TM|TC|TS|WM)\(((((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%)?:((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%|((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%:(((\d{1,2})(\.\d{0,10})?|100(\.0{0,10})?)%)?)\)|(TM|TC|TS|WM|PR)\(((\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)):((\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)))?|((\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)))?:(\d+(\.\d{0,10})?|(\d+(\.\d{0,10})?[Ee][+-]?\d+)))\)`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
