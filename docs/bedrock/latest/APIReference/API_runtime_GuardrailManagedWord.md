---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_GuardrailManagedWord.html
---

# GuardrailManagedWord
<a name="API_runtime_GuardrailManagedWord"></a>

A managed word configured in a guardrail.

## Contents
<a name="API_runtime_GuardrailManagedWord_Contents"></a>

 ** action **   <a name="bedrock-Type-runtime_GuardrailManagedWord-action"></a>
The action for the managed word.
Type: String
Valid Values: `BLOCKED | NONE`
Required: Yes

 ** match **   <a name="bedrock-Type-runtime_GuardrailManagedWord-match"></a>
The match for the managed word.
Type: String
Required: Yes

 ** type **   <a name="bedrock-Type-runtime_GuardrailManagedWord-type"></a>
The type for the managed word.
Type: String
Valid Values: `PROFANITY`
Required: Yes

 ** detected **   <a name="bedrock-Type-runtime_GuardrailManagedWord-detected"></a>
Indicates whether managed word content that breaches the guardrail configuration is detected.
Type: Boolean
Required: No

## See Also
<a name="API_runtime_GuardrailManagedWord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailManagedWord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailManagedWord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailManagedWord)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
