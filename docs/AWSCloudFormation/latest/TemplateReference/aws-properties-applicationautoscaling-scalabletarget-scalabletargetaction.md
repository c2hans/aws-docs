---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationAutoScaling::ScalableTarget ScalableTargetAction
<a name="aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction"></a>

`ScalableTargetAction` specifies the minimum and maximum capacity for the `ScalableTargetAction` property of the [AWS::ApplicationAutoScaling::ScalableTarget ScheduledAction](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalabletarget-scheduledaction.html) property type.

## Syntax
<a name="aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction-syntax.json"></a>

```
{
  "[MaxCapacity](#cfn-applicationautoscaling-scalabletarget-scalabletargetaction-maxcapacity)" : {{Integer}},
  "[MinCapacity](#cfn-applicationautoscaling-scalabletarget-scalabletargetaction-mincapacity)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction-syntax.yaml"></a>

```
  [MaxCapacity](#cfn-applicationautoscaling-scalabletarget-scalabletargetaction-maxcapacity): {{Integer}}
  [MinCapacity](#cfn-applicationautoscaling-scalabletarget-scalabletargetaction-mincapacity): {{Integer}}
```

## Properties
<a name="aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction-properties"></a>

`MaxCapacity`  <a name="cfn-applicationautoscaling-scalabletarget-scalabletargetaction-maxcapacity"></a>
The maximum capacity.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinCapacity`  <a name="cfn-applicationautoscaling-scalabletarget-scalabletargetaction-mincapacity"></a>
The minimum capacity.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-applicationautoscaling-scalabletarget-scalabletargetaction--seealso"></a>
+  [Configure Application Auto Scaling resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-application-auto-scaling.html)
+ [Getting started](https://docs.aws.amazon.com/autoscaling/application/userguide/getting-started.html) in the *Application Auto Scaling User Guide*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
