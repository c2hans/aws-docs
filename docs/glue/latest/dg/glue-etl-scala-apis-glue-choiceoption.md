---
source_url: https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-choiceoption.html
---

# AWS Glue Scala ChoiceOption APIs
<a name="glue-etl-scala-apis-glue-choiceoption"></a>

**Topics**
+ [ChoiceOption trait](#glue-etl-scala-apis-glue-choiceoption-trait)
+ [ChoiceOption object](#glue-etl-scala-apis-glue-choiceoption-object)
+ [Case class ChoiceOptionWithResolver](#glue-etl-scala-apis-glue-choiceoptionwithresolver-case-class)
+ [Case class MatchCatalogSchemaChoiceOption](#glue-etl-scala-apis-glue-matchcatalogschemachoiceoption-case-class)

**Package: com.amazonaws.services.glue**

## ChoiceOption trait
<a name="glue-etl-scala-apis-glue-choiceoption-trait"></a>

```
trait ChoiceOption extends Serializable
```

## ChoiceOption object
<a name="glue-etl-scala-apis-glue-choiceoption-object"></a>

 **ChoiceOption**

```
object ChoiceOption
```

A general strategy to resolve choice applicable to all `ChoiceType` nodes in a `DynamicFrame`.
+ `val CAST`
+ `val MAKE_COLS`
+ `val MAKE_STRUCT`
+ `val MATCH_CATALOG`
+ `val PROJECT`

### Def apply
<a name="glue-etl-scala-apis-glue-choiceoption-object-def-apply"></a>

```
def apply(choice: String): ChoiceOption
```

## Case class ChoiceOptionWithResolver
<a name="glue-etl-scala-apis-glue-choiceoptionwithresolver-case-class"></a>

```
case class ChoiceOptionWithResolver(name: String, choiceResolver: ChoiceResolver) extends ChoiceOption {}
```

## Case class MatchCatalogSchemaChoiceOption
<a name="glue-etl-scala-apis-glue-matchcatalogschemachoiceoption-case-class"></a>

```
case class MatchCatalogSchemaChoiceOption() extends ChoiceOption {}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
