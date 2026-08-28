---
source_url: https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-bkup.html
---

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Work with Database Backups for AWS Elemental Conductor File
<a name="config-cond-cf-cg-bkup"></a>

**Important**
To set up database backup for the entire cluster, you need perform this setup only on the Conductor node. If you have two Conductor nodes, you need perform this setup only on the primary Conductor node.

All nodes in the cluster – Conductor and worker nodes – share the same database. The AWS Elemental Conductor File node is automatically configured to back up the database to a local disk. The following sections describe how to work with the backup.

**Topics**
+ [View Folder for Database Backups](config-cond-cf-cg-bkup-view.md)
+ [Change Folder for Database Backups](config-cond-cf-cg-bkup-change.md)
+ [Restore a Database Backup](config-cond-cf-cg-bkup-restore.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor File. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cf2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
