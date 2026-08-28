---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveMemoryRetrieveDetails.html
---

# AgenticRetrieveMemoryRetrieveDetails
<a name="API_agent-runtime_AgenticRetrieveMemoryRetrieveDetails"></a>

A long-term memory retrieval that the agent chose to perform. The record reports the query and the namespace. The corresponding Retrieval step reports the results.

## Contents
<a name="API_agent-runtime_AgenticRetrieveMemoryRetrieveDetails_Contents"></a>

 ** inputQuery **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemoryRetrieveDetails-inputQuery"></a>
The query that the agent composed.
Type: [AgenticRetrieveMessageContent](API_agent-runtime_AgenticRetrieveMessageContent.md) object
Required: Yes

 ** memoryId **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemoryRetrieveDetails-memoryId"></a>
The identifier of the AgentCore Memory resource retrieved from.
Type: String
Required: Yes

 ** namespace **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemoryRetrieveDetails-namespace"></a>
The namespace prefix retrieved from, as supplied in the request. This field is present when the request specified namespace.
Type: String
Required: No

 ** namespacePath **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemoryRetrieveDetails-namespacePath"></a>
The parent namespace retrieved from hierarchically, as supplied in the request. This field is present when the request specified namespacePath.
Type: String
Required: No

 ** strategyId **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMemoryRetrieveDetails-strategyId"></a>
The extraction strategy that restricted retrieval, if the request specified one.
Type: String
Required: No

## See Also
<a name="API_agent-runtime_AgenticRetrieveMemoryRetrieveDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMemoryRetrieveDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMemoryRetrieveDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMemoryRetrieveDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
