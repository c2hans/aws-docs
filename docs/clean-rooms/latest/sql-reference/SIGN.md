---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/SIGN.html
---

# SIGN function
<a name="SIGN"></a>

 The SIGN function returns the sign (positive or negative) of a number. The result of the SIGN function is `1`, `-1`, or `0` indicating the sign of the argument.

## Syntax
<a name="SIGN-synopsis"></a>

```
SIGN (number)
```

## Argument
<a name="SIGN-argument"></a>

 *number*
Number or expression that evaluates to a number. It can be the DECIMALor FLOAT8 type. AWS Clean Rooms can convert other data types per the implicit conversion rules.

## Return type
<a name="SIGN-return-type"></a>

SIGN returns the same numeric data type as the input argument(s). If the input is DECIMAL, the output is DECIMAL(1,0).

## Examples
<a name="SIGN-examples"></a>

To determine the sign of the commission paid for a given transaction from the SALES table, use the following example.

```
SELECT commission, SIGN(commission)
FROM sales WHERE salesid=10000;

+------------+------+
| commission | sign |
+------------+------+
|      28.05 |    1 |
+------------+------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
