---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/scheduled-scaling-delete-scheduled-action.html
---

# Delete a scheduled action
<a name="scheduled-scaling-delete-scheduled-action"></a>

To delete a scheduled action, use one of the following methods:

------
#### [ Console ]

**To delete a scheduled action**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select your Auto Scaling group.

1. On the **Automatic scaling** tab, in **Scheduled actions**, select a scheduled action.

1. Choose **Actions**, **Delete**.

1. When prompted for confirmation, choose **Yes, Delete**.

------
#### [ AWS CLI ]

Use the following [delete-scheduled-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-scheduled-action.html) command.

```
aws autoscaling delete-scheduled-action --auto-scaling-group-name {{my-asg}} \
  --scheduled-action-name {{my-recurring-action}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
