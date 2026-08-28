---
source_url: https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-IsUnique.html
---

# IsUnique
<a name="dqdl-rule-types-IsUnique"></a>

Checks whether all of the values in a column are unique, and returns a Boolean value.

**Syntax**

```
IsUnique {{<COL_NAME>}}
```
+ **COL\_NAME** – The name of the column that you want to evaluate the data quality rule against.

  **Supported column types**: Any column type

**Examples**

The following example rule checks whether all of the values in a column named `email` are unique.

```
IsUnique "email"
IsUnique "Customer_ID" where "Customer_ID < 10"
```

The following example rule checks multiple columns.

```
IsUnique "vendorid" "tpep_pickup_datetime"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
