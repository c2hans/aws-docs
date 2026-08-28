---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns_ProgressiveDialerConfig.html
---

# ProgressiveDialerConfig
<a name="API_connect-outbound-campaigns_ProgressiveDialerConfig"></a>

Contains progressive dialer configuration for an outbound campaign.

## Contents
<a name="API_connect-outbound-campaigns_ProgressiveDialerConfig_Contents"></a>

 ** bandwidthAllocation **   <a name="connect-Type-connect-outbound-campaigns_ProgressiveDialerConfig-bandwidthAllocation"></a>
Bandwidth allocation for the progressive dialer.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: Yes

 ** dialingCapacity **   <a name="connect-Type-connect-outbound-campaigns_ProgressiveDialerConfig-dialingCapacity"></a>
The allocation of dialing capacity between multiple active campaigns.
Type: Double
Valid Range: Minimum value of 0.01. Maximum value of 1.
Required: No

## See Also
<a name="API_connect-outbound-campaigns_ProgressiveDialerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/ProgressiveDialerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/ProgressiveDialerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/ProgressiveDialerConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
