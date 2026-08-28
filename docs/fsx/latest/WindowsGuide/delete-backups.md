---
source_url: https://docs.aws.amazon.com/fsx/latest/WindowsGuide/delete-backups.html
---

# Deleting backups
<a name="delete-backups"></a>

You can delete any user-initiated and automatic daily backups of your file system using the Amazon FSx console, CLI, or API, described in the following procedures. For deleting backups taken by AWS Backup, which have type of **AWS Backup**, you must use the the AWS Backup console, CLI, or API. Deleting a backup is a permanent, unrecoverable action. Any data in a deleted backup is also deleted. Do not delete a backup unless you're sure you won't need that backup again in the future.

**To delete a backup (console)**

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. From the console dashboard, choose **Backups** from the left side navigation.

1. Choose the backup that you want to delete from the **Backups** table, and then choose **Delete backup**.

1. In the **Delete backups** dialog box that opens, confirm that the ID of the backup identifies the backup that you want to delete.

1. Confirm that the check box is checked for the backup that you want to delete.

1. Choose **Delete backups**.

Your backup and all included data are now permanently and unrecoverably deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
