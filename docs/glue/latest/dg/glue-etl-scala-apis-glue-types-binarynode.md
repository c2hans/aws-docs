---
source_url: https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-binarynode.html
---

# AWS Glue Scala BinaryNode APIs
<a name="glue-etl-scala-apis-glue-types-binarynode"></a>

**Package: com.amazonaws.services.glue.types**

## BinaryNode case class
<a name="glue-etl-scala-apis-glue-types-binarynode-case-class"></a>

 **BinaryNode**

```
case class BinaryNode extends ScalarNode(value, TypeCode.BINARY)  (
           value : Array[Byte] )
```

### BinaryNode val fields
<a name="glue-etl-scala-apis-glue-types-binarynode-case-class-vals"></a>
+ `ordering`

### BinaryNode def methods
<a name="glue-etl-scala-apis-glue-types-binarynode-case-class-defs"></a>

```
def clone
```

```
def equals( other : Any )
```

```
def hashCode : Int
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
