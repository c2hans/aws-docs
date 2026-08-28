---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/instance-refresh-overview.html
---

# How an instance refresh works in an Auto Scaling group
<a name="instance-refresh-overview"></a>

This topic describes how an instance refresh works and introduces the key concepts you need to understand to use it effectively.

**Topics**
+ [How it works](#instance-refresh-how-it-works)
+ [Core concepts](#instance-refresh-core-concepts)
+ [Health check grace period](#instance-refresh-health-check-grace-period)
+ [Instance type compatibility](#instance-type-compatibility)
+ [Limitations](#instance-refresh-limitations)

## How it works
<a name="instance-refresh-how-it-works"></a>

To refresh instances in an Auto Scaling group, you can define a new configuration that contains the latest version of your application and any other updates you want to make.

Instance refresh supports two strategies for updating instances:
+ **Rolling strategy (default)** — Terminates instances and launches new ones in batches according to your preferences. This ensures that your Auto Scaling group maintains its desired capacity and availability throughout the update process.
+ **Replace root volume strategy** — Updates instances by replacing only the root volume without terminating the instance. This preserves instance network interfaces, non-root EBS volumes, and instance store data.

Requirements for replace root volume strategy:
+ Your Auto Scaling group must use a mixed instances policy
+ All overrides in the mixed instances policy must specify an `ImageId`
+ AMIs must contain only a single root volume
+ All instances must match the group's launch template configuration
+ You must start the instance refresh with a desired configuration having a mixed instances policy containing `ImageId` overrides.

When skip matching is enabled, Auto Scaling compares each instance's current AMI ID against the AMI IDs in your desired configuration. It only replaces instances where the AMI IDs don't match, allowing you to skip instances that are already updated.

### Perform an instance refresh
<a name="instance-refresh-process"></a>

Start an instance refresh to replace existing instances with new ones based on that configuration.

1. Create a new launch template or update the existing template with the desired configuration changes, such as a new Amazon Machine Image (AMI). For more information, see [Create a launch template for an Auto Scaling group](create-launch-template.md).

1. Start the instance refresh using the Amazon EC2 Auto Scaling console, AWS CLI, or SDK:
   + Specify the new launch template or launch template version you created. This will be used to launch new instances.
   + Set the preferred minimum and maximum healthy percentage. This controls how many instances are replaced simultaneously and whether new instances are launched before terminating old ones.
   + Configure any optional settings, such as:
     + **Checkpoints** – Pause the instance refresh after a certain percentage of replacements to verify progress.
     + **Bake time** – Pause at the end of instance refresh to validate instance health before the instance refresh is considered complete.
     + **Skip matching** – Compare old instances to the new configuration and only replace those that don't match. When you start an instance refresh from the console, skip matching is on by default.
     + **Multiple instance types** – Apply a new or updated [mixed instances policy](ec2-auto-scaling-mixed-instances-groups.md) as part of the desired configuration.

When the instance refresh has started, Amazon EC2 Auto Scaling will:
+ Replace instances in batches based on the minimum and maximum healthy percentages.
+ Launch the new instances first before terminating the old ones if the minimum healthy percentage is set to 100 percent. This ensures that your desired capacity is maintained at all times.
+ Check instances for health status and give them time to warm up before more instances are replaced.
+ Terminate and replace instances that are found to be unhealthy.
+ Automatically update the Auto Scaling group settings with the new configuration changes after the instance refresh succeeds.
+ Replace `InService` instances before instances that are in a warm pool.

The following flow diagram illustrates the launch before terminate behavior when you set the minimum healthy percentage to 100 percent.

![A diagram showing how an instance refresh works when the minimum healthy percentage is set to 100 percent.](http://docs.aws.amazon.com/autoscaling/ec2/userguide/images/instance-refresh-high-level-flowchart-diagram.png)

**Note**
The minimum and maximum healthy percentages for an instance refresh only need to be specified if you have not set an instance maintenance policy, or if you need to override the existing policy. For more information, see [Instance maintenance policies](ec2-auto-scaling-instance-maintenance-policy.md).
Similarly, you only need to specify the instance warmup period for an instance refresh if you have not enabled the default warmup, or if you need to override the default. For more information, see [Set the default instance warmup for an Auto Scaling group](ec2-auto-scaling-default-instance-warmup.md).

## Core concepts
<a name="instance-refresh-core-concepts"></a>

Before you get started, familiarize yourself with the following instance refresh core concepts:

**Minimum healthy percentage**
The *minimum healthy percentage* is the percentage of the desired capacity to keep in service, healthy, and ready to use during an instance refresh so that the refresh can continue. For example, if the minimum healthy percentage is 90 percent and the maximum healthy percentage is 100 percent, then 10 percent of capacity will be replaced at a time. If the new instances don't pass their health checks, Amazon EC2 Auto Scaling terminates and replaces them. If the instance refresh can't launch any healthy instances, it will eventually fail, leaving the other 90 percent of the group untouched. If the new instances stay healthy and finish their warmup period, Amazon EC2 Auto Scaling can continue to replace other instances.
An instance refresh can replace instances one at a time, several at a time, or all at once. To replace one instance at a time, set both the minimum and maximum healthy percentage to 100 percent. This changes the behavior of an instance refresh to launch before terminating, which prevents the group's capacity from falling below 100 percent of its desired capacity. To replace all instances at once, set a minimum healthy percentage of 0 percent.

**Maximum healthy percentage**
The *maximum healthy percentage* is the percentage of the desired capacity that your Auto Scaling group can increase to when replacing instances. The difference between the minimum and maximum cannot be greater than 100. A larger range increases the number of instances that can be replaced at the same time.

**Instance warmup**
The *instance warmup* is the time period from when a new instance's state changes to `InService` to when it is considered to have finished initializing. During an instance refresh, if the instances pass their health checks, Amazon EC2 Auto Scaling does not immediately move on to replacing the next instance after determining that a newly launched instance is healthy. It waits for the warmup period before it moves on to replacing the next instance. This can be helpful when your application still needs some initialization time before it responds to requests.
The instance warmup works the same way as the default instance warmup. Therefore, the same scaling considerations apply. For more information, see [Set the default instance warmup for an Auto Scaling group](ec2-auto-scaling-default-instance-warmup.md).

**Desired configuration**
The *desired configuration* is the new configuration that you want Amazon EC2 Auto Scaling to deploy across your Auto Scaling group. For example, you can specify a new launch template and new instance types for your instances. During an instance refresh, Amazon EC2 Auto Scaling updates the Auto Scaling group to the desired configuration. If a scale-out event occurs during an instance refresh, Amazon EC2 Auto Scaling launches new instances with the desired configuration instead of the group's current settings. After the instance refresh succeeds, Amazon EC2 Auto Scaling updates the Auto Scaling group settings to reflect the new desired configuration that you specified as part of the instance refresh.

**Skip matching**
Skip matching tells Amazon EC2 Auto Scaling to ignore instances that already have your latest updates. This way, you don't replace more instances than you need to. This is helpful when you want to make sure your Auto Scaling group uses a particular version of your launch template and only replaces those instances that use a different version.

**Checkpoints**
A *checkpoint* is a point in time where the instance refresh pauses for a specified amount of time. An instance refresh can contain multiple checkpoints. Amazon EC2 Auto Scaling emits events for each checkpoint. Therefore, you can add an EventBridge rule to send the events to a target, such as Amazon SNS, to be notified when a checkpoint is reached. After a checkpoint is reached, you have the opportunity to verify your deployment. If any problems are identified, you can cancel the instance refresh or roll it back. The ability to deploy updates in phases is a key benefit of checkpoints. If you don't use checkpoints, rolling replacements are performed continuously.

To learn more about all of the default settings you can configure when starting an instance refresh, see [Understand the default values for an instance refresh](understand-instance-refresh-default-values.md).

## Health check grace period
<a name="instance-refresh-health-check-grace-period"></a>

Amazon EC2 Auto Scaling determines whether an instance is healthy based on the status of the health checks that your Auto Scaling group uses. For more information, see [Health checks for instances in an Auto Scaling group](ec2-auto-scaling-health-checks.md).

To make sure that these health checks start as soon as possible, don't set the group's health check grace period too high, but high enough for your Elastic Load Balancing health checks to determine whether a target is available to handle requests. For more information, see [Set the health check grace period for an Auto Scaling group](health-check-grace-period.md).

## Instance type compatibility
<a name="instance-type-compatibility"></a>

Before you change your instance type, it's a good idea to verify that it works with your launch template. This confirms compatibility with the AMI that you specified. For example, let's say you launched your original instances from a paravirtual (PV) AMI, but you want to change to a current generation instance type that is only supported by a hardware virtual machine (HVM) AMI. In this case, you must use an HVM AMI in your launch template.

To confirm compatibility of the instance type without launching instances, use the [run-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-instances.html) command with the `--dry-run` option, as shown in the following example.

```
aws ec2 run-instances --launch-template LaunchTemplateName={{my-template}},Version='{{1}}' --dry-run
```

For information about how compatibility is determined, see [Compatibility for changing the instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/resize-limitations.html) in the *Amazon EC2 User Guide*.

## Limitations
<a name="instance-refresh-limitations"></a>
+ **Total duration** — The maximum amount of time that an instance refresh can continue to actively replace instances is 14 days.
+ **Difference in behavior specific to weighted groups** — If a mixed instances group is configured with an instance weight that is larger than or equal to the group's desired capacity, Amazon EC2 Auto Scaling might replace all `InService` instances at once. To avoid this situation, follow the recommendation in the [Configure an Auto Scaling group to use instance weights](ec2-auto-scaling-mixed-instances-groups-instance-weighting.md) topic. Specify a desired capacity that is larger than your largest weight when you use weights with your Auto Scaling group.
+ **One-hour timeout** — When an instance refresh is unable to continue making replacements because it is waiting to replace instances on standby or protected from scale in, or the new instances do not pass their health checks, Amazon EC2 Auto Scaling keeps retrying for an hour. It also provides a status message to help you resolve the issue. If the problem persists after an hour, the operation fails. The intention is to give it time to recover if there is a temporary issue.
+ **Deploying code via user data** — Skip matching doesn't check for code changes that are deployed from a user data script. If you use user data to pull new code and install these updates on new instances, we recommend that you turn off skip matching to make sure that all instances receive your latest code, even without a launch template version update.
+ **Update restriction** — If you attempt to update an Auto Scaling group's launch template, launch configuration, or mixed instances policy while an instance refresh with a desired configuration is active, the request will fail with the following validation error: `An active instance refresh with a desired configuration exists. All configuration options derived from the desired configuration are not available for update while the instance refresh is active.`
+ **Attribute-based instance selection** — If your Auto Scaling group uses attribute-based instance selection (specifying `InstanceRequirements` in a mixed instances policy), the following instance refresh parameters aren't supported:
  + **SkipMatching** - An instance refresh will fail if you start it with the `SkipMatching` parameter in an Auto Scaling group that has `InstanceRequirements` configured.
  + **DesiredConfiguration** - An instance refresh will fail if you start it with the `DesiredConfiguration` parameter in an Auto Scaling group that has `InstanceRequirements` configured.

  If you need to perform an instance refresh on an Auto Scaling group with attribute-based instance selection, start the instance refresh without these parameters.
+ Root volume replacement doesn’t support Elastic Load Balancing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
