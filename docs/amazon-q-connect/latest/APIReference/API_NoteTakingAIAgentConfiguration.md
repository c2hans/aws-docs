---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_NoteTakingAIAgentConfiguration.html
---

# NoteTakingAIAgentConfiguration
<a name="API_amazon-q-connect_NoteTakingAIAgentConfiguration"></a>

The configuration for AI Agents of type `NOTE_TAKING`.

## Contents
<a name="API_amazon-q-connect_NoteTakingAIAgentConfiguration_Contents"></a>

 ** locale **   <a name="connect-Type-amazon-q-connect_NoteTakingAIAgentConfiguration-locale"></a>
The locale setting for language-specific case summarization generation (for example, en\_US, es\_ES).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** noteTakingAIGuardrailId **   <a name="connect-Type-amazon-q-connect_NoteTakingAIAgentConfiguration-noteTakingAIGuardrailId"></a>
The AI Guardrail identifier used by the Note Taking AI Agent.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}`
Required: No

 ** noteTakingAIPromptId **   <a name="connect-Type-amazon-q-connect_NoteTakingAIAgentConfiguration-noteTakingAIPromptId"></a>
The AI Prompt identifier used by the Note Taking AI Agent.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}`
Required: No

## See Also
<a name="API_amazon-q-connect_NoteTakingAIAgentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/NoteTakingAIAgentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/NoteTakingAIAgentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/NoteTakingAIAgentConfiguration)
