---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-autoscalinggroupprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::CapacityProvider AutoScalingGroupProvider
<a name="aws-properties-ecs-capacityprovider-autoscalinggroupprovider"></a>

The details of the Auto Scaling group for the capacity provider.

## Syntax
<a name="aws-properties-ecs-capacityprovider-autoscalinggroupprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-capacityprovider-autoscalinggroupprovider-syntax.json"></a>

```
{
  "[AutoScalingGroupArn](#cfn-ecs-capacityprovider-autoscalinggroupprovider-autoscalinggrouparn)" : {{String}},
  "[ManagedDraining](#cfn-ecs-capacityprovider-autoscalinggroupprovider-manageddraining)" : {{String}},
  "[ManagedScaling](#cfn-ecs-capacityprovider-autoscalinggroupprovider-managedscaling)" : {{ManagedScaling}},
  "[ManagedTerminationProtection](#cfn-ecs-capacityprovider-autoscalinggroupprovider-managedterminationprotection)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-capacityprovider-autoscalinggroupprovider-syntax.yaml"></a>

```
  [AutoScalingGroupArn](#cfn-ecs-capacityprovider-autoscalinggroupprovider-autoscalinggrouparn): {{String}}
  [ManagedDraining](#cfn-ecs-capacityprovider-autoscalinggroupprovider-manageddraining): {{String}}
  [ManagedScaling](#cfn-ecs-capacityprovider-autoscalinggroupprovider-managedscaling): {{
    ManagedScaling}}
  [ManagedTerminationProtection](#cfn-ecs-capacityprovider-autoscalinggroupprovider-managedterminationprotection): {{String}}
```

## Properties
<a name="aws-properties-ecs-capacityprovider-autoscalinggroupprovider-properties"></a>

`AutoScalingGroupArn`  <a name="cfn-ecs-capacityprovider-autoscalinggroupprovider-autoscalinggrouparn"></a>
The Amazon Resource Name (ARN) that identifies the Auto Scaling group, or the Auto Scaling group name.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ManagedDraining`  <a name="cfn-ecs-capacityprovider-autoscalinggroupprovider-manageddraining"></a>
The managed draining option for the Auto Scaling group capacity provider. When you enable this, Amazon ECS manages and gracefully drains the EC2 container instances that are in the Auto Scaling group capacity provider.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | ENABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManagedScaling`  <a name="cfn-ecs-capacityprovider-autoscalinggroupprovider-managedscaling"></a>
The managed scaling settings for the Auto Scaling group capacity provider.
*Required*: No
*Type*: [ManagedScaling](aws-properties-ecs-capacityprovider-managedscaling.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManagedTerminationProtection`  <a name="cfn-ecs-capacityprovider-autoscalinggroupprovider-managedterminationprotection"></a>
The managed termination protection setting to use for the Auto Scaling group capacity provider. This determines whether the Auto Scaling group has managed termination protection. The default is off.
When using managed termination protection, managed scaling must also be used otherwise managed termination protection doesn't work.
When managed termination protection is on, Amazon ECS prevents the Amazon EC2 instances in an Auto Scaling group that contain tasks from being terminated during a scale-in action. The Auto Scaling group and each instance in the Auto Scaling group must have instance protection from scale-in actions on as well. For more information, see [Instance Protection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html#instance-protection) in the *AWS Auto Scaling User Guide*.
When managed termination protection is off, your Amazon EC2 instances aren't protected from termination when the Auto Scaling group scales in.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | ENABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ecs-capacityprovider-autoscalinggroupprovider--seealso"></a>
+  [ Defining an Amazon ECS capacity provider](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-capacityprovider.html#aws-resource-ecs-capacityprovider--examples)
