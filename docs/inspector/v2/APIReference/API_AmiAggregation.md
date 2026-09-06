---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AmiAggregation.html
---

# AmiAggregation
<a name="API_AmiAggregation"></a>

The details that define an aggregation based on Amazon machine images (AMIs).

## Contents
<a name="API_AmiAggregation_Contents"></a>

 ** amis **   <a name="inspector2-Type-AmiAggregation-amis"></a>
The IDs of AMIs to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** sortBy **   <a name="inspector2-Type-AmiAggregation-sortBy"></a>
The value to sort results by.
Type: String
Valid Values: `CRITICAL | HIGH | ALL | AFFECTED_INSTANCES`
Required: No

 ** sortOrder **   <a name="inspector2-Type-AmiAggregation-sortOrder"></a>
The order to sort results by.
Type: String
Valid Values: `ASC | DESC`
Required: No

## See Also
<a name="API_AmiAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AmiAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AmiAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AmiAggregation)
