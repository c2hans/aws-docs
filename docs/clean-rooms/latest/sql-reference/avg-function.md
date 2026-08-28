---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/avg-function.html
---

# AVG function
<a name="avg-function"></a>

The AVG function returns the average (arithmetic mean) of the input expression values. The AVG function works with numeric values and ignores NULL values.

## Syntax
<a name="avg-function-syntax"></a>

```
AVG ({{column}})
```

## Arguments
<a name="avg-function-arguments"></a>

{{column}}
The target column that the function operates on. The column is one of the following data types:
+ SMALLINT
+ INTEGER
+ BIGINT
+ DECIMAL
+ DOUBLE
+ FLOAT

## Data types
<a name="avg-function-data-types"></a>

The argument types supported by the AVG function are SMALLINT, INTEGER, BIGINT, DECIMAL, and DOUBLE.

The return types supported by the AVG function are:
+ BIGINT for any integer type argument
+ DOUBLE for a floating point argument
+ Returns the same data type as expression for any other argument type

The default precision for an AVG function result with a DECIMAL argument is 38. The scale of the result is the same as the scale of the argument. For example, an AVG of a DEC(5,2) column returns a DEC(38,2) data type.

## Example
<a name="avg-function-example"></a>

Find the average quantity sold per transaction from the SALES table.

```
select avg(qtysold) from sales;
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
