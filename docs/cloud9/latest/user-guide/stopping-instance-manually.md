---
source_url: https://docs.aws.amazon.com/cloud9/latest/user-guide/stopping-instance-manually.html
---

 AWS Cloud9 is no longer available to new customers. Existing customers of AWS Cloud9 can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/)

# Manually stopping your environment's EC2 instance
<a name="stopping-instance-manually"></a>

The [EC2 Instance](settings-project-change.md#settings-project-change-ec2-instance) setting allows you to automatically stop your environment's Amazon EC2 instance as quickly as 30 minutes after you close all web browser instances that are connected to the IDE.

You also can manually stop the instance immediately using the console.

To manually stop an environment's EC2 instance, choose the following steps:

1. After you closed all web browser instances that are connected to the IDE, choose **Your environments** in the AWS Cloud9 console.

1. Choose the button in the top-right of the pane that shows details of the environment that you were using, and choose **View details**.

1. In **Environment details**, under **EC2 Instance**, choose **Go To Instance**.

1. In the Amazon EC2 console, under **Instance state**, choose the check box to select your environment's instance. The **Instance state** might indicate that the instance is still running.

1. Choose **Instance state** and select **Stop instance**.

1. When prompted for confirmation, choose **Stop**. It can take a few minutes for the instance to stop.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud9. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud9` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
