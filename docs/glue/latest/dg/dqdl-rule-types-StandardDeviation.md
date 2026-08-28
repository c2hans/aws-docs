---
source_url: https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-StandardDeviation.html
---

# StandardDeviation
<a name="dqdl-rule-types-StandardDeviation"></a>

Checks the standard deviation of all of the values in a column against a given expression.

**Syntax**

```
StandardDeviation {{<COL_NAME>}} {{<EXPRESSION>}}
```
+ **COL\_NAME** – The name of the column that you want to evaluate the data quality rule against.

  **Supported column types**: Byte, Decimal, Double, Float, Integer, Long, Short
+ **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions).

**Example: Standard deviation**

The following example rule checks whether the standard deviation of the values in a column named `colA` is less than a specified value.

```
StandardDeviation "Star_Rating" < 1.5
StandardDeviation "Salary" < 3500 where "Customer_ID < 10"
```

 **Sample dynamic rules**
+ `StandardDeviation "colA" > avg(last(10) + 0.1`
+ `StandardDeviation "colA" between min(last(10)) - 1 and max(last(10)) + 1`

**Null behavior**

 The `StandardDeviation` rule will ignore rows with `NULL` values in the calculation of standard deviation. For example:

```
+---+-----------+-----------+
|id |units1     |units2     |
+---+-----------+-----------+
|100|0          |0          |
|101|null       |0          |
|102|20         |20         |
|103|null       |0          |
|104|40         |40         |
+---+-----------+-----------+
```

 The standard deviation of column `units1` will not consider rows 101 and 103 and result to 16.33. The standard deviation for column `units2` will result in 16.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
