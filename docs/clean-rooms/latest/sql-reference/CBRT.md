---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/CBRT.html
---

# CBRT function
<a name="CBRT"></a>

 The CBRT function is a mathematical function that calculates the cube root of a number.

## Syntax
<a name="CBRT-synopsis"></a>

```
CBRT (number)
```

## Argument
<a name="CBRT-argument"></a>

CBRT takes a DOUBLE PRECISION number as an argument.

## Return type
<a name="CBRT-return-type"></a>

CBRT returns a DOUBLE PRECISION number.

## Examples
<a name="CBRT-examples"></a>

Calculate the cube root of the commission paid for a given transaction:

```
select cbrt(commission) from sales where salesid=10000;

cbrt
------------------
3.03839539048843
(1 row)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
