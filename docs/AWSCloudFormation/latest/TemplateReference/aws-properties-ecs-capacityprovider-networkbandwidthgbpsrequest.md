---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-networkbandwidthgbpsrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::CapacityProvider NetworkBandwidthGbpsRequest
<a name="aws-properties-ecs-capacityprovider-networkbandwidthgbpsrequest"></a>

The minimum and maximum network bandwidth in gigabits per second (Gbps) for instance type selection. This is important for network-intensive workloads.

## Syntax
<a name="aws-properties-ecs-capacityprovider-networkbandwidthgbpsrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-capacityprovider-networkbandwidthgbpsrequest-syntax.json"></a>

```
{
  "[Max](#cfn-ecs-capacityprovider-networkbandwidthgbpsrequest-max)" : {{Number}},
  "[Min](#cfn-ecs-capacityprovider-networkbandwidthgbpsrequest-min)" : {{Number}}
}
```

### YAML
<a name="aws-properties-ecs-capacityprovider-networkbandwidthgbpsrequest-syntax.yaml"></a>

```
  [Max](#cfn-ecs-capacityprovider-networkbandwidthgbpsrequest-max): {{Number}}
  [Min](#cfn-ecs-capacityprovider-networkbandwidthgbpsrequest-min): {{Number}}
```

## Properties
<a name="aws-properties-ecs-capacityprovider-networkbandwidthgbpsrequest-properties"></a>

`Max`  <a name="cfn-ecs-capacityprovider-networkbandwidthgbpsrequest-max"></a>
The maximum network bandwidth in Gbps. Instance types with higher network bandwidth are excluded from selection.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-ecs-capacityprovider-networkbandwidthgbpsrequest-min"></a>
The minimum network bandwidth in Gbps. Instance types with lower network bandwidth are excluded from selection.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
