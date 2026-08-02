---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsS3BucketServerSideEncryptionByDefault.html
---

# AwsS3BucketServerSideEncryptionByDefault
<a name="API_AwsS3BucketServerSideEncryptionByDefault"></a>

Specifies the default server-side encryption to apply to new objects in the bucket.

## Contents
<a name="API_AwsS3BucketServerSideEncryptionByDefault_Contents"></a>

 ** KMSMasterKeyID **   <a name="securityhub-Type-AwsS3BucketServerSideEncryptionByDefault-KMSMasterKeyID"></a>
 AWS KMS key ID to use for the default encryption.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SSEAlgorithm **   <a name="securityhub-Type-AwsS3BucketServerSideEncryptionByDefault-SSEAlgorithm"></a>
Server-side encryption algorithm to use for the default encryption. Valid values are `aws: kms` or `AES256`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsS3BucketServerSideEncryptionByDefault_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsS3BucketServerSideEncryptionByDefault)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsS3BucketServerSideEncryptionByDefault)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsS3BucketServerSideEncryptionByDefault)
