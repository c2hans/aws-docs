---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_TestCaseEntryPoint.html
---

# TestCaseEntryPoint
<a name="API_TestCaseEntryPoint"></a>

Defines the starting point for a test case.

## Contents
<a name="API_TestCaseEntryPoint_Contents"></a>

 ** ChatEntryPointParameters **   <a name="connect-Type-TestCaseEntryPoint-ChatEntryPointParameters"></a>
Parameters for chat entry point.
Type: [ChatEntryPointParameters](API_ChatEntryPointParameters.md) object
Required: No

 ** Type **   <a name="connect-Type-TestCaseEntryPoint-Type"></a>
The type of entry point.
Type: String
Valid Values: `VOICE_CALL | CHAT`
Required: No

 ** VoiceCallEntryPointParameters **   <a name="connect-Type-TestCaseEntryPoint-VoiceCallEntryPointParameters"></a>
Parameters for voice call entry point.
Type: [VoiceCallEntryPointParameters](API_VoiceCallEntryPointParameters.md) object
Required: No

## See Also
<a name="API_TestCaseEntryPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/TestCaseEntryPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/TestCaseEntryPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/TestCaseEntryPoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
