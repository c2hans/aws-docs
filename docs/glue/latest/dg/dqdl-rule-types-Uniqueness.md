---
source_url: https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-Uniqueness.html
---

# Uniqueness
<a name="dqdl-rule-types-Uniqueness"></a>

Checks the percentage of unique values in a column against a given expression. Unique values occur exactly once.

**Syntax**

```
Uniqueness {{<COL_NAME>}} {{<EXPRESSION>}}
```
+ **COL\_NAME** – The name of the column that you want to evaluate the data quality rule against.

  **Supported column types**: Any column type
+ **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions).

**Example**

The following example rule checks whether the percentage of unique values in a column matches certain numeric criteria.

```
Uniqueness "email" = 1.0
Uniqueness "Customer_ID" != 1.0 where "Customer_ID < 10"
```

The following example rule checks multiple columns.

```
Uniqueness "vendorid" "tpep_pickup_datetime" = 1
```

 **Sample dynamic rules**
+ `Uniqueness "colA" between min(last(10)) and max(last(10))`
+ `Uniqueness "colA" >= avg(last(10))`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
