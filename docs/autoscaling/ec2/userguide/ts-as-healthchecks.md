---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ts-as-healthchecks.html
---

# Troubleshoot unhealthy instances in Amazon EC2 Auto Scaling
<a name="ts-as-healthchecks"></a>

The following are error messages returned by Amazon EC2 Auto Scaling, the potential causes, and the steps you can take to resolve the issues.

To retrieve an error message, see [View the reason for health check failures](replace-unhealthy-instance.md).

**Topics**
+ [An instance was taken out of service in response to an EC2 instance status check failure](#ts-failed-status-checks)
+ [An instance was taken out of service in response to an EC2 health check that indicated it had been terminated or stopped](#ts-terminated-or-stopped)
+ [An instance was taken out of service in response to an ELB system health check failure](#ts-failed-elb-health-checks)
+ [Additional resources](#troubleshoot-health-checks-additional-resources)

## An instance was taken out of service in response to an EC2 instance status check failure
<a name="ts-failed-status-checks"></a>

**Problem**: Auto Scaling instances fail the Amazon EC2 status checks.

**Cause 1**: If there are issues that cause Amazon EC2 to consider the instances in your Auto Scaling group impaired, Amazon EC2 Auto Scaling automatically replaces the instances as part of its health checks.

**Note**
Amazon EC2 provides two status checks: the **system status check**, which detects problems with the underlying host or infrastructure, and the **instance status check**, which detects problems with the configuration or state of the instance itself. This error message applies when either an instance or system status check fails. To determine which check failed for a specific instance, view the status check details for the instance in the Amazon EC2 console, or call the `DescribeInstanceStatus` API. You can also use the `StatusCheckFailed_System` and `StatusCheckFailed_Instance` Amazon CloudWatch metrics to see which check failed. For more information, see [Status checks for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html) in the *Amazon EC2 User Guide*.

**Solution 1**: When a status check fails, you typically must address the problem yourself by making instance configuration changes until your application is no longer exhibiting any problems. To resolve this issue, follow these steps:

1. Manually create an Amazon EC2 instance that is not part of the Auto Scaling group and investigate the problem. For general help with investigating impaired instances, see [Troubleshoot instances with failed status checks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstances.html) in the *Amazon EC2 User Guide*.

1. After you confirm that your instance launched successfully and is healthy, deploy a new, error-free instance configuration to the Auto Scaling group.

1. Delete the instance that you created to avoid ongoing charges to your AWS account.

## An instance was taken out of service in response to an EC2 health check that indicated it had been terminated or stopped
<a name="ts-terminated-or-stopped"></a>

**Problem**: Auto Scaling instances that have been stopped, rebooted, or terminated are replaced.

**Cause 1**: A user manually stopped, rebooted, or terminated the instance.

**Solution 1**: If you need to stop or reboot the instances in your Auto Scaling group, we recommend that you put the instances on standby first. For more information, see [Temporarily remove instances from your Auto Scaling group](as-enter-exit-standby.md).

**Cause 2**: Amazon EC2 Auto Scaling attempts to replace Spot Instances after the Amazon EC2 Spot service interrupts the instances, because the Spot price increases above your maximum price or capacity is no longer available.

**Solution 2**: There is no guarantee that a Spot Instance exists to fulfill the request at any given point in time. However, you can try the following:
+ Use a higher Spot maximum price (possibly the On-Demand price). By setting your maximum price higher, it gives the Amazon EC2 Spot service a better chance of launching and maintaining your required amount of capacity.
+ Increase the number of different capacity pools that you can launch instances from by running multiple instance types in multiple Availability Zones. For more information, see [Auto Scaling groups with multiple instance types and purchase options](ec2-auto-scaling-mixed-instances-groups.md).
+ If you use multiple instance types, consider enabling the Capacity Rebalancing feature. This is useful if you want the Amazon EC2 Spot service to attempt to launch a new Spot Instance before a running instance is terminated. For more information, see [Capacity Rebalancing in Auto Scaling to replace at-risk Spot Instances](ec2-auto-scaling-capacity-rebalancing.md).

**Cause 3**: With Capacity Blocks, Amazon EC2 terminates any instances that are still running 30 minutes before the end time of the Capacity Block. This abrupt termination causes your Auto Scaling group to try to launch new instances to maintain its desired capacity, even as the Capacity Block is ending.

**Solution 3**: To resolve this issue, try the following:
+ Decrease the desired capacity of the Auto Scaling group to prevent it from trying to launch new instances. For more information, see [Manual scaling for Amazon EC2 Auto Scaling](ec2-auto-scaling-scaling-manually.md).
+ Make sure you scale in your Auto Scaling group 30 minutes before the Capacity Block end time so that you do not encounter this error frequently. Make sure any lifecycle hooks have completed 30 minutes before the Capacity Block end time. For more information, see [Target Capacity Blocks or interruptible Capacity Reservations from a launch template](capacity-reservation-create-asg-procedure.md#target-capacity-blocks-or-interruptible-capacity-reservations-from-a-launch-template).

## An instance was taken out of service in response to an ELB system health check failure
<a name="ts-failed-elb-health-checks"></a>

**Problem**: Auto Scaling instances might pass the EC2 status checks. But they might fail the Elastic Load Balancing health checks for the target groups or Classic Load Balancers with which the Auto Scaling group is registered.

**Cause 1**: If your Auto Scaling group relies on health checks provided by Elastic Load Balancing, Amazon EC2 Auto Scaling determines the health status of your instances by checking the results of both the EC2 status checks and the Elastic Load Balancing health checks. The load balancer performs health checks by sending a request to each instance and waiting for the correct response, or by establishing a connection with the instance. An instance might fail the Elastic Load Balancing health check because an application running on the instance has issues that cause the load balancer to consider the instance out of service.

**Solution 1**: To pass the Elastic Load Balancing health checks:
+ Verify that the health check settings of your target groups are correctly configured. You define health check settings for your load balancer per target group. For more information, see [Configure health checks for targets](getting-started-elastic-load-balancing.md#elb-health-checks-for-targets).
+ Make note of the success codes that the load balancer is expecting, and verify that your application is configured correctly to return these codes on success.
+ Verify that the security groups for your load balancer and Auto Scaling group are correctly configured.
+ Verify that the load balancer is configured in the same Availability Zones as your Auto Scaling group.

**Solution 2**: Update the Auto Scaling group to turn off Elastic Load Balancing health checks. For instructions for how to turn off these health checks, see [ Detach a target group or Classic Load Balancer](https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html#as-remove-load-balancer).

**Cause 2**: There is a mismatch between the health check grace period and the instance startup time.

**Solution 3**: Edit the health check grace period for your Auto Scaling group. Set the grace period to a long enough time period to support the number of consecutive successful health checks required before Elastic Load Balancing considers a newly launched instance healthy. For more information, see [Set the health check grace period for an Auto Scaling group](health-check-grace-period.md).

## Additional resources
<a name="troubleshoot-health-checks-additional-resources"></a>

If you have a different issue, see the following AWS re:Post articles for additional troubleshooting help:
+  [Why did Amazon EC2 Auto Scaling terminate an instance?](https://repost.aws/knowledge-center/auto-scaling-instance-how-terminated)
+  [Why didn't Amazon EC2 Auto Scaling terminate an unhealthy instance?](https://repost.aws/knowledge-center/auto-scaling-terminate-instance)
