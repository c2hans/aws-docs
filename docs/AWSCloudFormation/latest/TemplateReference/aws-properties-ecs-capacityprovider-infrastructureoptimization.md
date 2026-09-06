---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-infrastructureoptimization.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::CapacityProvider InfrastructureOptimization
<a name="aws-properties-ecs-capacityprovider-infrastructureoptimization"></a>

The configuration that controls how Amazon ECS optimizes your infrastructure.

## Syntax
<a name="aws-properties-ecs-capacityprovider-infrastructureoptimization-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-capacityprovider-infrastructureoptimization-syntax.json"></a>

```
{
  "[ScaleInAfter](#cfn-ecs-capacityprovider-infrastructureoptimization-scaleinafter)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-capacityprovider-infrastructureoptimization-syntax.yaml"></a>

```
  [ScaleInAfter](#cfn-ecs-capacityprovider-infrastructureoptimization-scaleinafter): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-capacityprovider-infrastructureoptimization-properties"></a>

`ScaleInAfter`  <a name="cfn-ecs-capacityprovider-infrastructureoptimization-scaleinafter"></a>
This parameter defines the number of seconds Amazon ECS Managed Instances waits before optimizing EC2 instances that have become idle or underutilized. A longer delay increases the likelihood of placing new tasks on idle or underutilized instances instances, reducing startup time. A shorter delay helps reduce infrastructure costs by optimizing idle or underutilized instances,instances more quickly.
Valid values are:
+ `null` - Uses the default optimization behavior.
+ `-1` - Disables automatic infrastructure optimization.
+ A value between `0` and `3600` (inclusive) - Specifies the number of seconds to wait before optimizing instances.
*Required*: No
*Type*: Integer
*Minimum*: `-1`
*Maximum*: `3600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
