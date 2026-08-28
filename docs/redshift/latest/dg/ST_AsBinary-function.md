---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/ST_AsBinary-function.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# ST\_AsBinary
<a name="ST_AsBinary-function"></a>

ST\_AsBinary returns the hexadecimal well-known binary (WKB) representation of an input geometry. For 3DZ, 3DM, and 4D geometries, ST\_AsBinary uses the Open Geospatial Consortium (OGC) standard value for the geometry type.

## Syntax
<a name="ST_AsBinary-function-syntax"></a>

```
ST_AsBinary(geom)
```

## Arguments
<a name="ST_AsBinary-function-arguments"></a>

 *geom*
A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type
<a name="ST_AsBinary-function-return"></a>

`VARBYTE`

If *geom* is null, then null is returned.

## Examples
<a name="ST_AsBinary-function-examples"></a>

The following SQL returns the hexadecimal WKB representation of a polygon.

```
SELECT ST_AsBinary(ST_GeomFromText('POLYGON((0 0,0 1,1 1,1 0,0 0))',4326));
```

```
st_asbinary
--------------------------------
01030000000100000005000000000000000000000000000000000000000000000000000000000000000000F03F000000000000F03F000000000000F03F000000000000F03F000000000000000000000000000000000000000000000000
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
