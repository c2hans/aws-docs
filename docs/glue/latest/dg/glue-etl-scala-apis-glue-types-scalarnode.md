---
source_url: https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-scalarnode.html
---

# AWS Glue Scala ScalarNode APIs
<a name="glue-etl-scala-apis-glue-types-scalarnode"></a>

**Topics**
+ [ScalarNode class](#glue-etl-scala-apis-glue-types-scalarnode-class)
+ [ScalarNode object](#glue-etl-scala-apis-glue-types-scalarnode-object)

**Package: com.amazonaws.services.glue.types**

## ScalarNode class
<a name="glue-etl-scala-apis-glue-types-scalarnode-class"></a>

**ScalarNode**

```
class ScalarNode extends DynamicNode  (
           value : Any,
           scalarType : TypeCode )
```

### ScalarNode def methods
<a name="glue-etl-scala-apis-glue-types-scalarnode-class-defs"></a>

```
def compare( other : Any,
             operator : String
           ) : Boolean
```

```
def getValue
```

```
def hashCode : Int
```

```
def nodeType
```

```
def toJson
```

## ScalarNode object
<a name="glue-etl-scala-apis-glue-types-scalarnode-object"></a>

 **ScalarNode**

```
object ScalarNode
```

### ScalarNode def methods
<a name="glue-etl-scala-apis-glue-types-scalarnode-object-defs"></a>

```
def apply( v : Any ) : DynamicNode
```

```
def compare( tv : Ordered[T],
             other : T,
             operator : String
           ) : Boolean
```

```
def compareAny( v : Any,
                y : Any,
                o : String )
```

```
def withEscapedSpecialCharacters( jsonToEscape : String ) : String
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
