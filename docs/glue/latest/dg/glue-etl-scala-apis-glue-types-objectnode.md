---
source_url: https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-objectnode.html
---

# AWS Glue Scala ObjectNode APIs
<a name="glue-etl-scala-apis-glue-types-objectnode"></a>

**Topics**
+ [ObjectNode object](#glue-etl-scala-apis-glue-types-objectnode-object)
+ [ObjectNode case class](#glue-etl-scala-apis-glue-types-objectnode-case-class)

**Package: com.amazonaws.services.glue.types**

## ObjectNode object
<a name="glue-etl-scala-apis-glue-types-objectnode-object"></a>

**ObjectNode**

```
object ObjectNode
```

### ObjectNode def methods
<a name="glue-etl-scala-apis-glue-types-objectnode-object-defs"></a>

```
def apply( frameKeys : Set[String],
           v1 : mutable.Map[String, DynamicNode],
           v2 : mutable.Map[String, DynamicNode],
           resolveWith : String
         ) : ObjectNode
```

## ObjectNode case class
<a name="glue-etl-scala-apis-glue-types-objectnode-case-class"></a>

 **ObjectNode**

```
case class ObjectNode extends MapLikeNode(value)  (
           val value : mutable.Map[String, DynamicNode] )
```

### ObjectNode def methods
<a name="glue-etl-scala-apis-glue-types-objectnode-case-class-defs"></a>

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
