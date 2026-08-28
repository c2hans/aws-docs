---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-sys-log-parse.html
---

# SYS\_LOG\_PARSE
<a name="sql-reference-sys-log-parse"></a>

Parses the standard syslog format:

```
 Mon DD HH:MM:SS server message
```

SYS\_LOG\_PARSE processes entries commonly found in UNIX/Linux system logs. System log entries start with a timestamp and are followed with a free form text field. SYS\_LOG\_PARSE output consists of two columns. The first column is named "COLUMN1" and is SQL data type TIMESTAMP. The second column is named "COLUMN2" and is SQL type VARCHAR().

**Note**
For more information about SYSLOG, see [IETF RFC3164](https://tools.ietf.org/html/rfc3164). For more information about date-time patterns and matching, see [Date and Time Patterns](sql-reference-parse-timestamp-format.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
