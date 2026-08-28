---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_PreviewConfig.html
---

# PreviewConfig
<a name="API_connect-outbound-campaigns-v2_PreviewConfig"></a>

Contains preview outbound mode configuration.

## Contents
<a name="API_connect-outbound-campaigns-v2_PreviewConfig_Contents"></a>

 ** bandwidthAllocation **   <a name="connect-Type-connect-outbound-campaigns-v2_PreviewConfig-bandwidthAllocation"></a>
Bandwidth allocation for the preview outbound mode.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 2.
Required: Yes

 ** timeoutConfig **   <a name="connect-Type-connect-outbound-campaigns-v2_PreviewConfig-timeoutConfig"></a>
Countdown timer configuration for preview outbound mode.
Type: [TimeoutConfig](API_connect-outbound-campaigns-v2_TimeoutConfig.md) object
Required: Yes

 ** agentActions **   <a name="connect-Type-connect-outbound-campaigns-v2_PreviewConfig-agentActions"></a>
Agent actions for the preview outbound mode.
Type: Array of strings
Valid Values: `DISCARD`
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_PreviewConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/PreviewConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/PreviewConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/PreviewConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
