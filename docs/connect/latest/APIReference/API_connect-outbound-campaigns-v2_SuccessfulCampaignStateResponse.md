---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_SuccessfulCampaignStateResponse.html
---

# SuccessfulCampaignStateResponse
<a name="API_connect-outbound-campaigns-v2_SuccessfulCampaignStateResponse"></a>

The state response when the campaign is successful.

## Contents
<a name="API_connect-outbound-campaigns-v2_SuccessfulCampaignStateResponse_Contents"></a>

 ** campaignId **   <a name="connect-Type-connect-outbound-campaigns-v2_SuccessfulCampaignStateResponse-campaignId"></a>
The identifier of the outbound campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-:/a-zA-Z0-9]+`
Required: No

 ** state **   <a name="connect-Type-connect-outbound-campaigns-v2_SuccessfulCampaignStateResponse-state"></a>
The state of the outbound campaign.
Type: String
Valid Values: `Initialized | Running | Paused | Stopped | Failed | Completed`
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_SuccessfulCampaignStateResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/SuccessfulCampaignStateResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/SuccessfulCampaignStateResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/SuccessfulCampaignStateResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
