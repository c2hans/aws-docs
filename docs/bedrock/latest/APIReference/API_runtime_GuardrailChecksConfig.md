---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_GuardrailChecksConfig.html
---

# GuardrailChecksConfig
<a name="API_runtime_GuardrailChecksConfig"></a>

The configuration for inline guardrail checks. Specify one or more check types to run against the messages.

## Contents
<a name="API_runtime_GuardrailChecksConfig_Contents"></a>

 ** contentFilter **   <a name="bedrock-Type-runtime_GuardrailChecksConfig-contentFilter"></a>
The content filter check configuration.
Type: [GuardrailChecksContentFilterConfig](API_runtime_GuardrailChecksContentFilterConfig.md) object
Required: No

 ** promptAttack **   <a name="bedrock-Type-runtime_GuardrailChecksConfig-promptAttack"></a>
The prompt attack check configuration.
Type: [GuardrailChecksPromptAttackConfig](API_runtime_GuardrailChecksPromptAttackConfig.md) object
Required: No

 ** sensitiveInformation **   <a name="bedrock-Type-runtime_GuardrailChecksConfig-sensitiveInformation"></a>
The sensitive information check configuration.
Type: [GuardrailChecksSensitiveInformationConfig](API_runtime_GuardrailChecksSensitiveInformationConfig.md) object
Required: No

## See Also
<a name="API_runtime_GuardrailChecksConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailChecksConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailChecksConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailChecksConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
