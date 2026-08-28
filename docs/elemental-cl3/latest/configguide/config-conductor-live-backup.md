---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-backup.html
---

# Configuring backup and restore on Conductor Live
<a name="config-conductor-live-backup"></a>

AWS Elemental Conductor Live is configured by default to create database backups to a directory on the node. We recommend that you modify the configuration to back up to a remote server. This section describes how to modify the configuration.

The Conductor Live backup command copies the following data to a backup server: profiles, channels, MPTS outputs, nodes, and redundancy groups. Backup files are named in the following format:

`elemental-db-backup_{{yyyy}}-{{mm}}-{{dd}}_{{hh}}-{{mm}}-{{ss}}.tar.bz2`

Backup when a Conductor Live node fails

If the primary Conductor Live fails, the other Conductor Live node (the new primary) takes over backups. The new primary stores the backups in the same location as the failed primary. You don't have to manage two backup files.

**Topics**
+ [Configuring for backup](conductor-live-config-bkup.md)
+ [Disabling database backups](conductor-live-config-bkup-dis.md)
+ [Restoring a backup](conductor-live-config-bkup-restore.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
