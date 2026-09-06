---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_MetricFilter.html
---

# MetricFilter
<a name="API_MetricFilter"></a>

A filter condition applied to a metric component in a calculation. Filters restrict the data included in the metric computation.

## Contents
<a name="API_MetricFilter_Contents"></a>

 ** MetricFilterKey **   <a name="connect-Type-MetricFilter-MetricFilterKey"></a>
The key identifying the field to filter on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** BooleanCondition **   <a name="connect-Type-MetricFilter-BooleanCondition"></a>
A boolean comparison condition.
Type: [MetricFilterBooleanCondition](API_MetricFilterBooleanCondition.md) object
Required: No

 ** Negate **   <a name="connect-Type-MetricFilter-Negate"></a>
Specifies whether the filter condition is negated. When set to `true`, the filter excludes matching data instead of including it.
Type: Boolean
Required: No

 ** NumberCondition **   <a name="connect-Type-MetricFilter-NumberCondition"></a>
A numeric comparison condition.
Type: [MetricFilterNumberCondition](API_MetricFilterNumberCondition.md) object
Required: No

 ** StringCondition **   <a name="connect-Type-MetricFilter-StringCondition"></a>
A string comparison condition.
Type: [MetricFilterStringCondition](API_MetricFilterStringCondition.md) object
Required: No

## See Also
<a name="API_MetricFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/MetricFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/MetricFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/MetricFilter)
