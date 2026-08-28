---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_is_varchar.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# IS\_VARCHAR function
<a name="r_is_varchar"></a>

Checks whether a variable is a `VARCHAR`. The IS\_VARCHAR function returns `true` for all strings. The function returns `false` for any other values.

The IS\_VARCHAR function is a superset of the IS\_CHAR function.

## Syntax
<a name="r_is_varchar-synopsis"></a>

```
IS_VARCHAR(super_expression)
```

## Arguments
<a name="r_is_varchar-arguments"></a>

*super\_expression*
A `SUPER` expression or column.

## Return type
<a name="r_is_varchar-returns"></a>

`BOOLEAN`

## Examples
<a name="r_is_varchar_example"></a>

To check if `abc` is a `VARCHAR` using the IS\_VARCHAR function, use the following example.

```
CREATE TABLE t(s SUPER);

INSERT INTO t VALUES ('abc');

SELECT s, IS_VARCHAR(s) FROM t;

+-------+------------+
|   s   | is_varchar |
+-------+------------+
| "abc" | true       |
+-------+------------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
