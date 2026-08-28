---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-securityprofile-statisticalthreshold.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::SecurityProfile StatisticalThreshold
<a name="aws-properties-iot-securityprofile-statisticalthreshold"></a>

A statistical ranking (percentile) that indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.

## Syntax
<a name="aws-properties-iot-securityprofile-statisticalthreshold-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-securityprofile-statisticalthreshold-syntax.json"></a>

```
{
  "[Statistic](#cfn-iot-securityprofile-statisticalthreshold-statistic)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-securityprofile-statisticalthreshold-syntax.yaml"></a>

```
  [Statistic](#cfn-iot-securityprofile-statisticalthreshold-statistic): {{String}}
```

## Properties
<a name="aws-properties-iot-securityprofile-statisticalthreshold-properties"></a>

`Statistic`  <a name="cfn-iot-securityprofile-statisticalthreshold-statistic"></a>
The percentile that resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period (`durationSeconds`) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below (`comparisonOperator`) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.
*Required*: No
*Type*: String
*Allowed values*: `Average | p0 | p0.1 | p0.01 | p1 | p10 | p50 | p90 | p99 | p99.9 | p99.99 | p100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
