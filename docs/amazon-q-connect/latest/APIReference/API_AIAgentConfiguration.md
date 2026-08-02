---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_AIAgentConfiguration.html
---

# AIAgentConfiguration
<a name="API_amazon-q-connect_AIAgentConfiguration"></a>

A typed union that specifies the configuration based on the type of AI Agent.

## Contents
<a name="API_amazon-q-connect_AIAgentConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** answerRecommendationAIAgentConfiguration **   <a name="connect-Type-amazon-q-connect_AIAgentConfiguration-answerRecommendationAIAgentConfiguration"></a>
The configuration for AI Agents of type `ANSWER_RECOMMENDATION`.
Type: [AnswerRecommendationAIAgentConfiguration](API_amazon-q-connect_AnswerRecommendationAIAgentConfiguration.md) object
Required: No

 ** caseSummarizationAIAgentConfiguration **   <a name="connect-Type-amazon-q-connect_AIAgentConfiguration-caseSummarizationAIAgentConfiguration"></a>
The configuration for AI Agents of type `CASE_SUMMARIZATION`.
Type: [CaseSummarizationAIAgentConfiguration](API_amazon-q-connect_CaseSummarizationAIAgentConfiguration.md) object
Required: No

 ** emailGenerativeAnswerAIAgentConfiguration **   <a name="connect-Type-amazon-q-connect_AIAgentConfiguration-emailGenerativeAnswerAIAgentConfiguration"></a>
Configuration for the EMAIL\_GENERATIVE\_ANSWER AI agent that provides comprehensive knowledge-based answers for customer queries.
Type: [EmailGenerativeAnswerAIAgentConfiguration](API_amazon-q-connect_EmailGenerativeAnswerAIAgentConfiguration.md) object
Required: No

 ** emailOverviewAIAgentConfiguration **   <a name="connect-Type-amazon-q-connect_AIAgentConfiguration-emailOverviewAIAgentConfiguration"></a>
Configuration for the EMAIL\_OVERVIEW AI agent that generates structured overview of email conversations.
Type: [EmailOverviewAIAgentConfiguration](API_amazon-q-connect_EmailOverviewAIAgentConfiguration.md) object
Required: No

 ** emailResponseAIAgentConfiguration **   <a name="connect-Type-amazon-q-connect_AIAgentConfiguration-emailResponseAIAgentConfiguration"></a>
Configuration for the EMAIL\_RESPONSE AI agent that generates professional email responses using knowledge base content.
Type: [EmailResponseAIAgentConfiguration](API_amazon-q-connect_EmailResponseAIAgentConfiguration.md) object
Required: No

 ** manualSearchAIAgentConfiguration **   <a name="connect-Type-amazon-q-connect_AIAgentConfiguration-manualSearchAIAgentConfiguration"></a>
The configuration for AI Agents of type `MANUAL_SEARCH`.
Type: [ManualSearchAIAgentConfiguration](API_amazon-q-connect_ManualSearchAIAgentConfiguration.md) object
Required: No

 ** noteTakingAIAgentConfiguration **   <a name="connect-Type-amazon-q-connect_AIAgentConfiguration-noteTakingAIAgentConfiguration"></a>
The configuration for AI Agents of type `NOTE_TAKING`.
Type: [NoteTakingAIAgentConfiguration](API_amazon-q-connect_NoteTakingAIAgentConfiguration.md) object
Required: No

 ** orchestrationAIAgentConfiguration **   <a name="connect-Type-amazon-q-connect_AIAgentConfiguration-orchestrationAIAgentConfiguration"></a>
The configuration for AI Agents of type `ORCHESTRATION`.
Type: [OrchestrationAIAgentConfiguration](API_amazon-q-connect_OrchestrationAIAgentConfiguration.md) object
Required: No

 ** selfServiceAIAgentConfiguration **   <a name="connect-Type-amazon-q-connect_AIAgentConfiguration-selfServiceAIAgentConfiguration"></a>
The configuration for AI Agents of type SELF\_SERVICE.
Type: [SelfServiceAIAgentConfiguration](API_amazon-q-connect_SelfServiceAIAgentConfiguration.md) object
Required: No

## See Also
<a name="API_amazon-q-connect_AIAgentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/AIAgentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/AIAgentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/AIAgentConfiguration)
