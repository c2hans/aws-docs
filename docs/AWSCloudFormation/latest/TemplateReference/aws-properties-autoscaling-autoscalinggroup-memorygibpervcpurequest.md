---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-autoscalinggroup-memorygibpervcpurequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::AutoScalingGroup MemoryGiBPerVCpuRequest
<a name="aws-properties-autoscaling-autoscalinggroup-memorygibpervcpurequest"></a>

`MemoryGiBPerVCpuRequest` is a property of the `InstanceRequirements` property of the [AWS::AutoScaling::AutoScalingGroup LaunchTemplateOverrides](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-launchtemplateoverrides.html) property type that describes the minimum and maximum amount of memory per vCPU for an instance type, in GiB.

## Syntax
<a name="aws-properties-autoscaling-autoscalinggroup-memorygibpervcpurequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-autoscalinggroup-memorygibpervcpurequest-syntax.json"></a>

```
{
  "[Max](#cfn-autoscaling-autoscalinggroup-memorygibpervcpurequest-max)" : {{Number}},
  "[Min](#cfn-autoscaling-autoscalinggroup-memorygibpervcpurequest-min)" : {{Number}}
}
```

### YAML
<a name="aws-properties-autoscaling-autoscalinggroup-memorygibpervcpurequest-syntax.yaml"></a>

```
  [Max](#cfn-autoscaling-autoscalinggroup-memorygibpervcpurequest-max): {{Number}}
  [Min](#cfn-autoscaling-autoscalinggroup-memorygibpervcpurequest-min): {{Number}}
```

## Properties
<a name="aws-properties-autoscaling-autoscalinggroup-memorygibpervcpurequest-properties"></a>

`Max`  <a name="cfn-autoscaling-autoscalinggroup-memorygibpervcpurequest-max"></a>
The memory maximum in GiB.
*Required*: No
*Type*: Number
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Min`  <a name="cfn-autoscaling-autoscalinggroup-memorygibpervcpurequest-min"></a>
The memory minimum in GiB.
*Required*: No
*Type*: Number
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)
