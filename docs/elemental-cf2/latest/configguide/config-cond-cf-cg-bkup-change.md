---
source_url: https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-bkup-change.html
---

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Change Folder for Database Backups
<a name="config-cond-cf-cg-bkup-change"></a>

The default folder for backups is on the node at `/home/elemental/database_backups`.

We strongly advise that you mount a remote folder as the location for backups. In that way, if the hardware unit fails, you can restore the database from that remote folder.

**To mount a remote folder**

1. Choose a remote server in your organization and designate a folder for backups.

1. Mount that folder to the AWS Elemental Conductor File node, as described in [Add Mount Points to AWS Elemental Conductor File Nodes](config-cond-cf-cg-mount.md).

1. In **Path to Store Management** in the Conductor File's settings, type the path to the mount folder. The path will always start with `/data/mnt/`. For example: `/data/mnt/conductor1_backup`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor File. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cf2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
