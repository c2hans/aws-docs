---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-max-instance-lifetime.html
---

# Replace Auto Scaling instances based on maximum instance lifetime
<a name="asg-max-instance-lifetime"></a>

The maximum instance lifetime specifies the maximum amount of time (in seconds) that an instance can be in service before it is terminated and replaced. A common use case might be a requirement to replace your instances on a schedule because of internal security policies or external compliance controls.

You must specify a value of at least 86,400 seconds (one day). To clear a previously set value, specify a new value of 0. This setting applies to all current and future instances in your Auto Scaling group.

**Topics**
+ [Considerations](#max-instance-lifetime-considerations)
+ [Set the maximum instance lifetime](#set-maximum-instance-lifetime)
+ [Limitations](#maximum-instance-lifetime-limitations)

## Considerations
<a name="max-instance-lifetime-considerations"></a>

The following are considerations when using this feature:
+ Whenever an earlier instance is replaced and a new instance launches, the new instance uses the launch template or launch configuration that is currently associated with the Auto Scaling group. If your launch template or launch configuration specifies the Amazon Machine Image (AMI) ID of a different version of your application, this version of your application will be deployed automatically.
+ Setting the maximum instance lifetime too low can cause instances to be replaced faster than desired. Amazon EC2 Auto Scaling will usually replace instances one at a time, with a pause between replacements. However, if the specified maximum instance lifetime doesn't provide enough time to replace each instance individually, Amazon EC2 Auto Scaling must replace more than one instance at a time. Several instances might be replaced at once, by up to 10 percent of the current capacity of your Auto Scaling group. To avoid replacing too many instances at once, either set a longer maximum instance lifetime or use instance scale-in protection to temporarily prevent individual instances from being terminated. For more information, see [Use instance scale-in protection to control instance termination](ec2-auto-scaling-instance-protection.md).
+ By default, Amazon EC2 Auto Scaling creates a new scaling activity for terminating the instance and then terminates it. While the instance is terminating, another scaling activity launches a new instance. You can change this behavior to launch before terminating by using an instance maintenance policy. For more information, see [Instance maintenance policies](ec2-auto-scaling-instance-maintenance-policy.md).

## Set the maximum instance lifetime
<a name="set-maximum-instance-lifetime"></a>

When you create an Auto Scaling group in the console, you cannot set the maximum instance lifetime. However, after the group is created, you can edit it to set the maximum instance lifetime.

**To set the maximum instance lifetime for a group (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to the Auto Scaling group.

   A split pane opens up at the bottom of the **Auto Scaling groups** page, showing information about the group you selected.

1. On the **Details** tab, choose **Advanced configurations**, **Edit**.

1. For **Maximum instance lifetime**, enter the maximum number of seconds that an instance can be in service.

1. Choose **Update**.

On the **Activity** tab, under **Activity history**, you can view the replacement of instances in the group throughout its history.

**To set the maximum instance lifetime for a group (AWS CLI)**
You can also use the AWS CLI to set the maximum instance lifetime for new or existing Auto Scaling groups.

For new Auto Scaling groups, use the [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command.

```
aws autoscaling create-auto-scaling-group --cli-input-json {{file://~/config.json}}
```

The following is an example `config.json` file that shows a maximum instance lifetime of `2592000` seconds (30 days).

```
{
    "AutoScalingGroupName": "{{my-asg}}",
    "LaunchTemplate": {
        "LaunchTemplateName": "{{my-launch-template}}",
        "Version": "{{$Default}}"
    },
    "MinSize": {{1}},
    "MaxSize": {{5}},
    "MaxInstanceLifetime": {{2592000}},
    "VPCZoneIdentifier": "{{subnet-5ea0c127}},{{subnet-6194ea3b}},{{subnet-c934b782}}",
    "Tags": []
}
```

For existing Auto Scaling groups, use the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command.

```
aws autoscaling update-auto-scaling-group --auto-scaling-group-name {{my-existing-asg}} --max-instance-lifetime {{2592000}}
```

**To verify the maximum instance lifetime for an Auto Scaling group**
Use the [describe-auto-scaling-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-groups.html) command.

```
aws autoscaling describe-auto-scaling-groups --auto-scaling-group-name {{my-asg}}
```

## Limitations
<a name="maximum-instance-lifetime-limitations"></a>
+ **Maximum lifetime not guaranteed to be exact for every instance**: Instances are not guaranteed to be replaced only at the end of their maximum duration. In some situations, Amazon EC2 Auto Scaling might need to start replacing instances immediately after you update the maximum instance lifetime parameter. The reason for this behavior is to avoid replacing all instances at the same time.
+ **Instance scale-in protection honored**: Amazon EC2 Auto Scaling provides instance scale-in protection to help you control which instances it can terminate. When this protection is enabled on an instance, Amazon EC2 Auto Scaling will not terminate the instance even if it has reached its maximum instance lifetime.
+ **Instances terminated before launch**: When there is only one instance in the Auto Scaling group, the maximum instance lifetime feature can result in an outage because Amazon EC2 Auto Scaling terminates an instance and then launches a new instance by default. To change this behavior to launch before terminating, see [Instance maintenance policies](ec2-auto-scaling-instance-maintenance-policy.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
