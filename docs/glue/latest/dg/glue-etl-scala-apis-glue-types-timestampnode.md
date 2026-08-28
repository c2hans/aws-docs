---
source_url: https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-timestampnode.html
---

# AWS Glue Scala TimestampNode APIs
<a name="glue-etl-scala-apis-glue-types-timestampnode"></a>

**Package: com.amazonaws.services.glue.types**

## TimestampNode case class
<a name="glue-etl-scala-apis-glue-types-timestampnode-case-class"></a>

**TimestampNode**

```
case class TimestampNode extends ScalarNode(value, TypeCode.TIMESTAMP)  (
           value : Timestamp )
```

### TimestampNode val fields
<a name="glue-etl-scala-apis-glue-types-timestampnode-case-class-vals"></a>
+ `ordering`

### TimestampNode def methods
<a name="glue-etl-scala-apis-glue-types-timestampnode-case-class-defs"></a>

```
def equals( other : Any )
```

```
def this( value : Long )
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
