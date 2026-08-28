---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns_OutboundCallConfig.html
---

# OutboundCallConfig
<a name="API_connect-outbound-campaigns_OutboundCallConfig"></a>

Contains outbound call configuration for an outbound campaign.

## Contents
<a name="API_connect-outbound-campaigns_OutboundCallConfig_Contents"></a>

 ** connectContactFlowId **   <a name="connect-Type-connect-outbound-campaigns_OutboundCallConfig-connectContactFlowId"></a>
The identifier of the published flow associated with the outbound call.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: Yes

 ** answerMachineDetectionConfig **   <a name="connect-Type-connect-outbound-campaigns_OutboundCallConfig-answerMachineDetectionConfig"></a>
Whether answering machine detection has been enabled.
Type: [AnswerMachineDetectionConfig](API_connect-outbound-campaigns_AnswerMachineDetectionConfig.md) object
Required: No

 ** connectQueueId **   <a name="connect-Type-connect-outbound-campaigns_OutboundCallConfig-connectQueueId"></a>
The identifier of the queue associated with the outbound call.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** connectSourcePhoneNumber **   <a name="connect-Type-connect-outbound-campaigns_OutboundCallConfig-connectSourcePhoneNumber"></a>
The phone number associated with the outbound call. This is the caller ID that is displayed to customers when an agent calls them.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

## See Also
<a name="API_connect-outbound-campaigns_OutboundCallConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/OutboundCallConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/OutboundCallConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/OutboundCallConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
