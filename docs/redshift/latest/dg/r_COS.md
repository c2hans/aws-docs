---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_COS.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# COS function
<a name="r_COS"></a>

COS is a trigonometric function that returns the cosine of a number. The return value is in radians and is between `-1` and `1`, inclusive.

## Syntax
<a name="r_COS-synopsis"></a>

```
COS(double_precision)
```

## Arguments
<a name="r_COS-argument"></a>

 *number*
The input parameter is a `DOUBLE PRECISION` number.

## Return type
<a name="r_COS-return-type"></a>

The COS function returns a `DOUBLE PRECISION` number.

## Examples
<a name="r_COS-examples"></a>

To return the cosine of `0`, use the following example.

```
SELECT COS(0);

+-----+
| cos |
+-----+
|   1 |
+-----+
```

To return the cosine of `pi`, use the following example.

```
SELECT COS(PI());

+-----+
| cos |
+-----+
|  -1 |
+-----+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
