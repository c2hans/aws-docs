---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_is_array.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# IS\_ARRAY function
<a name="r_is_array"></a>

Checks whether a variable is an array. The function returns `true` if the variable is an array. The function also includes empty arrays. Otherwise, the function returns `false` for all other values, including null.

## Syntax
<a name="r_is_array-synopsis"></a>

```
IS_ARRAY(super_expression)
```

## Arguments
<a name="r_is_array-arguments"></a>

*super\_expression*
A `SUPER` expression or column.

## Return type
<a name="r_is_array-returns"></a>

`BOOLEAN`

## Examples
<a name="r_is_array_example"></a>

To check if `[1,2]` is an array using the IS\_ARRAY function, use the following example.

```
SELECT IS_ARRAY(JSON_PARSE('[1,2]'));

+----------+
| is_array |
+----------+
| true     |
+----------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
