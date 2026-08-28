---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-mod.html
---

# MOD
<a name="sql-reference-mod"></a>

```
MOD ( <dividend>, <divisor> )
 <dividend> := <integer-expression>
 <divisor>  := <integer-expression>
```

Returns the remainder when the first argument (the dividend is divided by the second numeric argument (the divisor). If the divisor is zero, a divide by zero error is raised.

## Examples
<a name="sqlrf-mod-examples"></a>

| Function | Result |
| --- | --- |
| MOD(4,2) | 0 |
| MOD(5,3) | 2 |
| MOD(-4,3) | -1 |
| MOD(5,12) | 5 |

## Limitations
<a name="sqlrf-mod-limitations"></a>

The Amazon Kinesis Data Analytics MOD function only supports arguments of scale 0 (integers). This is a departure from the SQL:2008 standard, which supports any numeric argument. Other numeric arguments can be CAST to an integer, of course.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
