---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-autoscalinggroup-instancemaintenancepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::AutoScalingGroup InstanceMaintenancePolicy
<a name="aws-properties-autoscaling-autoscalinggroup-instancemaintenancepolicy"></a>

`InstanceMaintenancePolicy` is a property of the [AWS::AutoScaling::AutoScalingGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html) resource.

For more information, see [Instance maintenance policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-maintenance-policy.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Syntax
<a name="aws-properties-autoscaling-autoscalinggroup-instancemaintenancepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-autoscalinggroup-instancemaintenancepolicy-syntax.json"></a>

```
{
  "[MaxHealthyPercentage](#cfn-autoscaling-autoscalinggroup-instancemaintenancepolicy-maxhealthypercentage)" : {{Integer}},
  "[MinHealthyPercentage](#cfn-autoscaling-autoscalinggroup-instancemaintenancepolicy-minhealthypercentage)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-autoscaling-autoscalinggroup-instancemaintenancepolicy-syntax.yaml"></a>

```
  [MaxHealthyPercentage](#cfn-autoscaling-autoscalinggroup-instancemaintenancepolicy-maxhealthypercentage): {{Integer}}
  [MinHealthyPercentage](#cfn-autoscaling-autoscalinggroup-instancemaintenancepolicy-minhealthypercentage): {{Integer}}
```

## Properties
<a name="aws-properties-autoscaling-autoscalinggroup-instancemaintenancepolicy-properties"></a>

`MaxHealthyPercentage`  <a name="cfn-autoscaling-autoscalinggroup-instancemaintenancepolicy-maxhealthypercentage"></a>
Specifies the upper threshold as a percentage of the desired capacity of the Auto Scaling group. It represents the maximum percentage of the group that can be in service and healthy, or pending, to support your workload when replacing instances. Value range is 100 to 200. To clear a previously set value, specify a value of `-1`.
Both `MinHealthyPercentage` and `MaxHealthyPercentage` must be specified, and the difference between them cannot be greater than 100. A large range increases the number of instances that can be replaced at the same time.
*Required*: No
*Type*: Integer
*Minimum*: `-1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinHealthyPercentage`  <a name="cfn-autoscaling-autoscalinggroup-instancemaintenancepolicy-minhealthypercentage"></a>
Specifies the lower threshold as a percentage of the desired capacity of the Auto Scaling group. It represents the minimum percentage of the group to keep in service, healthy, and ready to use to support your workload when replacing instances. Value range is 0 to 100. To clear a previously set value, specify a value of `-1`.
*Required*: No
*Type*: Integer
*Minimum*: `-1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
