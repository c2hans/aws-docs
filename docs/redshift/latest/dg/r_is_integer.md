---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_is_integer.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# IS\_INTEGER function
<a name="r_is_integer"></a>

Returns `true` for numbers of scale 0 in the 32-bit range, and `false` for anything else (including null and floating point numbers).

The IS\_INTEGER function is a superset of the IS\_SMALLINT function.

## Syntax
<a name="r_is_integer-synopsis"></a>

```
IS_INTEGER(super_expression)
```

## Arguments
<a name="r_is_integer-arguments"></a>

*super\_expression*
A `SUPER` expression or column.

## Return type
<a name="r_is_integer-returns"></a>

`BOOLEAN`

## Examples
<a name="r_is_integer_example"></a>

To check if `5` is an `INTEGER` using the IS\_INTEGER function, use the following example.

```
CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (5);

SELECT s, IS_INTEGER(s) FROM t;

+---+------------+
| s | is_integer |
+---+------------+
| 5 | true       |
+---+------------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
