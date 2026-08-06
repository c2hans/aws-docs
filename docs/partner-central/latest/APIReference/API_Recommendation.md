---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_Recommendation.html
---

# Recommendation
<a name="API_Recommendation"></a>

A recommendation from an agent-driven source.

## Contents
<a name="API_Recommendation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Details **   <a name="AWSPartnerCentral-Type-Recommendation-Details"></a>
Human-readable recommendation text from this source.
Type: String
Required: Yes

 ** Type **   <a name="AWSPartnerCentral-Type-Recommendation-Type"></a>
The recommendation source type. Known values: `OpportunityQuality`, `SolutionRecommendation`, `SpecialistRecommendation`.
Type: String
Required: Yes

 ** Attributes **   <a name="AWSPartnerCentral-Type-Recommendation-Attributes"></a>
Source-specific metadata as key-value pairs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 25 items.
Required: No

## See Also
<a name="API_Recommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/Recommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/Recommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/Recommendation)
