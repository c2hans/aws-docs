---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.DBMail.View.html
---

# Viewing messages, logs, and attachments
<a name="SQLServer.DBMail.View"></a>

You use RDS stored procedures to view messages, event logs, and attachments.

**To view all email messages**
+ Use the following SQL query.

  ```
  SELECT * FROM msdb.dbo.rds_fn_sysmail_allitems(); --WHERE sent_status='sent' or 'failed' or 'unsent'
  ```

**To view all email event logs**
+ Use the following SQL query.

  ```
  SELECT * FROM msdb.dbo.rds_fn_sysmail_event_log();
  ```

**To view all email attachments**
+ Use the following SQL query.

  ```
  SELECT * FROM msdb.dbo.rds_fn_sysmail_mailattachments();
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
