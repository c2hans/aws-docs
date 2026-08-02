---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Aggregate.html
---

# Aggregate
<a name="API_Aggregate"></a>

Specifies a transform that groups rows by chosen fields and computes the aggregated value by specified function.

## Contents
<a name="API_Aggregate_Contents"></a>

 ** Aggs **   <a name="Glue-Type-Aggregate-Aggs"></a>
Specifies the aggregate functions to be performed on specified fields.
Type: Array of [AggregateOperation](API_AggregateOperation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Required: Yes

 ** Groups **   <a name="Glue-Type-Aggregate-Groups"></a>
Specifies the fields to group by.
Type: Array of arrays of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Inputs **   <a name="Glue-Type-Aggregate-Inputs"></a>
Specifies the fields and rows to use as inputs for the aggregate transform.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-Aggregate-Name"></a>
The name of the transform node.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

## See Also
<a name="API_Aggregate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Aggregate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Aggregate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Aggregate)
