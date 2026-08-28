---
source_url: https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-turn-off-database-point-in-time-backup.html
---

# Disable point-in-time backups for Lightsail databases
<a name="amazon-lightsail-turn-off-database-point-in-time-backup"></a>

Use the following procedure to disable point-in-time backups for your Lightsail managed database.

**Important**
With point-in-time backups, you can easily recover your data if your database ever fails. We recommend that you leave point in time backups enabled for your Lightsail managed database.

## Prerequisite
<a name="turn-off-database-point-in-time-backup-prerequisite"></a>

Use the AWS Command Line Interface (AWS CLI), or AWS CloudShell to enable or disable point-in-time backups for your Lightsail database. CloudShell is a browser-based, pre-authenticated shell that you can launch directly from the Lightsail console. For more information, see [Set up and configure the AWS CLI for Lightsail operations](lightsail-how-to-set-up-and-configure-aws-cli.md), and [Manage Lightsail resources with AWS CloudShell](amazon-lightsail-cloudshell.md).

## Disable database point-in-time backups
<a name="turn-off-database-point-in-time-backup"></a>

To disable the point-in-time backups for your managed database in Lightsail, you must update the database using the `update-relational-database` Lightsail command of the AWS CLI. For more information, see [update-relational-database](https://docs.aws.amazon.com/cli/latest/reference/lightsail/update-relational-database.html) in the *AWS CLI Command Reference*.
+ Enter the following command in a Terminal, Command Prompt, or CloudShell window:

  ```
  aws lightsail update-relational-database --region {{Region}} --relational-database-name {{DatabaseName}} --disable-backup-retention --apply-immediately
  ```

  The `--disable-backup-retention` value in the command turns off the point-in-time backup for the specified database. In the command, replace:
  + {{DatabaseName}} with the name of your database.
  + {{Region}} with the AWS Region of your database.

You should see an operation response with a status of `Succeeded`. The status of your database will change to **Modifying** for a short period of time while it's being updated. When the status of your database changes back to **Available**, the point-in-time restore options will be disabled as shown in the following example.

![AWS CLI command to disable point-in-time backup.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/database-disable-backup-output-cli.png)

**Note**
To enable the point-in-time backup, run the same command listed earlier but with the `--enable-backup-retention` parameter instead.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
