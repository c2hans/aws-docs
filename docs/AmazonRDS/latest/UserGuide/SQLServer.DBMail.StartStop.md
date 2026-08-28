---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.DBMail.StartStop.html
---

# Starting and stopping mail queue
<a name="SQLServer.DBMail.StartStop"></a>

Use the following instructions to start and stop the DB mail queue:

**Topics**
+ [Starting the mail queue](#SQLServer.DBMail.Start)
+ [Stopping the mail queue](#SQLServer.DBMail.Stop)

## Starting the mail queue
<a name="SQLServer.DBMail.Start"></a>

You use the `rds_sysmail_control` stored procedure to start the Database Mail process.

**Note**
Enabling Database Mail automatically starts the mail queue.

**To start the mail queue**
+ Use the following SQL statement.

  ```
  EXECUTE msdb.dbo.rds_sysmail_control start;
  GO
  ```

## Stopping the mail queue
<a name="SQLServer.DBMail.Stop"></a>

You use the `rds_sysmail_control` stored procedure to stop the Database Mail process.

**To stop the mail queue**
+ Use the following SQL statement.

  ```
  EXECUTE msdb.dbo.rds_sysmail_control stop;
  GO
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
