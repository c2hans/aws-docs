---
source_url: https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-resolvespec.html
---

# AWS Glue Scala ResolveSpec APIs
<a name="glue-etl-scala-apis-glue-resolvespec"></a>

**Topics**
+ [ResolveSpec object](#glue-etl-scala-apis-glue-resolvespec-object)
+ [ResolveSpec case class](#glue-etl-scala-apis-glue-resolvespec-case-class)

**Package: com.amazonaws.services.glue**

## ResolveSpec object
<a name="glue-etl-scala-apis-glue-resolvespec-object"></a>

 **ResolveSpec**

```
object ResolveSpec
```

### Def
<a name="glue-etl-scala-apis-glue-resolvespec-object-def-apply_1"></a>

```
def apply( path : String,
           action : String
         ) : ResolveSpec
```

Creates a `ResolveSpec`.
+ `path` — A string representation of the choice field that needs to be resolved.
+ `action` — A resolution action. The action can be one of the following: `Project`, `KeepAsStruct`, or `Cast`.

Returns the `ResolveSpec`.

### Def
<a name="glue-etl-scala-apis-glue-resolvespec-object-def-apply_2"></a>

```
def apply( product : Product2[String, String] ) : ResolveSpec
```

Creates a `ResolveSpec`.
+ `product` — `Product2` of: source path, resolution action.

Returns the `ResolveSpec`.

## ResolveSpec case class
<a name="glue-etl-scala-apis-glue-resolvespec-case-class"></a>

```
case class ResolveSpec extends Product2[String, String]  (
           path : SchemaPath,
           action : String )
```

Creates a `ResolveSpec`.
+ `path` — The `SchemaPath` of the choice field that needs to be resolved.
+ `action` — A resolution action. The action can be one of the following: `Project`, `KeepAsStruct`, or `Cast`.

### ResolveSpec def methods
<a name="glue-etl-scala-apis-glue-resolvespec-case-class-defs"></a>

```
def _1 : String
```

```
def _2 : String
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
