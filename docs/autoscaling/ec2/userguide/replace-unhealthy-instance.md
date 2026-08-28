---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/replace-unhealthy-instance.html
---

# View the reason for health check failures
<a name="replace-unhealthy-instance"></a>

Using the following procedure, you can view information about any instances replaced due to a health check.

By default, Amazon EC2 Auto Scaling creates a new scaling activity for terminating the unhealthy instance and then terminates it. While the instance is terminating, another scaling activity launches a new instance. You can change this behavior to start launching a new instance as soon as possible by using an instance maintenance policy. For more information, see [Instance maintenance policies](ec2-auto-scaling-instance-maintenance-policy.md).

------
#### [ Console ]

**Viewing the reason for health check failures**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to the Auto Scaling group.

   A split pane opens up in the bottom of the **Auto Scaling groups** page.

1. On the **Activity** tab, under **Activity history**, the **Status** column shows whether your Auto Scaling group has successfully launched or terminated instances.

   If it terminated any unhealthy instances, the **Cause** column shows the date and time of the termination and the reason for the health check failure. For example, `At 2022-05-14T20:11:53Z an instance was taken out of service in response to a user health-check`. This message indicates that a custom health check marked the instance unhealthy.

   For help with health check failures, see [Troubleshoot unhealthy instances in Amazon EC2 Auto Scaling](ts-as-healthchecks.md).

------
#### [ AWS CLI ]

**Viewing the reason for health check failures**
Use the following [describe-scaling-activities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-scaling-activities.html) command.

```
aws autoscaling describe-scaling-activities --auto-scaling-group-name {{my-asg}}
```

The following is an example response, where `Cause` contains the reason for the health check failure.

```
{
  "Activities": [
    {
      "ActivityId": "4c65e23d-a35a-4e7d-b6e4-2eaa8753dc12",
      "AutoScalingGroupName": "my-asg",
      "Description": "Terminating EC2 instance: i-04925c838b6438f14",
      "Cause": "At 2021-04-01T21:48:35Z an instance was taken out of service in response to a user health-check.",
      "StartTime": "2021-04-01T21:48:35.859Z",
      "EndTime": "2021-04-01T21:49:18Z",
      "StatusCode": "Successful",
      "Progress": 100,
      "Details": "{\"Subnet ID\":\"subnet-5ea0c127\",\"Availability Zone\":\"us-west-2a\"...}",
      "AutoScalingGroupARN": "arn:aws:autoscaling:us-west-2:123456789012:autoScalingGroup:283179a2-f3ce-423d-93f6-66bb518232f7:autoScalingGroupName/my-asg"
    },
...
  ]
}
```

For a description of the fields in the output, see [Activity](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_Activity.html) in the *Amazon EC2 Auto Scaling API Reference*.

To describe the scaling activities after the Auto Scaling group has been deleted, add the `--include-deleted-groups` option to the [describe-scaling-activities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-scaling-activities.html) command.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
