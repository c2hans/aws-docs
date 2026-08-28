---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/ST_IsValid-function.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# ST\_IsValid
<a name="ST_IsValid-function"></a>

ST\_IsValid returns true if the 2D projection of the input geometry is valid. For more information about the definition of a valid geometry, see [Geometric validity](spatial-terminology.md#spatial-terminology-validity).

## Syntax
<a name="ST_IsValid-function-syntax"></a>

```
ST_IsValid(geom)
```

## Arguments
<a name="ST_IsValid-function-arguments"></a>

 *geom*
A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type
<a name="ST_IsValid-function-return"></a>

`BOOLEAN`

If *geom* is null, then null is returned.

## Examples
<a name="ST_IsValid-function-examples"></a>

The following SQL checks if the specified polygon is valid. In this example, the polygon is invalid because the interior of the polygon isn't simply connected.

```
SELECT ST_IsValid(ST_GeomFromText('POLYGON((0 0,10 0,10 10,0 10,0 0),(5 0,10 5,5 10,0 5,5 0))'));
```

```
 st_isvalid
-----------
 false
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
