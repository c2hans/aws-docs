---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_GuardrailChecksResults.html
---

# GuardrailChecksResults
<a name="API_runtime_GuardrailChecksResults"></a>

The results from the guardrail checks evaluation, organized by check type.

## Contents
<a name="API_runtime_GuardrailChecksResults_Contents"></a>

 ** contentFilter **   <a name="bedrock-Type-runtime_GuardrailChecksResults-contentFilter"></a>
The content filter check results.
Type: [GuardrailChecksContentFilterResult](API_runtime_GuardrailChecksContentFilterResult.md) object
Required: No

 ** promptAttack **   <a name="bedrock-Type-runtime_GuardrailChecksResults-promptAttack"></a>
The prompt attack check results.
Type: [GuardrailChecksPromptAttackResult](API_runtime_GuardrailChecksPromptAttackResult.md) object
Required: No

 ** sensitiveInformation **   <a name="bedrock-Type-runtime_GuardrailChecksResults-sensitiveInformation"></a>
The sensitive information check results.
Type: [GuardrailChecksSensitiveInformationResult](API_runtime_GuardrailChecksSensitiveInformationResult.md) object
Required: No

## See Also
<a name="API_runtime_GuardrailChecksResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailChecksResults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailChecksResults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailChecksResults)
