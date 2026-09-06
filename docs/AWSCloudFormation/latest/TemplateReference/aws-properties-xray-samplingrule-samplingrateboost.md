---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-xray-samplingrule-samplingrateboost.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::XRay::SamplingRule SamplingRateBoost
<a name="aws-properties-xray-samplingrule-samplingrateboost"></a>

Enable temporary sampling rate increases when you detect anomalies to improve visibility.

## Syntax
<a name="aws-properties-xray-samplingrule-samplingrateboost-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-xray-samplingrule-samplingrateboost-syntax.json"></a>

```
{
  "[CooldownWindowMinutes](#cfn-xray-samplingrule-samplingrateboost-cooldownwindowminutes)" : {{Integer}},
  "[MaxRate](#cfn-xray-samplingrule-samplingrateboost-maxrate)" : {{Number}}
}
```

### YAML
<a name="aws-properties-xray-samplingrule-samplingrateboost-syntax.yaml"></a>

```
  [CooldownWindowMinutes](#cfn-xray-samplingrule-samplingrateboost-cooldownwindowminutes): {{Integer}}
  [MaxRate](#cfn-xray-samplingrule-samplingrateboost-maxrate): {{Number}}
```

## Properties
<a name="aws-properties-xray-samplingrule-samplingrateboost-properties"></a>

`CooldownWindowMinutes`  <a name="cfn-xray-samplingrule-samplingrateboost-cooldownwindowminutes"></a>
Sets the time window (in minutes) in which only one sampling rate boost can be triggered. After a boost occurs, no further boosts are allowed until the next window.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxRate`  <a name="cfn-xray-samplingrule-samplingrateboost-maxrate"></a>
Defines max temporary sampling rate to apply when a boost is triggered. Calculated boost rate by X-Ray will be less than or equal to this max rate.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
