---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_GuardrailChecksMessage.html
---

# GuardrailChecksMessage
<a name="API_runtime_GuardrailChecksMessage"></a>

A message to evaluate against guardrail checks, containing a role and content blocks.

## Contents
<a name="API_runtime_GuardrailChecksMessage_Contents"></a>

 ** content **   <a name="bedrock-Type-runtime_GuardrailChecksMessage-content"></a>
The content blocks for the message.
Type: Array of [GuardrailChecksContentBlock](API_runtime_GuardrailChecksContentBlock.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** role **   <a name="bedrock-Type-runtime_GuardrailChecksMessage-role"></a>
The role of the message sender.
Type: String
Valid Values: `user | assistant | system`
Required: Yes

## See Also
<a name="API_runtime_GuardrailChecksMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailChecksMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailChecksMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailChecksMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
