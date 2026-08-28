---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_CommunicationLimit.html
---

# CommunicationLimit
<a name="API_connect-outbound-campaigns-v2_CommunicationLimit"></a>

Contains information about a communication limit.

## Contents
<a name="API_connect-outbound-campaigns-v2_CommunicationLimit_Contents"></a>

 ** frequency **   <a name="connect-Type-connect-outbound-campaigns-v2_CommunicationLimit-frequency"></a>
The frequency of communication limit evaluation.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 30.
Required: Yes

 ** maxCountPerRecipient **   <a name="connect-Type-connect-outbound-campaigns-v2_CommunicationLimit-maxCountPerRecipient"></a>
The maximum outreaching count for each recipient.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** unit **   <a name="connect-Type-connect-outbound-campaigns-v2_CommunicationLimit-unit"></a>
The unit of communication limit evaluation.
Type: String
Valid Values: `DAY`
Required: Yes

## See Also
<a name="API_connect-outbound-campaigns-v2_CommunicationLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/CommunicationLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/CommunicationLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/CommunicationLimit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
