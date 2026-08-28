---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RerankQuery.html
---

# RerankQuery
<a name="API_agent-runtime_RerankQuery"></a>

Contains information about a query to submit to the reranker model.

## Contents
<a name="API_agent-runtime_RerankQuery_Contents"></a>

 ** textQuery **   <a name="bedrock-Type-agent-runtime_RerankQuery-textQuery"></a>
Contains information about a text query.
Type: [RerankTextDocument](API_agent-runtime_RerankTextDocument.md) object
Required: Yes

 ** type **   <a name="bedrock-Type-agent-runtime_RerankQuery-type"></a>
The type of the query.
Type: String
Valid Values: `TEXT`
Required: Yes

## See Also
<a name="API_agent-runtime_RerankQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/RerankQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/RerankQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/RerankQuery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
