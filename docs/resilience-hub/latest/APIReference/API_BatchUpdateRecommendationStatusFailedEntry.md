---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_BatchUpdateRecommendationStatusFailedEntry.html
---

# BatchUpdateRecommendationStatusFailedEntry
<a name="API_BatchUpdateRecommendationStatusFailedEntry"></a>

List of operational recommendations that did not get included or excluded.

## Contents
<a name="API_BatchUpdateRecommendationStatusFailedEntry_Contents"></a>

 ** entryId **   <a name="resiliencehub-Type-BatchUpdateRecommendationStatusFailedEntry-entryId"></a>
An identifier of an entry in this batch that is used to communicate the result.
The `entryId`s of a batch request need to be unique within a request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** errorMessage **   <a name="resiliencehub-Type-BatchUpdateRecommendationStatusFailedEntry-errorMessage"></a>
Indicates the error that occurred while excluding an operational recommendation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: Yes

## See Also
<a name="API_BatchUpdateRecommendationStatusFailedEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/BatchUpdateRecommendationStatusFailedEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/BatchUpdateRecommendationStatusFailedEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/BatchUpdateRecommendationStatusFailedEntry)
