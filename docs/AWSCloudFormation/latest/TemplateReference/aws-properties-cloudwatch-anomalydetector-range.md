---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-anomalydetector-range.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::AnomalyDetector Range
<a name="aws-properties-cloudwatch-anomalydetector-range"></a>

Each `Range` specifies one range of days or times to exclude from use for training or updating an anomaly detection model.

## Syntax
<a name="aws-properties-cloudwatch-anomalydetector-range-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-anomalydetector-range-syntax.json"></a>

```
{
  "[EndTime](#cfn-cloudwatch-anomalydetector-range-endtime)" : {{String}},
  "[StartTime](#cfn-cloudwatch-anomalydetector-range-starttime)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-anomalydetector-range-syntax.yaml"></a>

```
  [EndTime](#cfn-cloudwatch-anomalydetector-range-endtime): {{String}}
  [StartTime](#cfn-cloudwatch-anomalydetector-range-starttime): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-anomalydetector-range-properties"></a>

`EndTime`  <a name="cfn-cloudwatch-anomalydetector-range-endtime"></a>
The end time of the range to exclude. The format is `yyyy-MM-dd'T'HH:mm:ss`. For example, `2019-07-01T23:59:59`.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9]{4})-([0-1][0-9])-([0-3][0-9])T([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartTime`  <a name="cfn-cloudwatch-anomalydetector-range-starttime"></a>
The start time of the range to exclude. The format is `yyyy-MM-dd'T'HH:mm:ss`. For example, `2019-07-01T23:59:59`.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9]{4})-([0-1][0-9])-([0-3][0-9])T([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
