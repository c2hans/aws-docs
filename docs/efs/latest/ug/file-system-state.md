---
source_url: https://docs.aws.amazon.com/efs/latest/ug/file-system-state.html
---

# Understanding file system status
<a name="file-system-state"></a>

You can view the status of Amazon EFS file systems using the Amazon EFS console or the AWS CLI. An Amazon EFS file system can have one of the status values described in the following table.

| File system state  | Description |
| --- | --- |
| AVAILABLE | The file system is in a healthy state, and is reachable and available for use. |
| CREATING | Amazon EFS is in the process of creating the new file system. |
| DELETING | Amazon EFS is deleting the file system in response to a user-initiated delete request. For more information, see [Deleting EFS file systems](delete-efs-fs.md).  |
| DELETED | Amazon EFS has deleted the file system in response to a user-initiated delete request. For more information, see [Deleting EFS file systems](delete-efs-fs.md).  |
| UPDATING | The file system is undergoing an update in response to a user-initiated update request. |
| ERROR | Applicable for One Zone file systems, including file systems in a replication configuration.<br />The file system is in a failed state and is unrecoverable. To access the file system data, restore a backup of this file system to a new file system. For more information, see [Backing up and replicating data in Amazon EFS](backup-replication.md) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic File System (EFS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query efs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
