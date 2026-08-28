---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_TextSegment.html
---

# TextSegment
<a name="API_TextSegment"></a>

Provides information about a text extract in a chat response that can be attributed to a source document.

## Contents
<a name="API_TextSegment_Contents"></a>

 ** beginOffset **   <a name="qbusiness-Type-TextSegment-beginOffset"></a>
The zero-based location in the response string where the source attribution starts.
Type: Integer
Required: No

 ** endOffset **   <a name="qbusiness-Type-TextSegment-endOffset"></a>
The zero-based location in the response string where the source attribution ends.
Type: Integer
Required: No

 ** mediaId **   <a name="qbusiness-Type-TextSegment-mediaId"></a>
 *This member has been deprecated.*
The identifier of the media object associated with the text segment in the source attribution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** mediaMimeType **   <a name="qbusiness-Type-TextSegment-mediaMimeType"></a>
 *This member has been deprecated.*
The MIME type (image/png) of the media object associated with the text segment in the source attribution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** snippetExcerpt **   <a name="qbusiness-Type-TextSegment-snippetExcerpt"></a>
The relevant text excerpt from a source that was used to generate a citation text segment in an Amazon Q Business chat response.
Type: [SnippetExcerpt](API_SnippetExcerpt.md) object
Required: No

 ** sourceDetails **   <a name="qbusiness-Type-TextSegment-sourceDetails"></a>
Source information for a segment of extracted text, including its media type.
Type: [SourceDetails](API_SourceDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_TextSegment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/TextSegment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/TextSegment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/TextSegment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
