---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/COS.html
---

# COS function
<a name="COS"></a>

COS is a trigonometric function that returns the cosine of a number. The return value is in radians and is between `-1` and `1`, inclusive.

## Syntax
<a name="COS-synopsis"></a>

```
COS(double_precision)
```

## Argument
<a name="COS-argument"></a>

 *number*
The input parameter is a double precision number.

## Return type
<a name="COS-return-type"></a>

The COS function returns a double precision number.

## Examples
<a name="COS-examples"></a>

The following example returns cosine of 0:

```
select cos(0);
cos
-----
1
(1 row)
```

The following example returns the cosine of PI:

```
select cos(pi());
cos
-----
-1
(1 row)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
