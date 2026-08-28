---
source_url: https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-UniqueValueRatio.html
---

# UniqueValueRatio
<a name="dqdl-rule-types-UniqueValueRatio"></a>

Checks the *unique value ratio* of a column against a given expression. A unique value ratio is the fraction of unique values divided by the number of all distinct values in a column. Unique values occur exactly one time, while distinct values occur *at least* once.

For example, the set `[a, a, b]` contains one unique value (`b`) and two distinct values (`a` and `b`). So the unique value ratio of the set is ½ = 0.5.

**Syntax**

```
UniqueValueRatio {{<COL_NAME>}} {{<EXPRESSION>}}
```
+ **COL\_NAME** – The name of the column that you want to evaluate the data quality rule against.

  **Supported column types**: Any column type
+ **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions).

**Example: Unique value ratio**

This example checks the unique value ratio of a column against a range of values.

```
UniqueValueRatio "test_score" between 0 and 0.5
UniqueValueRatio "Customer_ID" between 0 and 0.9 where "Customer_ID < 10"
```

 **Sample dynamic rules**
+ `UniqueValueRatio "colA" > avg(last(10))`
+ `UniqueValueRatio "colA" <= index(last(10),2) + std(last(5))`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
