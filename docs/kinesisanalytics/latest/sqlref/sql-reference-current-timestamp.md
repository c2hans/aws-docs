---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-current-timestamp.html
---

# CURRENT\_TIMESTAMP
<a name="sql-reference-current-timestamp"></a>

Returns the current database system timestamp (as defined on the environment on which Amazon Kinesis Data Analytics is running) as a datetime value.

For more information, see [CURRENT\_TIME](sql-reference-current-time.md), [CURRENT\_DATE](sql-reference-current-date.md), [LOCALTIME](sql-reference-localtime.md), [LOCALTIMESTAMP](sql-reference-local-timestamp.md),  and [CURRENT\_ROW\_TIMESTAMP](sql-reference-current-row-timestamp.md).

## Example
<a name="current-timestamp-example"></a>

```
+--------------------+
| CURRENT_TIMESTAMP  |
+--------------------+
| 20:52:05           |
+--------------------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
