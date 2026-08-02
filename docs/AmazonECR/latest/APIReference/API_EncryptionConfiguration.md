---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_EncryptionConfiguration.html
---

# EncryptionConfiguration
<a name="API_EncryptionConfiguration"></a>

The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest.

By default, when no encryption configuration is set or the `AES256` encryption type is used, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts your data at rest using an AES256 encryption algorithm. This does not require any action on your part.

For more control over the encryption of the contents of your repository, you can use server-side encryption with AWS Key Management Service key stored in AWS Key Management Service (AWS KMS) to encrypt your images. For more information, see [Amazon ECR encryption at rest](https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html) in the *Amazon Elastic Container Registry User Guide*.

## Contents
<a name="API_EncryptionConfiguration_Contents"></a>

 ** encryptionType **   <a name="ECR-Type-EncryptionConfiguration-encryptionType"></a>
The encryption type to use.
If you use the `KMS` encryption type, the contents of the repository will be encrypted using server-side encryption with AWS Key Management Service key stored in AWS KMS. When you use AWS KMS to encrypt your data, you can either use the default AWS managed AWS KMS key for Amazon ECR, or specify your own AWS KMS key, which you already created.
If you use the `KMS_DSSE` encryption type, the contents of the repository will be encrypted with two layers of encryption using server-side encryption with the AWS KMS Management Service key stored in AWS KMS. Similar to the `KMS` encryption type, you can either use the default AWS managed AWS KMS key for Amazon ECR, or specify your own AWS KMS key, which you've already created.
If you use the `AES256` encryption type, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts the images in the repository using an AES256 encryption algorithm.
For more information, see [Amazon ECR encryption at rest](https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html) in the *Amazon Elastic Container Registry User Guide*.
Type: String
Valid Values: `AES256 | KMS | KMS_DSSE`
Required: Yes

 ** kmsKey **   <a name="ECR-Type-EncryptionConfiguration-kmsKey"></a>
If you use the `KMS` encryption type, specify the AWS KMS key to use for encryption. The alias, key ID, or full ARN of the AWS KMS key can be specified. The key must exist in the same Region as the repository. If no key is specified, the default AWS managed AWS KMS key for Amazon ECR will be used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/EncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/EncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/EncryptionConfiguration)
