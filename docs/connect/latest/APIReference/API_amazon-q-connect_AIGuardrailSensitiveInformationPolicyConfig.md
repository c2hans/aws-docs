---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_AIGuardrailSensitiveInformationPolicyConfig.html
---

# AIGuardrailSensitiveInformationPolicyConfig
<a name="API_amazon-q-connect_AIGuardrailSensitiveInformationPolicyConfig"></a>

Contains details about PII entities and regular expressions to configure for the AI Guardrail.

## Contents
<a name="API_amazon-q-connect_AIGuardrailSensitiveInformationPolicyConfig_Contents"></a>

 ** piiEntitiesConfig **   <a name="connect-Type-amazon-q-connect_AIGuardrailSensitiveInformationPolicyConfig-piiEntitiesConfig"></a>
A list of PII entities to configure to the AI Guardrail.
Type: Array of [GuardrailPiiEntityConfig](API_amazon-q-connect_GuardrailPiiEntityConfig.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** regexesConfig **   <a name="connect-Type-amazon-q-connect_AIGuardrailSensitiveInformationPolicyConfig-regexesConfig"></a>
A list of regular expressions to configure to the AI Guardrail.
Type: Array of [GuardrailRegexConfig](API_amazon-q-connect_GuardrailRegexConfig.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_amazon-q-connect_AIGuardrailSensitiveInformationPolicyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/AIGuardrailSensitiveInformationPolicyConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/AIGuardrailSensitiveInformationPolicyConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/AIGuardrailSensitiveInformationPolicyConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
