---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/ST_Centroid-function.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# ST\_Centroid
<a name="ST_Centroid-function"></a>

ST\_Centroid returns a point that represents a centroid of a geometry as follows:
+ For `POINT` geometries, it returns the point whose coordinates are the average of the coordinates of the points in the geometry.
+ For `LINESTRING` geometries, it returns the point whose coordinates are the weighted average of the midpoints of the segments of the geometry, where the weights are the lengths of the segments of the geometry.
+ For `POLYGON` geometries, it returns the point whose coordinates are the weighted average of the centroids of a triangulation of the areal geometry where the weights are the areas of the triangles in the triangulation.
+ For geometry collections, it returns the weighted average of the centroids of the geometries of maximum topological dimension in the geometry collection.

## Syntax
<a name="ST_Centroid-function-syntax"></a>

```
ST_Centroid(geom)
```

## Arguments
<a name="ST_Centroid-function-arguments"></a>

 *geom*
A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type
<a name="ST_Centroid-function-return"></a>

`GEOMETRY`

If *geom* is null, then null is returned.

If *geom* is empty, then null is returned.

## Examples
<a name="ST_Centroid-function-examples"></a>

The following SQL returns central point of an input linestring.

```
SELECT ST_AsEWKT(ST_Centroid(ST_GeomFromText('LINESTRING(110 40, 2 3, -10 80, -7 9, -22 -33)', 4326)))
```

```
                     st_asewkt
----------------------------------------------------
 SRID=4326;POINT(15.6965103455214 27.0206782881905)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
