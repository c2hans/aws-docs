---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/enable-default-instance-warmup.html
---

# Enable the default instance warmup for a group
<a name="enable-default-instance-warmup"></a>

You can enable the default instance warmup when you create an Auto Scaling group. You can also enable it for existing groups.

By enabling the default instance warmup feature, you no longer have to specify values for warmup parameters for the following features:
+ [Instance refresh](instance-refresh-overview.md#instance-refresh-core-concepts)
+ [Target tracking scaling](as-scaling-target-tracking.md#as-target-tracking-scaling-warmup)
+ [Step scaling](as-scaling-simple-step.md#as-step-scaling-warmup)

------
#### [ Console ]

**To enable the default instance warmup for a new group (console)**
When you create the Auto Scaling group, on the **Configure advanced options** page, under **Additional settings**, select the **Enable default instance warmup** option. Choose the warmup time that you need for your application.

------
#### [ AWS CLI ]

**To enable the default instance warmup for a new group (AWS CLI)**
To enable the default instance warmup for an Auto Scaling group, add the `--default-instance-warmup` option and specify a value, in seconds, from 0 to 3600. After it's enabled, a value of `-1` will turn this setting off.

The following [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command creates an Auto Scaling group with the name {{my-asg}} and enables the default instance warmup with a value of {{120}} seconds.

```
aws autoscaling create-auto-scaling-group --auto-scaling-group-name {{my-asg}} --default-instance-warmup {{120}} ...
```

**Tip**
If this command throws an error, make sure that you have updated the AWS CLI locally to the latest version.

------

------
#### [ Console ]

**To enable the default instance warmup for an existing group (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. On the navigation bar at the top of the screen, choose the AWS Region that you created your Auto Scaling group in.

1. Select the check box next to the Auto Scaling group.

   A split pane opens up in the bottom of the page.

1. On the **Details** tab, choose **Advanced configurations**, **Edit**.

1. For **Default instance warmup**, choose the warmup time that you need for your application.

1. Choose **Update**.

------
#### [ AWS CLI ]

**To enable the default instance warmup for an existing group (AWS CLI)**
The following example uses the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command to enable the default instance warmup with a value of {{120}} seconds for an existing Auto Scaling group named {{my-asg}}.

```
aws autoscaling update-auto-scaling-group --auto-scaling-group-name {{my-asg}} --default-instance-warmup {{120}}
```

**Tip**
If this command throws an error, make sure that you have updated the AWS CLI locally to the latest version.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
