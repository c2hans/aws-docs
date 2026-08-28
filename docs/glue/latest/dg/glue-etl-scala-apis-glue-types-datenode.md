---
source_url: https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-datenode.html
---

# AWS Glue Scala DateNode APIs
<a name="glue-etl-scala-apis-glue-types-datenode"></a>

**Package: com.amazonaws.services.glue.types**

## DateNode case class
<a name="glue-etl-scala-apis-glue-types-datenode-case-class"></a>

 **DateNode**

```
case class DateNode extends ScalarNode(value, TypeCode.DATE)  (
           value : Date )
```

### DateNode val fields
<a name="glue-etl-scala-apis-glue-types-datenode-case-class-vals"></a>
+ `ordering`

### DateNode def methods
<a name="glue-etl-scala-apis-glue-types-datenode-case-class-defs"></a>

```
def equals( other : Any )
```

```
def this( value : Int )
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
