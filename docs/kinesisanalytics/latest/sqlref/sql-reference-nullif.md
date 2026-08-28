---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-nullif.html
---

# NULLIF
<a name="sql-reference-nullif"></a>

```
NULLIF ( <value-expression>, <value-expression> )
```

Returns null if the two input arguments are equal, otherwise returns the first value. Both arguments must be of comparable type, or an exception is raised.

## Examples
<a name="sql-reference-nullif-examples"></a>

| Function | Result |
| --- | --- |
| NULLIF(4,2) | 4 |
| NULLIF(4,4) | <null> |
| NULLIF('amy','fred') | amy |
| NULLIF('amy', cast(null as varchar(3))) | amy |
| NULLIF(cast(null as varchar(3)),'fred') | <null> |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
