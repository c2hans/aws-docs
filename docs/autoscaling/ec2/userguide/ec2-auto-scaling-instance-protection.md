---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html
---

# Use instance scale-in protection to control instance termination
<a name="ec2-auto-scaling-instance-protection"></a>

Instance scale-in protection gives you control over which instances Amazon EC2 Auto Scaling can terminate. A common use case for this feature is scaling container-based workloads. For more information, see [Design your applications to gracefully handle instance termination](gracefully-handle-instance-termination.md).

By default, instance scale-in protection is disabled when you create an Auto Scaling group. This means that Amazon EC2 Auto Scaling can terminate any instance in the group.

You can protect instances as soon as they launch by enabling the instance scale-in protection setting on your Auto Scaling group. Instance scale-in protection starts when the instance state is `InService`. Then, to control which instances can terminate, disable the scale-in protection setting on individual instances within the Auto Scaling group. By doing so, you can continue to protect certain instances from unwanted terminations.

**Topics**
+ [Considerations](#instance-protection-considerations)
+ [Change scale-in protection for an Auto Scaling group](#instance-protection-group)
+ [Change scale-in protection for an instance](#instance-protection-instance)

## Considerations
<a name="instance-protection-considerations"></a>

The following are considerations when using instance scale-in protection:
+ If all instances in an Auto Scaling group are protected from scale in, and a scale in event occurs, its desired capacity is decremented. However, the Auto Scaling group can't terminate the required number of instances until their instance scale in protection settings are disabled. In the AWS Management Console, the **Activity history** for the Auto Scaling group includes the following message if all instances in an Auto Scaling group are protected from scale in when a scale in event occurs: `Could not scale to desired capacity because all remaining instances are protected from scale in.`
+ If you detach an instance that is protected from scale in, its instance scale in protection setting is lost. When you attach the instance to the group again, it inherits the current instance scale in protection setting of the group. When Amazon EC2 Auto Scaling launches a new instance or moves an instance from a warm pool into the Auto Scaling group, the instance inherits the instance scale in protection setting of the Auto Scaling group.
+ Instance scale-in protection does not protect Auto Scaling instances from the following:
  + Health check replacement if the instance fails health checks. For more information, see [Health checks for instances in an Auto Scaling group](ec2-auto-scaling-health-checks.md).
  + Spot Instance interruptions. A Spot Instance is terminated when capacity is no longer available or the Spot price exceeds your maximum price.
  + A Capacity Block reservation ends. Amazon EC2 reclaims the Capacity Block instances even if they are protected from scale in.
  + Manual termination through the `terminate-instance-in-auto-scaling-group` command. For more information, see [Terminate instances in your Auto Scaling group (AWS CLI)](ec2-auto-scaling-scaling-manually.md#terminate-an-instance-aws-cli).
  + Manual termination through the Amazon EC2 console, CLI commands, and API operations. To protect Auto Scaling instances from manual termination, enable Amazon EC2 termination protection. (This does not prevent Amazon EC2 Auto Scaling from terminating instances or manual termination through the `terminate-instance-in-auto-scaling-group` command.) For information about enabling Amazon EC2 termination protection in a launch template, see [Create a launch template using advanced settings](advanced-settings-for-your-launch-template.md).

## Change scale-in protection for an Auto Scaling group
<a name="instance-protection-group"></a>

You can enable or disable the instance scale-in protection setting for an Auto Scaling group. When you enable it, all new instances launched by the group will have instance scale-in protection enabled.

Enabling or disabling this setting for an Auto Scaling group does not affect existing instances.

------
#### [ Console ]

**To enable scale-in protection for a new Auto Scaling group**
When you create the Auto Scaling group, on the **Configure group size and scaling policies** page, under **Instance scale-in protection**, select the **Enable instance scale-in protection** check box.

**To enable or disable scale-in protection for an existing group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select check box next to the Auto Scaling group.

   A split pane opens up in the bottom of the page.

1. On the **Details** tab, choose **Advanced configurations**, **Edit**.

1. For **Instance scale-in protection**, select or clear the **Enable instance-scale protection** check box to enable or disable this option as required.

1. Choose **Update**.

------
#### [ AWS CLI ]

**To enable scale-in protection for a new Auto Scaling group**
Use the following [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command to enable instance scale-in protection.

```
aws autoscaling create-auto-scaling-group --auto-scaling-group-name {{my-asg}} --new-instances-protected-from-scale-in ...
```

**To enable scale-in protection for an existing group**
Use the following [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command to enable instance scale-in protection for the specified Auto Scaling group.

```
aws autoscaling update-auto-scaling-group --auto-scaling-group-name {{my-asg}} --new-instances-protected-from-scale-in
```

**To disable scale-in protection for an existing group**
Use the following command to disable instance scale-in protection for the specified group.

```
aws autoscaling update-auto-scaling-group --auto-scaling-group-name {{my-asg}} --no-new-instances-protected-from-scale-in
```

------

## Change scale-in protection for an instance
<a name="instance-protection-instance"></a>

By default, an instance gets its instance scale-in protection setting from its Auto Scaling group. However, you can enable or disable instance scale-in protection for individual instances after they launch.

------
#### [ Console ]

**To enable or disable scale-in protection for an instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to your Auto Scaling group.

   A split pane opens up in the bottom of the page.

1. On the **Instance management** tab, in **Instances**, select an instance.

1. To enable instance scale-in protection, choose **Actions**, **Set scale-in protection**. When prompted, choose **Set scale-in protection**.

1. To disable instance scale-in protection, choose **Actions**, **Remove scale-in protection**. When prompted, choose **Remove scale-in protection**.

------
#### [ AWS CLI ]

**To enable scale-in protection for an instance**
Use the following [set-instance-protection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/set-instance-protection.html) command to enable instance scale-in protection for the specified instance.

```
aws autoscaling set-instance-protection --instance-ids {{i-5f2e8a0d}} --auto-scaling-group-name {{my-asg}} --protected-from-scale-in
```

**To disable scale-in protection for an instance**
Use the following command to disable instance scale-in protection for the specified instance.

```
aws autoscaling set-instance-protection --instance-ids {{i-5f2e8a0d}} --auto-scaling-group-name {{my-asg}} --no-protected-from-scale-in
```

------

**Note**
Remember, instance scale-in protection does not guarantee that instances won't be terminated in the event of a human error—for example, if someone manually terminates an instance using the Amazon EC2 console or AWS CLI. To protect your instance from accidental termination, you can use Amazon EC2 termination protection. However, even with termination protection and instance scale-in protection enabled, data saved to instance storage can be lost if a health check determines that an instance is unhealthy or if the group itself is accidentally deleted. As with any environment, a best practice is to back up your data frequently, or whenever it's appropriate for your business continuity requirements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
