---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_EmailGenerativeAnswerAIAgentConfiguration.html
---

# EmailGenerativeAnswerAIAgentConfiguration
<a name="API_amazon-q-connect_EmailGenerativeAnswerAIAgentConfiguration"></a>

Configuration settings for the EMAIL\_GENERATIVE\_ANSWER AI agent including prompts, locale, and knowledge base associations.

## Contents
<a name="API_amazon-q-connect_EmailGenerativeAnswerAIAgentConfiguration_Contents"></a>

 ** associationConfigurations **   <a name="connect-Type-amazon-q-connect_EmailGenerativeAnswerAIAgentConfiguration-associationConfigurations"></a>
Configuration settings for knowledge base associations used by the email generative answer agent.
Type: Array of [AssociationConfiguration](API_amazon-q-connect_AssociationConfiguration.md) objects
Required: No

 ** emailGenerativeAnswerAIPromptId **   <a name="connect-Type-amazon-q-connect_EmailGenerativeAnswerAIAgentConfiguration-emailGenerativeAnswerAIPromptId"></a>
The ID of the System AI prompt used for generating comprehensive knowledge-based answers from email queries.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}`
Required: No

 ** emailQueryReformulationAIPromptId **   <a name="connect-Type-amazon-q-connect_EmailGenerativeAnswerAIAgentConfiguration-emailQueryReformulationAIPromptId"></a>
The ID of the System AI prompt used for reformulating email queries to optimize knowledge base search results.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}`
Required: No

 ** locale **   <a name="connect-Type-amazon-q-connect_EmailGenerativeAnswerAIAgentConfiguration-locale"></a>
The locale setting for language-specific email processing and response generation (for example, en\_US, es\_ES).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_amazon-q-connect_EmailGenerativeAnswerAIAgentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/EmailGenerativeAnswerAIAgentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/EmailGenerativeAnswerAIAgentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/EmailGenerativeAnswerAIAgentConfiguration)
