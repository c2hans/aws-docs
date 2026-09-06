---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_FailedCampaignStateResponse.html
---

# FailedCampaignStateResponse
<a name="API_connect-outbound-campaigns-v2_FailedCampaignStateResponse"></a>

Contains information about a failed campaign.

## Contents
<a name="API_connect-outbound-campaigns-v2_FailedCampaignStateResponse_Contents"></a>

 ** campaignId **   <a name="connect-Type-connect-outbound-campaigns-v2_FailedCampaignStateResponse-campaignId"></a>
The identifier of the outbound campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-:/a-zA-Z0-9]+`
Required: No

 ** failureCode **   <a name="connect-Type-connect-outbound-campaigns-v2_FailedCampaignStateResponse-failureCode"></a>
The failure code of the campaign.
Type: String
Valid Values: `ResourceNotFound | UnknownError`
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_FailedCampaignStateResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/FailedCampaignStateResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/FailedCampaignStateResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/FailedCampaignStateResponse)
