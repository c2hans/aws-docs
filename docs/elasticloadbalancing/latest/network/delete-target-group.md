---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/network/delete-target-group.html
---

# Delete a target group for your Network Load Balancer
<a name="delete-target-group"></a>

You can delete a target group if it is not referenced by the forward actions of any listener rules. Deleting a target group does not affect the targets registered with the target group. If you no longer need a registered EC2 instance, you can stop or terminate it.

------
#### [ Console ]

**To delete a target group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, under **Load Balancing**, choose **Target Groups**.

1. Select the target group and choose **Actions**, **Delete**.

1. Choose **Delete**.

------
#### [ AWS CLI ]

**To delete a target group**
Use the [delete-target-group](https://docs.aws.amazon.com/cli/latest/reference/elbv2/delete-target-group.html) command.

```
aws elbv2 delete-target-group \
    --target-group-arn {{target-group-arn}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
