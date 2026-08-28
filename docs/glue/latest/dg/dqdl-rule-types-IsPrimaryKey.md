---
source_url: https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-IsPrimaryKey.html
---

# IsPrimaryKey
<a name="dqdl-rule-types-IsPrimaryKey"></a>

Checks whether a column contains a primary key. A column contains a primary key if all of the values in the column are unique and complete (non-null). You can also check for primary keys with multiple columns.

**Syntax**

```
IsPrimaryKey {{<COL_NAME>}}
```
+ **COL\_NAME** – The name of the column that you want to evaluate the data quality rule against.

  **Supported column types**: Any column type

**Example: Primary key**

The following example rule checks whether the column named `Customer_ID` contains a primary key.

```
IsPrimaryKey "Customer_ID"
IsPrimaryKey "Customer_ID" where "Customer_ID < 10"
```

 **Example: Primary key with multiple columns. Any of the following examples are valid.**

```
IsPrimaryKey "colA" "colB"
IsPrimaryKey "colA" "colB" "colC"
IsPrimaryKey colA "colB" "colC"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
