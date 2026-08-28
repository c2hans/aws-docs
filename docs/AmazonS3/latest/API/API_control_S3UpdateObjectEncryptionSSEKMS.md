---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3UpdateObjectEncryptionSSEKMS.html
---

# S3UpdateObjectEncryptionSSEKMS
<a name="API_control_S3UpdateObjectEncryptionSSEKMS"></a>

If `SSEKMS` is specified for `UpdateObjectEncryption`, this data type specifies the AWS KMS key Amazon Resource Name (ARN) to use and whether to use an S3 Bucket Key for server-side encryption using AWS Key Management Service (AWS KMS) keys (SSE-KMS).

## Contents
<a name="API_control_S3UpdateObjectEncryptionSSEKMS_Contents"></a>

 ** KMSKeyArn **   <a name="AmazonS3-Type-control_S3UpdateObjectEncryptionSSEKMS-KMSKeyArn"></a>
Specifies the AWS KMS key Amazon Resource Name (ARN) to use for the updated server-side encryption type. Required if `UpdateObjectEncryption` specifies `SSEKMS`.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-zA-Z0-9-]*:kms:[a-z0-9-]+:[0-9]{12}:key/[a-zA-Z0-9-]+`
Required: Yes

 ** BucketKeyEnabled **   <a name="AmazonS3-Type-control_S3UpdateObjectEncryptionSSEKMS-BucketKeyEnabled"></a>
Specifies whether Amazon S3 should use an S3 Bucket Key for object encryption with server-side encryption using AWS Key Management Service (AWS KMS) keys (SSE-KMS). If this value isn't specified, it defaults to `false`. Setting this value to `true` causes Amazon S3 to use an S3 Bucket Key for update object encryption with SSE-KMS.
Type: Boolean
Required: No

## See Also
<a name="API_control_S3UpdateObjectEncryptionSSEKMS_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3UpdateObjectEncryptionSSEKMS)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3UpdateObjectEncryptionSSEKMS)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3UpdateObjectEncryptionSSEKMS)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
