---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_is_decimal.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# IS\_DECIMAL function
<a name="r_is_decimal"></a>

Checks whether a value is a `DECIMAL`. The IS\_DECIMAL function returns `true` for numbers that are not floating points. The function returns `false` for any other values, including null.

The IS\_DECIMAL function is a superset of IS\_BIGINT.

## Syntax
<a name="r_is_decimal-synopsis"></a>

```
IS_DECIMAL(super_expression)
```

## Arguments
<a name="r_is_decimal-arguments"></a>

*super\_expression*
A `SUPER` expression or column.

## Return type
<a name="r_is_decimal-returns"></a>

`BOOLEAN`

## Examples
<a name="r_is_decimal_example"></a>

To check if `1.22` is a `DECIMAL` using the IS\_DECIMAL function, use the following example.

```
CREATE TABLE t(s SUPER);

INSERT INTO t VALUES (1.22);

SELECT s, IS_DECIMAL(s) FROM t;

+------+------------+
|  s   | is_decimal |
+------+------------+
| 1.22 | true       |
+------+------------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
