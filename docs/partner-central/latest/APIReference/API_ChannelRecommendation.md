---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ChannelRecommendation.html
---

# ChannelRecommendation

Aggregated outreach guidance for leads that share the same country, geography, region, and company segment. It names the outreach channel most commonly recommended for that group and, optionally, the days and times that channel is best used. This is group-level guidance. It doesn't describe an individual lead's contact history or rank recommendations for a specific lead.

## Contents
<a name="API_ChannelRecommendation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RecommendedChannel **   <a name="AWSPartnerCentral-Type-ChannelRecommendation-RecommendedChannel"></a>
The recommended outreach channel for the group of similar leads. Valid values are `EMAIL` and `CALL`.
Type: String
Required: Yes

 ** BestOutreachWindows **   <a name="AWSPartnerCentral-Type-ChannelRecommendation-BestOutreachWindows"></a>
The recommended day-specific outreach windows for the recommended channel, expressed in Coordinated Universal Time (UTC). Each window applies to one day, and more than one window can fall on the same day. This field is optional and appears only when window guidance is available.
Type: Array of [BestOutreachWindow](API_BestOutreachWindow.md) objects
Array Members: Minimum number of 1 item. Maximum number of 7 items.
Required: No

## See Also
<a name="API_ChannelRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ChannelRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ChannelRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ChannelRecommendation)
