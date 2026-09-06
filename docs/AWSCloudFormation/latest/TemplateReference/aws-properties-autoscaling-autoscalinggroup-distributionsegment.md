---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-autoscalinggroup-distributionsegment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::AutoScalingGroup DistributionSegment
<a name="aws-properties-autoscaling-autoscalinggroup-distributionsegment"></a>

Use this structure to specify the capacity types that Amazon EC2 Auto Scaling prioritizes when it launches instances.

## Syntax
<a name="aws-properties-autoscaling-autoscalinggroup-distributionsegment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-autoscalinggroup-distributionsegment-syntax.json"></a>

```
{
  "[TargetCapacityTypes](#cfn-autoscaling-autoscalinggroup-distributionsegment-targetcapacitytypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-autoscaling-autoscalinggroup-distributionsegment-syntax.yaml"></a>

```
  [TargetCapacityTypes](#cfn-autoscaling-autoscalinggroup-distributionsegment-targetcapacitytypes): {{
    - String}}
```

## Properties
<a name="aws-properties-autoscaling-autoscalinggroup-distributionsegment-properties"></a>

`TargetCapacityTypes`  <a name="cfn-autoscaling-autoscalinggroup-distributionsegment-targetcapacitytypes"></a>
The capacity types to prioritize, in order. Amazon EC2 Auto Scaling attempts to launch instances in the priority order of the capacity types, and within each capacity type, in the order of instance types listed in your launch template `Overrides`.
The following lists the valid values:
on-demand-capacity-reservation
On-Demand Capacity Reservations.
capacity-block
Capacity Blocks.
interruptible-capacity-reservation
Interruptible Capacity Reservations.
on-demand
On-Demand capacity. Include this value to allow the group to fall back to On-Demand capacity when the preceding capacity types are unavailable.
*Required*: Yes
*Type*: Array of String
*Allowed values*: `on-demand-capacity-reservation | capacity-block | interruptible-capacity-reservation | on-demand`
*Minimum*: `1`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)
