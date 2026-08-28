---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_RetrieveResult.html
---

# RetrieveResult
<a name="API_amazon-q-connect_RetrieveResult"></a>

A single result from a content retrieval operation.

## Contents
<a name="API_amazon-q-connect_RetrieveResult_Contents"></a>

 ** associationId **   <a name="connect-Type-amazon-q-connect_RetrieveResult-associationId"></a>
The identifier of the assistant association for the retrieved result.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** contentText **   <a name="connect-Type-amazon-q-connect_RetrieveResult-contentText"></a>
The text content of the retrieved result.
Type: String
Required: Yes

 ** referenceType **   <a name="connect-Type-amazon-q-connect_RetrieveResult-referenceType"></a>
A type to define the KB origin of a retrieved content.
Type: String
Valid Values: `WEB_CRAWLER | KNOWLEDGE_BASE | BEDROCK_KB_S3 | BEDROCK_KB_WEB | BEDROCK_KB_CONFLUENCE | BEDROCK_KB_SALESFORCE | BEDROCK_KB_SHAREPOINT | BEDROCK_KB_KENDRA | BEDROCK_KB_CUSTOM_DOCUMENT | BEDROCK_KB_SQL`
Required: Yes

 ** sourceId **   <a name="connect-Type-amazon-q-connect_RetrieveResult-sourceId"></a>
The URL, URI, or ID of the retrieved content when available, or a UUID when unavailable.
Type: String
Required: Yes

## See Also
<a name="API_amazon-q-connect_RetrieveResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/RetrieveResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/RetrieveResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/RetrieveResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
