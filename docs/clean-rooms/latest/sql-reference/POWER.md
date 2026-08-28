---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/POWER.html
---

# POWER function
<a name="POWER"></a>

 The POWER function is an exponential function that raises a numeric expression to the power of a second numeric expression. For example, 2 to the third power is calculated as `POWER(2,3)`, with a result of `8`.

## Syntax
<a name="POWER-synopsis"></a>

```
{POWER(expression1, expression2)
```

## Arguments
<a name="POWER-arguments"></a>

 *expression1*
Numeric expression to be raised. Must be an `INTEGER`, `DECIMAL`, or `FLOAT` data type.

 *expression2*
Power to raise *expression1*. Must be an `INTEGER`, `DECIMAL`, or `FLOAT` data type.

## Return type
<a name="POWER-return-type"></a>

`DOUBLE PRECISION`

## Example
<a name="POWER-examples"></a>

```
SELECT (SELECT SUM(qtysold) FROM sales, date
WHERE sales.dateid=date.dateid
AND year=2008) * POW((1+7::FLOAT/100),10) qty2010;

+-------------------+
|      qty2010      |
+-------------------+
| 679353.7540885945 |
+-------------------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
