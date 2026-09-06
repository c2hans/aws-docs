---
source_url: https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_CampaignSummary.html
---

# CampaignSummary
<a name="API_connect-outbound-campaigns_CampaignSummary"></a>

Contains summary information about an outbound campaign.

## Contents
<a name="API_connect-outbound-campaigns_CampaignSummary_Contents"></a>

 ** arn **   <a name="connect-Type-connect-outbound-campaigns_CampaignSummary-arn"></a>
The Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 500.
Required: Yes

 ** connectInstanceId **   <a name="connect-Type-connect-outbound-campaigns_CampaignSummary-connectInstanceId"></a>
The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-_.a-zA-Z0-9]+`
Required: Yes

 ** id **   <a name="connect-Type-connect-outbound-campaigns_CampaignSummary-id"></a>
The identifier of the campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-:/a-zA-Z0-9]+`
Required: Yes

 ** name **   <a name="connect-Type-connect-outbound-campaigns_CampaignSummary-name"></a>
The name of the campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: Yes

## See Also
<a name="API_connect-outbound-campaigns_CampaignSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/CampaignSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/CampaignSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/CampaignSummary)
