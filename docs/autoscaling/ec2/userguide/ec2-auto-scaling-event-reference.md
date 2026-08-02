---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-event-reference.html
---

# Amazon EC2 Auto Scaling event reference
<a name="ec2-auto-scaling-event-reference"></a>

Using Amazon EventBridge, you can create *rules* that match incoming *events* and route them to *targets* for processing.

**Topics**
+ [Lifecycle action events](#ec2-auto-scaling-lifecycle-action-events)
+ [Successful scaling events](#ec2-auto-scaling-successful-scaling-events)
+ [Unsuccessful scaling events](#ec2-auto-scaling-unsuccessful-scaling-events)

## Lifecycle action events
<a name="ec2-auto-scaling-lifecycle-action-events"></a>

When you add lifecycle hooks to your Auto Scaling group, Amazon EC2 Auto Scaling sends events to EventBridge when an instance transitions into a wait state. Events are produced on a best-effort basis.

**Topics**
+ [Scale-out lifecycle action](#launch-lifecycle-action)
+ [Scale-in lifecycle action](#terminate-lifecycle-action)

### Scale-out lifecycle action
<a name="launch-lifecycle-action"></a>

The following example event shows that Amazon EC2 Auto Scaling moved an instance to a `Pending:Wait` state due to a launch lifecycle hook.

```
{
  "version": "0",
  "id": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
  "detail-type": "EC2 Instance-launch Lifecycle Action",
  "source": "aws.autoscaling",
  "account": "{{123456789012}}",
  "time": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
  "region": "{{us-west-2}}",
  "resources": [
    "{{auto-scaling-group-arn}}"
  ],
  "detail": {
    "LifecycleActionToken": "{{87654321}}-{{4321}}-{{4321}}-{{4321}}-{{210987654321}}",
    "AutoScalingGroupName": "{{my-asg}}",
    "LifecycleHookName": "{{my-lifecycle-hook}}",
    "EC2InstanceId": "i-{{1234567890abcdef0}}",
    "LifecycleTransition": "autoscaling:EC2_INSTANCE_LAUNCHING",
    "NotificationMetadata": "{{additional-info}}",
    "Origin": "{{EC2}}",
    "Destination": "{{AutoScalingGroup}}"
  }
}
```

### Scale-in lifecycle action
<a name="terminate-lifecycle-action"></a>

The following example event shows that Amazon EC2 Auto Scaling moved an instance to a `Terminating:Wait` state due to a termination lifecycle hook.

**Important**
When an Auto Scaling group returns instances to a warm pool on scale in, returning instances to the warm pool can also generate `EC2 Instance-terminate Lifecycle Action` events. Events that are delivered when an instance moves to the wait state on scale in have `WarmPool` as the value for `Destination`. For more information, see [Instance reuse policy](ec2-auto-scaling-warm-pools.md#instance-reuse-policy).

```
{
  "version": "0",
  "id": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
  "detail-type": "EC2 Instance-terminate Lifecycle Action",
  "source": "aws.autoscaling",
  "account": "{{123456789012}}",
  "time": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
  "region": "{{us-west-2}}",
  "resources": [
    "{{auto-scaling-group-arn}}"
  ],
  "detail": {
    "LifecycleActionToken":"{{87654321}}-{{4321}}-{{4321}}-{{4321}}-{{210987654321}}",
    "AutoScalingGroupName":"{{my-asg}}",
    "LifecycleHookName":"{{my-lifecycle-hook}}",
    "EC2InstanceId":"i-{{1234567890abcdef0}}",
    "LifecycleTransition":"autoscaling:EC2_INSTANCE_TERMINATING",
    "NotificationMetadata":"{{additional-info}}",
    "Origin": "AutoScalingGroup",
    "Destination": "{{EC2}}"
  }
}
```

## Successful scaling events
<a name="ec2-auto-scaling-successful-scaling-events"></a>

The following examples show the event types for successful scaling events. Events are produced on a best-effort basis.

**Topics**
+ [Successful scale-out event](#launch-successful)
+ [Successful scale-in event](#terminate-successful)

### Successful scale-out event
<a name="launch-successful"></a>

The following example event shows that Amazon EC2 Auto Scaling successfully launched an instance.

```
{
  "version": "0",
  "id": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
  "detail-type": "EC2 Instance Launch Successful",
  "source": "aws.autoscaling",
  "account": "{{123456789012}}",
  "time": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
  "region": "{{us-west-2}}",
  "resources": [
    "{{auto-scaling-group-arn}}",
    "{{instance-arn}}"
  ],
  "detail": {
    "StatusCode": "InProgress",
    "Description": "Launching a new EC2 instance: i-{{12345678}}",
    "AutoScalingGroupName": "{{my-asg}}",
    "ActivityId": "{{87654321}}-{{4321}}-{{4321}}-{{4321}}-{{210987654321}}",
    "Details": {
      "Availability Zone": "{{us-west-2b}}",
      "Subnet ID": "subnet-{{12345678}}"
    },
    "RequestId": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
    "StatusMessage": "",
    "EndTime": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
    "EC2InstanceId": "i-{{1234567890abcdef0}}",
    "StartTime": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
    "Cause": "{{description-text}}",
    "Origin": "{{EC2}}",
    "Destination": "{{AutoScalingGroup}}"
  }
}
```

### Successful scale-in event
<a name="terminate-successful"></a>

The following example event shows that Amazon EC2 Auto Scaling successfully terminated an instance.

**Important**
When an Auto Scaling group returns instances to a warm pool on scale in, returning instances to the warm pool can also generate `EC2 Instance Terminate Successful` events. Events that are delivered when an instance successfully returns to the warm pool have `WarmPool` as the value for `Destination`. For more information, see [Instance reuse policy](ec2-auto-scaling-warm-pools.md#instance-reuse-policy).

```
{
  "version": "0",
  "id": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
  "detail-type": "EC2 Instance Terminate Successful",
  "source": "aws.autoscaling",
  "account": "{{123456789012}}",
  "time": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
  "region": "{{us-west-2}}",
  "resources": [
    "{{auto-scaling-group-arn}}",
    "{{instance-arn}}"
  ],
  "detail": {
    "StatusCode": "InProgress",
    "Description": "Terminating EC2 instance: i-{{12345678}}",
    "AutoScalingGroupName": "{{my-asg}}",
    "ActivityId": "{{87654321}}-{{4321}}-{{4321}}-{{4321}}-{{210987654321}}",
    "Details": {
      "Availability Zone": "{{us-west-2b}}",
      "Subnet ID": "subnet-{{12345678}}"
    },
    "RequestId": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
    "StatusMessage": "",
    "EndTime": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
    "EC2InstanceId": "i-{{1234567890abcdef0}}",
    "StartTime": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
    "Cause": "{{description-text}}",
    "Origin": "AutoScalingGroup",
    "Destination": "{{EC2}}"
  }
}
```

## Unsuccessful scaling events
<a name="ec2-auto-scaling-unsuccessful-scaling-events"></a>

The following examples show the event types for unsuccessful scaling events. Events are produced on a best-effort basis.

**Topics**
+ [Unsuccessful scale-out event](#launch-unsuccessful)
+ [Unsuccessful scale-in event](#terminate-unsuccessful)

### Unsuccessful scale-out event
<a name="launch-unsuccessful"></a>

The following example event shows that Amazon EC2 Auto Scaling failed to launch an instance.

```
{
  "version": "0",
  "id": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
  "detail-type": "EC2 Instance Launch Unsuccessful",
  "source": "aws.autoscaling",
  "account": "{{123456789012}}",
  "time": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
  "region": "{{us-west-2}}",
  "resources": [
    "{{auto-scaling-group-arn}}",
    "{{instance-arn}}"
  ],
  "detail": {
    "StatusCode": "Failed",
    "AutoScalingGroupName": "{{my-asg}}",
    "ActivityId": "{{87654321}}-{{4321}}-{{4321}}-{{4321}}-{{210987654321}}",
    "Details": {
      "Availability Zone": "{{us-west-2b}}",
      "Subnet ID": "subnet-{{12345678}}"
    },
    "RequestId": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
    "StatusMessage": "{{message-text}}",
    "EndTime": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
    "EC2InstanceId": "i-{{1234567890abcdef0}}",
    "StartTime": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
    "Cause": "{{description-text}}",
    "Origin": "{{EC2}}",
    "Destination": "{{AutoScalingGroup}}"
  }
}
```

### Unsuccessful scale-in event
<a name="terminate-unsuccessful"></a>

The following example event shows that Amazon EC2 Auto Scaling failed to terminate an instance.

**Important**
When an Auto Scaling group returns instances to a warm pool on scale in, failing to return instances to the warm pool can also generate `EC2 Instance Terminate Unsuccessful` events. Events that are delivered when an instance fails to return to the warm pool have `WarmPool` as the value for `Destination`. For more information, see [Instance reuse policy](ec2-auto-scaling-warm-pools.md#instance-reuse-policy).

```
{
  "version": "0",
  "id": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
  "detail-type": "EC2 Instance Terminate Unsuccessful",
  "source": "aws.autoscaling",
  "account": "{{123456789012}}",
  "time": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
  "region": "{{us-west-2}}",
  "resources": [
    "{{auto-scaling-group-arn}}",
    "{{instance-arn}}"
  ],
  "detail": {
    "StatusCode": "Failed",
    "AutoScalingGroupName": "{{my-asg}}",
    "ActivityId": "{{87654321}}-{{4321}}-{{4321}}-{{4321}}-{{210987654321}}",
    "Details": {
      "Availability Zone": "{{us-west-2b}}",
      "Subnet ID": "subnet-{{12345678}}"
    },
    "RequestId": "{{12345678}}-{{1234}}-{{1234}}-{{1234}}-{{123456789012}}",
    "StatusMessage": "{{message-text}}",
    "EndTime": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
    "EC2InstanceId": "i-{{1234567890abcdef0}}",
    "StartTime": "{{yyyy}}-{{mm}}-{{dd}}T{{hh}}:{{mm}}:{{ss}}Z",
    "Cause": "{{description-text}}",
    "Origin": "AutoScalingGroup",
    "Destination": "{{EC2}}"
  }
}
```
