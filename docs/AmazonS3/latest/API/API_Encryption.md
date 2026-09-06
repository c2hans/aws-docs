---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_Encryption.html
---

# Encryption
<a name="API_Encryption"></a>

Contains the type of server-side encryption used.

## Contents
<a name="API_Encryption_Contents"></a>

 ** EncryptionType **   <a name="AmazonS3-Type-Encryption-EncryptionType"></a>
The server-side encryption algorithm used when storing job results in Amazon S3 (for example, AES256, `aws:kms`).
Type: String
Valid Values: `AES256 | aws:fsx | aws:kms | aws:kms:dsse`
Required: Yes

 ** KMSContext **   <a name="AmazonS3-Type-Encryption-KMSContext"></a>
If the encryption type is `aws:kms`, this optional value can be used to specify the encryption context for the restore results.
Type: String
Required: No

 ** KMSKeyId **   <a name="AmazonS3-Type-Encryption-KMSKeyId"></a>
If the encryption type is `aws:kms`, this optional value specifies the ID of the symmetric encryption customer managed key to use for encryption of job results. Amazon S3 only supports symmetric encryption KMS keys. For more information, see [Asymmetric keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the * AWS Key Management Service Developer Guide*.
Type: String
Required: No

## See Also
<a name="API_Encryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Encryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Encryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Encryption)
