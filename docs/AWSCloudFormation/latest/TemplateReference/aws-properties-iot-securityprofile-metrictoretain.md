---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-securityprofile-metrictoretain.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::SecurityProfile MetricToRetain
<a name="aws-properties-iot-securityprofile-metrictoretain"></a>

The metric you want to retain. Dimensions are optional.

## Syntax
<a name="aws-properties-iot-securityprofile-metrictoretain-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-securityprofile-metrictoretain-syntax.json"></a>

```
{
  "[ExportMetric](#cfn-iot-securityprofile-metrictoretain-exportmetric)" : {{Boolean}},
  "[Metric](#cfn-iot-securityprofile-metrictoretain-metric)" : {{String}},
  "[MetricDimension](#cfn-iot-securityprofile-metrictoretain-metricdimension)" : {{MetricDimension}}
}
```

### YAML
<a name="aws-properties-iot-securityprofile-metrictoretain-syntax.yaml"></a>

```
  [ExportMetric](#cfn-iot-securityprofile-metrictoretain-exportmetric): {{Boolean}}
  [Metric](#cfn-iot-securityprofile-metrictoretain-metric): {{String}}
  [MetricDimension](#cfn-iot-securityprofile-metrictoretain-metricdimension): {{
    MetricDimension}}
```

## Properties
<a name="aws-properties-iot-securityprofile-metrictoretain-properties"></a>

`ExportMetric`  <a name="cfn-iot-securityprofile-metrictoretain-exportmetric"></a>
The value indicates exporting metrics related to the `MetricToRetain` when it's true.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Metric`  <a name="cfn-iot-securityprofile-metrictoretain-metric"></a>
A standard of measurement.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9:_-]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricDimension`  <a name="cfn-iot-securityprofile-metrictoretain-metricdimension"></a>
The dimension of the metric.
*Required*: No
*Type*: [MetricDimension](aws-properties-iot-securityprofile-metricdimension.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
