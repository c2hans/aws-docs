---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-acceleratortotalmemorymibrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::CapacityProvider AcceleratorTotalMemoryMiBRequest
<a name="aws-properties-ecs-capacityprovider-acceleratortotalmemorymibrequest"></a>

The minimum and maximum total accelerator memory in mebibytes (MiB) for instance type selection. This is important for GPU workloads that require specific amounts of video memory.

## Syntax
<a name="aws-properties-ecs-capacityprovider-acceleratortotalmemorymibrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-capacityprovider-acceleratortotalmemorymibrequest-syntax.json"></a>

```
{
  "[Max](#cfn-ecs-capacityprovider-acceleratortotalmemorymibrequest-max)" : {{Integer}},
  "[Min](#cfn-ecs-capacityprovider-acceleratortotalmemorymibrequest-min)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-capacityprovider-acceleratortotalmemorymibrequest-syntax.yaml"></a>

```
  [Max](#cfn-ecs-capacityprovider-acceleratortotalmemorymibrequest-max): {{Integer}}
  [Min](#cfn-ecs-capacityprovider-acceleratortotalmemorymibrequest-min): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-capacityprovider-acceleratortotalmemorymibrequest-properties"></a>

`Max`  <a name="cfn-ecs-capacityprovider-acceleratortotalmemorymibrequest-max"></a>
The maximum total accelerator memory in MiB. Instance types with more accelerator memory are excluded from selection.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-ecs-capacityprovider-acceleratortotalmemorymibrequest-min"></a>
The minimum total accelerator memory in MiB. Instance types with less accelerator memory are excluded from selection.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
