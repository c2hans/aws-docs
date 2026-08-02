---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-autoscalingpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster AutoScalingPolicy
<a name="aws-properties-emr-cluster-autoscalingpolicy"></a>

`AutoScalingPolicy` is a subproperty of `InstanceGroupConfig`. `AutoScalingPolicy` defines how an instance group dynamically adds and terminates EC2 instances in response to the value of a CloudWatch metric. For more information, see [Using Automatic Scaling in Amazon EMR](https://docs.aws.amazon.com//emr/latest/ManagementGuide/emr-automatic-scaling.html) in the *Amazon EMR Management Guide*.

## Syntax
<a name="aws-properties-emr-cluster-autoscalingpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-autoscalingpolicy-syntax.json"></a>

```
{
  "[Constraints](#cfn-emr-cluster-autoscalingpolicy-constraints)" : {{ScalingConstraints}},
  "[Rules](#cfn-emr-cluster-autoscalingpolicy-rules)" : {{[ ScalingRule, ... ]}}
}
```

### YAML
<a name="aws-properties-emr-cluster-autoscalingpolicy-syntax.yaml"></a>

```
  [Constraints](#cfn-emr-cluster-autoscalingpolicy-constraints): {{
    ScalingConstraints}}
  [Rules](#cfn-emr-cluster-autoscalingpolicy-rules): {{
    - ScalingRule}}
```

## Properties
<a name="aws-properties-emr-cluster-autoscalingpolicy-properties"></a>

`Constraints`  <a name="cfn-emr-cluster-autoscalingpolicy-constraints"></a>
The upper and lower Amazon EC2 instance limits for an automatic scaling policy. Automatic scaling activity will not cause an instance group to grow above or below these limits.
*Required*: Yes
*Type*: [ScalingConstraints](aws-properties-emr-cluster-scalingconstraints.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rules`  <a name="cfn-emr-cluster-autoscalingpolicy-rules"></a>
The scale-in and scale-out rules that comprise the automatic scaling policy.
*Required*: Yes
*Type*: Array of [ScalingRule](aws-properties-emr-cluster-scalingrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
