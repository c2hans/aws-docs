---
source_url: https://docs.aws.amazon.com/snowball/latest/developer-guide/terminate-instance.html
---

AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

# Terminating an Amazon EC2-compatible instance with AWS OpsHub
<a name="terminate-instance"></a>

After you terminate an Amazon EC2-compatible instance, you can't restart the instance.

**To terminate an Amazon EC2-compatible instance**

1. Open the AWS OpsHub application.

1. In the **Start computing** section on the dashboard, choose **Get started**. Or, choose the **Services** menu at the top, and then choose **Compute (EC2)** to open the **Compute** page. You can see all your compute resources in the **Resources** section.

1. In the **Instance name** column, under **Instances**, find the instance that you want to terminate.

1. Choose the instance, and choose the **Actions**menu. From the **Actions** menu, choose **Terminate**.
![Instances tab showing instance chose and Actions menu showing Terminate chosen.](http://docs.aws.amazon.com/snowball/latest/developer-guide/images/opshub-instance-terminate-console.png)

1. In the **Terminate instances window, choose **Confirm terminate****.
![Terminate instances window showing instance name and Confirm terminate button.](http://docs.aws.amazon.com/snowball/latest/developer-guide/images/opshub-instance-terminate-instances-console.png)
**Note**
After the instance is terminated, you can't restart it.

   The **State** changes to **Terminating**, and then to **Terminated** when done.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball Edge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
