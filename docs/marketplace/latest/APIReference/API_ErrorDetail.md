---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ErrorDetail.html
---

# ErrorDetail
<a name="API_ErrorDetail"></a>

Details about the error.

## Contents
<a name="API_ErrorDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ErrorCode **   <a name="AWSMarketplaceService-Type-ErrorDetail-ErrorCode"></a>
The error code that identifies the type of error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 72.
Pattern: `^[a-zA-Z_]+$`
Required: No

 ** ErrorMessage **   <a name="AWSMarketplaceService-Type-ErrorDetail-ErrorMessage"></a>
The message for the error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(.)+$`
Required: No

## See Also
<a name="API_ErrorDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ErrorDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ErrorDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ErrorDetail)
