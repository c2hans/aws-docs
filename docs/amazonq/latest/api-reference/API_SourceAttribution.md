---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_SourceAttribution.html
---

# SourceAttribution
<a name="API_SourceAttribution"></a>

The documents used to generate an Amazon Q Business web experience response.

## Contents
<a name="API_SourceAttribution_Contents"></a>

 ** citationNumber **   <a name="qbusiness-Type-SourceAttribution-citationNumber"></a>
The number attached to a citation in an Amazon Q Business generated response.
Type: Integer
Required: No

 ** datasourceId **   <a name="qbusiness-Type-SourceAttribution-datasourceId"></a>
The identifier of the data source from which the document was ingested. This field is not present if the document is ingested by directly calling the BatchPutDocument API (similar to checkDocumentAccess). If the document is from a file-upload data source, the datasource will be "uploaded-docs-file-stat-datasourceid".
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** documentId **   <a name="qbusiness-Type-SourceAttribution-documentId"></a>
The unique identifier of the source document used in the citation, obtained from the Amazon Q Business index during chat response generation. This ID is used as input to the `GetDocumentContent` API to retrieve the actual document content for user verification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** indexId **   <a name="qbusiness-Type-SourceAttribution-indexId"></a>
The identifier of the index containing the source document's metadata and access control information. This links the citation back to the specific Amazon Q Business index where the document's searchable content and permissions are stored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** snippet **   <a name="qbusiness-Type-SourceAttribution-snippet"></a>
The content extract from the document on which the generated response is based.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** textMessageSegments **   <a name="qbusiness-Type-SourceAttribution-textMessageSegments"></a>
A text extract from a source document that is used for source attribution.
Type: Array of [TextSegment](API_TextSegment.md) objects
Required: No

 ** title **   <a name="qbusiness-Type-SourceAttribution-title"></a>
The title of the document which is the source for the Amazon Q Business generated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** updatedAt **   <a name="qbusiness-Type-SourceAttribution-updatedAt"></a>
The Unix timestamp when the Amazon Q Business application was last updated.
Type: Timestamp
Required: No

 ** url **   <a name="qbusiness-Type-SourceAttribution-url"></a>
The URL of the document which is the source for the Amazon Q Business generated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_SourceAttribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/SourceAttribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/SourceAttribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/SourceAttribution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
