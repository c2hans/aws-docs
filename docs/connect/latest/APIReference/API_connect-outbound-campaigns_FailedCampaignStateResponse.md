---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns_FailedCampaignStateResponse.html
---

# FailedCampaignStateResponse
<a name="API_connect-outbound-campaigns_FailedCampaignStateResponse"></a>

Contains information about a failed campaign.

## Contents
<a name="API_connect-outbound-campaigns_FailedCampaignStateResponse_Contents"></a>

 ** campaignId **   <a name="connect-Type-connect-outbound-campaigns_FailedCampaignStateResponse-campaignId"></a>
The identifier of the campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-:/a-zA-Z0-9]+`
Required: No

 ** failureCode **   <a name="connect-Type-connect-outbound-campaigns_FailedCampaignStateResponse-failureCode"></a>
The failure code of the campaign.
Type: String
Valid Values: `ResourceNotFound | UnknownError`
Required: No

## See Also
<a name="API_connect-outbound-campaigns_FailedCampaignStateResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/FailedCampaignStateResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/FailedCampaignStateResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/FailedCampaignStateResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
