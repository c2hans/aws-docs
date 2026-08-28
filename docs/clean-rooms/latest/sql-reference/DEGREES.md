---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/DEGREES.html
---

# DEGREES function
<a name="DEGREES"></a>

Converts an angle in radians to its equivalent in degrees.

## Syntax
<a name="DEGREES-synopsis"></a>

```
DEGREES(number)
```

## Argument
<a name="DEGREES-argument"></a>

 *number*
The input parameter is a `DOUBLE PRECISION` number.

## Return type
<a name="DEGREES-return-type"></a>

`DOUBLE PRECISION`

## Example
<a name="DEGREES-examples"></a>

To return the degree equivalent of .5 radians, use the following example.

```
SELECT DEGREES(.5);

+-------------------+
|      degrees      |
+-------------------+
| 28.64788975654116 |
+-------------------+
```

To convert PI radians to degrees, use the following example.

```
SELECT DEGREES(pi());

+---------+
| degrees |
+---------+
|     180 |
+---------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
