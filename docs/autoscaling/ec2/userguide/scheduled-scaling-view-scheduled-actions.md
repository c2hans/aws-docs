---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/scheduled-scaling-view-scheduled-actions.html
---

# View scheduled action details
<a name="scheduled-scaling-view-scheduled-actions"></a>

To view details of upcoming scheduled actions for your Auto Scaling group, use one of the following methods:

------
#### [ Console ]

**To view scheduled action details**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select your Auto Scaling group.

1. On the **Automatic scaling** tab, in the **Scheduled actions** section, you can view upcoming scheduled actions.

Note that the console shows the values for **Start time** and **End time** in your local time with the UTC offset in effect at the specified date and time. The UTC offset is the difference, in hours and minutes, from local time to UTC. The value for **Time zone** shows your requested time zone, for example, `America/New_York`.

------
#### [ AWS CLI ]

Use the following [describe-scheduled-actions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-scheduled-actions.html) command.

```
aws autoscaling describe-scheduled-actions --auto-scaling-group-name {{my-asg}}
```

If successful, this command returns output similar to the following.

```
{
  "ScheduledUpdateGroupActions": [
    {
      "AutoScalingGroupName": "my-asg",
      "ScheduledActionName": "my-recurring-action",
      "Recurrence": "30 0 1 1,6,12 *",
      "ScheduledActionARN": "arn:aws:autoscaling:us-west-2:123456789012:scheduledUpdateGroupAction:8e86b655-b2e6-4410-8f29-b4f094d6871c:autoScalingGroupName/my-asg:scheduledActionName/my-recurring-action",
      "StartTime": "2020-12-01T00:30:00Z",
      "Time": "2020-12-01T00:30:00Z",
      "MinSize": 1,
      "MaxSize": 6,
      "DesiredCapacity": 4
    }
  ]
}
```

------

## Verify scaling activities
<a name="scheduled-scaling-verify-scaling-activities"></a>

To verify the scaling activities associated with scheduled scaling, see [Verify a scaling activity for an Auto Scaling group](as-verify-scaling-activity.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
