---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ErrorDetail.html
---

# ErrorDetail
<a name="API_ErrorDetail"></a>

Provides information about a Amazon Q Business request error.

## Contents
<a name="API_ErrorDetail_Contents"></a>

 ** errorCode **   <a name="qbusiness-Type-ErrorDetail-errorCode"></a>
The code associated with the Amazon Q Business request error.
Type: String
Valid Values: `InternalError | InvalidRequest | ResourceInactive | ResourceNotFound`
Required: No

 ** errorMessage **   <a name="qbusiness-Type-ErrorDetail-errorMessage"></a>
The message explaining the Amazon Q Business request error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_ErrorDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/ErrorDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/ErrorDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/ErrorDetail)
