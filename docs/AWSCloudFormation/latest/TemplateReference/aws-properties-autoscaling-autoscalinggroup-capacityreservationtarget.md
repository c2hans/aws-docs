---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-autoscalinggroup-capacityreservationtarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::AutoScalingGroup CapacityReservationTarget
<a name="aws-properties-autoscaling-autoscalinggroup-capacityreservationtarget"></a>

 The target for the Capacity Reservation. Specify Capacity Reservations IDs or Capacity Reservation resource group ARNs.

## Syntax
<a name="aws-properties-autoscaling-autoscalinggroup-capacityreservationtarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-autoscalinggroup-capacityreservationtarget-syntax.json"></a>

```
{
  "[CapacityReservationIds](#cfn-autoscaling-autoscalinggroup-capacityreservationtarget-capacityreservationids)" : {{[ String, ... ]}},
  "[CapacityReservationResourceGroupArns](#cfn-autoscaling-autoscalinggroup-capacityreservationtarget-capacityreservationresourcegrouparns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-autoscaling-autoscalinggroup-capacityreservationtarget-syntax.yaml"></a>

```
  [CapacityReservationIds](#cfn-autoscaling-autoscalinggroup-capacityreservationtarget-capacityreservationids): {{
    - String}}
  [CapacityReservationResourceGroupArns](#cfn-autoscaling-autoscalinggroup-capacityreservationtarget-capacityreservationresourcegrouparns): {{
    - String}}
```

## Properties
<a name="aws-properties-autoscaling-autoscalinggroup-capacityreservationtarget-properties"></a>

`CapacityReservationIds`  <a name="cfn-autoscaling-autoscalinggroup-capacityreservationtarget-capacityreservationids"></a>
 The Capacity Reservation IDs to launch instances into.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CapacityReservationResourceGroupArns`  <a name="cfn-autoscaling-autoscalinggroup-capacityreservationtarget-capacityreservationresourcegrouparns"></a>
 The resource group ARNs of the Capacity Reservation to launch instances into.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
