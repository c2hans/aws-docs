---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_UpdateRecommendationStatusRequestEntry.html
---

# UpdateRecommendationStatusRequestEntry
<a name="API_UpdateRecommendationStatusRequestEntry"></a>

Defines the operational recommendation item that is to be included or excluded.

## Contents
<a name="API_UpdateRecommendationStatusRequestEntry_Contents"></a>

 ** entryId **   <a name="resiliencehub-Type-UpdateRecommendationStatusRequestEntry-entryId"></a>
An identifier for an entry in this batch that is used to communicate the result.
The `entryId`s of a batch request need to be unique within a request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** excluded **   <a name="resiliencehub-Type-UpdateRecommendationStatusRequestEntry-excluded"></a>
Indicates if the operational recommendation needs to be excluded. If set to True, the operational recommendation will be excluded.
Type: Boolean
Required: Yes

 ** referenceId **   <a name="resiliencehub-Type-UpdateRecommendationStatusRequestEntry-referenceId"></a>
Reference identifier of the operational recommendation item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** appComponentId **   <a name="resiliencehub-Type-UpdateRecommendationStatusRequestEntry-appComponentId"></a>
Indicates the identifier of the AppComponent.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{0,254}`
Required: No

 ** excludeReason **   <a name="resiliencehub-Type-UpdateRecommendationStatusRequestEntry-excludeReason"></a>
Indicates the reason for excluding an operational recommendation.
Type: String
Valid Values: `AlreadyImplemented | NotRelevant | ComplexityOfImplementation`
Required: No

 ** item **   <a name="resiliencehub-Type-UpdateRecommendationStatusRequestEntry-item"></a>
The operational recommendation item.
Type: [UpdateRecommendationStatusItem](API_UpdateRecommendationStatusItem.md) object
Required: No

## See Also
<a name="API_UpdateRecommendationStatusRequestEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/UpdateRecommendationStatusRequestEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/UpdateRecommendationStatusRequestEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/UpdateRecommendationStatusRequestEntry)
