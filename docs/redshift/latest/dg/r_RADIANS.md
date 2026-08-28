---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_RADIANS.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# RADIANS function
<a name="r_RADIANS"></a>

The RADIANS function converts an angle in degrees to its equivalent in radians.

## Syntax
<a name="r_RADIANS-synopsis"></a>

```
RADIANS(number)
```

## Argument
<a name="r_RADIANS-argument"></a>

 *number*
The input parameter is a `DOUBLE PRECISION` number.

## Return type
<a name="r_RADIANS-return-type"></a>

`DOUBLE PRECISION`

## Examples
<a name="r_RADIANS-examples"></a>

To return the radian equivalent of 180 degrees, use the following example.

```
SELECT RADIANS(180);

+-------------------+
|      radians      |
+-------------------+
| 3.141592653589793 |
+-------------------+
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
