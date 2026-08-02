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
