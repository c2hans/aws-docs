---
source_url: https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_SuccessfulCampaignStateResponse.html
---

# SuccessfulCampaignStateResponse
<a name="API_connect-outbound-campaigns_SuccessfulCampaignStateResponse"></a>

The state response when the campaign is successful.

## Contents
<a name="API_connect-outbound-campaigns_SuccessfulCampaignStateResponse_Contents"></a>

 ** campaignId **   <a name="connect-Type-connect-outbound-campaigns_SuccessfulCampaignStateResponse-campaignId"></a>
The identifier of the campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-:/a-zA-Z0-9]+`
Required: No

 ** state **   <a name="connect-Type-connect-outbound-campaigns_SuccessfulCampaignStateResponse-state"></a>
The state of the campaign.
Type: String
Valid Values: `Initialized | Running | Paused | Stopped | Failed`
Required: No

## See Also
<a name="API_connect-outbound-campaigns_SuccessfulCampaignStateResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/SuccessfulCampaignStateResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/SuccessfulCampaignStateResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/SuccessfulCampaignStateResponse)
