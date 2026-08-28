---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_Campaign.html
---

# Campaign
<a name="API_connect-outbound-campaigns-v2_Campaign"></a>

Contains information about an outbound campaign.

## Contents
<a name="API_connect-outbound-campaigns-v2_Campaign_Contents"></a>

 ** arn **   <a name="connect-Type-connect-outbound-campaigns-v2_Campaign-arn"></a>
The Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 500.
Required: Yes

 ** channelSubtypeConfig **   <a name="connect-Type-connect-outbound-campaigns-v2_Campaign-channelSubtypeConfig"></a>
Contains channel subtype configuration.
Type: [ChannelSubtypeConfig](API_connect-outbound-campaigns-v2_ChannelSubtypeConfig.md) object
Required: Yes

 ** connectInstanceId **   <a name="connect-Type-connect-outbound-campaigns-v2_Campaign-connectInstanceId"></a>
The identifier of the Connect Customer instance. You can find the `instanceId` in the ARN of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-_.a-zA-Z0-9]+`
Required: Yes

 ** id **   <a name="connect-Type-connect-outbound-campaigns-v2_Campaign-id"></a>
The identifier of the outbound campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-:/a-zA-Z0-9]+`
Required: Yes

 ** name **   <a name="connect-Type-connect-outbound-campaigns-v2_Campaign-name"></a>
The name of the outbound campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: Yes

 ** communicationLimitsOverride **   <a name="connect-Type-connect-outbound-campaigns-v2_Campaign-communicationLimitsOverride"></a>
Contains communication limits override configuration.
Type: [CommunicationLimitsConfig](API_connect-outbound-campaigns-v2_CommunicationLimitsConfig.md) object
Required: No

 ** communicationTimeConfig **   <a name="connect-Type-connect-outbound-campaigns-v2_Campaign-communicationTimeConfig"></a>
Contains communication time configuration.
Type: [CommunicationTimeConfig](API_connect-outbound-campaigns-v2_CommunicationTimeConfig.md) object
Required: No

 ** connectCampaignFlowArn **   <a name="connect-Type-connect-outbound-campaigns-v2_Campaign-connectCampaignFlowArn"></a>
The Amazon Resource Name (ARN) of the Connect Customer campaign flow associated with the outbound campaign.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 500.
Pattern: `arn:[a-zA-Z0-9-]+:[a-zA-Z0-9-]+:[a-z]{2}-[a-z]+-\d{1,2}:[a-zA-Z0-9-]+:[^:]+(?:/[^:]+)*(?:/[^:]+)?(?:\:[^:]+)?`
Required: No

 ** entryLimitsConfig **   <a name="connect-Type-connect-outbound-campaigns-v2_Campaign-entryLimitsConfig"></a>
Contains entry limits configuration for an outbound campaign.
Type: [EntryLimitsConfig](API_connect-outbound-campaigns-v2_EntryLimitsConfig.md) object
Required: No

 ** schedule **   <a name="connect-Type-connect-outbound-campaigns-v2_Campaign-schedule"></a>
Contains schedule configuration.
Type: [Schedule](API_connect-outbound-campaigns-v2_Schedule.md) object
Required: No

 ** source **   <a name="connect-Type-connect-outbound-campaigns-v2_Campaign-source"></a>
Contains source configuration.
Type: [Source](API_connect-outbound-campaigns-v2_Source.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** tags **   <a name="connect-Type-connect-outbound-campaigns-v2_Campaign-tags"></a>
The tags used to organize, track, or control access for this resource. For example, `{ "tags": {"key1":"value1", "key2":"value2"} }`.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** type **   <a name="connect-Type-connect-outbound-campaigns-v2_Campaign-type"></a>
The type of campaign.
Type: String
Valid Values: `MANAGED | JOURNEY`
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_Campaign_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/Campaign)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/Campaign)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/Campaign)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
