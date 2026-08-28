---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/ATAN.html
---

# ATAN function
<a name="ATAN"></a>

ATAN is a trigonometric function that returns the arc tangent of a number. The return value is in radians and is between `-PI` and `PI`.

## Syntax
<a name="ATAN-synopsis"></a>

```
ATAN(number)
```

## Arguments
<a name="ATAN-argument"></a>

 *number*
The input parameter is a `DOUBLE PRECISION` number.

## Return type
<a name="ATAN-return-type"></a>

`DOUBLE PRECISION`

## Examples
<a name="ATAN-examples"></a>

To return the arc tangent of `1` and multiply it by 4, use the following example.

```
SELECT ATAN(1) * 4 AS pi;

+-------------------+
|        pi         |
+-------------------+
| 3.141592653589793 |
+-------------------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
