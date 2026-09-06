---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_IndexSummary.html
---

# IndexSummary
<a name="API_S3VectorBuckets_IndexSummary"></a>

Summary information about a vector index.

## Contents
<a name="API_S3VectorBuckets_IndexSummary_Contents"></a>

 ** creationTime **   <a name="AmazonS3-Type-S3VectorBuckets_IndexSummary-creationTime"></a>
Date and time when the vector index was created.
Type: Timestamp
Required: Yes

 ** indexArn **   <a name="AmazonS3-Type-S3VectorBuckets_IndexSummary-indexArn"></a>
The Amazon Resource Name (ARN) of the vector index.
Type: String
Pattern: `arn:aws[-a-z0-9]*:s3vectors:[a-z0-9-]+:[0-9]{12}:bucket/[a-z0-9][a-z0-9-.]{1,61}[a-z0-9]/index/[a-z0-9][a-z0-9-.]{1,61}[a-z0-9]`
Required: Yes

 ** indexName **   <a name="AmazonS3-Type-S3VectorBuckets_IndexSummary-indexName"></a>
The name of the vector index.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: Yes

 ** vectorBucketName **   <a name="AmazonS3-Type-S3VectorBuckets_IndexSummary-vectorBucketName"></a>
The name of the vector bucket that contains the vector index.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: Yes

## See Also
<a name="API_S3VectorBuckets_IndexSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/IndexSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/IndexSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/IndexSummary)
