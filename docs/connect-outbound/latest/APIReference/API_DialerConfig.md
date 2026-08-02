---
source_url: https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_DialerConfig.html
---

# DialerConfig
<a name="API_connect-outbound-campaigns_DialerConfig"></a>

Contains dialer configuration for an outbound campaign.

## Contents
<a name="API_connect-outbound-campaigns_DialerConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** agentlessDialerConfig **   <a name="connect-Type-connect-outbound-campaigns_DialerConfig-agentlessDialerConfig"></a>
The configuration of the agentless dialer.
Type: [AgentlessDialerConfig](API_connect-outbound-campaigns_AgentlessDialerConfig.md) object
Required: No

 ** predictiveDialerConfig **   <a name="connect-Type-connect-outbound-campaigns_DialerConfig-predictiveDialerConfig"></a>
The configuration of the predictive dialer.
Type: [PredictiveDialerConfig](API_connect-outbound-campaigns_PredictiveDialerConfig.md) object
Required: No

 ** progressiveDialerConfig **   <a name="connect-Type-connect-outbound-campaigns_DialerConfig-progressiveDialerConfig"></a>
The configuration of the progressive dialer.
Type: [ProgressiveDialerConfig](API_connect-outbound-campaigns_ProgressiveDialerConfig.md) object
Required: No

## See Also
<a name="API_connect-outbound-campaigns_DialerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/DialerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/DialerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/DialerConfig)
