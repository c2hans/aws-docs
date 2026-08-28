---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-abs.html
---

# ABS
<a name="sql-reference-abs"></a>

Returns the absolute value of the input argument. Returns `null` if the input argument is null.

```
ABS ( {{<numeric-expression>}}  {{<interval-expression>}}
      )
```

## Examples
<a name="sqlrf_abs_examples"></a>

| Function | Result |
| --- | --- |
| ABS(2.0) | 2.0 |
| ABS(-1.0) | 1.0 |
| ABS(0) | 0 |
| ABS(-3 \* 3) | 9 |
| ABS(INTERVAL '-3 4:20' DAY TO MINUTE) | INTERVAL '3 4:20' DAY TO MINUTE |

If you use `cast as VARCHAR` in SQLline to show the output, the value is returned as `+3 04:20`.

```
 values(cast(ABS(INTERVAL '-3 4:20' DAY TO MINUTE) AS VARCHAR(8)));
  +-----------+
    EXPR$0
  +-----------+
   +3 04:20
  +-----------+
  1 row selected
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
