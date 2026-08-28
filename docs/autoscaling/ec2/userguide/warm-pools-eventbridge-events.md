---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/warm-pools-eventbridge-events.html
---

# Warm pool example events and patterns
<a name="warm-pools-eventbridge-events"></a>

Amazon EC2 Auto Scaling supports several predefined patterns in Amazon EventBridge. This simplifies how an event pattern is created. You select field values on a form, and EventBridge generates the pattern for you. At this time, Amazon EC2 Auto Scaling doesn't support predefined patterns for any events that are emitted by an Auto Scaling group with a warm pool. You must enter the pattern as a JSON object. This section and the [Create EventBridge rules for warm pool events](warm-pool-events-eventbridge-rules.md) topic show you how to use an event pattern to select events and send them to targets.

To create EventBridge rules that filter for warm pool-related events that Amazon EC2 Auto Scaling sends to EventBridge, include the `Origin` and `Destination` fields from the `detail` section of the event.

The values of `Origin` and `Destination` can be the following:

`EC2` \| `AutoScalingGroup` \| `WarmPool`

**Topics**
+ [Example events](#warm-pool-events)
+ [Example event patterns](#warm-pools-eventbridge-patterns)

## Example events
<a name="warm-pool-events"></a>

When you add lifecycle hooks to your Auto Scaling group, Amazon EC2 Auto Scaling sends events to EventBridge when an instance transitions into a wait state. For more information, see [Use lifecycle hooks with a warm pool in Auto Scaling group](warm-pool-instance-lifecycle.md).

This section includes examples of these events when your Auto Scaling group has a warm pool. Events are emitted on a best-effort basis.

**Note**
For events that Amazon EC2 Auto Scaling sends to EventBridge when scaling is successful, see [Successful scaling events](ec2-auto-scaling-event-reference.md#ec2-auto-scaling-successful-scaling-events). For events when scaling is unsuccessful, see [Unsuccessful scaling events](ec2-auto-scaling-event-reference.md#ec2-auto-scaling-unsuccessful-scaling-events).

**Topics**
+ [Scale-out lifecycle action](#warm-pool-scale-out-events)
+ [Scale-in lifecycle action](#warm-pool-scale-in-events)

### Scale-out lifecycle action
<a name="warm-pool-scale-out-events"></a>

Events that are delivered when an instance transitions into a wait state for scale-out events have `EC2 Instance-launch Lifecycle Action` as the value for `detail-type`. In the `detail` object, the values for the `Origin` and `Destination` attributes show where the instance is coming from and where it's going.

In this example scale-out event, a new instance launches and its state changes to `Warmed:Pending:Wait` because it's added to the warm pool. For more information, see [Lifecycle state transitions for instances in a warm pool](warm-pool-instance-lifecycle.md#lifecycle-state-transitions).

```
{
  "version": "0",
  "id": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
  "detail-type": "EC2 Instance-launch Lifecycle Action",
  "source": "aws.autoscaling",
  "account": "{{123456789012}}",
  "time": "{{2021}}-{{01}}-{{13}}T{{00}}:{{12}}:{{37}}.{{214}}Z",
  "region": "{{us-west-2}}",
  "resources": [
    "{{auto-scaling-group-arn}}"
  ],
  "detail": {
    "LifecycleActionToken": "{{71514b9d}}-{{6a40}}-{{4b26}}-{{8523}}-{{05e7eEXAMPLE}}",
    "AutoScalingGroupName": "{{my-asg}}",
    "LifecycleHookName": "{{my-launch-lifecycle-hook}}",
    "EC2InstanceId": "i-{{1234567890abcdef0}}",
    "LifecycleTransition": "autoscaling:EC2_INSTANCE_LAUNCHING",
    "NotificationMetadata": "{{additional-info}}",
    "Origin": "EC2",
    "Destination": "WarmPool"
  }
}
```

In this example scale-out event, the state of the instance changes to `Pending:Wait` because it's added to the Auto Scaling group from the warm pool. For more information, see [Lifecycle state transitions for instances in a warm pool](warm-pool-instance-lifecycle.md#lifecycle-state-transitions).

```
{
  "version": "0",
  "id": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
  "detail-type": "EC2 Instance-launch Lifecycle Action",
  "source": "aws.autoscaling",
  "account": "{{123456789012}}",
  "time": "{{2021}}-{{01}}-{{19}}T{{00}}:{{35}}:{{52}}.{{359}}Z",
  "region": "{{us-west-2}}",
  "resources": [
    "{{auto-scaling-group-arn}}"
  ],
  "detail": {
    "LifecycleActionToken": "{{19cc4d4a}}-{{e450}}-{{4d1c}}-{{b448}}-{{0de67EXAMPLE}}",
    "AutoScalingGroupName": "{{my-asg}}",
    "LifecycleHookName": "{{my-launch-lifecycle-hook}}",
    "EC2InstanceId": "i-{{1234567890abcdef0}}",
    "LifecycleTransition": "autoscaling:EC2_INSTANCE_LAUNCHING",
    "NotificationMetadata": "{{additional-info}}",
    "Origin": "WarmPool",
    "Destination": "AutoScalingGroup"
  }
}
```

### Scale-in lifecycle action
<a name="warm-pool-scale-in-events"></a>

Events that are delivered when an instance transitions into a wait state for scale-in events have `EC2 Instance-terminate Lifecycle Action` as the value for `detail-type`. In the `detail` object, the values for the `Origin` and `Destination` attributes show where the instance is coming from and where it's going.

In this example scale-in event, the state of an instance changes to `Warmed:Pending:Wait` because it's returned to the warm pool. For more information, see [Lifecycle state transitions for instances in a warm pool](warm-pool-instance-lifecycle.md#lifecycle-state-transitions).

```
{
  "version": "0",
  "id": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
  "detail-type": "EC2 Instance-terminate Lifecycle Action",
  "source": "aws.autoscaling",
  "account": "{{123456789012}}",
  "time": "{{2022}}-{{03}}-{{28}}T{{00}}:{{12}}:{{37}}.{{214}}Z",
  "region": "{{us-west-2}}",
  "resources": [
    "{{auto-scaling-group-arn}}"
  ],
  "detail": {
    "LifecycleActionToken": "{{42694b3d}}-{{4b70}}-{{6a62}}-{{8523}}-{{09a1eEXAMPLE}}",
    "AutoScalingGroupName": "{{my-asg}}",
    "LifecycleHookName": "{{my-termination-lifecycle-hook}}",
    "EC2InstanceId": "i-{{1234567890abcdef0}}",
    "LifecycleTransition": "autoscaling:EC2_INSTANCE_TERMINATING",
    "NotificationMetadata": "{{additional-info}}",
    "Origin": "AutoScalingGroup",
    "Destination": "WarmPool"
  }
}
```

## Example event patterns
<a name="warm-pools-eventbridge-patterns"></a>

The preceding section provides example events emitted by Amazon EC2 Auto Scaling.

EventBridge event patterns have the same structure as the events that they match. The pattern quotes the fields that you want to match and provides the values that you're looking for.

The following fields in the event form the event pattern that is defined in the rule to invoke an action:

`"source": "aws.autoscaling"`
Identifies that the event is from Amazon EC2 Auto Scaling.

`"detail-type": "{{EC2 Instance-launch Lifecycle Action}}"`
Identifies the event type.

`"Origin": "{{EC2}}"`
Identifies where the instance is coming from.

`"Destination": "{{WarmPool}}"`
Identifies where the instance is going to.

Use the following sample event pattern to capture all `EC2 Instance-launch Lifecycle Action` events that are associated with instances entering the warm pool.

```
{
  "source": [ "aws.autoscaling" ],
  "detail-type": [ "EC2 Instance-launch Lifecycle Action" ],
  "detail": {
      "Origin": [ "EC2" ],
      "Destination": [ "WarmPool" ]
   }
}
```

Use the following sample event pattern to capture all `EC2 Instance-launch Lifecycle Action` events that are associated with instances leaving the warm pool because of a scale-out event.

```
{
  "source": [ "aws.autoscaling" ],
  "detail-type": [ "EC2 Instance-launch Lifecycle Action" ],
  "detail": {
      "Origin": [ "WarmPool" ],
      "Destination": [ "AutoScalingGroup" ]
   }
}
```

Use the following sample event pattern to capture all `EC2 Instance-launch Lifecycle Action` events that are associated with instances launching directly into the Auto Scaling group.

```
{
  "source": [ "aws.autoscaling" ],
  "detail-type": [ "EC2 Instance-launch Lifecycle Action" ],
  "detail": {
      "Origin": [ "EC2" ],
      "Destination": [ "AutoScalingGroup" ]
   }
}
```

Use the following sample event pattern to capture all `EC2 Instance-terminate Lifecycle Action` events that are associated with instances returning to the warm pool on scale in.

```
{
  "source": [ "aws.autoscaling" ],
  "detail-type": [ "EC2 Instance-terminate Lifecycle Action" ],
  "detail": {
      "Origin": [ "AutoScalingGroup" ],
      "Destination": [ "WarmPool" ]
   }
}
```

Use the following sample event pattern to capture all events that are associated with `EC2 Instance-launch Lifecycle Action`, regardless of the origin or destination.

```
{
  "source": [ "aws.autoscaling" ],
  "detail-type": [ "EC2 Instance-launch Lifecycle Action" ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
