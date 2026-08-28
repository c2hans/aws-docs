---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sum-function.html
---

# SUM and SUM DISTINCT functions
<a name="sum-function"></a>

The SUM function returns the sum of the input column or expression values. The SUM function works with numeric values and ignores NULL values.

The SUM DISTINCT function eliminates all duplicate values from the specified expression before calculating the sum.

## Syntax
<a name="sum-function-syntax"></a>

```
SUM (DISTINCT {{column}} )
```

## Arguments
<a name="sum-function-arguments"></a>

{{column}}
The target column that the function operates on. The column is any numeric data types.

## Examples
<a name="sum-function-examples"></a>

Find the sum of all commissions paid from the SALES table.

```
select sum(commission) from sales
```

Find the sum of all distinct commissions paid from the SALES table.

```
select sum (distinct (commission)) from sales
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
