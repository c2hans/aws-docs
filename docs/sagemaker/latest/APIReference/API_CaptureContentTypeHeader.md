---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CaptureContentTypeHeader.html
---

# CaptureContentTypeHeader
<a name="API_CaptureContentTypeHeader"></a>

Configuration specifying how to treat different headers. If no headers are specified Amazon SageMaker AI will by default base64 encode when capturing the data.

## Contents
<a name="API_CaptureContentTypeHeader_Contents"></a>

 ** CsvContentTypes **   <a name="sagemaker-Type-CaptureContentTypeHeader-CsvContentTypes"></a>
The list of all content type headers that Amazon SageMaker AI will treat as CSV and capture accordingly.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*\/[a-zA-Z0-9](-*[a-zA-Z0-9.])*`
Required: No

 ** JsonContentTypes **   <a name="sagemaker-Type-CaptureContentTypeHeader-JsonContentTypes"></a>
The list of all content type headers that SageMaker AI will treat as JSON and capture accordingly.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*\/[a-zA-Z0-9](-*[a-zA-Z0-9.])*`
Required: No

## See Also
<a name="API_CaptureContentTypeHeader_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CaptureContentTypeHeader)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CaptureContentTypeHeader)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CaptureContentTypeHeader)
