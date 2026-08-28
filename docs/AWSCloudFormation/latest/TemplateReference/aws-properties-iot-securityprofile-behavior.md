---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-securityprofile-behavior.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::SecurityProfile Behavior
<a name="aws-properties-iot-securityprofile-behavior"></a>

A Device Defender security profile behavior.

## Syntax
<a name="aws-properties-iot-securityprofile-behavior-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-securityprofile-behavior-syntax.json"></a>

```
{
  "[Criteria](#cfn-iot-securityprofile-behavior-criteria)" : {{BehaviorCriteria}},
  "[ExportMetric](#cfn-iot-securityprofile-behavior-exportmetric)" : {{Boolean}},
  "[Metric](#cfn-iot-securityprofile-behavior-metric)" : {{String}},
  "[MetricDimension](#cfn-iot-securityprofile-behavior-metricdimension)" : {{MetricDimension}},
  "[Name](#cfn-iot-securityprofile-behavior-name)" : {{String}},
  "[SuppressAlerts](#cfn-iot-securityprofile-behavior-suppressalerts)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-iot-securityprofile-behavior-syntax.yaml"></a>

```
  [Criteria](#cfn-iot-securityprofile-behavior-criteria): {{
    BehaviorCriteria}}
  [ExportMetric](#cfn-iot-securityprofile-behavior-exportmetric): {{Boolean}}
  [Metric](#cfn-iot-securityprofile-behavior-metric): {{String}}
  [MetricDimension](#cfn-iot-securityprofile-behavior-metricdimension): {{
    MetricDimension}}
  [Name](#cfn-iot-securityprofile-behavior-name): {{String}}
  [SuppressAlerts](#cfn-iot-securityprofile-behavior-suppressalerts): {{Boolean}}
```

## Properties
<a name="aws-properties-iot-securityprofile-behavior-properties"></a>

`Criteria`  <a name="cfn-iot-securityprofile-behavior-criteria"></a>
The criteria that determine if a device is behaving normally in regard to the `metric`.
In the AWS IoT console, you can choose to be sent an alert through Amazon SNS when AWS IoT Device Defender detects that a device is behaving anomalously.
*Required*: No
*Type*: [BehaviorCriteria](aws-properties-iot-securityprofile-behaviorcriteria.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportMetric`  <a name="cfn-iot-securityprofile-behavior-exportmetric"></a>
Value indicates exporting metrics related to the behavior when it is true.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Metric`  <a name="cfn-iot-securityprofile-behavior-metric"></a>
What is measured by the behavior.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9:_-]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricDimension`  <a name="cfn-iot-securityprofile-behavior-metricdimension"></a>
The dimension of the metric.
*Required*: No
*Type*: [MetricDimension](aws-properties-iot-securityprofile-metricdimension.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-iot-securityprofile-behavior-name"></a>
The name you've given to the behavior.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9:_-]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SuppressAlerts`  <a name="cfn-iot-securityprofile-behavior-suppressalerts"></a>
The alert status. If you set the value to `true`, alerts will be suppressed.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
