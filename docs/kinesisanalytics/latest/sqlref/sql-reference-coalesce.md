---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-coalesce.html
---

# COALESCE
<a name="sql-reference-coalesce"></a>

```
COALESCE (
      <value-expression>
      {,<value-expression>}... )
```

The COALESCE function takes a list of expressions (all of which must be of the same type) and returns the first non-null argument from the list. If all of the expressions are null, COALESCE returns null.

## Examples
<a name="sql-reference-coalesce-examples"></a>

| Expression | Result |
| --- | --- |
| COALESCE('chair') | chair |
| COALESCE('chair', null, 'sofa') | chair |
| COALESCE(null, null, 'sofa') | sofa |
| COALESCE(null, 2, 5) | 2 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
