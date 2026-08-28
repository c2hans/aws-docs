---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_CampaignSummary.html
---

# CampaignSummary
<a name="API_connect-outbound-campaigns-v2_CampaignSummary"></a>

Contains summary information about an outbound campaign.

## Contents
<a name="API_connect-outbound-campaigns-v2_CampaignSummary_Contents"></a>

 ** arn **   <a name="connect-Type-connect-outbound-campaigns-v2_CampaignSummary-arn"></a>
The Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 500.
Required: Yes

 ** channelSubtypes **   <a name="connect-Type-connect-outbound-campaigns-v2_CampaignSummary-channelSubtypes"></a>
The channel subtypes of the outbound campaign.
Type: Array of strings
Valid Values: `TELEPHONY | SMS | EMAIL | WHATSAPP`
Required: Yes

 ** connectInstanceId **   <a name="connect-Type-connect-outbound-campaigns-v2_CampaignSummary-connectInstanceId"></a>
The identifier of the Connect Customer instance. You can find the `instanceId` in the ARN of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-_.a-zA-Z0-9]+`
Required: Yes

 ** id **   <a name="connect-Type-connect-outbound-campaigns-v2_CampaignSummary-id"></a>
The identifier of the outbound campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-:/a-zA-Z0-9]+`
Required: Yes

 ** name **   <a name="connect-Type-connect-outbound-campaigns-v2_CampaignSummary-name"></a>
The name of the outbound campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: Yes

 ** connectCampaignFlowArn **   <a name="connect-Type-connect-outbound-campaigns-v2_CampaignSummary-connectCampaignFlowArn"></a>
The Amazon Resource Name (ARN) of the Connect Customer campaign flow associated with the outbound campaign.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 500.
Pattern: `arn:[a-zA-Z0-9-]+:[a-zA-Z0-9-]+:[a-z]{2}-[a-z]+-\d{1,2}:[a-zA-Z0-9-]+:[^:]+(?:/[^:]+)*(?:/[^:]+)?(?:\:[^:]+)?`
Required: No

 ** entryLimitsConfig **   <a name="connect-Type-connect-outbound-campaigns-v2_CampaignSummary-entryLimitsConfig"></a>
Contains entry limits configuration for an outbound campaign.
Type: [EntryLimitsConfig](API_connect-outbound-campaigns-v2_EntryLimitsConfig.md) object
Required: No

 ** schedule **   <a name="connect-Type-connect-outbound-campaigns-v2_CampaignSummary-schedule"></a>
The schedule configuration of the outbound campaign.
Type: [Schedule](API_connect-outbound-campaigns-v2_Schedule.md) object
Required: No

 ** type **   <a name="connect-Type-connect-outbound-campaigns-v2_CampaignSummary-type"></a>
The type of campaign.
Type: String
Valid Values: `MANAGED | JOURNEY`
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_CampaignSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/CampaignSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/CampaignSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/CampaignSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
