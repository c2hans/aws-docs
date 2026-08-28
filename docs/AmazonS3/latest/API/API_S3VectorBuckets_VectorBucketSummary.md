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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
