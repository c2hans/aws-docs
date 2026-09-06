---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-job-exponentialrolloutrate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Job ExponentialRolloutRate
<a name="aws-properties-iot-job-exponentialrolloutrate"></a>

Allows you to create an exponential rate of rollout for a job.

## Syntax
<a name="aws-properties-iot-job-exponentialrolloutrate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-job-exponentialrolloutrate-syntax.json"></a>

```
{
  "[BaseRatePerMinute](#cfn-iot-job-exponentialrolloutrate-baserateperminute)" : {{Integer}},
  "[IncrementFactor](#cfn-iot-job-exponentialrolloutrate-incrementfactor)" : {{Number}},
  "[RateIncreaseCriteria](#cfn-iot-job-exponentialrolloutrate-rateincreasecriteria)" : {{RateIncreaseCriteria}}
}
```

### YAML
<a name="aws-properties-iot-job-exponentialrolloutrate-syntax.yaml"></a>

```
  [BaseRatePerMinute](#cfn-iot-job-exponentialrolloutrate-baserateperminute): {{Integer}}
  [IncrementFactor](#cfn-iot-job-exponentialrolloutrate-incrementfactor): {{Number}}
  [RateIncreaseCriteria](#cfn-iot-job-exponentialrolloutrate-rateincreasecriteria): {{
    RateIncreaseCriteria}}
```

## Properties
<a name="aws-properties-iot-job-exponentialrolloutrate-properties"></a>

`BaseRatePerMinute`  <a name="cfn-iot-job-exponentialrolloutrate-baserateperminute"></a>
The minimum number of things that will be notified of a pending job, per minute at the start of job rollout. This parameter allows you to define the initial rate of rollout.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncrementFactor`  <a name="cfn-iot-job-exponentialrolloutrate-incrementfactor"></a>
The exponential factor to increase the rate of rollout for a job.
AWS IoT Core supports up to one digit after the decimal (for example, 1.5, but not 1.55).
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RateIncreaseCriteria`  <a name="cfn-iot-job-exponentialrolloutrate-rateincreasecriteria"></a>
The criteria to initiate the increase in rate of rollout for a job.
*Required*: Yes
*Type*: [RateIncreaseCriteria](aws-properties-iot-job-rateincreasecriteria.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
