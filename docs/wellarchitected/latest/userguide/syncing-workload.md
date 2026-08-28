---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/userguide/syncing-workload.html
---

# Syncing a workload
<a name="syncing-workload"></a>

 For Automatic syncing, the connector automatically syncs improvement items when you update a workload (for example, when you complete a question or select a new best practice).

 In both Manual and Automatic syncing, any changes made in Jira (like completing a question or best practice) are synced back to AWS Well-Architected Tool.

**To manually sync a workload**

1.  When you are ready to sync your workload to Jira, select **Workloads** in the left navigation pane. Then, select the workload you want to sync.

1.  In the workload overview, choose **Sync with Jira**.

1.  Select the lens you want to sync.

1.  For **Questions to sync to Jira**, select the questions or entire pillars you want to sync to the Jira project.

   1.  For any questions you want to remove, select the **X** icon next to the question title.

1.  Choose **Sync**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
