---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_S3.html
---

# S3
<a name="API_S3"></a>

Information required for Amazon Q Business to find a specific file in an Amazon S3 bucket.

## Contents
<a name="API_S3_Contents"></a>

 ** bucket **   <a name="qbusiness-Type-S3-bucket"></a>
The name of the S3 bucket that contains the file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`
Required: Yes

 ** key **   <a name="qbusiness-Type-S3-key"></a>
The name of the file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## See Also
<a name="API_S3_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/S3)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/S3)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/S3)
