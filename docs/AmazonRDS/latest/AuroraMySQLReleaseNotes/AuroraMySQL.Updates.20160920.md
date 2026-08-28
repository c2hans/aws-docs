---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.20160920.html
---

# Aurora MySQL database engine updates: 2016-09-20 (version 1.7.1) (Deprecated)
<a name="AuroraMySQL.Updates.20160920"></a>

**Version:** 1.7.1

## Improvements
<a name="AuroraMySQL.Updates.20160920.Improvements"></a>
+ Fixes an issue where an Aurora Replica crashes if the InnoDB full-text search cache is full.
+ Fixes an issue where the database engine crashes if a worker thread in the thread pool waits for itself.
+ Fixes an issue where an Aurora Replica crashes if a metadata lock on a table causes a deadlock.
+ Fixes an issue where the database engine crashes due to a race condition between two worker threads in the thread pool.
+ Fixes an issue where an unnecessary failover occurs under heavy load if the monitoring agent doesn't detect the advancement of write operations to the distributed storage subsystem.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
