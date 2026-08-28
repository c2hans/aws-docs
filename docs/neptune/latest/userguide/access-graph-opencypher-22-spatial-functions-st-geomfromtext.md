---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-22-spatial-functions-st-geomfromtext.html
---

# ST\_GeomFromText
<a name="access-graph-opencypher-22-spatial-functions-st-geomfromtext"></a>

ST\_GeomFromText constructs a geometry object from a well-known text (WKT) representation of an input geometry.

**Syntax**

```
ST_GeomFromText(wkt_string)
```

**Arguments**
+ `wkt_string` - A value of data type STRING that is a WKT representation of a geometry.

**Return type**

GEOMETRY

If wkt\_string is null, then null is returned.

If wkt\_string is not valid, then a BadRequestException is returned.

**Examples**

```
RETURN ST_GeomFromText('POLYGON((0 0,0 1,1 1,1 0,0 0))')
POLYGON((0 0,0 1,1 1,1 0,0 0))
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
