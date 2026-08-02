---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_EncryptionConfiguration.html
---

# EncryptionConfiguration
<a name="API_EncryptionConfiguration"></a>

The encryption configuration details.

## Contents
<a name="API_EncryptionConfiguration_Contents"></a>

 ** kmsKeyArn **   <a name="datazone-Type-EncryptionConfiguration-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key to use for encryption. This field is required only when `sseAlgorithm` is set to `aws:kms`.
Type: String
Required: No

 ** sseAlgorithm **   <a name="datazone-Type-EncryptionConfiguration-sseAlgorithm"></a>
The server-side encryption algorithm to use. Valid values are AES256 for S3-managed encryption keys, or aws:kms for AWS KMS-managed encryption keys. If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see [Permissions requirements for S3 Tables SSE-KMS encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html).
Type: String
Required: No

## See Also
<a name="API_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/EncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/EncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/EncryptionConfiguration)
