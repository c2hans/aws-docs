---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-acceleratorcountrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::CapacityProvider AcceleratorCountRequest
<a name="aws-properties-ecs-capacityprovider-acceleratorcountrequest"></a>

The minimum and maximum number of accelerators (such as GPUs) for instance type selection. This is used for workloads that require specific numbers of accelerators.

## Syntax
<a name="aws-properties-ecs-capacityprovider-acceleratorcountrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-capacityprovider-acceleratorcountrequest-syntax.json"></a>

```
{
  "[Max](#cfn-ecs-capacityprovider-acceleratorcountrequest-max)" : {{Integer}},
  "[Min](#cfn-ecs-capacityprovider-acceleratorcountrequest-min)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-capacityprovider-acceleratorcountrequest-syntax.yaml"></a>

```
  [Max](#cfn-ecs-capacityprovider-acceleratorcountrequest-max): {{Integer}}
  [Min](#cfn-ecs-capacityprovider-acceleratorcountrequest-min): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-capacityprovider-acceleratorcountrequest-properties"></a>

`Max`  <a name="cfn-ecs-capacityprovider-acceleratorcountrequest-max"></a>
The maximum number of accelerators. Instance types with more accelerators are excluded from selection.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-ecs-capacityprovider-acceleratorcountrequest-min"></a>
The minimum number of accelerators. Instance types with fewer accelerators are excluded from selection.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
