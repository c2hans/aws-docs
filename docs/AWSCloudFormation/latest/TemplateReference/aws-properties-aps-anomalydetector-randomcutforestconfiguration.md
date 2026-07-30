---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aps-anomalydetector-randomcutforestconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::AnomalyDetector RandomCutForestConfiguration
<a name="aws-properties-aps-anomalydetector-randomcutforestconfiguration"></a>

Configuration for the Random Cut Forest algorithm used for anomaly detection in time-series data.

## Syntax
<a name="aws-properties-aps-anomalydetector-randomcutforestconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aps-anomalydetector-randomcutforestconfiguration-syntax.json"></a>

```
{
  "[IgnoreNearExpectedFromAbove](#cfn-aps-anomalydetector-randomcutforestconfiguration-ignorenearexpectedfromabove)" : {{IgnoreNearExpected}},
  "[IgnoreNearExpectedFromBelow](#cfn-aps-anomalydetector-randomcutforestconfiguration-ignorenearexpectedfrombelow)" : {{IgnoreNearExpected}},
  "[Query](#cfn-aps-anomalydetector-randomcutforestconfiguration-query)" : {{String}},
  "[SampleSize](#cfn-aps-anomalydetector-randomcutforestconfiguration-samplesize)" : {{Integer}},
  "[ShingleSize](#cfn-aps-anomalydetector-randomcutforestconfiguration-shinglesize)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-aps-anomalydetector-randomcutforestconfiguration-syntax.yaml"></a>

```
  [IgnoreNearExpectedFromAbove](#cfn-aps-anomalydetector-randomcutforestconfiguration-ignorenearexpectedfromabove): {{
    IgnoreNearExpected}}
  [IgnoreNearExpectedFromBelow](#cfn-aps-anomalydetector-randomcutforestconfiguration-ignorenearexpectedfrombelow): {{
    IgnoreNearExpected}}
  [Query](#cfn-aps-anomalydetector-randomcutforestconfiguration-query): {{String}}
  [SampleSize](#cfn-aps-anomalydetector-randomcutforestconfiguration-samplesize): {{Integer}}
  [ShingleSize](#cfn-aps-anomalydetector-randomcutforestconfiguration-shinglesize): {{Integer}}
```

## Properties
<a name="aws-properties-aps-anomalydetector-randomcutforestconfiguration-properties"></a>

`IgnoreNearExpectedFromAbove`  <a name="cfn-aps-anomalydetector-randomcutforestconfiguration-ignorenearexpectedfromabove"></a>
Configuration for ignoring values that are near expected values from above during anomaly detection.
*Required*: No
*Type*: [IgnoreNearExpected](aws-properties-aps-anomalydetector-ignorenearexpected.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IgnoreNearExpectedFromBelow`  <a name="cfn-aps-anomalydetector-randomcutforestconfiguration-ignorenearexpectedfrombelow"></a>
Configuration for ignoring values that are near expected values from below during anomaly detection.
*Required*: No
*Type*: [IgnoreNearExpected](aws-properties-aps-anomalydetector-ignorenearexpected.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Query`  <a name="cfn-aps-anomalydetector-randomcutforestconfiguration-query"></a>
The Prometheus query used to retrieve the time-series data for anomaly detection.
Random Cut Forest queries must be wrapped by a supported PromQL aggregation operator. For more information, see [Aggregation operators](https://prometheus.io/docs/prometheus/latest/querying/operators/#aggregation-operators) on the *Prometheus docs* website.
**Supported PromQL aggregation operators**: `avg`, `count`, `group`, `max`, `min`, `quantile`, `stddev`, `stdvar`, and `sum`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SampleSize`  <a name="cfn-aps-anomalydetector-randomcutforestconfiguration-samplesize"></a>
The number of data points sampled from the input stream for the Random Cut Forest algorithm. The default number is 256 consecutive data points.
*Required*: No
*Type*: Integer
*Minimum*: `256`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShingleSize`  <a name="cfn-aps-anomalydetector-randomcutforestconfiguration-shinglesize"></a>
The number of consecutive data points used to create a shingle for the Random Cut Forest algorithm. The default number is 8 consecutive data points.
*Required*: No
*Type*: Integer
*Minimum*: `2`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
