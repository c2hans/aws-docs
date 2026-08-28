---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/ST_Reverse-function.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# ST\_Reverse
<a name="ST_Reverse-function"></a>

ST\_Reverse reverses the order of the vertices for linear and areal geometries. For point or multipoint geometries, a copy of the original geometry is returned. For geometry collections, ST\_Reverse reverses the order of the vertices for each of the geometries in the collection.

The dimension of the returned geometry is the same as that of the input geometry.

## Syntax
<a name="ST_Reverse-function-syntax"></a>

```
ST_Reverse(geom)
```

## Arguments
<a name="ST_Reverse-function-arguments"></a>

 *geom*
A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type
<a name="ST_Reverse-function-return"></a>

`GEOMETRY`

The spatial reference system identifier (SRID) of the returned geometry is the same as that of the input geometry.

If *geom* is null, then null is returned.

## Examples
<a name="ST_Reverse-function-examples"></a>

The following SQL reverses the order of the points in a linestring.

```
SELECT ST_AsEWKT(ST_Reverse(ST_GeomFromText('LINESTRING(1 0,2 0,3 0,4 0)', 4326)));
```

```
    st_asewkt
------------------------------------
  SRID=4326;LINESTRING(4 0,3 0,2 0,1 0)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
