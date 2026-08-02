---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_RecommendationItem.html
---

# RecommendationItem
<a name="API_RecommendationItem"></a>

Defines a recommendation.

## Contents
<a name="API_RecommendationItem_Contents"></a>

 ** alreadyImplemented **   <a name="resiliencehub-Type-RecommendationItem-alreadyImplemented"></a>
Specifies if the recommendation has already been implemented.
Type: Boolean
Required: No

 ** discoveredAlarm **   <a name="resiliencehub-Type-RecommendationItem-discoveredAlarm"></a>
Indicates the previously implemented Amazon CloudWatch alarm discovered by AWS Resilience Hub.
Type: [Alarm](API_Alarm.md) object
Required: No

 ** excluded **   <a name="resiliencehub-Type-RecommendationItem-excluded"></a>
Indicates if an operational recommendation item is excluded.
Type: Boolean
Required: No

 ** excludeReason **   <a name="resiliencehub-Type-RecommendationItem-excludeReason"></a>
Indicates the reason for excluding an operational recommendation.
Type: String
Valid Values: `AlreadyImplemented | NotRelevant | ComplexityOfImplementation`
Required: No

 ** latestDiscoveredExperiment **   <a name="resiliencehub-Type-RecommendationItem-latestDiscoveredExperiment"></a>
Indicates the experiment created in AWS FIS that was discovered by AWS Resilience Hub, which matches the recommendation.
Type: [Experiment](API_Experiment.md) object
Required: No

 ** resourceId **   <a name="resiliencehub-Type-RecommendationItem-resourceId"></a>
Identifier of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** targetAccountId **   <a name="resiliencehub-Type-RecommendationItem-targetAccountId"></a>
Identifier of the target account.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** targetRegion **   <a name="resiliencehub-Type-RecommendationItem-targetRegion"></a>
The target region.
Type: String
Pattern: `[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]`
Required: No

## See Also
<a name="API_RecommendationItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/RecommendationItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/RecommendationItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/RecommendationItem)
