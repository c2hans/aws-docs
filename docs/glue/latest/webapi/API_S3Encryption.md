---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_S3Encryption.html
---

# S3Encryption
<a name="API_S3Encryption"></a>

Specifies how Amazon Simple Storage Service (Amazon S3) data should be encrypted.

## Contents
<a name="API_S3Encryption_Contents"></a>

 ** KmsKeyArn **   <a name="Glue-Type-S3Encryption-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.
Type: String
Pattern: `^$|arn:aws[a-z0-9-]*:kms:.*`
Required: No

 ** S3EncryptionMode **   <a name="Glue-Type-S3Encryption-S3EncryptionMode"></a>
The encryption mode to use for Amazon S3 data.
Type: String
Valid Values: `DISABLED | SSE-KMS | SSE-S3`
Required: No

## See Also
<a name="API_S3Encryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/S3Encryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/S3Encryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/S3Encryption)
