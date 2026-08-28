---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/understand-instance-refresh-default-values.html
---

# Understand the default values for an instance refresh
<a name="understand-instance-refresh-default-values"></a>

Before you start an instance refresh, you can customize various preferences that affect the instance refresh. Some preference defaults are different depending on whether you use the console or the command line (AWS CLI or AWS SDK).

The following table lists the default values for the instance refresh settings.

| Setting | AWS CLI or AWS SDK | Amazon EC2 Auto Scaling console |
| --- | --- | --- |
| CloudWatch alarm | Disabled (null) | Disabled |
| Auto rollback | Disabled (false) | Disabled |
| Bake time | Zero | Zero |
| Checkpoints | Disabled (false) | Disabled |
| Checkpoint delay | 1 hour (3600 seconds) | 1 hour |
| Instance warmup | The [default instance warmup](ec2-auto-scaling-default-instance-warmup.md), if defined, or the [health check grace period](health-check-grace-period.md) otherwise. | The [default instance warmup](ec2-auto-scaling-default-instance-warmup.md), if defined, or the [health check grace period](health-check-grace-period.md) otherwise. |
| Maximum healthy percentage | Varies based on your instance maintenance policy. If no instance maintenance policy, this defaults to 100 percent (null). | Varies based on your instance maintenance policy. If no instance maintenance policy, this defaults to 100 percent (null). |
| Minimum healthy percentage | Varies based on your instance maintenance policy. If no instance maintenance policy, this defaults to 90 percent. | Varies based on your instance maintenance policy. If no instance maintenance policy, this defaults to 90 percent. |
| Scale-in protected instances | Wait | Ignore |
| Skip matching | Disabled (false) | Enabled |
| Standby instances | Wait | Ignore |

A description of each setting follows:

**CloudWatch alarm (`AlarmSpecification`)**
The CloudWatch alarm specification. CloudWatch alarms can be used to identify any issues and fail the operation if an alarm goes into the `ALARM` state. For more information, see [Start an instance refresh with auto rollback](instance-refresh-rollback.md#instance-refresh-using-auto-rollback).

**Auto rollback (`AutoRollback`)**
Controls whether Amazon EC2 Auto Scaling rolls back the Auto Scaling group to its previous configuration if the instance refresh fails. For more information, see [Undo changes with a manual or auto rollback](instance-refresh-rollback.md).

**Bake time (`BakeTime`)**
The amount of time to wait at the end of an instance refresh before the instance refresh is considered complete.

**Checkpoints (`CheckpointPercentages`)**
Controls whether Amazon EC2 Auto Scaling replaces instances in phases. This is useful if you need to perform verifications on your instances before replacing all instances. For more information, see [Add checkpoints to an instance refresh](asg-adding-checkpoints-instance-refresh.md).

**Checkpoint delay (`CheckpointDelay`)**
The amount of time, in seconds, to wait after a checkpoint before continuing. For more information, see [Add checkpoints to an instance refresh](asg-adding-checkpoints-instance-refresh.md).

**Instance warmup (`InstanceWarmup`)**
A time period, in seconds, during which Amazon EC2 Auto Scaling waits until a new instance is considered to have finished initializing before moving on to replacing the next instance. If you have already correctly defined a default instance warmup for the Auto Scaling group, then you don't need to change the instance warmup (unless you want to override the default). For more information, see [Set the default instance warmup for an Auto Scaling group](ec2-auto-scaling-default-instance-warmup.md).

**Maximum healthy percentage (`MaxHealthyPercentage`)**
The percentage of the desired capacity of the Auto Scaling group that your group can increase to when replacing instances.

**Minimum healthy percentage (`MinHealthyPercentage`)**
The percentage of the desired capacity of the Auto Scaling group that must be in service, healthy, and ready to use before the operation can continue.

**Scale-in protected instances (`ScaleInProtectedInstances`)**
Controls what Amazon EC2 Auto Scaling does if instances that are protected from scale in are found. For more information about these instances, see [Use instance scale-in protection to control instance termination](ec2-auto-scaling-instance-protection.md).
Amazon EC2 Auto Scaling provides the following options:
+ **Replace** (`Refresh`) – Replaces instances that are protected from scale in.
+ **Ignore** (`Ignore`) – Ignores instances that are protected from scale in and continues to replace instances that are not protected.
+ **Wait** (`Wait`) – Waits one hour for you to remove scale-in protection. If you don't do so, the instance refresh fails.

**Skip matching (`SkipMatching`)**
Controls whether Amazon EC2 Auto Scaling skips replacing instances that match the desired configuration. If no desired configuration is specified, then it skips replacing instances that have the same launch template and instance types that the Auto Scaling group was using before the instance refresh started. For more information, see [Use an instance refresh with skip matching](asg-instance-refresh-skip-matching.md).

**Standby instances (`StandbyInstances`)**
Controls what Amazon EC2 Auto Scaling does if instances are found in `Standby` state. For more information about these instances, see [Temporarily remove instances from your Auto Scaling group](as-enter-exit-standby.md).
Amazon EC2 Auto Scaling provides the following options:
+ **Terminate** (`Terminate`) – Terminates instances that are in `Standby`.
+ **Ignore** (`Ignore`) – Ignores instances that are in `Standby` and continues to replace instances that are in the `InService` state.
+ **Wait** (`Wait`) – Waits one hour for you to return the instances to service. If you don't do so, the instance refresh fails.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
