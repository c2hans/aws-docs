---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_AutomatedReasoningPolicyBuildStepMessage.html
---

# AutomatedReasoningPolicyBuildStepMessage
<a name="API_AutomatedReasoningPolicyBuildStepMessage"></a>

Represents a message generated during a build step, providing information about what happened or any issues encountered.

## Contents
<a name="API_AutomatedReasoningPolicyBuildStepMessage_Contents"></a>

 ** message **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildStepMessage-message"></a>
The content of the message, describing what occurred during the build step.
Type: String
Required: Yes

 ** messageType **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildStepMessage-messageType"></a>
The type of message (e.g., INFO, WARNING, ERROR) indicating its severity and purpose.
Type: String
Valid Values: `INFO | WARNING | ERROR`
Required: Yes

## See Also
<a name="API_AutomatedReasoningPolicyBuildStepMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyBuildStepMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyBuildStepMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyBuildStepMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
