---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html
---

# Monitoring Amazon Aurora log files
<a name="USER_LogAccess"></a>

Every RDS database engine generates logs that you can access for auditing and troubleshooting. The type of logs depends on your database engine.

You can access database logs for DB instances using the AWS Management Console, the AWS Command Line Interface (AWS CLI), or the Amazon RDS API. You can't view, watch, or download transaction logs.

**Note**
In some cases, logs contain hidden data. Therefore, the AWS Management Console might show content in a log file, but the log file might be empty when you download it.

**Topics**
+ [Viewing and listing database log files](USER_LogAccess.Procedural.Viewing.md)
+ [Downloading a database log file](USER_LogAccess.Procedural.Downloading.md)
+ [Watching a database log file](USER_LogAccess.Procedural.Watching.md)
+ [Publishing database logs to Amazon CloudWatch Logs](USER_LogAccess.Procedural.UploadtoCloudWatch.md)
+ [Reading log file contents using REST](DownloadCompleteDBLogFile.md)
+ [AuroraMySQL database log files](USER_LogAccess.Concepts.MySQL.md)
+ [Aurora PostgreSQL database log files](USER_LogAccess.Concepts.PostgreSQL.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
