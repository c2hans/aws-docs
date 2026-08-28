---
source_url: https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-Sum.html
---

# Sum
<a name="dqdl-rule-types-Sum"></a>

Checks the sum of all the values in a column against a given expression.

**Syntax**

```
Sum {{<COL_NAME>}} {{<EXPRESSION>}}
```
+ **COL\_NAME** – The name of the column that you want to evaluate the data quality rule against.

  **Supported column types**: Byte, Decimal, Double, Float, Integer, Long, Short
+ **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions).

**Example: Sum**

The following example rule checks whether the sum of all of the values in a column exceeds a given threshold.

```
Sum "transaction_total" > 500000
Sum "Salary" < 55600 where "Customer_ID < 10"
```

 **Sample dynamic rules**
+ `Sum "ColA" > avg(last(10))`
+ `Sum "colA" between min(last(10)) - 1 and max(last(10)) + 1`

**Null behavior**

 The `Sum` rule will ignore rows with `NULL` values in the calculation of sum. For example:

```
+---+-----------+
|id |units      |
+---+-----------+
|100|0          |
|101|null       |
|102|20         |
|103|null       |
|104|40         |
+---+-----------+
```

 The sum of column `units` will not consider rows 101 and 103 and result to (0 \+ 20 \+ 40) = 60.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
