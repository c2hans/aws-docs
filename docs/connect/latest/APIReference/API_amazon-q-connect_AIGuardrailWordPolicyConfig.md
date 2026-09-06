---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_AIGuardrailWordPolicyConfig.html
---

# AIGuardrailWordPolicyConfig
<a name="API_amazon-q-connect_AIGuardrailWordPolicyConfig"></a>

Contains details about the word policy to configured for the AI Guardrail.

## Contents
<a name="API_amazon-q-connect_AIGuardrailWordPolicyConfig_Contents"></a>

 ** managedWordListsConfig **   <a name="connect-Type-amazon-q-connect_AIGuardrailWordPolicyConfig-managedWordListsConfig"></a>
A list of managed words to configure for the AI Guardrail.
Type: Array of [GuardrailManagedWordsConfig](API_amazon-q-connect_GuardrailManagedWordsConfig.md) objects
Required: No

 ** wordsConfig **   <a name="connect-Type-amazon-q-connect_AIGuardrailWordPolicyConfig-wordsConfig"></a>
A list of words to configure for the AI Guardrail.
Type: Array of [GuardrailWordConfig](API_amazon-q-connect_GuardrailWordConfig.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_amazon-q-connect_AIGuardrailWordPolicyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/AIGuardrailWordPolicyConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/AIGuardrailWordPolicyConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/AIGuardrailWordPolicyConfig)
