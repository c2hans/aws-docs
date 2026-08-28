---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-log10.html
---

# LOG10
<a name="sql-reference-log10"></a>

```
LOG10 ( <number-expression> )
```

Returns the base 10 logarithm of the input argument. If the argument is negative or 0, an exception is raised. Returns null if the input argument is null.

## Examples
<a name="sql-reference-log10-examples"></a>

|  Function  |  Result  |
| --- | --- |
| LOG10(1) | 0.0 |
| LOG10(100) | 2.0 |
| log10(cast('23' as decimal)) | 1.3617278360175928 |

##
<a name="sql-reference-log10-notes"></a>

**Note**
LOG10 is not a SQL:2008 standard function; it is an Amazon Kinesis Data Analytics extension to the standard.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
