---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_is_float.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# IS\_FLOAT function
<a name="r_is_float"></a>

Checks whether a value is a floating point number. The IS\_FLOAT function returns `true` for floating point numbers (`FLOAT4` and `FLOAT8`). The function returns `false` for any other values.

The set of IS\_DECIMAL the set of IS\_FLOAT are disjoint.

## Syntax
<a name="r_is_float-synopsis"></a>

```
IS_FLOAT(super_expression)
```

## Arguments
<a name="r_is_float-arguments"></a>

*super\_expression*
A `SUPER` expression or column.

## Return type
<a name="r_is_float-returns"></a>

`BOOLEAN`

## Examples
<a name="r_is_float_example"></a>

To check if `2.22::FLOAT` is a `FLOAT` using the IS\_FLOAT function, use the following example.

```
CREATE TABLE t(s SUPER);

INSERT INTO t VALUES(2.22::FLOAT);

SELECT s, IS_FLOAT(s) FROM t;

+---------+----------+
|    s    | is_float |
+---------+----------+
| 2.22e+0 | true     |
+---------+----------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
