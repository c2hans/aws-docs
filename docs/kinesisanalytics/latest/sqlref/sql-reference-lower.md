---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-lower.html
---

# LOWER
<a name="sql-reference-lower"></a>

```
LOWER ( <character-expression> )
```

Converts a string to all lower-case characters. Returns null if input argument is null, and the empty string if the input argument is an empty string.

## Examples
<a name="sql-reference-lower-examples"></a>

| Function | Result |
| --- | --- |
| LOWER('abcDEFghi123') | abcdefghi123 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
