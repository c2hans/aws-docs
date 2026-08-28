---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_DLOG10.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# DLOG10 function
<a name="r_DLOG10"></a>

The DLOG10 returns the base 10 logarithm of the input parameter.

Synonym of [LOG function](r_LOG.md).

## Syntax
<a name="r_DLOG10-synopsis"></a>

```
DLOG10(number)
```

## Argument
<a name="r_DLOG10-argument"></a>

 *number*
The input parameter is a `DOUBLE PRECISION` number.

## Return type
<a name="r_DLOG10-return-type"></a>

`DOUBLE PRECISION`

## Example
<a name="r_DLOG10-example"></a>

To return the base 10 logarithm of the number 100, use the following example.

```
SELECT DLOG10(100);

+--------+
| dlog10 |
+--------+
|      2 |
+--------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
