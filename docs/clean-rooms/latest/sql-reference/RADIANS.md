---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/RADIANS.html
---

# RADIANS function
<a name="RADIANS"></a>

The RADIANS function converts an angle in degrees to its equivalent in radians.

## Syntax
<a name="RADIANS-synopsis"></a>

```
RADIANS(number)
```

## Argument
<a name="RADIANS-argument"></a>

 *number*
The input parameter is a `DOUBLE PRECISION` number.

## Return type
<a name="RADIANS-return-type"></a>

`DOUBLE PRECISION`

## Example
<a name="RADIANS-examples"></a>

To return the radian equivalent of 180 degrees, use the following example.

```
SELECT RADIANS(180);

+-------------------+
|      radians      |
+-------------------+
| 3.141592653589793 |
+-------------------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
