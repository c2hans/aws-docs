---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_EncryptionConfiguration.html
---

# EncryptionConfiguration
<a name="API_S3VectorBuckets_EncryptionConfiguration"></a>

The encryption configuration for a vector bucket or index. By default, if you don't specify, all new vectors in Amazon S3 vector buckets use server-side encryption with Amazon S3 managed keys (SSE-S3), specifically `AES256`. You can optionally override bucket level encryption settings, and set a specific encryption configuration for a vector index at the time of index creation.

## Contents
<a name="API_S3VectorBuckets_EncryptionConfiguration_Contents"></a>

 ** kmsKeyArn **   <a name="AmazonS3-Type-S3VectorBuckets_EncryptionConfiguration-kmsKeyArn"></a>
 AWS Key Management Service (KMS) customer managed key ID to use for the encryption configuration. This parameter is allowed if and only if `sseType` is set to `aws:kms`.
To specify the KMS key, you must use the format of the KMS key Amazon Resource Name (ARN).
For example, specify Key ARN in the following format: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[-a-z0-9]*:kms:[-a-z0-9]*:[0-9]{12}:key/.+)`
Required: No

 ** sseType **   <a name="AmazonS3-Type-S3VectorBuckets_EncryptionConfiguration-sseType"></a>
The server-side encryption type to use for the encryption configuration of the vector bucket. By default, if you don't specify, all new vectors in Amazon S3 vector buckets use server-side encryption with Amazon S3 managed keys (SSE-S3), specifically `AES256`.
Type: String
Valid Values: `AES256 | aws:kms`
Required: No

## See Also
<a name="API_S3VectorBuckets_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/EncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/EncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/EncryptionConfiguration)
