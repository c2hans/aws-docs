---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_DiskEncryptionConfiguration.html
---

# DiskEncryptionConfiguration
<a name="API_DiskEncryptionConfiguration"></a>

The configuration object that allows encrypting local disks.

## Contents
<a name="API_DiskEncryptionConfiguration_Contents"></a>

 ** encryptionContext **   <a name="emrserverless-Type-DiskEncryptionConfiguration-encryptionContext"></a>
Specifies the optional encryption context that will be used when encrypting the data. An encryption context is a collection of non-secret key-value pairs that represent additional authenticated data.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 8 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 384.
Required: No

 ** encryptionKeyArn **   <a name="emrserverless-Type-DiskEncryptionConfiguration-encryptionKeyArn"></a>
The KMS key ARN to encrypt local disks.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z0-9-]*):kms:[a-zA-Z0-9\-]*:([0-9]{12}):key\/[a-zA-Z0-9-]+`
Required: No

## See Also
<a name="API_DiskEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/DiskEncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/DiskEncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/DiskEncryptionConfiguration)
