---
source_url: https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-srvr-cg-bkup-restore.html
---

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Restore a Backup
<a name="config-wrkr-srvr-cg-bkup-restore"></a>

Follow this procedure if you ever need to restore a backed-up version of the database.

*To restore the database*

1. At your workstation, start a remote terminal session to the AWS Elemental Server hardware unit. Log in with the elemental user credentials.

1. Type the following command to identify the version of AWS Elemental Server that is currently installed.

   `[elemental@hostname ~]$ cat /opt/elemental_se/versions.txt`

   Several lines of information appear, including the version number. For example: `AWS Elemental Server (2.16.1.12345)`.

1. Run the install script with the restore option.

   `[elemental@hostname ~]$ sudo sh product `

   ` --restore-db-backup path backup-file --https`

   where:

   1. `product` is the product installer, including the version number that you obtained in the previous step: `elemental_production_server_2.16.1.12345.run`.

   1. `path` is the path to the backup file. This path could simply be the remote folder where backups were originally stored.

   1. `backup-file` is the file that you want to restore. The file is unzipped and copied to the appropriate folder. Do not unzip the file manually before restoring it\!

   1. `--https` keeps SSL enabled. If you omit this flag, SSL is disabled when you run the install script. If you don't have or don't want SSL, omit this flag.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Server. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-server` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
