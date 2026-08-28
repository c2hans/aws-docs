---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/ST_Points-function.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# ST\_Points
<a name="ST_Points-function"></a>

ST\_Points returns a multipoint geometry containing all nonempty points in the input geometry. ST\_Points doesn't remove points that are duplicated in the input, including the start and end points of ring geometries.

## Syntax
<a name="ST_Points-function-syntax"></a>

```
ST_Points(geom)
```

## Arguments
<a name="ST_Points-function-arguments"></a>

 *geom*
A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type
<a name="ST_Points-function-return"></a>

`GEOMETRY` of subtype `MULTIPOINT`.

The spatial reference system identifier (SRID) value of the returned geometry is the same as *geom*.

If *geom* is null, then null is returned.

If *geom* is empty, then the empty multipoint is returned.

## Examples
<a name="ST_Points-function-examples"></a>

The following SQL examples construct a multipoint geometry from the input geometry. The result is a multipoint geometry containing the nonempty points in the input geometry.

```
SELECT ST_AsEWKT(ST_Points(ST_SetSRID(ST_GeomFromText('LINESTRING(1 0,2 0,3 0)'), 4326)));
```

```
st_asewkt
-------------
SRID=4326;MULTIPOINT((1 0),(2 0),(3 0))
```

```
SELECT ST_AsEWKT(ST_Points(ST_SetSRID(ST_GeomFromText('MULTIPOLYGON(((0 0,1 0,0 1,0 0)))'), 4326)));
```

```
st_asewkt
-------------
SRID=4326;MULTIPOINT((0 0),(1 0),(0 1),(0 0))
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
