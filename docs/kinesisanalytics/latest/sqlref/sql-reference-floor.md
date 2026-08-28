---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-floor.html
---

# FLOOR
<a name="sql-reference-floor"></a>

```
FLOOR ( <time-unit> )
```

When called with a numeric argument, FLOOR returns the largest integer equal to or smaller than the input argument.

When called with a date, time, or timestamp expression, FLOOR returns the largest value equal to or smaller than the input, subject to the precision specified by <time unit>.

FLOOR returns null if any input argument is null.

## Examples
<a name="sqlref-floor-examples"></a>

|  Function  |  Result  |
| --- | --- |
| FLOOR(2.0) | 2 |
| FLOOR(-1.0) | -1 |
| FLOOR(5.2) | 5 |
| FLOOR(-3.3) | -4 |
| FLOOR(-3 \* 3.1) | -10 |
| FLOOR(TIMESTAMP '2004-09-30 13:48:23' TO HOUR) | TIMESTAMP '2004-09-30 13:00:00' |
| FLOOR(TIMESTAMP '2004-09-30 13:48:23' TO MINUTE) | TIMESTAMP '2004-09-30 13:48:00' |
| FLOOR(TIMESTAMP '2004-09-30 13:48:23' TO DAY) | TIMESTAMP '2004-09-30 00:00:00.0' |
| FLOOR(TIMESTAMP '2004-09-30 13:48:23' TO YEAR) | TIMESTAMP '2004-01-01 00:00:00.0' |

## Notes
<a name="sqlrf-floor-notes"></a>

**Note**
FLOOR ( <datetime expression> TO <timeunit> ) is an Amazon Kinesis Data Analytics extension.
The STEP function is similar to FLOOR but can round values down to arbitrary intervals, such as 30 seconds. For more information, see [STEP](sql-reference-step.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
