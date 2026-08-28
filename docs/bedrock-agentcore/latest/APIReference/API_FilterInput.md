---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_FilterInput.html
---

# FilterInput
<a name="API_FilterInput"></a>

Contains filter criteria for listing events.

## Contents
<a name="API_FilterInput_Contents"></a>

 ** branch **   <a name="BedrockAgentCore-Type-FilterInput-branch"></a>
The branch filter criteria to apply when listing events.
Type: [BranchFilter](API_BranchFilter.md) object
Required: No

 ** eventMetadata **   <a name="BedrockAgentCore-Type-FilterInput-eventMetadata"></a>
Event metadata filter criteria to apply when retrieving events.
Type: Array of [EventMetadataFilterExpression](API_EventMetadataFilterExpression.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

## See Also
<a name="API_FilterInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/FilterInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/FilterInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/FilterInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
