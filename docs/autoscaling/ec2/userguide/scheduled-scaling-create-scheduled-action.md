---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/scheduled-scaling-create-scheduled-action.html
---

# Create a scheduled action
<a name="scheduled-scaling-create-scheduled-action"></a>

To create a scheduled action for your Auto Scaling group, use one of the following methods:

------
#### [ Console ]

**To create a scheduled action**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to your Auto Scaling group.

   A split pane opens up in the bottom of the page.

1. On the **Automatic scaling** tab, in **Scheduled actions**, choose **Create scheduled action**.

1. Enter a **Name** for the scheduled action.

1. For **Desired capacity**, **Min**, **Max**, choose the new desired capacity of the group and the new minimum and maximum size limits. The desired capacity must be equal to or greater than the minimum group size, and equal to or less than the maximum group size.

1. For **Recurrence**, choose one of the available options.
   + If you want to scale on a recurring schedule, choose how often Amazon EC2 Auto Scaling should run the scheduled action.
     + If you choose an option that begins with **Every**, the cron expression is created for you.
     + If you choose **Cron**, enter a cron expression that specifies when to perform the action.
   + If you want to scale only once, choose **Once**.

1. For **Time zone**, choose a time zone. The default is `Etc/UTC`.

   All of the time zones listed are from the IANA Time Zone database. For more information, see [https://en.wikipedia.org/wiki/List\_of\_tz\_database\_time\_zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

1. Define a date and time for **Specific start time**.
   + If you chose a recurring schedule, the start time defines when the first scheduled action in the recurring series runs.
   + If you chose **Once** as the recurrence, the start time defines the date and time for the schedule action to run.

1.  (Optional) For recurring schedules, you can specify an end time by choosing **Set End Time** and then choosing a date and time for **End by**.

1. Choose **Create**. The console displays the scheduled actions for the Auto Scaling group.

------
#### [ AWS CLI ]

To create a scheduled action, you can use one of the following example commands. Replace each {{user input placeholder}} with your own information.

**Example: To scale one time only**
Use the following [put-scheduled-update-group-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-scheduled-update-group-action.html) command with the `--start-time "YYYY-MM-DDThh:mm:ssZ"` and `--desired-capacity` options.

```
aws autoscaling put-scheduled-update-group-action --scheduled-action-name {{my-one-time-action}} \
  --auto-scaling-group-name {{my-asg}} --start-time "{{2021-03-31T08:00:00Z}}" --desired-capacity {{3}}
```

**Example: To schedule scaling on a recurring schedule**
Use the following [put-scheduled-update-group-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-scheduled-update-group-action.html) command with the `--recurrence "cron expression"` and `--desired-capacity` options.

```
aws autoscaling put-scheduled-update-group-action --scheduled-action-name {{my-recurring-action}} \
  --auto-scaling-group-name {{my-asg}} --recurrence "{{0 9 * * *}}" --desired-capacity {{3}}
```

By default, Amazon EC2 Auto Scaling runs the specified recurrence schedule based on the UTC time zone. To specify a different time zone, include the `--time-zone` option and the name of the IANA time zone, as in the following example.

```
--time-zone "{{America/New_York}}"
```

For more information, see [https://en.wikipedia.org/wiki/List\_of\_tz\_database\_time\_zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
