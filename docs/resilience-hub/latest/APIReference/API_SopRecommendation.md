---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_SopRecommendation.html
---

# SopRecommendation
<a name="API_SopRecommendation"></a>

Defines a standard operating procedure (SOP) recommendation.

## Contents
<a name="API_SopRecommendation_Contents"></a>

 ** recommendationId **   <a name="resiliencehub-Type-SopRecommendation-recommendationId"></a>
Identifier for the SOP recommendation.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}`
Required: Yes

 ** referenceId **   <a name="resiliencehub-Type-SopRecommendation-referenceId"></a>
Reference identifier for the SOP recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** serviceType **   <a name="resiliencehub-Type-SopRecommendation-serviceType"></a>
The service type.
Type: String
Valid Values: `SSM`
Required: Yes

 ** appComponentName **   <a name="resiliencehub-Type-SopRecommendation-appComponentName"></a>
Name of the AppComponent.
Type: String
Pattern: `\S{1,255}`
Required: No

 ** description **   <a name="resiliencehub-Type-SopRecommendation-description"></a>
Description of the SOP recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** items **   <a name="resiliencehub-Type-SopRecommendation-items"></a>
The recommendation items.
Type: Array of [RecommendationItem](API_RecommendationItem.md) objects
Required: No

 ** name **   <a name="resiliencehub-Type-SopRecommendation-name"></a>
Name of the SOP recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** prerequisite **   <a name="resiliencehub-Type-SopRecommendation-prerequisite"></a>
Prerequisite for the SOP recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** recommendationStatus **   <a name="resiliencehub-Type-SopRecommendation-recommendationStatus"></a>
Status of the recommended standard operating procedure.
Type: String
Valid Values: `Implemented | Inactive | NotImplemented | Excluded`
Required: No

## See Also
<a name="API_SopRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/SopRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/SopRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/SopRecommendation)
