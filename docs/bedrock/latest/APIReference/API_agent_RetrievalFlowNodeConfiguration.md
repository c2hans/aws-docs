---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_RetrievalFlowNodeConfiguration.html
---

# RetrievalFlowNodeConfiguration
<a name="API_agent_RetrievalFlowNodeConfiguration"></a>

Contains configurations for a Retrieval node in a flow. This node retrieves data from the Amazon S3 location that you specify and returns it as the output.

## Contents
<a name="API_agent_RetrievalFlowNodeConfiguration_Contents"></a>

 ** serviceConfiguration **   <a name="bedrock-Type-agent_RetrievalFlowNodeConfiguration-serviceConfiguration"></a>
Contains configurations for the service to use for retrieving data to return as the output from the node.
Type: [RetrievalFlowNodeServiceConfiguration](API_agent_RetrievalFlowNodeServiceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_agent_RetrievalFlowNodeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/RetrievalFlowNodeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/RetrievalFlowNodeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/RetrievalFlowNodeConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
