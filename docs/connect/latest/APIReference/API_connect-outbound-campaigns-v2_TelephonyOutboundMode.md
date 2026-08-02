---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_TelephonyOutboundMode.html
---

# TelephonyOutboundMode
<a name="API_connect-outbound-campaigns-v2_TelephonyOutboundMode"></a>

Contains information about telephony outbound mode.

## Contents
<a name="API_connect-outbound-campaigns-v2_TelephonyOutboundMode_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** agentless **   <a name="connect-Type-connect-outbound-campaigns-v2_TelephonyOutboundMode-agentless"></a>
The agentless outbound mode configuration for telephony.
Type: [AgentlessConfig](API_connect-outbound-campaigns-v2_AgentlessConfig.md) object
Required: No

 ** predictive **   <a name="connect-Type-connect-outbound-campaigns-v2_TelephonyOutboundMode-predictive"></a>
The predictive outbound mode configuration for telephony.
Type: [PredictiveConfig](API_connect-outbound-campaigns-v2_PredictiveConfig.md) object
Required: No

 ** preview **   <a name="connect-Type-connect-outbound-campaigns-v2_TelephonyOutboundMode-preview"></a>
The preview outbound mode configuration for telephony.
Type: [PreviewConfig](API_connect-outbound-campaigns-v2_PreviewConfig.md) object
Required: No

 ** progressive **   <a name="connect-Type-connect-outbound-campaigns-v2_TelephonyOutboundMode-progressive"></a>
The progressive outbound mode configuration for telephony.
Type: [ProgressiveConfig](API_connect-outbound-campaigns-v2_ProgressiveConfig.md) object
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_TelephonyOutboundMode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/TelephonyOutboundMode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/TelephonyOutboundMode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/TelephonyOutboundMode)
