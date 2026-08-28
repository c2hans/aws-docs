---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-group-replacing-instances.html
---

# Replace the instances in your Auto Scaling group
<a name="ec2-auto-scaling-group-replacing-instances"></a>

Amazon EC2 Auto Scaling offers capabilities that let you replace the Amazon EC2 instances in your Auto Scaling group after making updates, such as adding a new launch template with a new Amazon Machine Image (AMI) or adding new instance types. It also helps you streamline updates by giving you the option of including them in the same operation that replaces the instances.

This section includes information to help you do the following:
+ Start an instance refresh to replace instances in your Auto Scaling group.
+ Declare specific updates that describe a desired configuration and update the Auto Scaling group to the desired configuration.
+ Skip replacing already updated instances.
+ Use checkpoints to update instances in phases and perform verifications on your instances at specific points.
+ Use bake time to pause at the end of an instance refresh to validate instance health.
+ Receive notifications by email when a checkpoint is reached.
+ Use a rollback to restore the Auto Scaling group to the configuration it was previously using.
+ Automatically roll back if the instance refresh fails for some reason or if any Amazon CloudWatch alarms you specify go into the `ALARM` state.
+ Limit the lifetime of instances to provide consistent software versions and instance configurations across the Auto Scaling group.
+ Replace root volumes without terminating instances while retaining network interfaces, non-root volumes, and IAM policies.

**Topics**
+ [Instance refresh](asg-instance-refresh.md)
+ [Maximum instance lifetime](asg-max-instance-lifetime.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
