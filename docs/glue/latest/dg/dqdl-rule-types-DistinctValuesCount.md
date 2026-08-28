---
source_url: https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-DistinctValuesCount.html
---

# DistinctValuesCount
<a name="dqdl-rule-types-DistinctValuesCount"></a>

Checks the number of distinct values in a column against a given expression.

**Syntax**

```
DistinctValuesCount {{<COL_NAME>}} {{<EXPRESSION>}}
```
+ **COL\_NAME** – The name of the column that you want to evaluate the data quality rule against.

  **Supported column types**: Any column type
+ **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions).

**Example: Distinct column value count**

The following example rule checks that the column named `State` contains more than 3 distinct values.

```
DistinctValuesCount "State" > 3
DistinctValuesCount "Customer_ID" < 6  where "Customer_ID < 10"
```

**Sample dynamic rules**
+ `DistinctValuesCount "colA" between avg(last(10))-1 and avg(last(10))+1`
+ `DistinctValuesCount "colA" <= index(last(10),2) + std(last(5))`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
