---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Document.html
---

# Document
<a name="API_Document"></a>

A document in an Amazon Q Business application.

## Contents
<a name="API_Document_Contents"></a>

 ** id **   <a name="qbusiness-Type-Document-id"></a>
The identifier of the document.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1825.
Pattern: `\P{C}*`
Required: Yes

 ** accessConfiguration **   <a name="qbusiness-Type-Document-accessConfiguration"></a>
Configuration information for access permission to a document.
Type: [AccessConfiguration](API_AccessConfiguration.md) object
Required: No

 ** attributes **   <a name="qbusiness-Type-Document-attributes"></a>
Custom attributes to apply to the document for refining Amazon Q Business web experience responses.
Type: Array of [DocumentAttribute](API_DocumentAttribute.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Required: No

 ** content **   <a name="qbusiness-Type-Document-content"></a>
The contents of the document.
Type: [DocumentContent](API_DocumentContent.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** contentType **   <a name="qbusiness-Type-Document-contentType"></a>
The file type of the document in the Blob field.
If you want to index snippets or subsets of HTML documents instead of the entirety of the HTML documents, you add the `HTML` start and closing tags (`<HTML>content</HTML>`) around the content.
Type: String
Valid Values: `PDF | HTML | MS_WORD | PLAIN_TEXT | PPT | RTF | XML | XSLT | MS_EXCEL | CSV | JSON | MD`
Required: No

 ** documentEnrichmentConfiguration **   <a name="qbusiness-Type-Document-documentEnrichmentConfiguration"></a>
The configuration information for altering document metadata and content during the document ingestion process.
Type: [DocumentEnrichmentConfiguration](API_DocumentEnrichmentConfiguration.md) object
Required: No

 ** mediaExtractionConfiguration **   <a name="qbusiness-Type-Document-mediaExtractionConfiguration"></a>
The configuration for extracting information from media in the document.
Type: [MediaExtractionConfiguration](API_MediaExtractionConfiguration.md) object
Required: No

 ** title **   <a name="qbusiness-Type-Document-title"></a>
The title of the document.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_Document_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/Document)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/Document)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/Document)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
