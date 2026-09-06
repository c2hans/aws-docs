---
source_url: https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_RecommendationResourceSummary.html
---

# RecommendationResourceSummary
<a name="API_RecommendationResourceSummary"></a>

Summary of a Recommendation Resource

## Contents
<a name="API_RecommendationResourceSummary_Contents"></a>

 ** arn **   <a name="ta-Type-RecommendationResourceSummary-arn"></a>
The ARN of the Recommendation Resource
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w-]+:trustedadvisor::\d{12}:recommendation-resource\/[\w-]+\/[\w-]+`
Required: Yes

 ** awsResourceId **   <a name="ta-Type-RecommendationResourceSummary-awsResourceId"></a>
The AWS resource identifier. There are certain checks that generate recommendation resources without an awsResourceId.
Type: String
Required: Yes

 ** id **   <a name="ta-Type-RecommendationResourceSummary-id"></a>
The ID of the Recommendation Resource
Type: String
Required: Yes

 ** lastUpdatedAt **   <a name="ta-Type-RecommendationResourceSummary-lastUpdatedAt"></a>
When the Recommendation Resource was last updated
Type: Timestamp
Required: Yes

 ** metadata **   <a name="ta-Type-RecommendationResourceSummary-metadata"></a>
Metadata associated with the Recommendation Resource
Type: String to string map
Required: Yes

 ** recommendationArn **   <a name="ta-Type-RecommendationResourceSummary-recommendationArn"></a>
The Recommendation ARN
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w-]+:trustedadvisor::\d{12}:recommendation\/[\w-]+`
Required: Yes

 ** regionCode **   <a name="ta-Type-RecommendationResourceSummary-regionCode"></a>
The AWS Region code that the Recommendation Resource is in
Type: String
Length Constraints: Minimum length of 9. Maximum length of 20.
Required: Yes

 ** status **   <a name="ta-Type-RecommendationResourceSummary-status"></a>
The current status of the Recommendation Resource
Type: String
Valid Values: `ok | warning | error`
Required: Yes

 ** exclusionStatus **   <a name="ta-Type-RecommendationResourceSummary-exclusionStatus"></a>
The exclusion status of the Recommendation Resource
Type: String
Valid Values: `excluded | included`
Required: No

## See Also
<a name="API_RecommendationResourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/trustedadvisor-2022-09-15/RecommendationResourceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/trustedadvisor-2022-09-15/RecommendationResourceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/trustedadvisor-2022-09-15/RecommendationResourceSummary)
