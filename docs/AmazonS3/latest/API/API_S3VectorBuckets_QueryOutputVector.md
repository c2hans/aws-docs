---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_QueryOutputVector.html
---

# QueryOutputVector
<a name="API_S3VectorBuckets_QueryOutputVector"></a>

The attributes of a vector in the approximate nearest neighbor search.

## Contents
<a name="API_S3VectorBuckets_QueryOutputVector_Contents"></a>

 ** key **   <a name="AmazonS3-Type-S3VectorBuckets_QueryOutputVector-key"></a>
The key of the vector in the approximate nearest neighbor search.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** distance **   <a name="AmazonS3-Type-S3VectorBuckets_QueryOutputVector-distance"></a>
The measure of similarity between the vector in the response and the query vector.
Type: Float
Required: No

 ** metadata **   <a name="AmazonS3-Type-S3VectorBuckets_QueryOutputVector-metadata"></a>
The metadata associated with the vector, if requested.
Type: JSON value
Required: No

## See Also
<a name="API_S3VectorBuckets_QueryOutputVector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/QueryOutputVector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/QueryOutputVector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/QueryOutputVector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
