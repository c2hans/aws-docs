---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ProtectedJobS3OutputConfigurationOutput.html
---

# ProtectedJobS3OutputConfigurationOutput
<a name="API_ProtectedJobS3OutputConfigurationOutput"></a>

 The output configuration for a protected job's S3 output.

## Contents
<a name="API_ProtectedJobS3OutputConfigurationOutput_Contents"></a>

 ** bucket **   <a name="API-Type-ProtectedJobS3OutputConfigurationOutput-bucket"></a>
 The S3 bucket for job output.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `.*(?!^(\d+\.)+\d+$)(^(([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])\.)*([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])$).*`
Required: Yes

 ** keyPrefix **   <a name="API-Type-ProtectedJobS3OutputConfigurationOutput-keyPrefix"></a>
The S3 prefix to unload the protected job results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[\w!.=*/-]*`
Required: No

## See Also
<a name="API_ProtectedJobS3OutputConfigurationOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ProtectedJobS3OutputConfigurationOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ProtectedJobS3OutputConfigurationOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ProtectedJobS3OutputConfigurationOutput)
