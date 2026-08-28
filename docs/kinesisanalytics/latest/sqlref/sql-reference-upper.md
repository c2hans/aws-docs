---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-upper.html
---

# UPPER
<a name="sql-reference-upper"></a>

```
< UPPER ( <character-expression> )
```

Converts a string to all upper-case characters. Returns null if the input argument is null, and the empty string if the input argument is an empty string.

## Examples
<a name="sqlrf-upper-examples"></a>

| Function | Result |
| --- | --- |
| UPPER('abcDEFghi123') | ABCDEFGHI123 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
