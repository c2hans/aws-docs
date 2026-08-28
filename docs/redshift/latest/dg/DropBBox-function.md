---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/DropBBox-function.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# DropBBox
<a name="DropBBox-function"></a>

DropBBox returns a copy of the input geometry that doesn't support encoding with a precomputed bounding box. For more information about support for bounding boxes, see [Bounding box](spatial-terminology.md#spatial-terminology-bounding-box).

## Syntax
<a name="DropBBox-function-syntax"></a>

```
DropBBox(geom)
```

## Arguments
<a name="DropBBox-function-arguments"></a>

 *geom*
A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type
<a name="DropBBox-function-return"></a>

`GEOMETRY`

If *geom* is null, then null is returned.

## Examples
<a name="DropBBox-function-examples"></a>

The following SQL returns a copy of an input polygon geometry that doesn't support being encoded with a bounding box.

```
SELECT ST_AsText(DropBBox(ST_GeomFromText('POLYGON((0 0,1 0,0 1,0 0))')));
```

```
 st_astext
----------
 POLYGON((0 0,1 0,0 1,0 0))
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
