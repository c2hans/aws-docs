---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/EXP.html
---

# EXP function
<a name="EXP"></a>

The EXP function implements the exponential function for a numeric expression, or the base of the natural logarithm, `e`, raised to the power of expression. The EXP function is the inverse of [LN function](LN.md).

## Syntax
<a name="EXP-synopsis"></a>

```
EXP (expression)
```

## Argument
<a name="EXP-argument"></a>

 *expression*
The expression must be an INTEGER, DECIMAL, or DOUBLE PRECISION data type.

## Return type
<a name="EXP-return-type"></a>

EXP returns a DOUBLE PRECISION number.

## Example
<a name="EXP-example"></a>

Use the EXP function to forecast ticket sales based on a continuous growth pattern. In this example, the subquery returns the number of tickets sold in 2008. That result is multiplied by the result of the EXP function, which specifies a continuous growth rate of 7% over 10 years.

```
select (select sum(qtysold) from sales, date
where sales.dateid=date.dateid
and year=2008) * exp((7::float/100)*10) qty2018;

qty2018
------------------
695447.483772222
(1 row)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
