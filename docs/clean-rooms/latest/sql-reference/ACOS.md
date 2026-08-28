---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/ACOS.html
---

# ACOS function
<a name="ACOS"></a>

ACOS is a trigonometric function that returns the arc cosine of a number. The return value is in radians and is between `0` and `PI`.

## Syntax
<a name="ACOS-synopsis"></a>

```
ACOS(number)
```

## Arguments
<a name="ACOS-arguments"></a>

 *number*
The input parameter is a `DOUBLE PRECISION` number.

## Return type
<a name="ACOS-return-type"></a>

`DOUBLE PRECISION`

## Examples
<a name="ACOS-examples"></a>

To return the arc cosine of `-1`, use the following example.

```
SELECT ACOS(-1);

+-------------------+
|       acos        |
+-------------------+
| 3.141592653589793 |
+-------------------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
