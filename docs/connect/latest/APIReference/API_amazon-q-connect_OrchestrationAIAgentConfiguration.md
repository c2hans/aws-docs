---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_OrchestrationAIAgentConfiguration.html
---

# OrchestrationAIAgentConfiguration
<a name="API_amazon-q-connect_OrchestrationAIAgentConfiguration"></a>

The configuration for AI Agents of type `ORCHESTRATION`.

## Contents
<a name="API_amazon-q-connect_OrchestrationAIAgentConfiguration_Contents"></a>

 ** orchestrationAIPromptId **   <a name="connect-Type-amazon-q-connect_OrchestrationAIAgentConfiguration-orchestrationAIPromptId"></a>
The AI Prompt identifier used by the Orchestration AI Agent.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}`
Required: Yes

 ** connectInstanceArn **   <a name="connect-Type-amazon-q-connect_OrchestrationAIAgentConfiguration-connectInstanceArn"></a>
The Amazon Resource Name (ARN) of the Amazon Connect instance used by the Orchestration AI Agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z-]+?:[a-z-]+?:[a-z0-9-]*?:([0-9]{12})?:[a-zA-Z0-9-:/]+`
Required: No

 ** locale **   <a name="connect-Type-amazon-q-connect_OrchestrationAIAgentConfiguration-locale"></a>
The locale setting for the Orchestration AI Agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** orchestrationAIGuardrailId **   <a name="connect-Type-amazon-q-connect_OrchestrationAIAgentConfiguration-orchestrationAIGuardrailId"></a>
The AI Guardrail identifier used by the Orchestration AI Agent.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}`
Required: No

 ** toolConfigurations **   <a name="connect-Type-amazon-q-connect_OrchestrationAIAgentConfiguration-toolConfigurations"></a>
The tool configurations used by the Orchestration AI Agent.
Type: Array of [ToolConfiguration](API_amazon-q-connect_ToolConfiguration.md) objects
Required: No

## See Also
<a name="API_amazon-q-connect_OrchestrationAIAgentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/OrchestrationAIAgentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/OrchestrationAIAgentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/OrchestrationAIAgentConfiguration)
