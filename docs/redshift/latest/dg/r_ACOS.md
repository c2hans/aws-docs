---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_ACOS.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# ACOS function
<a name="r_ACOS"></a>

ACOS is a trigonometric function that returns the arc cosine of a number. The return value is in radians and is between `0` and `PI`.

## Syntax
<a name="r_ACOS-synopsis"></a>

```
ACOS(number)
```

## Arguments
<a name="r_ACOS-arguments"></a>

 *number*
The input parameter is a `DOUBLE PRECISION` number.

## Return type
<a name="r_ACOS-return-type"></a>

`DOUBLE PRECISION`

## Examples
<a name="r_ACOS-examples"></a>

To return the arc cosine of `-1`, use the following example.

```
SELECT ACOS(-1);

+-------------------+
|       acos        |
+-------------------+
| 3.141592653589793 |
+-------------------+
```

To convert the arc cosine of `.5` to the equivalent number of degrees, use the following example.

```
SELECT (ACOS(.5) * 180/(SELECT PI())) AS degrees;

+-------------------+
|      degrees      |
+-------------------+
| 60.00000000000001 |
+-------------------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
