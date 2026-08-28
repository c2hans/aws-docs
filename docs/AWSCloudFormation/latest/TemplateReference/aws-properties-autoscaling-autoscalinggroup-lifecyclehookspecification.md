---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::AutoScalingGroup LifecycleHookSpecification
<a name="aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification"></a>

`LifecycleHookSpecification` specifies a lifecycle hook for the `LifecycleHookSpecificationList` property of the [AWS::AutoScaling::AutoScalingGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html) resource. A lifecycle hook specifies actions to perform when Amazon EC2 Auto Scaling launches or terminates instances.

For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html) in the *Amazon EC2 Auto Scaling User Guide*. You can find a sample template snippet in the [Examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-lifecyclehook.html#aws-resource-as-lifecyclehook--examples) section of the `AWS::AutoScaling::LifecycleHook` resource.

## Syntax
<a name="aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification-syntax.json"></a>

```
{
  "[DefaultResult](#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-defaultresult)" : {{String}},
  "[HeartbeatTimeout](#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-heartbeattimeout)" : {{Integer}},
  "[LifecycleHookName](#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-lifecyclehookname)" : {{String}},
  "[LifecycleTransition](#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-lifecycletransition)" : {{String}},
  "[NotificationMetadata](#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-notificationmetadata)" : {{String}},
  "[NotificationTargetARN](#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-notificationtargetarn)" : {{String}},
  "[RoleARN](#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification-syntax.yaml"></a>

```
  [DefaultResult](#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-defaultresult): {{String}}
  [HeartbeatTimeout](#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-heartbeattimeout): {{Integer}}
  [LifecycleHookName](#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-lifecyclehookname): {{String}}
  [LifecycleTransition](#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-lifecycletransition): {{String}}
  [NotificationMetadata](#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-notificationmetadata): {{String}}
  [NotificationTargetARN](#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-notificationtargetarn): {{String}}
  [RoleARN](#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-rolearn): {{String}}
```

## Properties
<a name="aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification-properties"></a>

`DefaultResult`  <a name="cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-defaultresult"></a>
The action the Auto Scaling group takes when the lifecycle hook timeout elapses or if an unexpected failure occurs. The default value is `ABANDON`.
Valid values: `CONTINUE` \| `ABANDON`
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HeartbeatTimeout`  <a name="cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-heartbeattimeout"></a>
The maximum time, in seconds, that can elapse before the lifecycle hook times out. The range is from `30` to `7200` seconds. The default value is `3600` seconds (1 hour).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LifecycleHookName`  <a name="cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-lifecyclehookname"></a>
The name of the lifecycle hook.
*Required*: Yes
*Type*: String
*Pattern*: `[A-Za-z0-9\-_\/]+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LifecycleTransition`  <a name="cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-lifecycletransition"></a>
The lifecycle transition. For Auto Scaling groups, there are two major lifecycle transitions.
+ To create a lifecycle hook for scale-out events, specify `autoscaling:EC2_INSTANCE_LAUNCHING`.
+ To create a lifecycle hook for scale-in events, specify `autoscaling:EC2_INSTANCE_TERMINATING`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotificationMetadata`  <a name="cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-notificationmetadata"></a>
Additional information that you want to include any time Amazon EC2 Auto Scaling sends a message to the notification target.
*Required*: No
*Type*: String
*Pattern*: `[\u0009\u000A\u000D\u0020-\u007e]+`
*Minimum*: `1`
*Maximum*: `4000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotificationTargetARN`  <a name="cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-notificationtargetarn"></a>
The Amazon Resource Name (ARN) of the notification target that Amazon EC2 Auto Scaling sends notifications to when an instance is in a wait state for the lifecycle hook. You can specify an Amazon SNS topic or an Amazon SQS queue.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleARN`  <a name="cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-rolearn"></a>
The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target. For information about creating this role, see [Prepare to add a lifecycle hook to your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/prepare-for-lifecycle-notifications.html) in the *Amazon EC2 Auto Scaling User Guide*.
Valid only if the notification target is an Amazon SNS topic or an Amazon SQS queue.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
