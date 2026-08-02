---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_SmsChannelSubtypeConfig.html
---

# SmsChannelSubtypeConfig
<a name="API_connect-outbound-campaigns-v2_SmsChannelSubtypeConfig"></a>

The configuration for the SMS channel subtype.

## Contents
<a name="API_connect-outbound-campaigns-v2_SmsChannelSubtypeConfig_Contents"></a>

 ** defaultOutboundConfig **   <a name="connect-Type-connect-outbound-campaigns-v2_SmsChannelSubtypeConfig-defaultOutboundConfig"></a>
The default SMS outbound configuration of an outbound campaign.
Type: [SmsOutboundConfig](API_connect-outbound-campaigns-v2_SmsOutboundConfig.md) object
Required: Yes

 ** outboundMode **   <a name="connect-Type-connect-outbound-campaigns-v2_SmsChannelSubtypeConfig-outboundMode"></a>
The outbound mode for SMS of an outbound campaign.
Type: [SmsOutboundMode](API_connect-outbound-campaigns-v2_SmsOutboundMode.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** capacity **   <a name="connect-Type-connect-outbound-campaigns-v2_SmsChannelSubtypeConfig-capacity"></a>
The allocation of SMS capacity between multiple running outbound campaigns.
Type: Double
Valid Range: Minimum value of 0.01. Maximum value of 1.
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_SmsChannelSubtypeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/SmsChannelSubtypeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/SmsChannelSubtypeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/SmsChannelSubtypeConfig)
