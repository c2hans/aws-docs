---
source_url: https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-dynamicnode.html
---

# AWS Glue Scala DynamicNode APIs
<a name="glue-etl-scala-apis-glue-types-dynamicnode"></a>

**Topics**
+ [DynamicNode class](#glue-etl-scala-apis-glue-types-dynamicnode-class)
+ [DynamicNode object](#glue-etl-scala-apis-glue-types-dynamicnode-object)

**Package: com.amazonaws.services.glue.types**

## DynamicNode class
<a name="glue-etl-scala-apis-glue-types-dynamicnode-class"></a>

**DynamicNode**

```
class DynamicNode extends Serializable with Cloneable
```

### DynamicNode def methods
<a name="glue-etl-scala-apis-glue-types-dynamicnode-class-defs"></a>

```
def getValue : Any
```

Get plain value and bind to the current record:

```
def nodeType : TypeCode
```

```
def toJson : String
```

Method for debug:

```
def toRow( schema : Schema,
           options : Map[String, ResolveOption]
         ) : Row
```

```
def typeName : String
```

## DynamicNode object
<a name="glue-etl-scala-apis-glue-types-dynamicnode-object"></a>

 **DynamicNode**

```
object DynamicNode
```

### DynamicNode def methods
<a name="glue-etl-scala-apis-glue-types-dynamicnode-object-defs"></a>

```
def quote( field : String,
           useQuotes : Boolean
         ) : String
```

```
def quote( node : DynamicNode,
           useQuotes : Boolean
         ) : String
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
