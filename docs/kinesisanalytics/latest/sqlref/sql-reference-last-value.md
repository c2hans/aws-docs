---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-last-value.html
---

# LAST\_VALUE
<a name="sql-reference-last-value"></a>

```
LAST_VALUE ( <value-expression> )  OVER <window-specification>
```

LAST\_VALUE returns the evaluation of the <value expression> from the last row that qualifies for the aggregate.

| Null Treatment Option | Effect |
| --- | --- |
| LAST\_VALUE(x) IGNORE NULLS OVER <window-specification> | Returns last non null value of x in <window-specification> |
| LAST\_VALUE(x) RESPECT NULLS OVER <window-specification> | Returns last value, including null of x in <window-specification> |
| LAST\_VALUE(x) OVER <window-specification> | Returns last value, including null of x in <window-specification> |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
