---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/instance-refresh-eventbridge-events.html
---

# Instance refresh example events and patterns
<a name="instance-refresh-eventbridge-events"></a>

Using Amazon EventBridge, you can create *rules* that match incoming *events* and route them to *targets* for processing.

**Topics**
+ [Instance refresh events](#instance-refresh-events)
+ [Instance refresh replace root volume lifecycle events](#instance-refresh-rvr-lifecycle-events)

## Instance refresh events
<a name="instance-refresh-events"></a>

The following examples show events for the instance refresh feature. Events are produced on a best-effort basis.

**Topics**
+ [Checkpoint reached](#instance-refresh-checkpoint-reached)
+ [Instance refresh started](#instance-refresh-started)
+ [Instance refresh succeeded](#instance-refresh-succeeded)
+ [Instance refresh failed](#instance-refresh-failed)
+ [Instance refresh cancelled](#instance-refresh-cancelled)
+ [Instance refresh rollback started](#instance-refresh-rollback-started)
+ [Instance refresh rollback succeeded](#instance-refresh-rollback-succeeded)
+ [Instance refresh rollback failed](#instance-refresh-rollback-failed)

### Checkpoint reached
<a name="instance-refresh-checkpoint-reached"></a>

When the number of instances that have been replaced reaches the percentage threshold defined for the checkpoint, Amazon EC2 Auto Scaling sends the following event.

```
{
  "version": "0",
  "id": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
  "detail-type": "EC2 Auto Scaling Instance Refresh Checkpoint Reached",
  "source": "aws.autoscaling",
  "account": "{{123456789012}}",
  "time": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
  "region": "{{us-west-2}}",
  "resources": [
    "{{auto-scaling-group-arn}}"
  ],
  "detail": {
    "InstanceRefreshId": "{{ab00cf8f}}-{{9126}}-{{4f3c}}-{{8010}}-{{dbb8cad6fb86}}",
    "AutoScalingGroupName": "{{my-asg}}",
    "CheckpointPercentage": "{{50}}",
    "CheckpointDelay": "{{300}}"
  }
}
```

### Instance refresh started
<a name="instance-refresh-started"></a>

When the status of an instance refresh changes to `InProgress`, Amazon EC2 Auto Scaling sends the following event.

```
{
  "version": "0",
  "id": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
  "detail-type": "EC2 Auto Scaling Instance Refresh Started",
  "source": "aws.autoscaling",
  "account": "{{123456789012}}",
  "time": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
  "region": "{{us-west-2}}",
  "resources": [
    "{{auto-scaling-group-arn}}"
  ],
  "detail": {
    "InstanceRefreshId": "{{c613620e}}-{{07e2}}-{{4ed2}}-{{a9e2}}-{{ef8258911ade}}",
    "AutoScalingGroupName": "{{my-asg}}"
  }
}
```

### Instance refresh succeeded
<a name="instance-refresh-succeeded"></a>

When the status of an instance refresh changes to `Successful`, Amazon EC2 Auto Scaling sends the following event.

```
{
  "version": "0",
  "id": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
  "detail-type": "EC2 Auto Scaling Instance Refresh Succeeded",
  "source": "aws.autoscaling",
  "account": "{{123456789012}}",
  "time": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
  "region": "{{us-west-2}}",
  "resources": [
    "{{auto-scaling-group-arn}}"
  ],
  "detail": {
    "InstanceRefreshId": "{{c613620e}}-{{07e2}}-{{4ed2}}-{{a9e2}}-{{ef8258911ade}}",
    "AutoScalingGroupName": "{{my-asg}}"
  }
}
```

### Instance refresh failed
<a name="instance-refresh-failed"></a>

When the status of an instance refresh changes to `Failed`, Amazon EC2 Auto Scaling sends the following event.

```
{
  "version": "0",
  "id": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
  "detail-type": "EC2 Auto Scaling Instance Refresh Failed",
  "source": "aws.autoscaling",
  "account": "{{123456789012}}",
  "time": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
  "region": "{{us-west-2}}",
  "resources": [
    "{{auto-scaling-group-arn}}"
  ],
  "detail": {
    "InstanceRefreshId": "{{c613620e}}-{{07e2}}-{{4ed2}}-{{a9e2}}-{{ef8258911ade}}",
    "AutoScalingGroupName": "{{my-asg}}"
  }
}
```

### Instance refresh cancelled
<a name="instance-refresh-cancelled"></a>

When the status of an instance refresh changes to `Cancelled`, Amazon EC2 Auto Scaling sends the following event.

```
{
  "version": "0",
  "id": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
  "detail-type": "EC2 Auto Scaling Instance Refresh Cancelled",
  "source": "aws.autoscaling",
  "account": "{{123456789012}}",
  "time": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
  "region": "{{us-west-2}}",
  "resources": [
    "{{auto-scaling-group-arn}}"
  ],
  "detail": {
    "InstanceRefreshId": "{{c613620e}}-{{07e2}}-{{4ed2}}-{{a9e2}}-{{ef8258911ade}}",
    "AutoScalingGroupName": "{{my-asg}}"
  }
}
```

### Instance refresh rollback started
<a name="instance-refresh-rollback-started"></a>

When the status of an instance refresh changes to `RollbackInProgress`, Amazon EC2 Auto Scaling sends the following event.

```
{
  "version": "0",
  "id": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
  "detail-type": "EC2 Auto Scaling Instance Refresh Rollback Started",
  "source": "aws.autoscaling",
  "account": "{{123456789012}}",
  "time": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
  "region": "{{us-west-2}}",
  "resources": [
    "{{auto-scaling-group-arn}}"
  ],
  "detail": {
    "InstanceRefreshId": "{{c613620e}}-{{07e2}}-{{4ed2}}-{{a9e2}}-{{ef8258911ade}}",
    "AutoScalingGroupName": "{{my-asg}}"
  }
}
```

### Instance refresh rollback succeeded
<a name="instance-refresh-rollback-succeeded"></a>

When the status of an instance refresh changes to `RollbackSuccessful`, Amazon EC2 Auto Scaling sends the following event.

```
{
  "version": "0",
  "id": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
  "detail-type": "EC2 Auto Scaling Instance Refresh Rollback Succeeded",
  "source": "aws.autoscaling",
  "account": "{{123456789012}}",
  "time": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
  "region": "{{us-west-2}}",
  "resources": [
    "{{auto-scaling-group-arn}}"
  ],
  "detail": {
    "InstanceRefreshId": "{{c613620e}}-{{07e2}}-{{4ed2}}-{{a9e2}}-{{ef8258911ade}}",
    "AutoScalingGroupName": "{{my-asg}}"
  }
}
```

### Instance refresh rollback failed
<a name="instance-refresh-rollback-failed"></a>

When the status of an instance refresh changes to `Failed`, Amazon EC2 Auto Scaling sends the following event.

```
{
  "version": "0",
  "id": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
  "detail-type": "EC2 Auto Scaling Instance Refresh Rollback Failed",
  "source": "aws.autoscaling",
  "account": "{{123456789012}}",
  "time": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
  "region": "{{us-west-2}}",
  "resources": [
    "{{auto-scaling-group-arn}}"
  ],
  "detail": {
    "InstanceRefreshId": "{{c613620e}}-{{07e2}}-{{4ed2}}-{{a9e2}}-{{ef8258911ade}}",
    "AutoScalingGroupName": "{{my-asg}}"
  }
}
```

## Instance refresh replace root volume lifecycle events
<a name="instance-refresh-rvr-lifecycle-events"></a>

When you add lifecycle hooks to your Auto Scaling group, Amazon EC2 Auto Scaling sends events to EventBridge when an instance transitions into a wait state. For more information, see [Use lifecycle hooks with replace root volume](replace-root-volume.md#replace-root-volume-lifecycle-hooks).

The following examples show events when your Auto Scaling group has instances undergoing a root volume replacement during an instance refresh. Events are emitted on a best-effort basis.

**Topics**
+ [Start replace root volume lifecycle action](#rvr-start-lifecycle-action)
+ [End replace root volume lifecycle action](#rvr-end-lifecycle-action)
+ [Example event patterns](#rvr-event-patterns)

### Start replace root volume lifecycle action
<a name="rvr-start-lifecycle-action"></a>

When an instance is selected for root volume replacement during Instance Refresh and its state changes to `ReplacingRootVolume:Wait`.

```
{
  "version": "0",
  "id": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
  "detail-type": "EC2 Instance-terminate Lifecycle Action",
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
    "LifecycleHookName": "{{my-terminate-lifecycle-hook}}",
    "EC2InstanceId": "i-{{1234567890abcdef0}}",
    "LifecycleTransition": "autoscaling:EC2_INSTANCE_TERMINATING",
    "NotificationMetadata": "{{additional-info}}",
    "Origin": "AutoScalingGroup",
    "Destination": "AutoScalingGroup",
    "Action": "ReplaceRootVolume"
  }
}
```

### End replace root volume lifecycle action
<a name="rvr-end-lifecycle-action"></a>

When an instance has completed root volume replacement and its state changes to `Pending:Wait`.

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
    "Origin": "AutoScalingGroup",
    "Destination": "AutoScalingGroup",
    "Action": "ReplaceRootVolume"
  }
}
```

### Example event patterns
<a name="rvr-event-patterns"></a>

The preceding section provides example events emitted by Amazon EC2 Auto Scaling during an instance refresh with replace root volume strategy. EventBridge event patterns have the same structure as the events that they match. The pattern quotes the fields that you want to match and provides the values that you're looking for. The following fields in the event form the event pattern that is defined in the rule to invoke an action:

`"source": "aws.autoscaling"`
Identifies that the event is from Amazon EC2 Auto Scaling.

`"detail-type": "{{EC2 Instance-launch Lifecycle Action}}"`
Identifies the event type.

`"Action": "{{ReplaceRootVolume}}"`
Identifies what action is being performed on the instance.

Use the following sample event pattern to capture all the events that are associated with instances preparing to replace their root volumes:

```
{
  "source": [ "aws.autoscaling" ],
  "detail-type": [ "EC2 Instance-terminate Lifecycle Action" ],
  "detail": {
      "Action": [ "ReplaceRootVolume" ]
   }
}
```

Use the following sample event pattern to capture all the events that are associated with instances returning to service after completing root volume replacement:

```
{
  "source": [ "aws.autoscaling" ],
  "detail-type": [ "EC2 Instance-launch Lifecycle Action" ],
  "detail": {
      "Action": [ "ReplaceRootVolume" ]
   }
}
```
