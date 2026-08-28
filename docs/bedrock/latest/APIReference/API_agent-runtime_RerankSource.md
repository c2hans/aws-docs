---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RerankSource.html
---

# RerankSource
<a name="API_agent-runtime_RerankSource"></a>

Contains information about a source for reranking.

## Contents
<a name="API_agent-runtime_RerankSource_Contents"></a>

 ** inlineDocumentSource **   <a name="bedrock-Type-agent-runtime_RerankSource-inlineDocumentSource"></a>
Contains an inline definition of a source for reranking.
Type: [RerankDocument](API_agent-runtime_RerankDocument.md) object
Required: Yes

 ** type **   <a name="bedrock-Type-agent-runtime_RerankSource-type"></a>
The type of the source.
Type: String
Valid Values: `INLINE`
Required: Yes

## See Also
<a name="API_agent-runtime_RerankSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/RerankSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/RerankSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/RerankSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
