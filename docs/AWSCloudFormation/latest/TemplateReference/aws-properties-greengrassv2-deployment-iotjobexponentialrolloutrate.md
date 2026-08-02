---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrassv2-deployment-iotjobexponentialrolloutrate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GreengrassV2::Deployment IoTJobExponentialRolloutRate
<a name="aws-properties-greengrassv2-deployment-iotjobexponentialrolloutrate"></a>

Contains information about an exponential rollout rate for a configuration deployment job.

## Syntax
<a name="aws-properties-greengrassv2-deployment-iotjobexponentialrolloutrate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrassv2-deployment-iotjobexponentialrolloutrate-syntax.json"></a>

```
{
  "[BaseRatePerMinute](#cfn-greengrassv2-deployment-iotjobexponentialrolloutrate-baserateperminute)" : {{Integer}},
  "[IncrementFactor](#cfn-greengrassv2-deployment-iotjobexponentialrolloutrate-incrementfactor)" : {{Number}},
  "[RateIncreaseCriteria](#cfn-greengrassv2-deployment-iotjobexponentialrolloutrate-rateincreasecriteria)" : {{IoTJobRateIncreaseCriteria}}
}
```

### YAML
<a name="aws-properties-greengrassv2-deployment-iotjobexponentialrolloutrate-syntax.yaml"></a>

```
  [BaseRatePerMinute](#cfn-greengrassv2-deployment-iotjobexponentialrolloutrate-baserateperminute): {{Integer}}
  [IncrementFactor](#cfn-greengrassv2-deployment-iotjobexponentialrolloutrate-incrementfactor): {{Number}}
  [RateIncreaseCriteria](#cfn-greengrassv2-deployment-iotjobexponentialrolloutrate-rateincreasecriteria): {{
    IoTJobRateIncreaseCriteria}}
```

## Properties
<a name="aws-properties-greengrassv2-deployment-iotjobexponentialrolloutrate-properties"></a>

`BaseRatePerMinute`  <a name="cfn-greengrassv2-deployment-iotjobexponentialrolloutrate-baserateperminute"></a>
The minimum number of devices that receive a pending job notification, per minute, when the job starts. This parameter defines the initial rollout rate of the job.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IncrementFactor`  <a name="cfn-greengrassv2-deployment-iotjobexponentialrolloutrate-incrementfactor"></a>
The exponential factor to increase the rollout rate for the job.
This parameter supports up to one digit after the decimal (for example, you can specify `1.5`, but not `1.55`).
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RateIncreaseCriteria`  <a name="cfn-greengrassv2-deployment-iotjobexponentialrolloutrate-rateincreasecriteria"></a>
The criteria to increase the rollout rate for the job.
*Required*: Yes
*Type*: [IoTJobRateIncreaseCriteria](aws-properties-greengrassv2-deployment-iotjobrateincreasecriteria.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
