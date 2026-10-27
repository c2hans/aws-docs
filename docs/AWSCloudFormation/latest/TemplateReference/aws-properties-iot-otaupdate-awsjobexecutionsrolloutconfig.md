---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-otaupdate-awsjobexecutionsrolloutconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::OTAUpdate AwsJobExecutionsRolloutConfig
<a name="aws-properties-iot-otaupdate-awsjobexecutionsrolloutconfig"></a>

Configuration for the rollout of OTA updates.

## Syntax
<a name="aws-properties-iot-otaupdate-awsjobexecutionsrolloutconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-otaupdate-awsjobexecutionsrolloutconfig-syntax.json"></a>

```
{
  "[ExponentialRate](#cfn-iot-otaupdate-awsjobexecutionsrolloutconfig-exponentialrate)" : {{AwsJobExponentialRolloutRate}},
  "[MaximumPerMinute](#cfn-iot-otaupdate-awsjobexecutionsrolloutconfig-maximumperminute)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-iot-otaupdate-awsjobexecutionsrolloutconfig-syntax.yaml"></a>

```
  [ExponentialRate](#cfn-iot-otaupdate-awsjobexecutionsrolloutconfig-exponentialrate): {{
    AwsJobExponentialRolloutRate}}
  [MaximumPerMinute](#cfn-iot-otaupdate-awsjobexecutionsrolloutconfig-maximumperminute): {{Integer}}
```

## Properties
<a name="aws-properties-iot-otaupdate-awsjobexecutionsrolloutconfig-properties"></a>

`ExponentialRate`  <a name="cfn-iot-otaupdate-awsjobexecutionsrolloutconfig-exponentialrate"></a>
The rate of increase for a job rollout. This parameter allows you to define an exponential rate increase for a job rollout.
*Required*: No
*Type*: [AwsJobExponentialRolloutRate](aws-properties-iot-otaupdate-awsjobexponentialrolloutrate.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaximumPerMinute`  <a name="cfn-iot-otaupdate-awsjobexecutionsrolloutconfig-maximumperminute"></a>
The maximum number of OTA update job executions started per minute.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
