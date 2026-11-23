---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ContentRecommendation.html
---

# ContentRecommendation

A recommendation for a listing field.

## Contents
<a name="API_ContentRecommendation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Alternatives **   <a name="AWSMarketplaceService-Type-ContentRecommendation-Alternatives"></a>
The proposed values for the field, in ranked order.
Type: [ContentAlternatives](API_ContentAlternatives.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** Findings **   <a name="AWSMarketplaceService-Type-ContentRecommendation-Findings"></a>
The checklist of criteria for the field, in ranked order. It includes the criteria that the field passes and the criteria that it fails. The list is empty if there are none.
Type: Array of [ListingFinding](API_ListingFinding.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Required: Yes

 ** FollowUpQuestions **   <a name="AWSMarketplaceService-Type-ContentRecommendation-FollowUpQuestions"></a>
Questions that you can answer to get a better recommendation. The list is empty if there are none.
Type: Array of [FollowUpQuestion](API_FollowUpQuestion.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: Yes

 ** Status **   <a name="AWSMarketplaceService-Type-ContentRecommendation-Status"></a>
The status of the recommendation. Valid values are:
+  `GENERATED` - The service proposed values for the field.
+  `INSUFFICIENT_CONTEXT` - The service couldn't propose a value. The follow-up questions say what is missing.
Type: String
Valid Values: `GENERATED | INSUFFICIENT_CONTEXT`
Required: Yes

## See Also
<a name="API_ContentRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ContentRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ContentRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ContentRecommendation)
