---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-initcap.html
---

# INITCAP
<a name="sql-reference-initcap"></a>

```
INITCAP ( <character-expression> )
```

Returns a converted version of the input string such that the first character of each space-delimited word is upper-cased, and all other characters are lower-cased.

## Examples
<a name="sql-reference-initcap-examples"></a>

| Function | Result |
| --- | --- |
| INITCAP('Each FIRST lEtTeR is cAPITALIZED') | Each First Letter Is Capitalized |

##
<a name="sqlrf-initcap-notes"></a>

**Note**
The INITCAP function is not part of the SQL:2008 standard. It is an Amazon Kinesis Data Analytics extension.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
