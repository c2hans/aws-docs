---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-anomalydetector-metricconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::AnomalyDetector MetricConfiguration
<a name="aws-properties-cloudwatch-anomalydetector-metricconfiguration"></a>

<a name="aws-properties-cloudwatch-anomalydetector-metricconfiguration-description"></a>The `MetricConfiguration` property type specifies Property description not available. for an [AWS::CloudWatch::AnomalyDetector](aws-resource-cloudwatch-anomalydetector.md).

## Syntax
<a name="aws-properties-cloudwatch-anomalydetector-metricconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-anomalydetector-metricconfiguration-syntax.json"></a>

```
{
  "[ExcludedTimeRanges](#cfn-cloudwatch-anomalydetector-metricconfiguration-excludedtimeranges)" : {{[ Range, ... ]}},
  "[MetricTimeZone](#cfn-cloudwatch-anomalydetector-metricconfiguration-metrictimezone)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-anomalydetector-metricconfiguration-syntax.yaml"></a>

```
  [ExcludedTimeRanges](#cfn-cloudwatch-anomalydetector-metricconfiguration-excludedtimeranges): {{
    - Range}}
  [MetricTimeZone](#cfn-cloudwatch-anomalydetector-metricconfiguration-metrictimezone): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-anomalydetector-metricconfiguration-properties"></a>

`ExcludedTimeRanges`  <a name="cfn-cloudwatch-anomalydetector-metricconfiguration-excludedtimeranges"></a>
Property description not available.
*Required*: No
*Type*: Array of [Range](aws-properties-cloudwatch-anomalydetector-range.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricTimeZone`  <a name="cfn-cloudwatch-anomalydetector-metricconfiguration-metrictimezone"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
