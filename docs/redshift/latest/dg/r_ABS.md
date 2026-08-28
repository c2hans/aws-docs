---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_ABS.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# ABS function
<a name="r_ABS"></a>

 ABS calculates the absolute value of a number, where that number can be a literal or an expression that evaluates to a number.

## Syntax
<a name="r_ABS-synopsis"></a>

```
ABS(number)
```

## Arguments
<a name="r_ABS-arguments"></a>

 *number*
Number or expression that evaluates to a number. It can be the `SMALLINT`, `INTEGER`, `BIGINT`, `DECIMAL`, `FLOAT4`, `FLOAT8`, or `SUPER` type.

## Return type
<a name="r_ABS-return-type"></a>

ABS returns the same data type as its argument.

## Examples
<a name="r_ABS-examples"></a>

To calculate the absolute value of `-38`, use the following example.

```
SELECT ABS(-38);

+-----+
| abs |
+-----+
|  38 |
+-----+
```

To calculate the absolute value of `(14-76)`, use the following example.

```
SELECT ABS(14-76);

+-----+
| abs |
+-----+
|  62 |
+-----+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
