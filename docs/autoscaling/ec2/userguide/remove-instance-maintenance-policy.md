---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/remove-instance-maintenance-policy.html
---

# Remove an instance maintenance policy
<a name="remove-instance-maintenance-policy"></a>

If you want to stop using an instance maintenance policy with your Auto Scaling group, you can remove it.

------
#### [ Console ]

**To remove an instance maintenance policy (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. On the navigation bar at the top of the screen, choose the AWS Region that you created your Auto Scaling group in.

1. Select the check box next to the Auto Scaling group.

   A split pane opens up in the bottom of the page.

1. On the **Details** tab, choose **Instance maintenance policy**, **Edit**.

1. Choose **No instance maintenance policy**.

1. Choose **Update**.

------
#### [ AWS CLI ]

**To remove an instance maintenance policy (AWS CLI)**
Add the `--instance-maintenance-policy` option to the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command. The following example removes the instance maintenance policy from the specified Auto Scaling group.

```
aws autoscaling update-auto-scaling-group --auto-scaling-group-name {{my-asg}} \
  --instance-maintenance-policy '{
      "MinHealthyPercentage": -1,
      "MaxHealthyPercentage": -1
    }'
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
