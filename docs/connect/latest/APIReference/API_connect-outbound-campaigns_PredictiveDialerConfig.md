---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns_PredictiveDialerConfig.html
---

# PredictiveDialerConfig
<a name="API_connect-outbound-campaigns_PredictiveDialerConfig"></a>

Contains predictive dialer configuration for an outbound campaign.

## Contents
<a name="API_connect-outbound-campaigns_PredictiveDialerConfig_Contents"></a>

 ** bandwidthAllocation **   <a name="connect-Type-connect-outbound-campaigns_PredictiveDialerConfig-bandwidthAllocation"></a>
Bandwidth allocation for the predictive dialer.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: Yes

 ** dialingCapacity **   <a name="connect-Type-connect-outbound-campaigns_PredictiveDialerConfig-dialingCapacity"></a>
The allocation of dialing capacity between multiple active campaigns.
Type: Double
Valid Range: Minimum value of 0.01. Maximum value of 1.
Required: No

## See Also
<a name="API_connect-outbound-campaigns_PredictiveDialerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/PredictiveDialerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/PredictiveDialerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/PredictiveDialerConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
