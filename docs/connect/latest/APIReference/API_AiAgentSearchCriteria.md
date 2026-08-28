---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AiAgentSearchCriteria.html
---

# AiAgentSearchCriteria
<a name="API_AiAgentSearchCriteria"></a>

The search criteria based on AI Agents metadata.

## Contents
<a name="API_AiAgentSearchCriteria_Contents"></a>

 ** AiAgentEscalated **   <a name="connect-Type-AiAgentSearchCriteria-AiAgentEscalated"></a>
A boolean flag indicating whether the contact initially handled by this AI agent was escalated to a human agent.
Type: Boolean
Required: No

 ** AiUseCase **   <a name="connect-Type-AiAgentSearchCriteria-AiUseCase"></a>
The use case or scenario for which the AI agent is involved in the contact.
Type: String
Valid Values: `AgentAssistance | SelfService`
Required: No

 ** Id **   <a name="connect-Type-AiAgentSearchCriteria-Id"></a>
ID of the AI Agent that was involved in the contact.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}`
Required: No

 ** VersionNumber **   <a name="connect-Type-AiAgentSearchCriteria-VersionNumber"></a>
Version of the AI agent that was involved in the contact. ID is required if VersionNumber is passed.
Type: Integer
Required: No

## See Also
<a name="API_AiAgentSearchCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AiAgentSearchCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AiAgentSearchCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AiAgentSearchCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
