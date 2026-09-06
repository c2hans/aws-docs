---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_ManualSearchAIAgentConfiguration.html
---

# ManualSearchAIAgentConfiguration
<a name="API_amazon-q-connect_ManualSearchAIAgentConfiguration"></a>

The configuration for the `MANUAL_SEARCH` AI Agent type.

## Contents
<a name="API_amazon-q-connect_ManualSearchAIAgentConfiguration_Contents"></a>

 ** answerGenerationAIGuardrailId **   <a name="connect-Type-amazon-q-connect_ManualSearchAIAgentConfiguration-answerGenerationAIGuardrailId"></a>
The AI Guardrail identifier for the Answer Generation guardrail used by the MANUAL\_SEARCH AI Agent.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}`
Required: No

 ** answerGenerationAIPromptId **   <a name="connect-Type-amazon-q-connect_ManualSearchAIAgentConfiguration-answerGenerationAIPromptId"></a>
The AI Prompt identifier for the Answer Generation prompt used by the MANUAL\_SEARCH AI Agent.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}`
Required: No

 ** associationConfigurations **   <a name="connect-Type-amazon-q-connect_ManualSearchAIAgentConfiguration-associationConfigurations"></a>
The association configurations for overriding behavior on this AI Agent.
Type: Array of [AssociationConfiguration](API_amazon-q-connect_AssociationConfiguration.md) objects
Required: No

 ** locale **   <a name="connect-Type-amazon-q-connect_ManualSearchAIAgentConfiguration-locale"></a>
The locale to which specifies the language and region settings that determine the response language for [QueryAssistant](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_QueryAssistant.html).
For more information on supported locales, see [Language support for Amazon Q in Connect](https://docs.aws.amazon.com/connect/latest/adminguide/supported-languages.html#qic-notes-languages).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_amazon-q-connect_ManualSearchAIAgentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ManualSearchAIAgentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ManualSearchAIAgentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ManualSearchAIAgentConfiguration)
