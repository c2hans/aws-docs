---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.DBMail.Delete.html
---

# Deleting messages
<a name="SQLServer.DBMail.Delete"></a>

You use the `rds_sysmail_delete_mailitems_sp` stored procedure to delete messages.

**Note**
RDS automatically deletes mail table items when DBMail history data reaches 1 GB in size, with a retention period of at least 24 hours.
If you want to keep mail items for a longer period, you can archive them. For more information, see [Create a SQL Server Agent job to archive Database Mail messages and event logs](https://docs.microsoft.com/en-us/sql/relational-databases/database-mail/create-a-sql-server-agent-job-to-archive-database-mail-messages-and-event-logs) in the Microsoft documentation.

**To delete all email messages**
+ Use the following SQL statement.

  ```
  DECLARE @GETDATE datetime
  SET @GETDATE = GETDATE();
  EXECUTE msdb.dbo.rds_sysmail_delete_mailitems_sp @sent_before = @GETDATE;
  GO
  ```

**To delete all email messages with a particular status**
+ Use the following SQL statement to delete all failed messages.

  ```
  DECLARE @GETDATE datetime
  SET @GETDATE = GETDATE();
  EXECUTE msdb.dbo.rds_sysmail_delete_mailitems_sp @sent_status = 'failed';
  GO
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
