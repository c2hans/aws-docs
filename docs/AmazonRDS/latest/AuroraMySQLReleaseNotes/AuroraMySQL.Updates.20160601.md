---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.20160601.html
---

# Aurora MySQL database engine updates: 2016-06-01 (version 1.6.5) (Deprecated)
<a name="AuroraMySQL.Updates.20160601"></a>

**Version:** 1.6.5

## New features
<a name="AuroraMySQL.Updates.20160601.New"></a>
+ **Efficient storage of Binary Logs** – Efficient storage of binary logs is now enabled by default for all Aurora MySQL DB clusters, and is not configurable. Efficient storage of binary logs was introduced in the April 2016 update. For more information, see [Aurora MySQL database engine updates: 2016-04-06 (version 1.6) (Deprecated)](AuroraMySQL.Updates.20160406.md).

## Improvements
<a name="AuroraMySQL.Updates.20160601.Improvements"></a>
+ Improved stability for Aurora Replicas when the primary instance is encountering a heavy workload.
+ Improved stability for Aurora Replicas when running queries on partitioned tables and tables with special characters in the table name.
+ Fixed connection issues when using secure connections.

## Integration of MySQL bug fixes
<a name="AuroraMySQL.Updates.20160601.BugFixes"></a>
+ SLAVE CAN'T CONTINUE REPLICATION AFTER MASTER'S CRASH RECOVERY (Port Bug \#17632285)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
