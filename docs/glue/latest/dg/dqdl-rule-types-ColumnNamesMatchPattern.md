---
source_url: https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-ColumnNamesMatchPattern.html
---

# ColumnNamesMatchPattern
<a name="dqdl-rule-types-ColumnNamesMatchPattern"></a>

Checks whether the names of all columns in the primary dataset match the given regular expression.

**Syntax**

```
ColumnNamesMatchPattern {{<PATTERN>}}
```
+ **PATTERN** – The pattern you want to evaluate the data quality rule against.

  **Supported column types**: Byte, Decimal, Double, Float, Integer, Long, Short

**Example: Column names match pattern**

The following example rule checks whether all columns start with the prefix "aws\_"

```
ColumnNamesMatchPattern "aws_.*"
ColumnNamesMatchPattern "aws_.*" where "weightinkgs > 10"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
