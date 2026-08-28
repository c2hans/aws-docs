---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancegroupconfig-autoscalingpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceGroupConfig AutoScalingPolicy
<a name="aws-properties-emr-instancegroupconfig-autoscalingpolicy"></a>

`AutoScalingPolicy` defines how an instance group dynamically adds and terminates EC2 instances in response to the value of a CloudWatch metric. For more information, see [Using Automatic Scaling in Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html) in the *Amazon EMR Management Guide*.

## Syntax
<a name="aws-properties-emr-instancegroupconfig-autoscalingpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancegroupconfig-autoscalingpolicy-syntax.json"></a>

```
{
  "[Constraints](#cfn-emr-instancegroupconfig-autoscalingpolicy-constraints)" : {{ScalingConstraints}},
  "[Rules](#cfn-emr-instancegroupconfig-autoscalingpolicy-rules)" : {{[ ScalingRule, ... ]}}
}
```

### YAML
<a name="aws-properties-emr-instancegroupconfig-autoscalingpolicy-syntax.yaml"></a>

```
  [Constraints](#cfn-emr-instancegroupconfig-autoscalingpolicy-constraints): {{
    ScalingConstraints}}
  [Rules](#cfn-emr-instancegroupconfig-autoscalingpolicy-rules): {{
    - ScalingRule}}
```

## Properties
<a name="aws-properties-emr-instancegroupconfig-autoscalingpolicy-properties"></a>

`Constraints`  <a name="cfn-emr-instancegroupconfig-autoscalingpolicy-constraints"></a>
The upper and lower Amazon EC2 instance limits for an automatic scaling policy. Automatic scaling activity will not cause an instance group to grow above or below these limits.
*Required*: Yes
*Type*: [ScalingConstraints](aws-properties-emr-instancegroupconfig-scalingconstraints.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rules`  <a name="cfn-emr-instancegroupconfig-autoscalingpolicy-rules"></a>
The scale-in and scale-out rules that comprise the automatic scaling policy.
*Required*: Yes
*Type*: Array of [ScalingRule](aws-properties-emr-instancegroupconfig-scalingrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
