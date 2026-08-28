---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_AnswerRecommendationAIAgentConfiguration.html
---

# AnswerRecommendationAIAgentConfiguration
<a name="API_amazon-q-connect_AnswerRecommendationAIAgentConfiguration"></a>

The configuration for the `ANSWER_RECOMMENDATION` AI Agent type.

## Contents
<a name="API_amazon-q-connect_AnswerRecommendationAIAgentConfiguration_Contents"></a>

 ** answerGenerationAIGuardrailId **   <a name="connect-Type-amazon-q-connect_AnswerRecommendationAIAgentConfiguration-answerGenerationAIGuardrailId"></a>
The AI Guardrail identifier for the Answer Generation Guardrail used by the `ANSWER_RECOMMENDATION` AI Agent.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}`
Required: No

 ** answerGenerationAIPromptId **   <a name="connect-Type-amazon-q-connect_AnswerRecommendationAIAgentConfiguration-answerGenerationAIPromptId"></a>
The AI Prompt identifier for the Answer Generation prompt used by the `ANSWER_RECOMMENDATION` AI Agent.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}`
Required: No

 ** associationConfigurations **   <a name="connect-Type-amazon-q-connect_AnswerRecommendationAIAgentConfiguration-associationConfigurations"></a>
The association configurations for overriding behavior on this AI Agent.
Type: Array of [AssociationConfiguration](API_amazon-q-connect_AssociationConfiguration.md) objects
Required: No

 ** intentLabelingGenerationAIPromptId **   <a name="connect-Type-amazon-q-connect_AnswerRecommendationAIAgentConfiguration-intentLabelingGenerationAIPromptId"></a>
The AI Prompt identifier for the Intent Labeling prompt used by the `ANSWER_RECOMMENDATION` AI Agent.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}`
Required: No

 ** locale **   <a name="connect-Type-amazon-q-connect_AnswerRecommendationAIAgentConfiguration-locale"></a>
The locale to which specifies the language and region settings that determine the response language for [QueryAssistant](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_QueryAssistant.html).
For more information on supported locales, see [Language support for Amazon Q in Connect](https://docs.aws.amazon.com/connect/latest/adminguide/supported-languages.html#qic-notes-languages).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** queryReformulationAIPromptId **   <a name="connect-Type-amazon-q-connect_AnswerRecommendationAIAgentConfiguration-queryReformulationAIPromptId"></a>
The AI Prompt identifier for the Query Reformulation prompt used by the `ANSWER_RECOMMENDATION` AI Agent.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}`
Required: No

 ** suggestedMessages **   <a name="connect-Type-amazon-q-connect_AnswerRecommendationAIAgentConfiguration-suggestedMessages"></a>
The suggested messages configuration for the Answer Recommendation AI Agent.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_amazon-q-connect_AnswerRecommendationAIAgentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/AnswerRecommendationAIAgentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/AnswerRecommendationAIAgentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/AnswerRecommendationAIAgentConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
