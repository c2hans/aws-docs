---
source_url: https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-dynamicframe-object.html
---

# The DynamicFrame object
<a name="glue-etl-scala-apis-glue-dynamicframe-object"></a>

**Package: com.amazonaws.services.glue**

```
object DynamicFrame
```

## Def apply
<a name="glue-etl-scala-apis-glue-dynamicframe-object-defs-apply"></a>

```
def apply( df : DataFrame,
           glueContext : GlueContext
         ) : DynamicFrame
```

## Def emptyDynamicFrame
<a name="glue-etl-scala-apis-glue-dynamicframe-object-defs-emptyDynamicFrame"></a>

```
def emptyDynamicFrame( glueContext : GlueContext ) : DynamicFrame
```

## Def fromPythonRDD
<a name="glue-etl-scala-apis-glue-dynamicframe-object-defs-fromPythonRDD"></a>

```
def fromPythonRDD( rdd : JavaRDD[Array[Byte]],
                   glueContext : GlueContext
                 ) : DynamicFrame
```

## Def ignoreErrors
<a name="glue-etl-scala-apis-glue-dynamicframe-object-defs-ignoreErrors"></a>

```
def ignoreErrors( fn : DynamicRecord => DynamicRecord ) : DynamicRecord
```

## Def inlineErrors
<a name="glue-etl-scala-apis-glue-dynamicframe-object-defs-inlineErrors"></a>

```
def inlineErrors( msg : String,
                  callSite : CallSite
                ) : (DynamicRecord => DynamicRecord)
```

## Def newFrameWithErrors
<a name="glue-etl-scala-apis-glue-dynamicframe-object-defs-newFrameWithErrors"></a>

```
def newFrameWithErrors( prevFrame : DynamicFrame,
                        rdd : RDD[DynamicRecord],
                        name : String = "",
                        transformationContext : String = "",
                        callSite : CallSite,
                        stageThreshold : Long,
                        totalThreshold : Long
                      ) : DynamicFrame
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
