---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-local-timestamp.html
---

# LOCALTIMESTAMP
<a name="sql-reference-local-timestamp"></a>

Returns the current timestamp as defined by the environment on Amazon Kinesis Data Analytics application is running. Time is always returned as UTC (GMT), not the local timezone.

For more information, see [CURRENT\_TIME](sql-reference-current-time.md), [CURRENT\_DATE](sql-reference-current-date.md), [CURRENT\_TIMESTAMP](sql-reference-current-timestamp.md), [LOCALTIME](sql-reference-localtime.md), and [CURRENT\_ROW\_TIMESTAMP](sql-reference-current-row-timestamp.md).

## Example
<a name="sql-reference-local-timestamp-example"></a>

```
values localtimestamp;
+--------------------------+
|      LOCALTIMESTAMP      |
+--------------------------+
| 2008-08-27 01:13:42.206  |
+--------------------------+
1 row selected (1.133 seconds)
```

## Limitations
<a name="sql-reference-local-timestamp-limitations"></a>

Amazon Kinesis Data Analytics does not support the optional <timestamp precision> parameter specified in SQL:2008. This is a departure from the SQL:2008 standard.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
