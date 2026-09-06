---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_CommunicationLimitsConfig.html
---

# CommunicationLimitsConfig
<a name="API_connect-outbound-campaigns-v2_CommunicationLimitsConfig"></a>

Contains communication limits configuration for an outbound campaign.

## Contents
<a name="API_connect-outbound-campaigns-v2_CommunicationLimitsConfig_Contents"></a>

 ** allChannelSubtypes **   <a name="connect-Type-connect-outbound-campaigns-v2_CommunicationLimitsConfig-allChannelSubtypes"></a>
The `CommunicationLimits` that apply to all channel subtypes defined in an outbound campaign.
This object is a Union. Only one member of this object can be specified or returned.
Type: [CommunicationLimits](API_connect-outbound-campaigns-v2_CommunicationLimits.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** instanceLimitsHandling **   <a name="connect-Type-connect-outbound-campaigns-v2_CommunicationLimitsConfig-instanceLimitsHandling"></a>
Opt-in or Opt-out from instance-level limits.
Type: String
Valid Values: `OPT_IN | OPT_OUT`
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_CommunicationLimitsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/CommunicationLimitsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/CommunicationLimitsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/CommunicationLimitsConfig)
