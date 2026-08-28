---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveTraceResultItem.html
---

# AgenticRetrieveTraceResultItem
<a name="API_agent-runtime_AgenticRetrieveTraceResultItem"></a>

A result item from an agentic retrieval trace.

## Contents
<a name="API_agent-runtime_AgenticRetrieveTraceResultItem_Contents"></a>

 ** content **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveTraceResultItem-content"></a>
The retrieved content.
Type: [RetrievalContent](API_agent-runtime_RetrievalContent.md) object
Required: No

 ** metadata **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveTraceResultItem-metadata"></a>
Metadata associated with the retrieved item.
Type: String to JSON value map
Required: No

 ** sourceRetriever **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveTraceResultItem-sourceRetriever"></a>
The source retriever that produced this result.
Type: [AgenticRetrieveSourceRetriever](API_agent-runtime_AgenticRetrieveSourceRetriever.md) object
Required: No

## See Also
<a name="API_agent-runtime_AgenticRetrieveTraceResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveTraceResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveTraceResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveTraceResultItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
