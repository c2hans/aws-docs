---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_PreEvaluationFilter.html
---

# PreEvaluationFilter
<a name="API_PreEvaluationFilter"></a>

A single pre-evaluation filter condition. Specifies a resource type, filter type, key, value, and operator to match against a resource attribute.

## Contents
<a name="API_PreEvaluationFilter_Contents"></a>

 ** FilterKey **   <a name="connect-Type-PreEvaluationFilter-FilterKey"></a>
The key of the attribute to filter on. For tag filters, this is the tag key.
Type: String
Required: Yes

 ** FilterType **   <a name="connect-Type-PreEvaluationFilter-FilterType"></a>
The type of filter to apply. Valid values: `TAG`.
Type: String
Valid Values: `TAG`
Required: Yes

 ** FilterValue **   <a name="connect-Type-PreEvaluationFilter-FilterValue"></a>
The value to match against. For tag filters, this is the tag value.
Type: String
Required: Yes

 ** Operator **   <a name="connect-Type-PreEvaluationFilter-Operator"></a>
The comparison operator for the filter condition. Valid values: `EQUALS`.
Type: String
Valid Values: `EQUALS`
Required: Yes

 ** ResourceType **   <a name="connect-Type-PreEvaluationFilter-ResourceType"></a>
The type of resource to filter on. Valid values: `CONTACT`.
Type: String
Valid Values: `CONTACT`
Required: Yes

## See Also
<a name="API_PreEvaluationFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/PreEvaluationFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/PreEvaluationFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/PreEvaluationFilter)
