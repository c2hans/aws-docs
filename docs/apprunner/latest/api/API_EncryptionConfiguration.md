---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_EncryptionConfiguration.html
---

# EncryptionConfiguration
<a name="API_EncryptionConfiguration"></a>

Describes a custom encryption key that AWS App Runner uses to encrypt copies of the source repository and service logs.

## Contents
<a name="API_EncryptionConfiguration_Contents"></a>

 ** KmsKey **   <a name="apprunner-Type-EncryptionConfiguration-KmsKey"></a>
The ARN of the KMS key that's used for encryption.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:kms:[a-z\-]+-[0-9]{1}:[0-9]{12}:key\/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## See Also
<a name="API_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/EncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/EncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/EncryptionConfiguration)
