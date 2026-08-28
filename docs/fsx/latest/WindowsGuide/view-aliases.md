---
source_url: https://docs.aws.amazon.com/fsx/latest/WindowsGuide/view-aliases.html
---

# Viewing DNS aliases for file systems and backups
<a name="view-aliases"></a>

You can view the DNS aliases currently associated with your FSx for Windows File Server file systems and backups using the AWS Management Console, the AWS CLI, and API, as described in the following procedures.

**To view DNS aliases associated with file systems**
+ Using the console — Choose a file system to view the **File systems** detail page. Choose the **Network & security** tab to view the **DNS aliases**.
+ Using the CLI or API — Use the `describe-file-system-aliases` CLI command or the [DescribeFileSystemAliases](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileSystemAliases.html) API operation.

**To view DNS aliases associated with backups**
+ Using the console — In the navigation pane, choose **Backups**, and then choose the backup that you want to view. In the **Summary** pane, view the **DNS aliases** field.
+ Using the CLI or API — Use the `describe-backups` CLI command or the [DescribeBackups](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeBackups.html) API operation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
