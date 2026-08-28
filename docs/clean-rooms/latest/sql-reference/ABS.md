---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/ABS.html
---

# ABS function
<a name="ABS"></a>

 ABS calculates the absolute value of a number, where that number can be a literal or an expression that evaluates to a number.

## Syntax
<a name="ABS-synopsis"></a>

```
ABS (number)
```

## Arguments
<a name="ABS-arguments"></a>

 *number*
Number or expression that evaluates to a number. It can be the SMALLINT, INTEGER, BIGINT, DECIMAL, FLOAT4, or FLOAT8 type.

## Return type
<a name="ABS-return-type"></a>

ABS returns the same data type as its argument.

## Examples
<a name="ABS-examples"></a>

Calculate the absolute value of -38:

```
select abs (-38);
abs
-------
38
(1 row)
```

Calculate the absolute value of (14-76):

```
select abs (14-76);
abs
-------
62
(1 row)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
