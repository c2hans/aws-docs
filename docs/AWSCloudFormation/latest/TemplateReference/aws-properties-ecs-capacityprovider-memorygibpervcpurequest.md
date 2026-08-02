---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-memorygibpervcpurequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::CapacityProvider MemoryGiBPerVCpuRequest
<a name="aws-properties-ecs-capacityprovider-memorygibpervcpurequest"></a>

The minimum and maximum amount of memory per vCPU in gibibytes (GiB). This helps ensure that instance types have the appropriate memory-to-CPU ratio for your workloads.

## Syntax
<a name="aws-properties-ecs-capacityprovider-memorygibpervcpurequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-capacityprovider-memorygibpervcpurequest-syntax.json"></a>

```
{
  "[Max](#cfn-ecs-capacityprovider-memorygibpervcpurequest-max)" : {{Number}},
  "[Min](#cfn-ecs-capacityprovider-memorygibpervcpurequest-min)" : {{Number}}
}
```

### YAML
<a name="aws-properties-ecs-capacityprovider-memorygibpervcpurequest-syntax.yaml"></a>

```
  [Max](#cfn-ecs-capacityprovider-memorygibpervcpurequest-max): {{Number}}
  [Min](#cfn-ecs-capacityprovider-memorygibpervcpurequest-min): {{Number}}
```

## Properties
<a name="aws-properties-ecs-capacityprovider-memorygibpervcpurequest-properties"></a>

`Max`  <a name="cfn-ecs-capacityprovider-memorygibpervcpurequest-max"></a>
The maximum amount of memory per vCPU in GiB. Instance types with a higher memory-to-vCPU ratio are excluded from selection.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-ecs-capacityprovider-memorygibpervcpurequest-min"></a>
The minimum amount of memory per vCPU in GiB. Instance types with a lower memory-to-vCPU ratio are excluded from selection.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
