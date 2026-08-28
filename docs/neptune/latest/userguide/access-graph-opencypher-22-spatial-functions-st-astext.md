---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-22-spatial-functions-st-astext.html
---

# ST\_AsText
<a name="access-graph-opencypher-22-spatial-functions-st-astext"></a>

ST\_AsText returns the well-known text (WKT) representation of an input geometry.

**Syntax**

```
ST_AsText(geo)
```

**Arguments**
+ `geo` - A value of data type GEOMETRY, or an expression that evaluates to a GEOMETRY.

**Return type**

STRING

If geo is null, then null is returned.

If the input parameter is not a Geometry, then a BadRequestException is returned.

If the result is larger than a 64-KB STRING, then an error is returned.

**Examples**

```
RETURN ST_AsText(ST_GeomFromText('POLYGON((0 0,0 1,1 1,1 0,0 0))'))
POLYGON((0 0,0 1,1 1,1 0,0 0))
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
