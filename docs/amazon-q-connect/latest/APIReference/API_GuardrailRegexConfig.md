---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GuardrailRegexConfig.html
---

# GuardrailRegexConfig
<a name="API_amazon-q-connect_GuardrailRegexConfig"></a>

The regular expression to configure for the AI Guardrail.

## Contents
<a name="API_amazon-q-connect_GuardrailRegexConfig_Contents"></a>

 ** action **   <a name="connect-Type-amazon-q-connect_GuardrailRegexConfig-action"></a>
The AI Guardrail action to configure when matching regular expression is detected.
Type: String
Valid Values: `BLOCK | ANONYMIZE`
Required: Yes

 ** name **   <a name="connect-Type-amazon-q-connect_GuardrailRegexConfig-name"></a>
The name of the regular expression to configure for the AI Guardrail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** pattern **   <a name="connect-Type-amazon-q-connect_GuardrailRegexConfig-pattern"></a>
The regular expression pattern to configure for the AI Guardrail.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** description **   <a name="connect-Type-amazon-q-connect_GuardrailRegexConfig-description"></a>
The description of the regular expression to configure for the AI Guardrail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

## See Also
<a name="API_amazon-q-connect_GuardrailRegexConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/GuardrailRegexConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/GuardrailRegexConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/GuardrailRegexConfig)
