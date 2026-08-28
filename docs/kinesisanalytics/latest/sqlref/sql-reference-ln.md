---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-ln.html
---

# LN
<a name="sql-reference-ln"></a>

```
LN ( <number-expression> )
```

Returns the natural log (that is, the log with respect to base e) of the input argument. If the argument is negative or 0, an exception is raised. Returns null if the input argument is null.

For more information, see [LOG10](sql-reference-log10.md) and [EXP](sql-reference-exp.md).

## Examples
<a name="sql-reference-ln-examples"></a>

| Function | Result |
| --- | --- |
| LN(1) | 0.0 |
| LN(10) | 2.302585092994046 |
| LN(2.5) | 0.9162907318741551 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
