---
source_url: https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-stringnode.html
---

# AWS Glue Scala StringNode APIs
<a name="glue-etl-scala-apis-glue-types-stringnode"></a>

**Package: com.amazonaws.services.glue.types**

## StringNode case class
<a name="glue-etl-scala-apis-glue-types-stringnode-case-class"></a>

 **StringNode**

```
case class StringNode extends ScalarNode(value, TypeCode.STRING)  (
           value : String )
```

### StringNode val fields
<a name="glue-etl-scala-apis-glue-types-stringnode-case-class-vals"></a>
+ `ordering`

### StringNode def methods
<a name="glue-etl-scala-apis-glue-types-stringnode-case-class-defs"></a>

```
def equals( other : Any )
```

```
def this( value : UTF8String )
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
