---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_VectorBucketSummary.html
---

# VectorBucketSummary
<a name="API_S3VectorBuckets_VectorBucketSummary"></a>

Summary information about a vector bucket.

## Contents
<a name="API_S3VectorBuckets_VectorBucketSummary_Contents"></a>

 ** creationTime **   <a name="AmazonS3-Type-S3VectorBuckets_VectorBucketSummary-creationTime"></a>
Date and time when the vector bucket was created.
Type: Timestamp
Required: Yes

 ** vectorBucketArn **   <a name="AmazonS3-Type-S3VectorBuckets_VectorBucketSummary-vectorBucketArn"></a>
The Amazon Resource Name (ARN) of the vector bucket.
Type: String
Pattern: `arn:aws[-a-z0-9]*:s3vectors:[a-z0-9-]+:[0-9]{12}:bucket/[a-z0-9][a-z0-9-.]{1,61}[a-z0-9]`
Required: Yes

 ** vectorBucketName **   <a name="AmazonS3-Type-S3VectorBuckets_VectorBucketSummary-vectorBucketName"></a>
The name of the vector bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: Yes

## See Also
<a name="API_S3VectorBuckets_VectorBucketSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/VectorBucketSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/VectorBucketSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/VectorBucketSummary)
