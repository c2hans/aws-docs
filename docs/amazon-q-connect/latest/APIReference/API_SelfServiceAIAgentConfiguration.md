---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_SelfServiceAIAgentConfiguration.html
---

# SelfServiceAIAgentConfiguration
<a name="API_amazon-q-connect_SelfServiceAIAgentConfiguration"></a>

The configuration for AI Agents of type SELF\_SERVICE.

## Contents
<a name="API_amazon-q-connect_SelfServiceAIAgentConfiguration_Contents"></a>

 ** associationConfigurations **   <a name="connect-Type-amazon-q-connect_SelfServiceAIAgentConfiguration-associationConfigurations"></a>
The association configurations for overriding behavior on this AI Agent.
Type: Array of [AssociationConfiguration](API_amazon-q-connect_AssociationConfiguration.md) objects
Required: No

 ** selfServiceAIGuardrailId **   <a name="connect-Type-amazon-q-connect_SelfServiceAIAgentConfiguration-selfServiceAIGuardrailId"></a>
The AI Guardrail identifier used by the SELF\_SERVICE AI Agent.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}`
Required: No

 ** selfServiceAnswerGenerationAIPromptId **   <a name="connect-Type-amazon-q-connect_SelfServiceAIAgentConfiguration-selfServiceAnswerGenerationAIPromptId"></a>
The AI Prompt identifier for the Self Service Answer Generation prompt used by the SELF\_SERVICE AI Agent
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}`
Required: No

 ** selfServicePreProcessingAIPromptId **   <a name="connect-Type-amazon-q-connect_SelfServiceAIAgentConfiguration-selfServicePreProcessingAIPromptId"></a>
The AI Prompt identifier for the Self Service Pre-Processing prompt used by the SELF\_SERVICE AI Agent
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}`
Required: No

## See Also
<a name="API_amazon-q-connect_SelfServiceAIAgentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/SelfServiceAIAgentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/SelfServiceAIAgentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/SelfServiceAIAgentConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
