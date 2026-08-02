---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_RelevantContent.html
---

# RelevantContent
<a name="API_RelevantContent"></a>

Represents a piece of content that is relevant to a search query.

## Contents
<a name="API_RelevantContent_Contents"></a>

 ** content **   <a name="qbusiness-Type-RelevantContent-content"></a>
The actual content of the relevant item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** documentAttributes **   <a name="qbusiness-Type-RelevantContent-documentAttributes"></a>
Additional attributes of the document containing the relevant content.
Type: Array of [DocumentAttribute](API_DocumentAttribute.md) objects
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Required: No

 ** documentId **   <a name="qbusiness-Type-RelevantContent-documentId"></a>
The unique identifier of the document containing the relevant content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1825.
Pattern: `\P{C}*`
Required: No

 ** documentTitle **   <a name="qbusiness-Type-RelevantContent-documentTitle"></a>
The title of the document containing the relevant content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** documentUri **   <a name="qbusiness-Type-RelevantContent-documentUri"></a>
The URI of the document containing the relevant content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(https?|ftp|file)://([^\s]*)`
Required: No

 ** scoreAttributes **   <a name="qbusiness-Type-RelevantContent-scoreAttributes"></a>
Attributes related to the relevance score of the content.
Type: [ScoreAttributes](API_ScoreAttributes.md) object
Required: No

## See Also
<a name="API_RelevantContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/RelevantContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/RelevantContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/RelevantContent)
