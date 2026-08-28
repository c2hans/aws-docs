---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/ST_YMax-function.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# ST\_YMax
<a name="ST_YMax-function"></a>

ST\_YMax returns the maximum second coordinate of an input geometry.

## Syntax
<a name="ST_YMax-function-syntax"></a>

```
ST_YMax(geom)
```

## Arguments
<a name="ST_YMax-function-arguments"></a>

 *geom*
A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type
<a name="ST_YMax-function-return"></a>

`DOUBLE PRECISION` value of the maximum second coordinate.

If *geom* is empty, then null is returned.

If *geom* is null, then null is returned.

## Examples
<a name="ST_YMax-function-examples"></a>

The following SQL returns the largest second coordinate of a linestring.

```
SELECT ST_YMax(ST_GeomFromText('LINESTRING(77.29 29.07,77.42 29.26,77.27 29.31,77.29 29.07)'));
```

```
st_ymax
-----------
 29.31
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
