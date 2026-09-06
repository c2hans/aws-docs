---
source_url: https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_OrganizationRecommendationResourceSummary.html
---

# OrganizationRecommendationResourceSummary
<a name="API_OrganizationRecommendationResourceSummary"></a>

Organization Recommendation Resource Summary

## Contents
<a name="API_OrganizationRecommendationResourceSummary_Contents"></a>

 ** arn **   <a name="ta-Type-OrganizationRecommendationResourceSummary-arn"></a>
The ARN of the Recommendation Resource
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w-]+:trustedadvisor::\d{12}:recommendation-resource\/[\w-]+\/[\w-]+`
Required: Yes

 ** awsResourceId **   <a name="ta-Type-OrganizationRecommendationResourceSummary-awsResourceId"></a>
The AWS resource identifier. There are certain checks that generate recommendation resources without an awsResourceId.
Type: String
Required: Yes

 ** id **   <a name="ta-Type-OrganizationRecommendationResourceSummary-id"></a>
The ID of the Recommendation Resource
Type: String
Required: Yes

 ** lastUpdatedAt **   <a name="ta-Type-OrganizationRecommendationResourceSummary-lastUpdatedAt"></a>
When the Recommendation Resource was last updated
Type: Timestamp
Required: Yes

 ** metadata **   <a name="ta-Type-OrganizationRecommendationResourceSummary-metadata"></a>
Metadata associated with the Recommendation Resource
Type: String to string map
Required: Yes

 ** recommendationArn **   <a name="ta-Type-OrganizationRecommendationResourceSummary-recommendationArn"></a>
The Recommendation ARN
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w-]+:trustedadvisor:::organization-recommendation\/[\w-]+`
Required: Yes

 ** regionCode **   <a name="ta-Type-OrganizationRecommendationResourceSummary-regionCode"></a>
The AWS Region code that the Recommendation Resource is in
Type: String
Length Constraints: Minimum length of 9. Maximum length of 20.
Required: Yes

 ** status **   <a name="ta-Type-OrganizationRecommendationResourceSummary-status"></a>
The current status of the Recommendation Resource
Type: String
Valid Values: `ok | warning | error`
Required: Yes

 ** accountId **   <a name="ta-Type-OrganizationRecommendationResourceSummary-accountId"></a>
The AWS account ID
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

 ** exclusionStatus **   <a name="ta-Type-OrganizationRecommendationResourceSummary-exclusionStatus"></a>
The exclusion status of the Recommendation Resource
Type: String
Valid Values: `excluded | included`
Required: No

## See Also
<a name="API_OrganizationRecommendationResourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/trustedadvisor-2022-09-15/OrganizationRecommendationResourceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/trustedadvisor-2022-09-15/OrganizationRecommendationResourceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/trustedadvisor-2022-09-15/OrganizationRecommendationResourceSummary)
