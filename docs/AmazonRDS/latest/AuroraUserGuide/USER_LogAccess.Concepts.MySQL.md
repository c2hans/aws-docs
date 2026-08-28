---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.Concepts.MySQL.html
---

# AuroraMySQL database log files
<a name="USER_LogAccess.Concepts.MySQL"></a>

You can monitor the Aurora MySQL logs directly through the Amazon RDS console, Amazon RDS API, AWS CLI, or AWS SDKs. You can also access MySQL logs by directing the logs to a database table in the main database and querying that table. You can use the mysqlbinlog utility to download a binary log.

For more information about viewing, downloading, and watching file-based database logs, see [Monitoring Amazon Aurora log files](USER_LogAccess.md).

**Topics**
+ [Overview of Aurora MySQL database logs](USER_LogAccess.MySQL.LogFileSize.md)
+ [Sending AuroraMySQL log output to tables](Appendix.MySQL.CommonDBATasks.Logs.md)
+ [Configuring Aurora MySQL binary logging](USER_LogAccess.MySQL.BinaryFormat.md)
+ [Accessing MySQL binary logs](USER_LogAccess.MySQL.Binarylog.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
