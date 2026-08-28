---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_CaseSummarizationAIAgentConfiguration.html
---

# CaseSummarizationAIAgentConfiguration
<a name="API_amazon-q-connect_CaseSummarizationAIAgentConfiguration"></a>

The configuration for AI Agents of type `CASE_SUMMARIZATION`.

## Contents
<a name="API_amazon-q-connect_CaseSummarizationAIAgentConfiguration_Contents"></a>

 ** caseSummarizationAIGuardrailId **   <a name="connect-Type-amazon-q-connect_CaseSummarizationAIAgentConfiguration-caseSummarizationAIGuardrailId"></a>
The AI Guardrail identifier used by the Case Summarization AI Agent.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}`
Required: No

 ** caseSummarizationAIPromptId **   <a name="connect-Type-amazon-q-connect_CaseSummarizationAIAgentConfiguration-caseSummarizationAIPromptId"></a>
The AI Prompt identifier used by the Case Summarization AI Agent.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}`
Required: No

 ** locale **   <a name="connect-Type-amazon-q-connect_CaseSummarizationAIAgentConfiguration-locale"></a>
The locale setting for the Case Summarization AI Agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_amazon-q-connect_CaseSummarizationAIAgentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/CaseSummarizationAIAgentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/CaseSummarizationAIAgentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/CaseSummarizationAIAgentConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
