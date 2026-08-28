---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/userguide/uninstalling-jira.html
---

# Uninstalling the connector
<a name="uninstalling-jira"></a>

 To fully uninstall the AWS Well-Architected Tool Connector for Jira, perform the following tasks:
+  Turn off Jira sync in any workloads that override account-level sync settings
+  Turn off Jira sync at the account level
+  Unlink your AWS account in Jira
+  Uninstall the connector from your Jira account

**To turn off the connector at the account level**
**Note**
 The following steps are performed in your AWS account.

1.  Select **Settings** in the left navigation pane.

1.  In the **Jira account syncing** section, choose **Edit**.

1.  Clear the **Turn on Jira account syncing** option.

1.  Choose **Save settings**.

**To unlink an AWS account**
**Note**
 All of the following steps are performed in your Jira account, not in your AWS account.

1.  Log in to your Jira account.

1.  In the top navigation bar, choose **Apps**, then select **Manage your apps**.

1.  Choose the dropdown arrow next to **AWS Well-Architected Tool Connector for Jira**, then choose **Configure**.

1.  In the AWS Well-Architected Tool Configuration pane, to unlink an AWS account, choose **X** under **Actions**.

**To uninstall the connector**
**Note**
 All of the following steps are performed in your Jira account, not in your AWS account.
 We recommend verifying that all connected AWS accounts are unlinked in the configuration of the connector prior to uninstalling the connector.

1.  Log in to your Jira account.

1.  In the top navigation bar, choose **Apps**, then select **Manage your apps**.

1.  Choose the dropdown arrow next to **AWS Well-Architected Tool Connector for Jira**.

1.  Choose **Uninstall**, then choose **Uninstall app**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
