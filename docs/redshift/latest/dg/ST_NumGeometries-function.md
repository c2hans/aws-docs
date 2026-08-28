---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/ST_NumGeometries-function.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# ST\_NumGeometries
<a name="ST_NumGeometries-function"></a>

ST\_NumGeometries returns the number of geometries in an input geometry.

## Syntax
<a name="ST_NumGeometries-function-syntax"></a>

```
ST_NumGeometries(geom)
```

## Arguments
<a name="ST_NumGeometries-function-arguments"></a>

 *geom*
A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type
<a name="ST_NumGeometries-function-return"></a>

`INTEGER` representing the number of geometries in *geom*.

If *geom* is null, then null is returned.

If *geom* is a single empty geometry, then `0` is returned.

If *geom* is a single nonempty geometry, then `1` is returned.

If *geom* is a `GEOMETRYCOLLECTION` or a `MULTI` subtype, then the number of geometries is returned.

## Examples
<a name="ST_NumGeometries-function-examples"></a>

The following SQL returns the number of geometries in the input multilinestring.

```
SELECT ST_NumGeometries(ST_GeomFromText('MULTILINESTRING((0 0,1 0,0 5),(3 4,13 26))'));
```

```
st_numgeometries
-------------
 2
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
