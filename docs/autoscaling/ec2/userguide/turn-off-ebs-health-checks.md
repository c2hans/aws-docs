---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/turn-off-ebs-health-checks.html
---

# Turn off the Amazon EBS health checks for an Auto Scaling group
<a name="turn-off-ebs-health-checks"></a>

The following topic describes how to turn off Amazon EBS health checks for an Auto Scaling group. If you don't require Amazon EBS health checks anymore, use the following procedure to turn them off.

------
#### [ Console ]

**Turning off Amazon EBS health checks for a group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to an existing group.

   A split pane opens up in the bottom of the **Auto Scaling groups** page.

1. On the **Details** tab, choose **Health checks**, **Edit**.

1. For **Health checks**, **Additional health check types**, deselect **Turn on Amazon EBS health checks**.

1. Choose **Update**.

------
#### [ AWS CLI ]

**Turning off Amazon EBS health checks for a group**
To update the health checks on an Auto Scaling group so that it no longer uses Amazon EBS health checks, use the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command. Include the `--health-check-type` option and a value of `EC2`.

```
aws autoscaling update-auto-scaling-group --auto-scaling-group-name {{my-asg}} \
  --health-check-type "EC2"
```

To turn off Amazon EBS health checks without turning off other health check types (such as Elastic Load Balancing), you must specify them instead of `EC2`. For example, for Elastic Load Balancing health checks, specify `ELB` for the `--health-check-type` option.

Value names are case sensitive.

------
