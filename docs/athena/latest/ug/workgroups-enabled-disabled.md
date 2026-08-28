---
source_url: https://docs.aws.amazon.com/athena/latest/ug/workgroups-enabled-disabled.html
---

# Enable or disable a workgroup
<a name="workgroups-enabled-disabled"></a>

If you have permissions to do so, you can enable or disable workgroups in the console, by using the API operations, or with the JDBC and ODBC drivers.

**To enable or disable a workgroup**

1. In the Athena console navigation pane, choose **Workgroups**.

1. On the **Workgroups** page, choose the link for the workgroup.

1. On the upper right, choose **Enable workgroup** or **Disable workgroup**.

1. At the confirmation prompt, choose **Enable** or **Disable**. If you disable a workgroup, its users cannot run queries in it, or create new named queries. If you enable a workgroup, users can use it to run queries.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
