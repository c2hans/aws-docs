---
source_url: https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-decimalnode.html
---

# AWS Glue Scala DecimalNode APIs
<a name="glue-etl-scala-apis-glue-types-decimalnode"></a>

**Package: com.amazonaws.services.glue.types**

## DecimalNode case class
<a name="glue-etl-scala-apis-glue-types-decimalnode-case-class"></a>

 **DecimalNode**

```
case class DecimalNode extends ScalarNode(value, TypeCode.DECIMAL)  (
           value : BigDecimal )
```

### DecimalNode val fields
<a name="glue-etl-scala-apis-glue-types-decimalnode-case-class-vals"></a>
+ `ordering`

### DecimalNode def methods
<a name="glue-etl-scala-apis-glue-types-decimalnode-case-class-defs"></a>

```
def equals( other : Any )
```

```
def this( value : Decimal )
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
