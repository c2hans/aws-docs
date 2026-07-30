---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-anomalydetector-ignorenearexpected.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::AnomalyDetector IgnoreNearExpected
<a name="aws-properties-aps-anomalydetector-ignorenearexpected"></a>

Configuration for threshold settings that determine when values near expected values should be ignored during anomaly detection.

## Syntax
<a name="aws-properties-aps-anomalydetector-ignorenearexpected-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-anomalydetector-ignorenearexpected-syntax.json"></a>

```
{
  "[Amount](#cfn-aps-anomalydetector-ignorenearexpected-amount)" : {{Number}},
  "[Ratio](#cfn-aps-anomalydetector-ignorenearexpected-ratio)" : {{Number}}
}
```

### YAML
<a name="aws-properties-aps-anomalydetector-ignorenearexpected-syntax.yaml"></a>

```
  [Amount](#cfn-aps-anomalydetector-ignorenearexpected-amount): {{Number}}
  [Ratio](#cfn-aps-anomalydetector-ignorenearexpected-ratio): {{Number}}
```

## Properties
<a name="aws-properties-aps-anomalydetector-ignorenearexpected-properties"></a>

`Amount`  <a name="cfn-aps-anomalydetector-ignorenearexpected-amount"></a>
The absolute amount by which values can differ from expected values before being considered anomalous.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ratio`  <a name="cfn-aps-anomalydetector-ignorenearexpected-ratio"></a>
The ratio by which values can differ from expected values before being considered anomalous.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
