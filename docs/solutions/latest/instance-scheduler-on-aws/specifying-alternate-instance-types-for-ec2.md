---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/specifying-alternate-instance-types-for-ec2.html
---

# Handling EC2 Insufficient Capacity Errors
<a name="specifying-alternate-instance-types-for-ec2"></a>

When Instance Scheduler fails to start an instance due to insufficient capacity, its default behavior is to issue a start-failed event (see [EventBridge Events](monitor-the-solution.md#monitoring-eventbridge-events)) and try again on the next scheduling interval. Alternatively, Instance Scheduler can be configured to resize your instance to alternative instance types before retrying the start operation. This feature helps improve instance availability in capacity constrained environments.

## Configuration
<a name="configuration"></a>

To enable alternate instance types for an EC2 instance, add the `IS-PreferredInstanceTypes` tag to the instance with a comma-separated list of instance types in order of preference (most preferred first):

```
IS-PreferredInstanceTypes: t3.medium,t3.large,m5.large
```

## How it works
<a name="how-it-works"></a>

The alternate instance types list is provided in order of preference, with the first type being the most preferred. When Instance Scheduler attempts to start an EC2 instance:

1. If the instance is not currently the most preferred size, attempts to resize it to the most preferred size before starting

1. If the start operation succeeds, no further alternates are attempted

1. If the start operation fails due to insufficient capacity:

   1. Attempts to resize to the next alternate instance type in the list

   1. Retries the start operation

   1. If still unsuccessful, tries the next alternate type

   1. Continues until successful or all alternates are exhausted

## Requirements and limitations
<a name="requirements-and-limitations"></a>

 **Instance compatibility**: Alternate instance types must be compatible with the instance’s current configuration (AMI, subnet, security groups, etc.). For more information, refer to [Change the instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html#resize-limitations) in the *Amazon EC2 User Guide*.

 **Tag format**: The `IS-PreferredInstanceTypes` tag value must be a comma-separated list of valid EC2 instance types.

## Example
<a name="example"></a>

For an instance originally configured as `t3.small`, you might configure:

```
Schedule: office-hours
IS-PreferredInstanceTypes: t3.small,t3.medium,t3.large,m5.large
```

If the `t3.small` instance fails to start due to capacity issues, Instance Scheduler will attempt to resize and start the instance as `t3.medium`, then `t3.large`, then `m5.large` until successful or all options are exhausted.
