---
source_url: https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-ColumnExists.html
---

# ColumnExists
<a name="dqdl-rule-types-ColumnExists"></a>

Checks whether a column exists.

**Syntax**

```
ColumnExists {{<COL_NAME>}}
```
+ **COL\_NAME** – The name of the column that you want to evaluate the data quality rule against.

  **Supported column types**: Any column type

**Example: Column exists**

The following example rule checks whether the column named `Middle_Name` exists.

```
ColumnExists "Middle_Name"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
