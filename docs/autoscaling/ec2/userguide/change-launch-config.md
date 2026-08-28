---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/change-launch-config.html
---

# Change the launch configuration for an Auto Scaling group
<a name="change-launch-config"></a>

**Important**
We provide information about launch configurations for customers who have not yet migrated from launch configurations to launch templates. For information about migrating your Auto Scaling groups to launch templates, see [Migrate your Auto Scaling groups to launch templates](migrate-to-launch-templates.md).

This topic describes how to associate a different launch configuration with your Auto Scaling group.

After you change the launch configuration, any new instances are launched using the new configuration options, but existing instances are not affected. For more information, see [Update Auto Scaling instances](update-auto-scaling-group.md#update-auto-scaling-instances).

**To change the launch configuration for an Auto Scaling group (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the left navigation pane, under **Auto Scaling**, choose **Auto Scaling Groups**.

1. Select the check box next to the Auto Scaling group.

   A split pane opens up in the bottom of the page.

1. On the **Details** tab, choose **Launch configuration**, **Edit**.

1. For **Launch configuration**, choose the launch configuration.

1. When you have finished, choose **Update**.

**To change the launch configuration for an Auto Scaling group using the command line**

You can use one of the following commands:
+ [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) (AWS CLI)
+ [Update-ASAutoScalingGroup](https://docs.aws.amazon.com/powershell/latest/reference/items/Update-ASAutoScalingGroup.html) (AWS Tools for Windows PowerShell)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
