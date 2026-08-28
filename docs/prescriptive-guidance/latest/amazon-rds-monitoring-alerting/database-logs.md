---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/database-logs.html
---

# Database logs
<a name="database-logs"></a>

MySQL and MariaDB databases generate logs that you can access for auditing and troubleshooting. Those logs are:
+ [Audit](https://mariadb.com/kb/en/mariadb-audit-plugin-log-format/) – The audit trail is a set of records that log the server's activity. For each client session, it records who connected to the server (user name and host), which queries were run, which tables were accessed, and which server variables were changed.
+ [Error](https://dev.mysql.com/doc/refman/8.0/en/error-log.html) – This log contains the server's (`mysqld`) startup and shutdown times, and diagnostic messages such as errors, warnings, and notes that occur during server startup and shutdown, and while the server is running.
+ [General](https://dev.mysql.com/doc/refman/8.0/en/query-log.html) – This log records the activity of `mysqld`, including the connect and disconnect activity for each client, and SQL queries received from clients. The general query log can be very useful when you suspect an error and want to know exactly what the client sent to `mysqld`.
+ [Slow query](https://dev.mysql.com/doc/refman/8.0/en/slow-query-log.html) – This log provides a record of SQL queries that took a long time to perform.

As a best practice, you should [publish database logs from Amazon RDS to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Procedural.UploadtoCloudWatch.html). With CloudWatch Logs, you can perform real-time analysis of the log data, store the data in highly durable storage, and manage the data with the CloudWatch Logs agent. You can [access and watch your database logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Procedural.Watching.html) from the Amazon RDS console. You can also use CloudWatch Logs Insights to interactively search and analyze your log data in CloudWatch Logs. The following example illustrates a query on the audit log that checks how many times `CONNECT` events appear in the log, who connected, and which client (IP address) they connected from. The excerpt from the audit log could look like this:

```
20221201 14:07:05,ip-10-22-1-51,rdsadmin,localhost,821,0,CONNECT,,,0,SOCKET
20221201 14:07:05,ip-10-22-1-51,rdsadmin,localhost,821,0,DISCONNECT,,,0,SOCKET
20221201 14:12:20,ip-10-22-1-51,rdsadmin,localhost,822,0,CONNECT,,,0,SOCKET
20221201 14:12:20,ip-10-22-1-51,rdsadmin,localhost,822,0,DISCONNECT,,,0,SOCKET
20221201 14:17:35,ip-10-22-1-51,rdsadmin,localhost,823,0,CONNECT,,,0,SOCKET
20221201 14:17:35,ip-10-22-1-51,rdsadmin,localhost,823,0,DISCONNECT,,,0,SOCKET
20221201 14:22:50,ip-10-22-1-51,rdsadmin,localhost,824,0,CONNECT,,,0,SOCKET
20221201 14:22:50,ip-10-22-1-51,rdsadmin,localhost,824,0,DISCONNECT,,,0,SOCKET
```

The example Log Insights query shows that `rdsadmin` connected to the database from `localhost` every 5 minutes, for a total of 22 times, as shown in the following illustration. These results indicate that the activity originated from internal Amazon RDS processes such as the monitoring system itself.

![Log Insights report](http://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/images/guide-img/9dd4cf9c-a2d9-4127-a3e3-2225b43b6c9a/images/f9afe6e8-c1cd-4f73-aaf2-c15c37974173.png)

Log events frequently include important messages that you want to count, such as warnings or errors about operations associated with MySQL and MariaDB DB instances. For example, if an operation fails, an error may occur and be recorded to the error log file as follows: `ERROR 1114 (HY000): The table zip_codes is full`. You might want to monitor these entries to understand the trend of your errors. You can [create custom CloudWatch metrics from Amazon RDS logs by using filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.html) to enable automatic monitoring of Amazon RDS database logs to monitor a specific log for specific patterns, and to generate an alarm if there are violations of expected behavior. [For example](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CountOccurrencesExample.html), create a metric filter for the log group `/aws/rds/instance/database-1/error` that would monitor the error log and search for the [specific pattern](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html), such as `ERROR`. Set the **Filter Pattern** to `ERROR` and **Metric Value** to `1`. The filter will detect every log record that has the keyword `ERROR`, and it will increment the count by 1 for every log event that contains "ERROR". After you create the filter, you can set an alarm to notify you in case errors are detected in the MySQL or MariaDB error log.

To learn more about monitoring the slow query log and error log by creating a CloudWatch dashboard and using CloudWatch Logs Insights, see the blog post [ Creating an Amazon CloudWatch dashboard to monitor Amazon RDS and Amazon Aurora MySQL.](https://aws.amazon.com/blogs/database/creating-an-amazon-cloudwatch-dashboard-to-monitor-amazon-rds-and-amazon-aurora-mysql/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
