---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-22-spatial-functions-st-intersect.html
---

# ST\_Intersects
<a name="access-graph-opencypher-22-spatial-functions-st-intersect"></a>

ST\_Intersects returns true if the 2D projections of the two input geometries have at least one point in common.

**Syntax**

```
ST_Intersects(geom1, geom2)
```

**Arguments**
+ `geom1` - A value of data type GEOMETRY or an expression that evaluates to a GEOMETRY type.
+ `geom2` - A value of data type GEOMETRY or an expression that evaluates to a GEOMETRY type.

**Return type**

BOOLEAN

If geom1 or geom2 is null, then null is returned.

If the input parameter is not a Geometry, then a BadRequestException is returned.

**Examples**

```
RETURN ST_Intersects(
    ST_GeomFromText('POLYGON((0 0,10 0,10 10,0 10,0 0),(2 2,2 5,5 5,5 2,2 2))'),
    ST_GeomFromText('MULTIPOINT((4 4),(6 6))'));
true
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
