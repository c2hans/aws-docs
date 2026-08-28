---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/ST_NumInteriorRings-function.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# ST\_NumInteriorRings
<a name="ST_NumInteriorRings-function"></a>

ST\_NumInteriorRings returns the number of rings in an input polygon geometry.

## Syntax
<a name="ST_NumInteriorRings-function-syntax"></a>

```
ST_NumInteriorRings(geom)
```

## Arguments
<a name="ST_NumInteriorRings-function-arguments"></a>

 *geom*
A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type
<a name="ST_NumInteriorRings-function-return"></a>

`INTEGER`

If *geom* is null, then null is returned.

If *geom* is not a polygon, then null is returned.

## Examples
<a name="ST_NumInteriorRings-function-examples"></a>

The following SQL returns the number of interior rings in the input polygon.

```
SELECT ST_NumInteriorRings(ST_GeomFromText('POLYGON((0 0,100 0,100 100,0 100,0 0),(1 1,1 5,5 1,1 1),(7 7,7 8,8 7,7 7))'));
```

```
 st_numinteriorrings
-------------
 2
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
