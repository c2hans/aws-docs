---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_Citation.html
---

# Citation
<a name="API_amazon-q-connect_Citation"></a>

A citation that references source content.

## Contents
<a name="API_amazon-q-connect_Citation_Contents"></a>

 ** citationSpan **   <a name="connect-Type-amazon-q-connect_Citation-citationSpan"></a>
Contains information about where the text with a citation begins and ends in the generated output.
Type: [CitationSpan](API_amazon-q-connect_CitationSpan.md) object
Required: Yes

 ** referenceType **   <a name="connect-Type-amazon-q-connect_Citation-referenceType"></a>
A type to define the KB origin of a cited content
Type: String
Valid Values: `WEB_CRAWLER | KNOWLEDGE_BASE | BEDROCK_KB_S3 | BEDROCK_KB_WEB | BEDROCK_KB_CONFLUENCE | BEDROCK_KB_SALESFORCE | BEDROCK_KB_SHAREPOINT | BEDROCK_KB_KENDRA | BEDROCK_KB_CUSTOM_DOCUMENT | BEDROCK_KB_SQL`
Required: Yes

 ** contentId **   <a name="connect-Type-amazon-q-connect_Citation-contentId"></a>
The identifier of the content being cited.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** knowledgeBaseId **   <a name="connect-Type-amazon-q-connect_Citation-knowledgeBaseId"></a>
The identifier of the knowledge base containing the cited content.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** sourceURL **   <a name="connect-Type-amazon-q-connect_Citation-sourceURL"></a>
The source URL for the citation.
Type: String
Required: No

 ** title **   <a name="connect-Type-amazon-q-connect_Citation-title"></a>
The title of the cited content.
Type: String
Required: No

## See Also
<a name="API_amazon-q-connect_Citation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/Citation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/Citation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/Citation)
