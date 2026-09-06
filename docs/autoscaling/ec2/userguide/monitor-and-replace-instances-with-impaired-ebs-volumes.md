---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/monitor-and-replace-instances-with-impaired-ebs-volumes.html
---

# Monitor Auto Scaling instances with impaired Amazon EBS volumes using health checks
<a name="monitor-and-replace-instances-with-impaired-ebs-volumes"></a>

You can turn on the Amazon EBS health checks for your Auto Scaling group to make sure that Amazon EC2 Auto Scaling monitors the entire system on which your application runs.

After you turn on these health checks, Amazon EC2 Auto Scaling receives the results of the Amazon EC2 status checks performed on an instance's attached EBS volumes. If a volume is not reachable or does not pass I/O status checks, the health check will fail, and the corresponding instance will be considered unhealthy. When Amazon EC2 Auto Scaling detects an unhealthy instance, it replaces it.

This topic assumes you're familiar with the attached EBS status checks. If you're not, see the [Attached EBS status checks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html#attached-ebs-status-checks) section of the *Amazon EC2 User Guide* for details. The following topic describes how to turn on the Amazon EC2 Auto Scaling health checks that rely on the attached EBS status checks.

**Note**
You can turn on the Amazon EBS health checks for all of your Auto Scaling groups. However, these health checks are only available for [instances built on the AWS Nitro System](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html).

## Turn on the Amazon EBS health checks for a group
<a name="turn-on-ebs-health-checks"></a>

You can turn on the Amazon EBS health checks for new and existing Auto Scaling groups.

------
#### [ Console ]

**Turning on Amazon EBS health checks for a new group**
When you create the Auto Scaling group, on the **Configure advanced options** page, for **Health checks**, **Additional health check types**, select **Turn on Amazon EBS health checks**. Then, for **Health check grace period**, enter the amount of time, in seconds. This amount of time is how long Amazon EC2 Auto Scaling must wait before checking the health status of an instance after it enters the `InService` state. For more information, see [Set the health check grace period for an Auto Scaling group](health-check-grace-period.md).

------
#### [ AWS CLI ]

**Turning on Amazon EBS health checks for a new group**
Add the `--health-check-type` option to the [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command. The following example specifies **`EBS`** for the `--health-check-type` option for a new Auto Scaling group named `{{my-asg}}`.

```
aws autoscaling create-auto-scaling-group --auto-scaling-group-name {{my-asg}} \
  --health-check-type "EBS" --health-check-grace-period {{60}} ...
```

You can specify multiple values for the `--health-check-type` option. For example, to add both Amazon EBS and Elastic Load Balancing health checks types, use the following command.

```
aws autoscaling create-auto-scaling-group --auto-scaling-group-name {{my-asg}} \
  --health-check-type "EBS,ELB" --health-check-grace-period {{60}} ...
```

Value names are case sensitive.

------

------
#### [ Console ]

**Turning on Amazon EBS health checks for an existing group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. On the navigation bar at the top of the screen, choose the AWS Region that you created your Auto Scaling group in.

1. Select the check box next to an existing group.

   A split pane opens up in the bottom of the **Auto Scaling groups** page.

1. On the **Details** tab, choose **Health checks**, **Edit**.

1. For **Health checks**, **Additional health check types**, select **Turn on Amazon EBS health checks**.

1. For **Health check grace period**, enter the amount of time, in seconds. This amount of time is how long Amazon EC2 Auto Scaling must wait before checking the health status of an instance after it enters the `InService` state. For more information, see [Set the health check grace period for an Auto Scaling group](health-check-grace-period.md).

1. Choose **Update**.

------
#### [ AWS CLI ]

**Turning on Amazon EBS health checks for an existing group**
Add the `--health-check-type` option to the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command. The following example specifies `EBS` for the `--health-check-type` option for an existing Auto Scaling group named `{{my-asg}}`.

```
aws autoscaling update-auto-scaling-group --auto-scaling-group-name {{my-asg}} \
  --health-check-type "EBS" --health-check-grace-period {{60}}
```

To use multiple health checks types, you can specify multiple values (for example, `EBS,ELB`) for the `--health-check-type` option.

Value names are case sensitive.

------
