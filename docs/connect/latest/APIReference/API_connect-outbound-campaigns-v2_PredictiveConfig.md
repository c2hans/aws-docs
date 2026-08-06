---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_PredictiveConfig.html
---

# PredictiveConfig
<a name="API_connect-outbound-campaigns-v2_PredictiveConfig"></a>

Contains predictive outbound mode configuration.

## Contents
<a name="API_connect-outbound-campaigns-v2_PredictiveConfig_Contents"></a>

 ** bandwidthAllocation **   <a name="connect-Type-connect-outbound-campaigns-v2_PredictiveConfig-bandwidthAllocation"></a>
Bandwidth allocation for the predictive outbound mode.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 2.
Required: Yes

 ** pacingStrategies **   <a name="connect-Type-connect-outbound-campaigns-v2_PredictiveConfig-pacingStrategies"></a>
The pacing strategies that the dialer enforces for the predictive outbound mode. Currently, you can specify one pacing strategy.
Type: Array of [PacingStrategy](API_connect-outbound-campaigns-v2_PacingStrategy.md) objects
Array Members: Fixed number of 1 item.
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_PredictiveConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/PredictiveConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/PredictiveConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/PredictiveConfig)
