---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.CloudWatch.Monitor.html
---

# Monitoring log events in Amazon CloudWatch
<a name="AuroraPostgreSQL.CloudWatch.Monitor"></a>

With Aurora PostgreSQL log events published and available as Amazon CloudWatch Logs, you can view and monitor events using Amazon CloudWatch. For more information about monitoring, see [View log data sent to CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#ViewingLogData).

When you turn on Log exports, a new log group is automatically created using the prefix `/aws/rds/cluster/` with the name of your Aurora PostgreSQL and the log type, as in the following pattern.

```
/aws/rds/cluster/{{your-cluster-name}}/postgresql
```

As an example, suppose that an Aurora PostgreSQL DB cluster named `docs-lab-apg-small` exports its log to Amazon CloudWatch Logs. Its log group name in Amazon CloudWatch is shown following.

```
/aws/rds/cluster/docs-lab-apg-small/postgresql
```

If a log group with the specified name exists, Aurora uses that log group to export log data for the Aurora DB cluster. Each DB instance in the Aurora PostgreSQL DB cluster uploads its PostgreSQL log to the log group as a distinct log stream. You can examine the log group and its log streams using the various graphical and analytical tools available in Amazon CloudWatch.

For example, you can search for information within the log events from your Aurora PostgreSQL DB cluster, and filter events by using the CloudWatch Logs console, the AWS CLI, or the CloudWatch Logs API. For more information, [Searching and filtering log data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html) in the *Amazon CloudWatch Logs User Guide*.

By default, new log groups are created using **Never expire** for their retention period. You can use the CloudWatch Logs console, the AWS CLI, or the CloudWatch Logs API to change the log retention period. To learn more, see [Change log data retention in CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SettingLogRetention.html) in the *Amazon CloudWatch Logs User Guide*.

**Tip**
You can use automated configuration, such as AWS CloudFormation, to create log groups with predefined log retention periods, metric filters, and access permissions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
