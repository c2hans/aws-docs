---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_SSEKMSFilter.html
---

# SSEKMSFilter
<a name="API_control_SSEKMSFilter"></a>

A filter that returns objects that are encrypted by server-side encryption with AWS KMS (SSE-KMS).

## Contents
<a name="API_control_SSEKMSFilter_Contents"></a>

 ** BucketKeyEnabled **   <a name="AmazonS3-Type-control_SSEKMSFilter-BucketKeyEnabled"></a>
Specifies whether Amazon S3 should use an S3 Bucket Key for object encryption with server-side encryption using AWS Key Management Service (AWS KMS) keys (SSE-KMS). If specified, will filter SSE-KMS encrypted objects by S3 Bucket Key status.
Type: Boolean
Required: No

 ** KmsKeyArn **   <a name="AmazonS3-Type-control_SSEKMSFilter-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the customer managed KMS key to use for the filter to return objects that are encrypted by the specified key. For best performance, use keys in the same Region as the S3 Batch Operations job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-zA-Z0-9-]*:kms:[a-z0-9-]+:[0-9]{12}:key/[a-zA-Z0-9-]+`
Required: No

## See Also
<a name="API_control_SSEKMSFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/SSEKMSFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/SSEKMSFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/SSEKMSFilter)
