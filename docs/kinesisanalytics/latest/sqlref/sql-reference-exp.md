---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-exp.html
---

# EXP
<a name="sql-reference-exp"></a>

```
EXP ( <number-expression> )
```

Returns the value of e (approximately 2.7182818284590455) raised to the power of the input argument. Returns null if the input argument is null.

## Examples
<a name="sqlrf-exp-examples"></a>

| Function | Result |
| --- | --- |
| EXP(1) | 2.7182818284590455 |
| EXP(0) | 1.0 |
| EXP(-1) | 0.36787944117144233 |
| EXP(10) | 22026.465794806718 |
| EXP(2.5) | 12.182493960703473 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
