---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-autoscalinggroup-retentiontriggers.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::AutoScalingGroup RetentionTriggers
<a name="aws-properties-autoscaling-autoscalinggroup-retentiontriggers"></a>

 Defines the specific triggers that cause instances to be retained in a Retained state rather than terminated. Each trigger corresponds to a different failure scenario during the instance lifecycle. This allows fine-grained control over when to preserve instances for manual intervention.

## Syntax
<a name="aws-properties-autoscaling-autoscalinggroup-retentiontriggers-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-autoscalinggroup-retentiontriggers-syntax.json"></a>

```
{
  "[TerminateHookAbandon](#cfn-autoscaling-autoscalinggroup-retentiontriggers-terminatehookabandon)" : {{String}}
}
```

### YAML
<a name="aws-properties-autoscaling-autoscalinggroup-retentiontriggers-syntax.yaml"></a>

```
  [TerminateHookAbandon](#cfn-autoscaling-autoscalinggroup-retentiontriggers-terminatehookabandon): {{String}}
```

## Properties
<a name="aws-properties-autoscaling-autoscalinggroup-retentiontriggers-properties"></a>

`TerminateHookAbandon`  <a name="cfn-autoscaling-autoscalinggroup-retentiontriggers-terminatehookabandon"></a>
 Specifies the action when a termination lifecycle hook is abandoned due to failure, timeout, or explicit abandonment (calling CompleteLifecycleAction).
 Set to `retain` to move instances to a retained state. Set to `terminate` for default termination behavior.
 Retained instances don't count toward desired capacity and remain until you call `TerminateInstanceInAutoScalingGroup`.
*Required*: No
*Type*: String
*Allowed values*: `retain | terminate`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
