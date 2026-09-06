---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_RightsizingRecommendationMetadata.html
---

# RightsizingRecommendationMetadata
<a name="API_RightsizingRecommendationMetadata"></a>

Metadata for a recommendation set.

## Contents
<a name="API_RightsizingRecommendationMetadata_Contents"></a>

 ** AdditionalMetadata **   <a name="awscostmanagement-Type-RightsizingRecommendationMetadata-AdditionalMetadata"></a>
Additional metadata that might be applicable to the recommendation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** GenerationTimestamp **   <a name="awscostmanagement-Type-RightsizingRecommendationMetadata-GenerationTimestamp"></a>
The timestamp for when AWS made the recommendation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** LookbackPeriodInDays **   <a name="awscostmanagement-Type-RightsizingRecommendationMetadata-LookbackPeriodInDays"></a>
The number of days of previous usage that AWS considers when making the recommendation.
Type: String
Valid Values: `SEVEN_DAYS | THIRTY_DAYS | SIXTY_DAYS`
Required: No

 ** RecommendationId **   <a name="awscostmanagement-Type-RightsizingRecommendationMetadata-RecommendationId"></a>
The ID for the recommendation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_RightsizingRecommendationMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/RightsizingRecommendationMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/RightsizingRecommendationMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/RightsizingRecommendationMetadata)
