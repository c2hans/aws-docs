---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-first-value.html
---

# FIRST\_VALUE
<a name="sql-reference-first-value"></a>

```
FIRST_VALUE( <value-expression>) <null treatment> OVER <window-specification>
```

FIRST\_VALUE returns the evaluation of the <value expression> from the first row that qualifies for the aggregate. FIRST\_VALUE requires the OVER clause, and is considered an [Analytic Functions](sql-reference-analytic-functions.md). FIRST\_VALUE has a null treatment option defined in the following table.

| Null treatment option | Effect |
| --- | --- |
| FIRST\_VALUE(x) IGNORE NULLS OVER <window-specification> | Returns first non null value of x in <window-specification> |
| FIRST\_VALUE(x) RESPECT NULLS OVER <window-specification> | Returns first value, including null of x in <window-specification> |
| FIRST\_VALUE(x) OVER <window-specification> | Returns first value, including null of x in <window-specification> |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
