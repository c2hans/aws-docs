---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/disable_PITR.html
---

# Turn off PITR for an Amazon Keyspaces table
<a name="disable_PITR"></a>

You can turn off PITR for an Amazon Keyspaces table at any time using the console, CQL, or the AWS CLI.

**Important**
Disabling PITR deletes your backup history immediately, even if you reenable PITR on the table within 35 days.

To learn how to restore a table, see [Restore a table from backup to a specified point in time in Amazon Keyspaces](restoretabletopointintime.md).

------
#### [ Console ]

**Disable PITR for a table using the console**

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home).

1. In the navigation pane, choose **Tables** and select the table you want to edit.

1. On the **Backups** tab, choose **Edit**.

1. In the **Edit point-in-time recovery settings** section, clear the **Enable Point-in-time recovery** check box.

1. Choose **Save changes**.

------
#### [ Cassandra Query Language (CQL) ]

**Disable PITR for a table using CQL**
+ To disable PITR for an existing table, run the following CQL command.

  ```
  ALTER TABLE {{mykeyspace.mytable}}
  WITH custom_properties = {'point_in_time_recovery': {'status': 'disabled'}}
  ```

------
#### [ CLI ]

**Disable PITR for a table using the AWS CLI**
+ To disable PITR for an existing table, run the following AWS CLI command.

  ```
  aws keyspaces update-table --keyspace-name 'myKeyspace' --table-name 'myTable' --point-in-time-recovery 'status=DISABLED'
  ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
