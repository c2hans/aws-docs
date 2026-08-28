---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-autoscalinggroup-instancelifecyclepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::AutoScalingGroup InstanceLifecyclePolicy
<a name="aws-properties-autoscaling-autoscalinggroup-instancelifecyclepolicy"></a>

 The instance lifecycle policy for the Auto Scaling group. This policy controls instance behavior when an instance transitions through its lifecycle states. Configure retention triggers to specify when instances should move to a `Retained` state instead of automatic termination.

For more information, see [ Control instance retention with instance lifecycle policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/instance-lifecycle-policy.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Syntax
<a name="aws-properties-autoscaling-autoscalinggroup-instancelifecyclepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-autoscalinggroup-instancelifecyclepolicy-syntax.json"></a>

```
{
  "[RetentionTriggers](#cfn-autoscaling-autoscalinggroup-instancelifecyclepolicy-retentiontriggers)" : {{RetentionTriggers}}
}
```

### YAML
<a name="aws-properties-autoscaling-autoscalinggroup-instancelifecyclepolicy-syntax.yaml"></a>

```
  [RetentionTriggers](#cfn-autoscaling-autoscalinggroup-instancelifecyclepolicy-retentiontriggers): {{
    RetentionTriggers}}
```

## Properties
<a name="aws-properties-autoscaling-autoscalinggroup-instancelifecyclepolicy-properties"></a>

`RetentionTriggers`  <a name="cfn-autoscaling-autoscalinggroup-instancelifecyclepolicy-retentiontriggers"></a>
 Specifies the conditions that trigger instance retention behavior. These triggers determine when instances should move to a `Retained` state instead of automatic termination. This allows you to maintain control over instance management when lifecycles transition and operations fail.
*Required*: No
*Type*: [RetentionTriggers](aws-properties-autoscaling-autoscalinggroup-retentiontriggers.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
