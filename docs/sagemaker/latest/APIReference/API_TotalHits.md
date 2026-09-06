---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TotalHits.html
---

# TotalHits
<a name="API_TotalHits"></a>

Represents the total number of matching results and indicates how accurate that count is.

The `Value` field provides the count, which may be exact or estimated. The `Relation` field indicates whether it's an exact figure or a lower bound. This helps understand the full scope of search results, especially when dealing with large result sets.

## Contents
<a name="API_TotalHits_Contents"></a>

 ** Relation **   <a name="sagemaker-Type-TotalHits-Relation"></a>
Indicates the relationship between the returned `Value` and the actual total number of matching results. Possible values are:
+  `EqualTo`: The `Value` is the exact count of matching results.
+  `GreaterThanOrEqualTo`: The `Value` is a lower bound of the actual count of matching results.
Type: String
Valid Values: `EqualTo | GreaterThanOrEqualTo`
Required: No

 ** Value **   <a name="sagemaker-Type-TotalHits-Value"></a>
The total number of matching results. This value may be exact or an estimate, depending on the `Relation` field.
Type: Long
Required: No

## See Also
<a name="API_TotalHits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TotalHits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TotalHits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TotalHits)
