---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-check-grace-period.html
---

# Set the health check grace period for an Auto Scaling group
<a name="health-check-grace-period"></a>

When an Amazon EC2 Auto Scaling health check determines that an `InService` instance is unhealthy, it replaces it with a new instance. The health check grace period specifies the minimum amount of time (in seconds) to keep a new instance in service before terminating it if it's found to be unhealthy.

An example use case might be a requirement for Amazon EC2 Auto Scaling to avoid taking action if the Elastic Load Balancing health checks fail and the cause is that the instance is still initializing. Elastic Load Balancing health checks run in parallel, starting when the instance is registered with the load balancer. The grace period prevents Amazon EC2 Auto Scaling from marking your newly launched instances `Unhealthy` and terminating them unnecessarily if they don't immediately pass these health checks after they enter the `InService` state.

In the console, by default, the health check grace period is 300 seconds when you create an Auto Scaling group. Its default value is 0 seconds when you create an Auto Scaling group using the AWS CLI or an SDK. A value of 0 turns off the health check grace period.

Setting this value too high reduces the effectiveness of the Amazon EC2 Auto Scaling health checks. If you use lifecycle hooks for instance launch, you can set the health check grace period to 0. With lifecycle hooks, Amazon EC2 Auto Scaling provides a way to make sure that instances are always initialized before they enter the `InService` state. For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](lifecycle-hooks.md).

The grace period applies to the following instances:
+ Newly launched instances
+ Instances that are put back into service after being in standby
+ Instances that you manually attach to the group

**Important**
During the health check grace period, if Amazon EC2 Auto Scaling detects that an instance is no longer in the Amazon EC2 `running` state, it immediately marks the instance `Unhealthy` and replaces it. For example, if you stop an instance in an Auto Scaling group, it is marked `Unhealthy` and replaced.

## Set the health check grace period for a group
<a name="set-health-check-grace-period"></a>

You can set the health check grace period for new and existing Auto Scaling groups.

------
#### [ Console ]

**To modify the health check grace period for a new group**
When you create the Auto Scaling group, enter the amount of time (in seconds) on the **Configure advanced options** page, **Health checks**, **Health check grace period**. This is how long Amazon EC2 Auto Scaling must wait before checking the health status of an instance after it enters the `InService` state.

------
#### [ AWS CLI ]

**To modify the health check grace period for a new group**
Add the `--health-check-grace-period` option to the [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command. The following example configures the health check grace period with a value of `{{60}}` seconds for a new Auto Scaling group named `{{my-asg}}`.

```
aws autoscaling create-auto-scaling-group --auto-scaling-group-name {{my-asg}} \
  --health-check-grace-period {{60}} ...
```

------

------
#### [ Console ]

**To modify the health check grace period for an existing group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. On the navigation bar at the top of the screen, choose the AWS Region that you created your Auto Scaling group in.

1. Select the check box next to the Auto Scaling group.

   A split pane opens up in the bottom of the page.

1. On the **Details** tab, choose **Health checks**, **Edit**.

1. Under **Health check grace period**, enter the amount of time, in seconds. This is how long Amazon EC2 Auto Scaling must wait before checking the health status of an instance after it enters the `InService` state.

1. Choose **Update**.

------
#### [ AWS CLI ]

**To modify the health check grace period for an existing group**
Add the `--health-check-grace-period` option to the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command. The following example configures the health check grace period with a value of `{{120}}` seconds for an existing Auto Scaling group named `{{my-asg}}`.

```
aws autoscaling update-auto-scaling-group --auto-scaling-group-name {{my-asg}} \
  --health-check-grace-period {{120}}
```

------

**Note**
We strongly recommend also setting the default instance warm-up time for your Auto Scaling group. For more information, see [Set the default instance warmup for an Auto Scaling group](ec2-auto-scaling-default-instance-warmup.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
