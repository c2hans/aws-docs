---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-scalingpolicy-targettrackingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::ScalingPolicy TargetTrackingConfiguration
<a name="aws-properties-autoscaling-scalingpolicy-targettrackingconfiguration"></a>

`TargetTrackingConfiguration` is a property of the [AWS::AutoScaling::ScalingPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-scalingpolicy.html) resource that specifies a target tracking scaling policy configuration for Amazon EC2 Auto Scaling.

For more information about scaling policies, see [Dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Syntax
<a name="aws-properties-autoscaling-scalingpolicy-targettrackingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-scalingpolicy-targettrackingconfiguration-syntax.json"></a>

```
{
  "[CustomizedMetricSpecification](#cfn-autoscaling-scalingpolicy-targettrackingconfiguration-customizedmetricspecification)" : {{CustomizedMetricSpecification}},
  "[DisableScaleIn](#cfn-autoscaling-scalingpolicy-targettrackingconfiguration-disablescalein)" : {{Boolean}},
  "[PredefinedMetricSpecification](#cfn-autoscaling-scalingpolicy-targettrackingconfiguration-predefinedmetricspecification)" : {{PredefinedMetricSpecification}},
  "[TargetValue](#cfn-autoscaling-scalingpolicy-targettrackingconfiguration-targetvalue)" : {{Number}}
}
```

### YAML
<a name="aws-properties-autoscaling-scalingpolicy-targettrackingconfiguration-syntax.yaml"></a>

```
  [CustomizedMetricSpecification](#cfn-autoscaling-scalingpolicy-targettrackingconfiguration-customizedmetricspecification): {{
    CustomizedMetricSpecification}}
  [DisableScaleIn](#cfn-autoscaling-scalingpolicy-targettrackingconfiguration-disablescalein): {{Boolean}}
  [PredefinedMetricSpecification](#cfn-autoscaling-scalingpolicy-targettrackingconfiguration-predefinedmetricspecification): {{
    PredefinedMetricSpecification}}
  [TargetValue](#cfn-autoscaling-scalingpolicy-targettrackingconfiguration-targetvalue): {{Number}}
```

## Properties
<a name="aws-properties-autoscaling-scalingpolicy-targettrackingconfiguration-properties"></a>

`CustomizedMetricSpecification`  <a name="cfn-autoscaling-scalingpolicy-targettrackingconfiguration-customizedmetricspecification"></a>
A customized metric. You must specify either a predefined metric or a customized metric.
*Required*: Conditional
*Type*: [CustomizedMetricSpecification](aws-properties-autoscaling-scalingpolicy-customizedmetricspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisableScaleIn`  <a name="cfn-autoscaling-scalingpolicy-targettrackingconfiguration-disablescalein"></a>
Indicates whether scaling in by the target tracking scaling policy is disabled. If scaling in is disabled, the target tracking scaling policy doesn't remove instances from the Auto Scaling group. Otherwise, the target tracking scaling policy can remove instances from the Auto Scaling group. The default is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PredefinedMetricSpecification`  <a name="cfn-autoscaling-scalingpolicy-targettrackingconfiguration-predefinedmetricspecification"></a>
A predefined metric. You must specify either a predefined metric or a customized metric.
*Required*: Conditional
*Type*: [PredefinedMetricSpecification](aws-properties-autoscaling-scalingpolicy-predefinedmetricspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetValue`  <a name="cfn-autoscaling-scalingpolicy-targettrackingconfiguration-targetvalue"></a>
The target value for the metric.
Some metrics are based on a count instead of a percentage, such as the request count for an Application Load Balancer or the number of messages in an SQS queue. If the scaling policy specifies one of these metrics, specify the target utilization as the optimal average request or message count per instance during any one-minute interval.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
