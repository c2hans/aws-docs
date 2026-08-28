---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth-enable.html
---

# Enabling IAM database authentication in Amazon Neptune
<a name="iam-auth-enable"></a>

By default, IAM database authentication is disabled when you create an Amazon Neptune DB cluster. You can enable IAM database authentication (or disable it again) using the AWS Management Console.

To create a new Neptune DB cluster with IAM authentication by using the console, follow the instructions for creating a Neptune DB cluster in [Launching a Neptune DB cluster using the AWS Management Console](manage-console-launch-console.md).

During the creation process, under **Additional settings**, choose **Turn on IAM Authentication**.

**To enable or disable IAM authentication for an existing DB instance or cluster**

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home).

1. In the navigation pane, choose **Clusters**.

1. Choose the Neptune DB cluster that you want to modify, and then choose **Modify**.

1. Under **Additional settings**, for **IAM DB Authentication**, choose either **Turn on IAM Authentication** or **Turn off IAM Authentication** (to disable). Then choose **Next**.

1. Under **Scheduling of modifications**, choose when to apply the change, and then choose **Submit**.

**Important**
Enabling or disabling IAM database authentication causes the DB engine to restart. This restart terminates all existing connections to the cluster and causes a brief interruption in availability. Plan to make this change during a maintenance window or at a time when the impact of a connection interruption is minimal.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
