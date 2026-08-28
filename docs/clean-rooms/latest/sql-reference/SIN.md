---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/SIN.html
---

# SIN function
<a name="SIN"></a>

SIN is a trigonometric function that returns the sine of a number. The return value is between `-1` and `1`.

## Syntax
<a name="SIN-synopsis"></a>

```
SIN(number)
```

## Argument
<a name="SIN-argument"></a>

 *number*
A `DOUBLE PRECISION` number in radians.

## Return type
<a name="SIN-return-type"></a>

`DOUBLE PRECISION`

## Example
<a name="SIN-examples"></a>

To return the sine of `-PI`, use the following example.

```
SELECT SIN(-PI());

+-------------------------+
|           sin           |
+-------------------------+
| -0.00000000000000012246 |
+-------------------------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
