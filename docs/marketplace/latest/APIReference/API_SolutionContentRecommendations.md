---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_SolutionContentRecommendations.html
---

# SolutionContentRecommendations

The content recommendations for a solution listing, with one member for each listing field. A member is absent if nothing is recommended for that field.

## Contents
<a name="API_SolutionContentRecommendations_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Citations **   <a name="AWSMarketplaceService-Type-SolutionContentRecommendations-Citations"></a>
The sources that the recommendations are based on. You can have up to 5 sources. The list is empty if there are none.
Type: Array of [RecommendationCitation](API_RecommendationCitation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: Yes

 ** AdditionalResources **   <a name="AWSMarketplaceService-Type-SolutionContentRecommendations-AdditionalResources"></a>
The recommendation for the additional resources. Each alternative has up to 8 resources.
Type: [ContentRecommendation](API_ContentRecommendation.md) object
Required: No

 ** CaseStudies **   <a name="AWSMarketplaceService-Type-SolutionContentRecommendations-CaseStudies"></a>
The recommendation for the case studies of the solution. Each alternative has up to 20 case studies.
Type: [ContentRecommendation](API_ContentRecommendation.md) object
Required: No

 ** IntegrationDetails **   <a name="AWSMarketplaceService-Type-SolutionContentRecommendations-IntegrationDetails"></a>
The recommendation for the integration details of the solution.
Type: [ContentRecommendation](API_ContentRecommendation.md) object
Required: No

 ** LongDescription **   <a name="AWSMarketplaceService-Type-SolutionContentRecommendations-LongDescription"></a>
The recommendation for the long description of the solution.
Type: [ContentRecommendation](API_ContentRecommendation.md) object
Required: No

 ** ShortDescription **   <a name="AWSMarketplaceService-Type-SolutionContentRecommendations-ShortDescription"></a>
The recommendation for the value proposition of the solution.
Type: [ContentRecommendation](API_ContentRecommendation.md) object
Required: No

 ** Title **   <a name="AWSMarketplaceService-Type-SolutionContentRecommendations-Title"></a>
The recommendation for the external title of the solution.
Type: [ContentRecommendation](API_ContentRecommendation.md) object
Required: No

 ** UseCases **   <a name="AWSMarketplaceService-Type-SolutionContentRecommendations-UseCases"></a>
The recommendation for the use cases of the solution.
Type: [ContentRecommendation](API_ContentRecommendation.md) object
Required: No

## See Also
<a name="API_SolutionContentRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/SolutionContentRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/SolutionContentRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/SolutionContentRecommendations)
