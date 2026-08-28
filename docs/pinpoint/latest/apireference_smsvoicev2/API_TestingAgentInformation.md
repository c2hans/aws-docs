---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_TestingAgentInformation.html
---

# TestingAgentInformation
<a name="API_TestingAgentInformation"></a>

Contains details about the testing agent associated with an RCS agent.

## Contents
<a name="API_TestingAgentInformation_Contents"></a>

 ** RegistrationId **   <a name="pinpoint-Type-TestingAgentInformation-RegistrationId"></a>
The unique identifier of the registration associated with the testing agent.
Type: String
Required: Yes

 ** Status **   <a name="pinpoint-Type-TestingAgentInformation-Status"></a>
The current status of the testing agent.
Type: String
Valid Values: `CREATED | PENDING | ACTIVE`
Required: Yes

 ** TestingAgentId **   <a name="pinpoint-Type-TestingAgentInformation-TestingAgentId"></a>
The unique identifier for the testing agent.
Type: String
Required: No

## See Also
<a name="API_TestingAgentInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/TestingAgentInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/TestingAgentInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/TestingAgentInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
