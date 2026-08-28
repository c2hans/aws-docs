---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_RetrievalFlowNodeServiceConfiguration.html
---

# RetrievalFlowNodeServiceConfiguration
<a name="API_agent_RetrievalFlowNodeServiceConfiguration"></a>

Contains configurations for the service to use for retrieving data to return as the output from the node.

## Contents
<a name="API_agent_RetrievalFlowNodeServiceConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** s3 **   <a name="bedrock-Type-agent_RetrievalFlowNodeServiceConfiguration-s3"></a>
Contains configurations for the Amazon S3 location from which to retrieve data to return as the output from the node.
Type: [RetrievalFlowNodeS3Configuration](API_agent_RetrievalFlowNodeS3Configuration.md) object
Required: No

## See Also
<a name="API_agent_RetrievalFlowNodeServiceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/RetrievalFlowNodeServiceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/RetrievalFlowNodeServiceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/RetrievalFlowNodeServiceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
