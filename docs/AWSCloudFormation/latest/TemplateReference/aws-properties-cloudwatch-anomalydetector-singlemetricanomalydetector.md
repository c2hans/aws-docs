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
*Minimum*: `1`
*Maximum*: `255`
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
*Pattern*: `^(Minimum|Maximum|Sum|Average|SampleCount|(p|tm)[0-9]{1,2}|(p|tm)[0-9]{1,2}\.[0-9]{1,2}|(p|tm)100)$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
