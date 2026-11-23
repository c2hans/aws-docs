---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_FeatureRecommendation.html
---

# FeatureRecommendation

A recommended AWS Marketplace feature for a listing.

## Contents
<a name="API_FeatureRecommendation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Action **   <a name="AWSMarketplaceService-Type-FeatureRecommendation-Action"></a>
What you should do. It might contain a link to the console.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** FeatureId **   <a name="AWSMarketplaceService-Type-FeatureRecommendation-FeatureId"></a>
The feature that is recommended. Valid values are `REQUEST_PRIVATE_OFFER`, `REQUEST_A_DEMO`, `PROMOTIONAL_MEDIA`, `FREE_TRIAL`, and `QUICK_LAUNCH`.
Type: String
Valid Values: `REQUEST_PRIVATE_OFFER | REQUEST_A_DEMO | PROMOTIONAL_MEDIA | FREE_TRIAL | QUICK_LAUNCH`
Required: Yes

 ** Rationale **   <a name="AWSMarketplaceService-Type-FeatureRecommendation-Rationale"></a>
Why the feature is recommended.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** Severity **   <a name="AWSMarketplaceService-Type-FeatureRecommendation-Severity"></a>
How much the recommendation blocks the listing. Valid values are `BLOCKING` and `ADVISORY`.
Type: String
Valid Values: `BLOCKING | ADVISORY`
Required: Yes

 ** Status **   <a name="AWSMarketplaceService-Type-FeatureRecommendation-Status"></a>
Whether the listing has the feature. Valid values are:
+  `PASS` - The listing already has the feature.
+  `FAIL` - The feature is one to turn on.
Type: String
Valid Values: `PASS | FAIL`
Required: Yes

## See Also
<a name="API_FeatureRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/FeatureRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/FeatureRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/FeatureRecommendation)
