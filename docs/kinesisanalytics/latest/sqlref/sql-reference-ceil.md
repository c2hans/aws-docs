---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-ceil.html
---

# CEIL / CEILING
<a name="sql-reference-ceil"></a>

```
 CEIL | CEILING ( <number-expression> )
 CEIL | CEILING ( <datetime-expression> TO <time-unit> )
 CEIL | CEILING ( <number-expression> )
 CEIL | CEILING ( <datetime-expression> TO <[[time-unit> )
```

When called with a numeric argument, CEILING returns the smallest integer equal to or larger than the input argument.

When called with a date, time, or timestamp expression, CEILING returns the smallest value equal to or larger than the input, subject to the precision specified by the <time unit>.

Returns null if any input argument is null.

## Examples
<a name="sql-reference-ceil-examples"></a>

| Function | Result |
| --- | --- |
| CEIL(2.0) | 2 |
| CEIL(-1.0) | -1 |
| CEIL(5.2) | 6 |
| CEILING(-3.3) | -3 |
| CEILING(-3 \* 3.1) | -9 |
| CEILING(TIMESTAMP '2004-09-30 13:48:23' TO HOUR) | TIMESTAMP '2004-09-30 14:00:00' |
| CEILING(TIMESTAMP '2004-09-30 13:48:23' TO MINUTE) | TIMESTAMP '2004-09-30 13:49:00' |
| CEILING(TIMESTAMP '2004-09-30 13:48:23' TO DAY) | TIMESTAMP '2004-10-01 00:00:00.0' |
| CEILING(TIMESTAMP '2004-09-30 13:48:23' TO YEAR) | TIMESTAMP '2005-01-01 00:00:00.0' |

## Notes
<a name="sqlrf_ceil_notes"></a>
+ CEIL and CEILING are synonyms for this function provided by the SQL:2008 standard.
+ CEIL(<datetime value expression> TO <time unit>) is an Amazon Kinesis Data Analytics extension.
+ For more information, see [FLOOR](sql-reference-floor.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
