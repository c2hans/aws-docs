---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveMemoryConfiguration.html
---

# AgenticRetrieveMemoryConfiguration
<a name="API_agent-runtime_AgenticRetrieveMemoryConfiguration"></a>

Specifies an AgentCore Memory resource and how this retrieval uses it. Set sessionBinding to restore and continue a session. Set retrievalConfigs to let the agent retrieve from long-term memory. You must specify at least one of the two.

## Contents
<a name="API_agent-runtime_AgenticRetrieveMemoryConfiguration_Contents"></a>

 ** memoryId **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemoryConfiguration-memoryId"></a>
The identifier of the AgentCore Memory resource to use. The resource must exist in your account and be in the ACTIVE state.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 111.
Pattern: `[a-zA-Z][a-zA-Z0-9\-_]{0,99}-[a-zA-Z0-9]{10}`
Required: Yes

 ** persistenceMode **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemoryConfiguration-persistenceMode"></a>
Specifies whether the agent-generated answer is written back to the given short-term memory session, and applies only when sessionBinding is set. Valid values:
+  `DEFAULT` (default) – Specifies that the question and the agent-generated answer are persisted to the session as a single event. This value requires generateResponse to be true.
+  `NONE` – Specifies that the session is left unchanged.
Type: String
Valid Values: `DEFAULT | NONE`
Required: No

 ** retrievalConfigs **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemoryConfiguration-retrievalConfigs"></a>
Specifies the long-term memory configuration the agent can retrieve from. The agent decides whether to retrieve and composes its own query. This field currently accepts at most one entry.
Type: Array of [AgenticRetrieveMemoryRetrievalConfig](API_agent-runtime_AgenticRetrieveMemoryRetrievalConfig.md) objects
Required: No

 ** sessionBinding **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemoryConfiguration-sessionBinding"></a>
The short-term memory session whose history is restored for this retrieval. To persist the agent-generated answer to the session, omit persistenceMode or set it to DEFAULT. To leave the session unchanged, set persistenceMode to NONE. Supply session history through the existing messages parameter or through short-term memory, but not both.
Type: [AgenticRetrieveMemorySessionBinding](API_agent-runtime_AgenticRetrieveMemorySessionBinding.md) object
Required: No

## See Also
<a name="API_agent-runtime_AgenticRetrieveMemoryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMemoryConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMemoryConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMemoryConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
