---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_InquiryFileContent.html
---

# InquiryFileContent
<a name="API_InquiryFileContent"></a>

File content structure for compliance inquiry uploads.

## Contents
<a name="API_InquiryFileContent_Contents"></a>

 ** content **   <a name="artifact-Type-InquiryFileContent-content"></a>
Binary content of the uploaded file.
Type: Base64-encoded binary data object
Required: Yes

 ** fileSections **   <a name="artifact-Type-InquiryFileContent-fileSections"></a>
List of file sections/sheets to process.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_\-\s]*`
Required: No

## See Also
<a name="API_InquiryFileContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/InquiryFileContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/InquiryFileContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/InquiryFileContent)
