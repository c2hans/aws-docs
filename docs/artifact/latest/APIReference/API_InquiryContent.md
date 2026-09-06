---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_InquiryContent.html
---

# InquiryContent
<a name="API_InquiryContent"></a>

Content for creating a compliance inquiry - either a single query or file content.

## Contents
<a name="API_InquiryContent_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** fileContent **   <a name="artifact-Type-InquiryContent-fileContent"></a>
File content with multiple questions.
Type: [InquiryFileContent](API_InquiryFileContent.md) object
Required: No

 ** query **   <a name="artifact-Type-InquiryContent-query"></a>
Single text query for AI-generated answer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

## See Also
<a name="API_InquiryContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/InquiryContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/InquiryContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/InquiryContent)
