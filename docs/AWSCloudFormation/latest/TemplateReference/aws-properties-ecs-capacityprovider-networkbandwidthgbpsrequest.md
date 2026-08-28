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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
