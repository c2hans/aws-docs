---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_LeadInsights.html
---

# LeadInsights

Contains insights that AI generates for a lead. These insights provide automated analysis to help partners evaluate the lead quality and prioritize engagement efforts.

## Contents
<a name="API_LeadInsights_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ChannelRecommendation **   <a name="AWSPartnerCentral-Type-LeadInsights-ChannelRecommendation"></a>
The outreach channel most commonly recommended for leads that share this lead's country, geography, region, and company segment. It includes the days and the Coordinated Universal Time (UTC) hours when that channel is best used. This is guidance for the group of similar leads. It doesn't describe this lead's own contact history. Present only when a recommendation is available for the lead.
Type: [ChannelRecommendation](API_ChannelRecommendation.md) object
Required: No

 ** LeadReadinessScore **   <a name="AWSPartnerCentral-Type-LeadInsights-LeadReadinessScore"></a>
A score that indicates the lead's readiness for engagement. Valid values are `Low`, `Medium`, and `High`. Use this score to prioritize leads based on their likelihood of conversion.
Type: String
Required: No

## See Also
<a name="API_LeadInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/LeadInsights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/LeadInsights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/LeadInsights)
