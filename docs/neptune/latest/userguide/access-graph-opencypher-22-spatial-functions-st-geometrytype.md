---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-22-spatial-functions-st-geometrytype.html
---

# ST\_GeometryType
<a name="access-graph-opencypher-22-spatial-functions-st-geometrytype"></a>

ST\_GeometryType returns the type of the geometry as a string.

**Syntax**

```
ST_GeometryType(geom)
```

**Arguments**
+ `geom` - A value of data type GEOMETRY or an expression that evaluates to a GEOMETRY type.

**Return type**

STRING

If geom is null, then null is returned.

If the input parameter is not a Geometry, then a BadRequestException is returned.

**Examples**

```
RETURN ST_GeometryType(ST_GeomFromText('LINESTRING(77.29 29.07,77.42 29.26,77.27 29.31,77.29 29.07)'));
ST_LineString
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
