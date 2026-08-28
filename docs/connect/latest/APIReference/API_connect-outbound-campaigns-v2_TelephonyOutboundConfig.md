---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_TelephonyOutboundConfig.html
---

# TelephonyOutboundConfig
<a name="API_connect-outbound-campaigns-v2_TelephonyOutboundConfig"></a>

The outbound configuration for telephony.

## Contents
<a name="API_connect-outbound-campaigns-v2_TelephonyOutboundConfig_Contents"></a>

 ** connectContactFlowId **   <a name="connect-Type-connect-outbound-campaigns-v2_TelephonyOutboundConfig-connectContactFlowId"></a>
The identifier of the published Connect Customer contact flow.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: Yes

 ** answerMachineDetectionConfig **   <a name="connect-Type-connect-outbound-campaigns-v2_TelephonyOutboundConfig-answerMachineDetectionConfig"></a>
The answering machine detection configuration.
Type: [AnswerMachineDetectionConfig](API_connect-outbound-campaigns-v2_AnswerMachineDetectionConfig.md) object
Required: No

 ** connectSourcePhoneNumber **   <a name="connect-Type-connect-outbound-campaigns-v2_TelephonyOutboundConfig-connectSourcePhoneNumber"></a>
The Connect Customer source phone number.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

 ** ringTimeout **   <a name="connect-Type-connect-outbound-campaigns-v2_TelephonyOutboundConfig-ringTimeout"></a>
The ring timeout configuration for outbound calls. Specifies how long to wait for the call to be answered before timing out.
Type: Integer
Valid Range: Minimum value of 15. Maximum value of 60.
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_TelephonyOutboundConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/TelephonyOutboundConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/TelephonyOutboundConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/TelephonyOutboundConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
