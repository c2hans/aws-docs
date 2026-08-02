---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/ec2-auto-scaling-group-scheduling.html
---

# EC2 Auto Scaling Group Scheduling
<a name="ec2-auto-scaling-group-scheduling"></a>

Instance Scheduler on AWS supports scheduling of EC2 Auto Scaling groups (ASGs) using Scheduled Scaling Actions. This differs from the implementation of EC2/RDS scheduling and will be further explained in this section

Refer to [Scheduled scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html) for more information on Scheduled Scaling Actions.

## ASG scheduling overview
<a name="asg-scheduling-overview"></a>

ASGs can be scheduled by applying a schedule tag as described in [Tagging instances for scheduling](operator-guide.md#tag-instances-for-scheduling)

## Definition of Running/Stopped for ASGs
<a name="definition-of-runningstopped-for-asgs"></a>

When an Auto Scaling Group is configured, a user specifies a minimum, desired, and maximum capacity for that ASG. Instance Scheduler refers to these values as the min-desired-max or MDM of an ASG.

The ** *running state* ** of an ASG is defined using the `IS-MinDesiredMax` control tag. This tag should contain the desired MDM values in the format `min-desired-max` (for example: `1-3-5`).

If the `IS-MinDesiredMax` tag is not provided when the ASG is first tagged for scheduling, it will be automatically generated from the current size of the ASG at the time of tagging.

For all ASGs the ** *stopped state* ** is defined as an MDM of 0-0-0.

## ASG Start/Stop Behavior
<a name="asg-startstop-behavior"></a>

When Instance Scheduler starts or stops an ASG, it modifies the ASG’s capacity settings:

 **Starting an ASG**: Sets the minimum, desired, and maximum capacity to the values defined in the `IS-MinDesiredMax` tag (or the automatically generated values from when the ASG was first tagged).

 **Stopping an ASG**: Sets the minimum, desired, and maximum capacity to 0-0-0, which causes all instances in the ASG to be terminated.

### Limitations
<a name="limitations"></a>

ASG scheduling is performed by converting Instance Scheduler on AWS schedules into scheduled scaling rules compatible with the ASG service. This translation works best for simple single-period schedules that do not use complex cron expressions.

The following schedule features are not supported for ASG scheduling:
+ Advanced schedule flags such as *enforced* and *retain running.*
+ N-th weekday, nearest weekday, and last weekday expressions in periods.
+ Multi-period schedules with immediately adjacent or overlapping periods.
  + When configuring scheduled scaling actions for multi-period schedules, Instance Scheduler on AWS directly translate the beginning/end of periods to start/stop actions for the ASG even when another overlapping or adjacent period would normally cause that action to be skipped.
