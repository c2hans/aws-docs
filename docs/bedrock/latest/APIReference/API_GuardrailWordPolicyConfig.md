---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailWordPolicyConfig.html
---

# GuardrailWordPolicyConfig
<a name="API_GuardrailWordPolicyConfig"></a>

Contains details about the word policy to configured for the guardrail.

## Contents
<a name="API_GuardrailWordPolicyConfig_Contents"></a>

 ** managedWordListsConfig **   <a name="bedrock-Type-GuardrailWordPolicyConfig-managedWordListsConfig"></a>
A list of managed words to configure for the guardrail.
Type: Array of [GuardrailManagedWordsConfig](API_GuardrailManagedWordsConfig.md) objects
Required: No

 ** wordsConfig **   <a name="bedrock-Type-GuardrailWordPolicyConfig-wordsConfig"></a>
A list of words to configure for the guardrail.
Type: Array of [GuardrailWordConfig](API_GuardrailWordConfig.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10000 items.
Required: No

## See Also
<a name="API_GuardrailWordPolicyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailWordPolicyConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailWordPolicyConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailWordPolicyConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
