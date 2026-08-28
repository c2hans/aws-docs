---
source_url: https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-mapnode.html
---

# AWS Glue Scala MapNode APIs
<a name="glue-etl-scala-apis-glue-types-mapnode"></a>

**Package: com.amazonaws.services.glue.types**

## MapNode case class
<a name="glue-etl-scala-apis-glue-types-mapnode-case-class"></a>

 **MapNode**

```
case class MapNode extends MapLikeNode(value)  (
           value : mutable.Map[String, DynamicNode] )
```

### MapNode def methods
<a name="glue-etl-scala-apis-glue-types-mapnode-case-class-defs"></a>

```
def clone
```

```
def equals( other : Any )
```

```
def hashCode : Int
```

```
def nodeType
```

```
def this
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
