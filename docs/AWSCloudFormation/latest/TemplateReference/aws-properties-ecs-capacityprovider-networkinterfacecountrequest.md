---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-networkinterfacecountrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::CapacityProvider NetworkInterfaceCountRequest
<a name="aws-properties-ecs-capacityprovider-networkinterfacecountrequest"></a>

The minimum and maximum number of network interfaces for instance type selection. This is useful for workloads that require multiple network interfaces.

## Syntax
<a name="aws-properties-ecs-capacityprovider-networkinterfacecountrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-capacityprovider-networkinterfacecountrequest-syntax.json"></a>

```
{
  "[Max](#cfn-ecs-capacityprovider-networkinterfacecountrequest-max)" : {{Integer}},
  "[Min](#cfn-ecs-capacityprovider-networkinterfacecountrequest-min)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-capacityprovider-networkinterfacecountrequest-syntax.yaml"></a>

```
  [Max](#cfn-ecs-capacityprovider-networkinterfacecountrequest-max): {{Integer}}
  [Min](#cfn-ecs-capacityprovider-networkinterfacecountrequest-min): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-capacityprovider-networkinterfacecountrequest-properties"></a>

`Max`  <a name="cfn-ecs-capacityprovider-networkinterfacecountrequest-max"></a>
The maximum number of network interfaces. Instance types that support more network interfaces are excluded from selection.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-ecs-capacityprovider-networkinterfacecountrequest-min"></a>
The minimum number of network interfaces. Instance types that support fewer network interfaces are excluded from selection.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
