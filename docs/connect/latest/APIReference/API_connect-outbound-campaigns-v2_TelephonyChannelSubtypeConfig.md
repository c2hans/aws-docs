---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_TelephonyChannelSubtypeConfig.html
---

# TelephonyChannelSubtypeConfig
<a name="API_connect-outbound-campaigns-v2_TelephonyChannelSubtypeConfig"></a>

The configuration for the telephony channel subtype.

## Contents
<a name="API_connect-outbound-campaigns-v2_TelephonyChannelSubtypeConfig_Contents"></a>

 ** defaultOutboundConfig **   <a name="connect-Type-connect-outbound-campaigns-v2_TelephonyChannelSubtypeConfig-defaultOutboundConfig"></a>
The default telephony outbound configuration of an outbound campaign.
Type: [TelephonyOutboundConfig](API_connect-outbound-campaigns-v2_TelephonyOutboundConfig.md) object
Required: Yes

 ** outboundMode **   <a name="connect-Type-connect-outbound-campaigns-v2_TelephonyChannelSubtypeConfig-outboundMode"></a>
The outbound mode for telephony of an outbound campaign.
Type: [TelephonyOutboundMode](API_connect-outbound-campaigns-v2_TelephonyOutboundMode.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** capacity **   <a name="connect-Type-connect-outbound-campaigns-v2_TelephonyChannelSubtypeConfig-capacity"></a>
The allocation of telephony capacity between multiple running outbound campaigns.
Type: Double
Valid Range: Minimum value of 0.01. Maximum value of 1.
Required: No

 ** connectQueueId **   <a name="connect-Type-connect-outbound-campaigns-v2_TelephonyChannelSubtypeConfig-connectQueueId"></a>
The identifier of the Connect Customer queue associated for telephony outbound requests of an outbound campaign.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_TelephonyChannelSubtypeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/TelephonyChannelSubtypeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/TelephonyChannelSubtypeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/TelephonyChannelSubtypeConfig)
