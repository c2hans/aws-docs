---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancegroupconfig-simplescalingpolicyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceGroupConfig SimpleScalingPolicyConfiguration
<a name="aws-properties-emr-instancegroupconfig-simplescalingpolicyconfiguration"></a>

`SimpleScalingPolicyConfiguration` is a subproperty of the `ScalingAction` property type. `SimpleScalingPolicyConfiguration` determines how an automatic scaling action adds or removes instances, the cooldown period, and the number of EC2 instances that are added each time the CloudWatch metric alarm condition is satisfied.

## Syntax
<a name="aws-properties-emr-instancegroupconfig-simplescalingpolicyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancegroupconfig-simplescalingpolicyconfiguration-syntax.json"></a>

```
{
  "[AdjustmentType](#cfn-emr-instancegroupconfig-simplescalingpolicyconfiguration-adjustmenttype)" : {{String}},
  "[CoolDown](#cfn-emr-instancegroupconfig-simplescalingpolicyconfiguration-cooldown)" : {{Integer}},
  "[ScalingAdjustment](#cfn-emr-instancegroupconfig-simplescalingpolicyconfiguration-scalingadjustment)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-emr-instancegroupconfig-simplescalingpolicyconfiguration-syntax.yaml"></a>

```
  [AdjustmentType](#cfn-emr-instancegroupconfig-simplescalingpolicyconfiguration-adjustmenttype): {{String}}
  [CoolDown](#cfn-emr-instancegroupconfig-simplescalingpolicyconfiguration-cooldown): {{Integer}}
  [ScalingAdjustment](#cfn-emr-instancegroupconfig-simplescalingpolicyconfiguration-scalingadjustment): {{Integer}}
```

## Properties
<a name="aws-properties-emr-instancegroupconfig-simplescalingpolicyconfiguration-properties"></a>

`AdjustmentType`  <a name="cfn-emr-instancegroupconfig-simplescalingpolicyconfiguration-adjustmenttype"></a>
The way in which Amazon EC2 instances are added (if `ScalingAdjustment` is a positive number) or terminated (if `ScalingAdjustment` is a negative number) each time the scaling activity is triggered. `CHANGE_IN_CAPACITY` is the default. `CHANGE_IN_CAPACITY` indicates that the Amazon EC2 instance count increments or decrements by `ScalingAdjustment`, which should be expressed as an integer. `PERCENT_CHANGE_IN_CAPACITY` indicates the instance count increments or decrements by the percentage specified by `ScalingAdjustment`, which should be expressed as an integer. For example, 20 indicates an increase in 20% increments of cluster capacity. `EXACT_CAPACITY` indicates the scaling activity results in an instance group with the number of Amazon EC2 instances specified by `ScalingAdjustment`, which should be expressed as a positive integer.
*Required*: No
*Type*: String
*Allowed values*: `CHANGE_IN_CAPACITY | PERCENT_CHANGE_IN_CAPACITY | EXACT_CAPACITY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CoolDown`  <a name="cfn-emr-instancegroupconfig-simplescalingpolicyconfiguration-cooldown"></a>
The amount of time, in seconds, after a scaling activity completes before any further trigger-related scaling activities can start. The default value is 0.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScalingAdjustment`  <a name="cfn-emr-instancegroupconfig-simplescalingpolicyconfiguration-scalingadjustment"></a>
The amount by which to scale in or scale out, based on the specified `AdjustmentType`. A positive value adds to the instance group's Amazon EC2 instance count while a negative number removes instances. If `AdjustmentType` is set to `EXACT_CAPACITY`, the number should only be a positive integer. If `AdjustmentType` is set to `PERCENT_CHANGE_IN_CAPACITY`, the value should express the percentage as an integer. For example, -20 indicates a decrease in 20% increments of cluster capacity.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
