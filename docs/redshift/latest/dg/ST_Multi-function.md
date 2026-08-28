---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/ST_Multi-function.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# ST\_Multi
<a name="ST_Multi-function"></a>

ST\_Multi converts a geometry to the corresponding multitype. If the input geometry is already a multitype or a geometry collection, a copy of it is returned. If the input geometry is a point, linestring, or polygon, then a multipoint, multilinestring, or multipolygon, respectively, that contains the input geometry is returned.

## Syntax
<a name="ST_Multi-function-syntax"></a>

```
ST_Multi(geom)
```

## Arguments
<a name="ST_Multi-function-arguments"></a>

 *geom*
A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type
<a name="ST_Multi-function-return"></a>

`GEOMETRY` with subtype `MULTIPOINT`, `MULTILINESTRING`, `MULTIPOLYGON`, or `GEOMETRYCOLLECTION`.

The spatial reference system identifier (SRID) of the returned geometry is the same as that of the input geometry.

If *geom* is null, then null is returned.

## Examples
<a name="ST_Multi-function-examples"></a>

The following SQL returns a multipoint from an input multipoint.

```
SELECT ST_AsEWKT(ST_Multi(ST_GeomFromText('MULTIPOINT((1 2),(3 4))', 4326)));
```

```
    st_asewkt
------------------------------------
  SRID=4326;MULTIPOINT((1 2),(3 4))
```

The following SQL returns a multipoint from an input point.

```
SELECT ST_AsEWKT(ST_Multi(ST_GeomFromText('POINT(1 2)', 4326)));
```

```
    st_asewkt
------------------------------------
  SRID=4326;MULTIPOINT((1 2))
```

The following SQL returns a geometry collection from an input geometry collection.

```
SELECT ST_AsEWKT(ST_Multi(ST_GeomFromText('GEOMETRYCOLLECTION(POINT(1 2),MULTIPOINT((1 2),(3 4)))', 4326)));
```

```
    st_asewkt
------------------------------------
  SRID=4326;GEOMETRYCOLLECTION(POINT(1 2),MULTIPOINT((1 2),(3 4)))
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
