---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_SSEKMSEncryption.html
---

# SSEKMSEncryption
<a name="API_SSEKMSEncryption"></a>

 If `SSEKMS` is specified for `ObjectEncryption`, this data type specifies the AWS KMS key Amazon Resource Name (ARN) to use and whether to use an S3 Bucket Key for server-side encryption using AWS Key Management Service (AWS KMS) keys (SSE-KMS).

## Contents
<a name="API_SSEKMSEncryption_Contents"></a>

 ** KMSKeyArn **   <a name="AmazonS3-Type-SSEKMSEncryption-KMSKeyArn"></a>
 Specifies the AWS KMS key Amazon Resource Name (ARN) to use for the updated server-side encryption type. Required if `ObjectEncryption` specifies `SSEKMS`.
You must specify the full AWS KMS key ARN. The KMS key ID and KMS key alias aren't supported.
Pattern: (`arn:aws[-a-z0-9]*:kms:[-a-z0-9]*:[0-9]{12}:key/.+`)
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-zA-Z0-9-]*:kms:[a-z0-9-]+:[0-9]{12}:key/[a-zA-Z0-9-]+`
Required: Yes

 ** BucketKeyEnabled **   <a name="AmazonS3-Type-SSEKMSEncryption-BucketKeyEnabled"></a>
 Specifies whether Amazon S3 should use an S3 Bucket Key for object encryption with server-side encryption using AWS Key Management Service (AWS KMS) keys (SSE-KMS). If this value isn't specified, it defaults to `false`. Setting this value to `true` causes Amazon S3 to use an S3 Bucket Key for object encryption with SSE-KMS. For more information, see [ Using Amazon S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html) in the *Amazon S3 User Guide*.
Valid Values: `true` \| `false`
Type: Boolean
Required: No

## See Also
<a name="API_SSEKMSEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/SSEKMSEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/SSEKMSEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/SSEKMSEncryption)
