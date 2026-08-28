---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_EmailResponseAIAgentConfiguration.html
---

# EmailResponseAIAgentConfiguration
<a name="API_amazon-q-connect_EmailResponseAIAgentConfiguration"></a>

Configuration settings for the EMAIL\_RESPONSE AI agent including prompts, locale, and knowledge base associations.

## Contents
<a name="API_amazon-q-connect_EmailResponseAIAgentConfiguration_Contents"></a>

 ** associationConfigurations **   <a name="connect-Type-amazon-q-connect_EmailResponseAIAgentConfiguration-associationConfigurations"></a>
Configuration settings for knowledge base associations used by the email response agent.
Type: Array of [AssociationConfiguration](API_amazon-q-connect_AssociationConfiguration.md) objects
Required: No

 ** emailQueryReformulationAIPromptId **   <a name="connect-Type-amazon-q-connect_EmailResponseAIAgentConfiguration-emailQueryReformulationAIPromptId"></a>
The ID of the System AI prompt used for reformulating email queries to optimize knowledge base search for response generation.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}`
Required: No

 ** emailResponseAIPromptId **   <a name="connect-Type-amazon-q-connect_EmailResponseAIAgentConfiguration-emailResponseAIPromptId"></a>
The ID of the System AI prompt used for generating professional email responses based on knowledge base content.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}`
Required: No

 ** locale **   <a name="connect-Type-amazon-q-connect_EmailResponseAIAgentConfiguration-locale"></a>
The locale setting for language-specific email response generation (for example, en\_US, es\_ES).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_amazon-q-connect_EmailResponseAIAgentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/EmailResponseAIAgentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/EmailResponseAIAgentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/EmailResponseAIAgentConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
