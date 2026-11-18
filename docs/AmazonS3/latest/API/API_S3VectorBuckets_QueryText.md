---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_QueryText.html
---

# QueryText
<a name="API_S3VectorBuckets_QueryText"></a>

A full-text search query for a single metadata key.

## Contents
<a name="API_S3VectorBuckets_QueryText_Contents"></a>

 ** metadataKey **   <a name="AmazonS3-Type-S3VectorBuckets_QueryText-metadataKey"></a>
The searchable metadata key to query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Required: Yes

 ** text **   <a name="AmazonS3-Type-S3VectorBuckets_QueryText-text"></a>
The full-text query string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## See Also
<a name="API_S3VectorBuckets_QueryText_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/QueryText)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/QueryText)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/QueryText)
