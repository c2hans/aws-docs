---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_OrchestratorConfigurationEntry.html
---

# OrchestratorConfigurationEntry
<a name="API_amazon-q-connect_OrchestratorConfigurationEntry"></a>

An entry in the orchestrator configuration list.

## Contents
<a name="API_amazon-q-connect_OrchestratorConfigurationEntry_Contents"></a>

 ** orchestratorUseCase **   <a name="connect-Type-amazon-q-connect_OrchestratorConfigurationEntry-orchestratorUseCase"></a>
The use case for the orchestrator configuration. (for example Connect.SelfService, Connect.AgentAssistance)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** aiAgentId **   <a name="connect-Type-amazon-q-connect_OrchestratorConfigurationEntry-aiAgentId"></a>
The identifier of the AI Agent in the orchestrator configuration.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}`
Required: No

## See Also
<a name="API_amazon-q-connect_OrchestratorConfigurationEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/OrchestratorConfigurationEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/OrchestratorConfigurationEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/OrchestratorConfigurationEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
