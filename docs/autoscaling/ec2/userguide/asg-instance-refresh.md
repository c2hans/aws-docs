---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html
---

# Use an instance refresh to update instances in an Auto Scaling group
<a name="asg-instance-refresh"></a>

You can use an instance refresh to update the instances in your Auto Scaling group. This feature can be useful when a configuration change requires you to replace instances or their root volumes, especially if your Auto Scaling group contains a large number of instances.

Some situations where an instance refresh can help include:
+ Deploying a new Amazon Machine Image (AMI) or user data script across your Auto Scaling group. You can create a new launch template with the changes and then use an instance refresh to roll out the updates immediately.
+ Migrating your instances to new instance types to take advantage of the latest improvements and optimizations.
+ Switching your Auto Scaling groups from using a launch configuration to using a launch template. You can copy your launch configurations to launch templates and then use an instance refresh to update your instances to the new templates. For more information about migrating to launch templates, see [Migrate your Auto Scaling groups to launch templates](migrate-to-launch-templates.md).
+ Applying security patches or software updates while preserving long-running instance state and avoiding capacity constraints with specialized instance types like GPU or Mac instances.

**Topics**
+ [How an instance refresh works](instance-refresh-overview.md)
+ [Understand the default values](understand-instance-refresh-default-values.md)
+ [Start an instance refresh](start-instance-refresh.md)
+ [Monitor an instance refresh](check-status-instance-refresh.md)
+ [Replace root volumes](replace-root-volume.md)
+ [Cancel an instance refresh](cancel-instance-refresh.md)
+ [Undo changes with a rollback](instance-refresh-rollback.md)
+ [Use skip matching](asg-instance-refresh-skip-matching.md)
+ [Add checkpoints](asg-adding-checkpoints-instance-refresh.md)
