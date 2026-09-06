---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-jobtemplate-exponentialrolloutrate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::JobTemplate ExponentialRolloutRate
<a name="aws-properties-iot-jobtemplate-exponentialrolloutrate"></a>

Allows you to create an exponential rate of rollout for a job.

## Syntax
<a name="aws-properties-iot-jobtemplate-exponentialrolloutrate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-jobtemplate-exponentialrolloutrate-syntax.json"></a>

```
{
  "[BaseRatePerMinute](#cfn-iot-jobtemplate-exponentialrolloutrate-baserateperminute)" : {{Integer}},
  "[IncrementFactor](#cfn-iot-jobtemplate-exponentialrolloutrate-incrementfactor)" : {{Number}},
  "[RateIncreaseCriteria](#cfn-iot-jobtemplate-exponentialrolloutrate-rateincreasecriteria)" : {{RateIncreaseCriteria}}
}
```

### YAML
<a name="aws-properties-iot-jobtemplate-exponentialrolloutrate-syntax.yaml"></a>

```
  [BaseRatePerMinute](#cfn-iot-jobtemplate-exponentialrolloutrate-baserateperminute): {{Integer}}
  [IncrementFactor](#cfn-iot-jobtemplate-exponentialrolloutrate-incrementfactor): {{Number}}
  [RateIncreaseCriteria](#cfn-iot-jobtemplate-exponentialrolloutrate-rateincreasecriteria): {{
    RateIncreaseCriteria}}
```

## Properties
<a name="aws-properties-iot-jobtemplate-exponentialrolloutrate-properties"></a>

`BaseRatePerMinute`  <a name="cfn-iot-jobtemplate-exponentialrolloutrate-baserateperminute"></a>
The minimum number of things that will be notified of a pending job, per minute at the start of job rollout. This parameter allows you to define the initial rate of rollout.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IncrementFactor`  <a name="cfn-iot-jobtemplate-exponentialrolloutrate-incrementfactor"></a>
The exponential factor to increase the rate of rollout for a job.
AWS IoT Core supports up to one digit after the decimal (for example, 1.5, but not 1.55).
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RateIncreaseCriteria`  <a name="cfn-iot-jobtemplate-exponentialrolloutrate-rateincreasecriteria"></a>
The criteria to initiate the increase in rate of rollout for a job.
*Required*: Yes
*Type*: [RateIncreaseCriteria](aws-properties-iot-jobtemplate-rateincreasecriteria.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
