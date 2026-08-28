---
source_url: https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame.html
---

# ErrorsAsDynamicFrame class
<a name="aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame"></a>

Returns a `DynamicFrame` that contains nested records for errors that occurred while the source `DynamicFrame` was created.

## Example
<a name="pyspark-ErrorsAsDynamicFrame-examples"></a>

We recommend that you use the [`DynamicFrame.errorsAsDynamicFrame()`](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-errorsAsDynamicFrame) method to retrieve and view error records. To view a code example, see [Example: Use errorsAsDynamicFrame to view error records](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-errorsAsDynamicFrame-example).

## Methods
<a name="aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-_methods"></a>
+ [\_\_call\_\_](#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-__call__)
+ [apply](#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-apply)
+ [name](#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-name)
+ [describeArgs](#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-describeArgs)
+ [describeReturn](#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-describeReturn)
+ [describeTransform](#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-describeTransform)
+ [describeErrors](#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-describeErrors)
+ [Describe](#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-describe)

## \_\_call\_\_(frame)
<a name="aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-__call__"></a>

Returns a `DynamicFrame` that contains nested error records that relate to the source `DynamicFrame`.
+ `frame` – The source `DynamicFrame` (required).

## apply(cls, \*args, \*\*kwargs)
<a name="aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-apply"></a>
+ `cls` – cls

## name(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-name"></a>
+ `cls` – cls

## describeArgs(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-describeArgs"></a>
+ `cls` – cls

## describeReturn(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-describeReturn"></a>
+ `cls` – cls

## describeTransform(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-describeTransform"></a>
+ `cls` – cls

## describeErrors(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-describeErrors"></a>
+ `cls` – cls

## describe(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-describe"></a>
+ `cls` – cls

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
