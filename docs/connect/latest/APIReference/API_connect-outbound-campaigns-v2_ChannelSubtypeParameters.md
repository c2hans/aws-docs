---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_ChannelSubtypeParameters.html
---

# ChannelSubtypeParameters
<a name="API_connect-outbound-campaigns-v2_ChannelSubtypeParameters"></a>

Contains channel subtype parameters for an outbound request of a campaign.

## Contents
<a name="API_connect-outbound-campaigns-v2_ChannelSubtypeParameters_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** email **   <a name="connect-Type-connect-outbound-campaigns-v2_ChannelSubtypeParameters-email"></a>
The overridden parameters of the email channel subtype.
Type: [EmailChannelSubtypeParameters](API_connect-outbound-campaigns-v2_EmailChannelSubtypeParameters.md) object
Required: No

 ** sms **   <a name="connect-Type-connect-outbound-campaigns-v2_ChannelSubtypeParameters-sms"></a>
The overridden parameters of the SMS channel subtype.
Type: [SmsChannelSubtypeParameters](API_connect-outbound-campaigns-v2_SmsChannelSubtypeParameters.md) object
Required: No

 ** telephony **   <a name="connect-Type-connect-outbound-campaigns-v2_ChannelSubtypeParameters-telephony"></a>
The overridden parameters of the telephony channel subtype.
Type: [TelephonyChannelSubtypeParameters](API_connect-outbound-campaigns-v2_TelephonyChannelSubtypeParameters.md) object
Required: No

 ** whatsApp **   <a name="connect-Type-connect-outbound-campaigns-v2_ChannelSubtypeParameters-whatsApp"></a>
The overridden parameters of the WhatsApp channel subtype.
Type: [WhatsAppChannelSubtypeParameters](API_connect-outbound-campaigns-v2_WhatsAppChannelSubtypeParameters.md) object
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_ChannelSubtypeParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/ChannelSubtypeParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/ChannelSubtypeParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/ChannelSubtypeParameters)
