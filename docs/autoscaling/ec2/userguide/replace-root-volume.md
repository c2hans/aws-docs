---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/replace-root-volume.html
---

# Replace root volumes during instance refresh
<a name="replace-root-volume"></a>

**Topics**
+ [How it works](#start-instance-refresh-replace-root-volume-how-it-works)
+ [Requirements](#start-instance-refresh-replace-root-volume-requirements)
+ [Start an instance refresh with Replace Root Volume](#start-instance-refresh-replace-root-volume-cli)
+ [Limitations](#start-instance-refresh-replace-root-volume-limitations)
+ [Use lifecycle hooks with replace root volume](#replace-root-volume-lifecycle-hooks)

## How it works
<a name="start-instance-refresh-replace-root-volume-how-it-works"></a>

Root volume replacement updates your instances by replacing only the root EBS volume while keeping the instance running. This removes the need to launch new instances and avoids potential capacity constraints. This process preserves all other instance resources including:
+ Network interfaces and IP addresses
+ Non-root EBS volumes
+ Instance store volumes and data
+ Security groups and IAM roles

During root volume replacement, your application continues running on the existing instance. The original root volume is detached, a new root volume is created from your specified AMI, and then attached to the same instance. Original root volumes are automatically deleted after successful replacement.

When you use the replace root volume strategy, instances go through these lifecycle states:

1. `ReplacingRootVolume` - Root volume replacement begins

1. `ReplacingRootVolume:Wait` - Waits for lifecycle hook completion (if configured)

1. `ReplacingRootVolume:Proceed` - Proceeds with replacement

1. `RootVolumeReplaced` - Replacement completed successfully

After root volume replacement completes, Auto Scaling conducts health checks on updated instances. If root volume replacement fails for an instance, Auto Scaling marks that instance for termination and replaces it with a new instance.

## Requirements
<a name="start-instance-refresh-replace-root-volume-requirements"></a>
+ Your Auto Scaling group must use a mixed instances policy
+ All overrides in the mixed instances policy must specify an `ImageId`
+ AMIs must contain only a single root volume
+ All instances must match the group's launch template configuration
+ You must start the instance refresh with a desired configuration having a mixed instances policy containing `ImageId` overrides.

## Start an instance refresh with Replace Root Volume
<a name="start-instance-refresh-replace-root-volume-cli"></a>

**To start an instance refresh with Replace Root Volume (AWS CLI)**
Use the following [start-instance-refresh ](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/start-instance-refresh.html) command to start an instance refresh from the AWS CLI. You can specify any preferences that you want to change in a JSON configuration file. When you reference the configuration file, provide the file path and name as shown in the following example.

```
aws autoscaling start-instance-refresh --cli-input-json file://config.json
```

Contents of `config.json`:

**Example**

```
{
  "AutoScalingGroupName": {{"my-asg"}},
  "Strategy" : {{"ReplaceRootVolume"}},
  "DesiredConfiguration":{
    "MixedInstancesPolicy":{
      "LaunchTemplate": {
        "LaunchTemplateSpecification": {
          "LaunchTemplateId":{{"my-launch-template"}},
          "Version": {{"1"}}
        },
        "Overrides": [
          {
            "InstanceType":{{"c5.large"}},
            "ImageId":{{"ami-1234example"}}
          },
          {
            "InstanceType":{{"m5.large"}},
            "ImageId":{{"ami-2345example"}}
          }
        ]
      }
    }
  },
  "Preferences": {
    "InstanceWarmup": {{60}},
    "MinHealthyPercentage": {{90}},
    "AutoRollback": {{true}},
    "ScaleInProtectedInstances": {{Ignore}},
    "StandbyInstances": {{Ignore}}
  }
}
```

If preferences are not provided, default values are used. For more information, see [Understand the default values for an instance refresh](understand-instance-refresh-default-values.md).

Example output:

```
{
    "InstanceRefreshId": "08b91cf7-8fa6-48af-b6a6-d227f40f1b9b"
}
```

## Limitations
<a name="start-instance-refresh-replace-root-volume-limitations"></a>
+ You can’t start an instance refresh with Replace Root Volume if the EC2 Auto Scaling group or the instance refresh desired configuration uses the `$Latest` or `$Default` launch template version.
+ You can’t start an instance refresh with Replace Root Volume on an Amazon EC2 Auto Scaling Group if it contains instances whose instance type is not present in the mixed instances policy.
+ During an instance refresh with Replace Root Volume, you can only attach instances with types that are present in the desired configuration's mixed instances policy.
+ You can’t start an instance refresh with Replace Root Volume on an EC2 Auto Scaling Group that has a warm pool.
+ You can't add a warm pool to an Amazon EC2 Auto Scaling group that has an active instance refresh with Replace Root Volume.

## Use lifecycle hooks with replace root volume
<a name="replace-root-volume-lifecycle-hooks"></a>

Instances undergoing root volume replacement follow their own lifecycle transitions, allowing you to invoke actions (for example, a Lambda function) before and/or after the replacement. For more information about lifecycle states during root volume replacement, see [Lifecycle state transitions for instances undergoing root volume replacement](lifecycle-hooks-overview.md#rvr-lifecycle-state-transitions).

For more information about adding a lifecycle hook, see [Add lifecycle hooks to your Auto Scaling group](adding-lifecycle-hooks.md). For more information about completing a lifecycle action, see [Complete a lifecycle action in an Auto Scaling group](completing-lifecycle-hooks.md).

Before root volume replacement, a lifecycle hook can be useful in the following scenarios:
+ You want to gracefully shut down your application before the root volume is replaced and the instance is rebooted.
+ You want to move data from the root volume to another location before the volume is replaced.

After root volume replacement, a lifecycle hook can be useful in the following scenarios:
+ You want to verify that your instance is fully ready with the new AMI before it starts receiving traffic.
+ You want to bootstrap application data that previously existed on the root volume.

When you add lifecycle hooks, consider the following:
+ When a lifecycle hook is configured for the `autoscaling:EC2_INSTANCE_TERMINATING` lifecycle action, an instance about to undergo root volume replacement pauses to perform a custom action when it reaches the `ReplacingRootVolume:Wait` state.
+ When a lifecycle hook is configured for the `autoscaling:EC2_INSTANCE_LAUNCHING` lifecycle action, an instance that just had its root volume replaced pauses to perform a custom action when it reaches the `Pending:Wait` state.

When instances reach a wait state, Amazon EC2 Auto Scaling sends a notification. Auto Scaling lifecycle hook notifications contain an `Action` field with value `ReplaceRootVolume` to indicate the instance is undergoing root volume replacement.

Examples of these notifications are available in the EventBridge section of this guide. For more information see [Instance refresh replace root volume lifecycle events](instance-refresh-eventbridge-events.md#instance-refresh-rvr-lifecycle-events).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
