---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.LastFailover.html
---

# Determining the last failover time for Amazon RDS for SQL Server
<a name="Appendix.SQLServer.CommonDBATasks.LastFailover"></a>

To determine the last failover time, use the following stored procedure:

```
execute msdb.dbo.rds_failover_time;
```

This procedure returns the following information.

| Output parameter | Description |
| --- | --- |
| errorlog\_available\_from | Shows the time from when error logs are available in the log directory. |
| recent\_failover\_time | Shows the last failover time if it's available from the error logs. Otherwise it shows `null`. |

**Note**
The stored procedure searches all of the available SQL Server error logs in the log directory to retrieve the most recent failover time. If the failover messages have been overwritten by SQL Server, then the procedure doesn't retrieve the failover time.

**Example of no recent failover**
This example shows the output when there is no recent failover in the error logs. No failover has happened since 2020-04-29 23:59:00.01.

| errorlog\_available\_from | recent\_failover\_time |
| --- | --- |
| 2020-04-29 23:59:00.0100000 | null |

**Example of recent failover**
This example shows the output when there is a failover in the error logs. The most recent failover was at 2020-05-05 18:57:51.89.

| errorlog\_available\_from | recent\_failover\_time |
| --- | --- |
| 2020-04-29 23:59:00.0100000 | 2020-05-05 18:57:51.8900000 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
