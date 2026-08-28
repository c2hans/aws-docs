---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-current-time.html
---

# CURRENT\_TIME
<a name="sql-reference-current-time"></a>

Returns the current Amazon Kinesis Data Analytics system time when the query executes. Time is in UTC, not the local time zone.

For more information, see [CURRENT\_TIMESTAMP](sql-reference-current-timestamp.md), [LOCALTIMESTAMP](sql-reference-local-timestamp.md), [LOCALTIME](sql-reference-localtime.md), [CURRENT\_ROW\_TIMESTAMP](sql-reference-current-row-timestamp.md), and [CURRENT\_DATE](sql-reference-current-date.md).

## Example
<a name="sql-reference-current-time-example"></a>

```
+---------------+
| CURRENT_TIME  |
+---------------+
| 20:52:05      |
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
