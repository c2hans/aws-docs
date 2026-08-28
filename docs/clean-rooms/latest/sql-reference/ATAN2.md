---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/ATAN2.html
---

# ATAN2 function
<a name="ATAN2"></a>

ATAN2 is a trigonometric function that returns the arc tangent of one number divided by another number. The return value is in radians and is between `PI/2` and `-PI/2`.

## Syntax
<a name="ATAN2-synopsis"></a>

```
ATAN2(number1, number2)
```

## Arguments
<a name="ATAN2-arguments"></a>

 *number1*
A `DOUBLE PRECISION` number.

 *number2*
A `DOUBLE PRECISION` number.

## Return type
<a name="ATAN2-return-type"></a>

`DOUBLE PRECISION`

## Examples
<a name="ATAN2-examples"></a>

To return the arc tangent of `2/2` and multiply it by 4, use the following example.

```
SELECT ATAN2(2,2) * 4 AS PI;

+-------------------+
|        pi         |
+-------------------+
| 3.141592653589793 |
+-------------------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
