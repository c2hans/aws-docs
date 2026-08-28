---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_RetrievalConfiguration.html
---

# RetrievalConfiguration
<a name="API_amazon-q-connect_RetrievalConfiguration"></a>

Configuration for content retrieval operations.

## Contents
<a name="API_amazon-q-connect_RetrievalConfiguration_Contents"></a>

 ** knowledgeSource **   <a name="connect-Type-amazon-q-connect_RetrievalConfiguration-knowledgeSource"></a>
The knowledge source configuration for content retrieval.
Type: [KnowledgeSource](API_amazon-q-connect_KnowledgeSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** filter **   <a name="connect-Type-amazon-q-connect_RetrievalConfiguration-filter"></a>
The filter configuration for content retrieval.
Type: [RetrievalFilterConfiguration](API_amazon-q-connect_RetrievalFilterConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** numberOfResults **   <a name="connect-Type-amazon-q-connect_RetrievalConfiguration-numberOfResults"></a>
The number of results to retrieve.
Type: Integer
Required: No

 ** overrideKnowledgeBaseSearchType **   <a name="connect-Type-amazon-q-connect_RetrievalConfiguration-overrideKnowledgeBaseSearchType"></a>
Override setting for the knowledge base search type during retrieval.
Type: String
Valid Values: `HYBRID | SEMANTIC`
Required: No

## See Also
<a name="API_amazon-q-connect_RetrievalConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/RetrievalConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/RetrievalConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/RetrievalConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
