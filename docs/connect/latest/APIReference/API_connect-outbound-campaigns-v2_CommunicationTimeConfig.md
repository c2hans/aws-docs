---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_CommunicationTimeConfig.html
---

# CommunicationTimeConfig
<a name="API_connect-outbound-campaigns-v2_CommunicationTimeConfig"></a>

Contains communication time configuration for an outbound campaign.

## Contents
<a name="API_connect-outbound-campaigns-v2_CommunicationTimeConfig_Contents"></a>

 ** localTimeZoneConfig **   <a name="connect-Type-connect-outbound-campaigns-v2_CommunicationTimeConfig-localTimeZoneConfig"></a>
The local timezone configuration.
Type: [LocalTimeZoneConfig](API_connect-outbound-campaigns-v2_LocalTimeZoneConfig.md) object
Required: Yes

 ** email **   <a name="connect-Type-connect-outbound-campaigns-v2_CommunicationTimeConfig-email"></a>
The communication time configuration for the email channel subtype.
Type: [TimeWindow](API_connect-outbound-campaigns-v2_TimeWindow.md) object
Required: No

 ** sms **   <a name="connect-Type-connect-outbound-campaigns-v2_CommunicationTimeConfig-sms"></a>
The communication time configuration for the SMS channel subtype.
Type: [TimeWindow](API_connect-outbound-campaigns-v2_TimeWindow.md) object
Required: No

 ** telephony **   <a name="connect-Type-connect-outbound-campaigns-v2_CommunicationTimeConfig-telephony"></a>
The communication time configuration for the telephony channel subtype.
Type: [TimeWindow](API_connect-outbound-campaigns-v2_TimeWindow.md) object
Required: No

 ** whatsApp **   <a name="connect-Type-connect-outbound-campaigns-v2_CommunicationTimeConfig-whatsApp"></a>
The communication time configuration for the WhatsApp channel subtype.
Type: [TimeWindow](API_connect-outbound-campaigns-v2_TimeWindow.md) object
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_CommunicationTimeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/CommunicationTimeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/CommunicationTimeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/CommunicationTimeConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
