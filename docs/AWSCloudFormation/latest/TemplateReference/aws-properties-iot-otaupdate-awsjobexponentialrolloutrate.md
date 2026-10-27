---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-otaupdate-awsjobexponentialrolloutrate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::OTAUpdate AwsJobExponentialRolloutRate
<a name="aws-properties-iot-otaupdate-awsjobexponentialrolloutrate"></a>

The rate of increase for a job rollout. This parameter allows you to define an exponential rate increase for a job rollout.

## Syntax
<a name="aws-properties-iot-otaupdate-awsjobexponentialrolloutrate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-otaupdate-awsjobexponentialrolloutrate-syntax.json"></a>

```
{
  "[BaseRatePerMinute](#cfn-iot-otaupdate-awsjobexponentialrolloutrate-baserateperminute)" : {{Integer}},
  "[IncrementFactor](#cfn-iot-otaupdate-awsjobexponentialrolloutrate-incrementfactor)" : {{Number}},
  "[RateIncreaseCriteria](#cfn-iot-otaupdate-awsjobexponentialrolloutrate-rateincreasecriteria)" : {{AwsJobRateIncreaseCriteria}}
}
```

### YAML
<a name="aws-properties-iot-otaupdate-awsjobexponentialrolloutrate-syntax.yaml"></a>

```
  [BaseRatePerMinute](#cfn-iot-otaupdate-awsjobexponentialrolloutrate-baserateperminute): {{Integer}}
  [IncrementFactor](#cfn-iot-otaupdate-awsjobexponentialrolloutrate-incrementfactor): {{Number}}
  [RateIncreaseCriteria](#cfn-iot-otaupdate-awsjobexponentialrolloutrate-rateincreasecriteria): {{
    AwsJobRateIncreaseCriteria}}
```

## Properties
<a name="aws-properties-iot-otaupdate-awsjobexponentialrolloutrate-properties"></a>

`BaseRatePerMinute`  <a name="cfn-iot-otaupdate-awsjobexponentialrolloutrate-baserateperminute"></a>
The minimum number of things that will be notified of a pending job, per minute, at the start of the job rollout. This is the initial rate of the rollout.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IncrementFactor`  <a name="cfn-iot-otaupdate-awsjobexponentialrolloutrate-incrementfactor"></a>
The rate of increase for a job rollout. The number of things notified is multiplied by this factor.
*Required*: Yes
*Type*: Number
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RateIncreaseCriteria`  <a name="cfn-iot-otaupdate-awsjobexponentialrolloutrate-rateincreasecriteria"></a>
The criteria to initiate the increase in rate of rollout for a job.
AWS IoT Core supports up to one digit after the decimal (for example, 1.5, but not 1.55).
*Required*: Yes
*Type*: [AwsJobRateIncreaseCriteria](aws-properties-iot-otaupdate-awsjobrateincreasecriteria.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
