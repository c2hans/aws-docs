---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_MetadataConfiguration.html
---

# MetadataConfiguration
<a name="API_S3VectorBuckets_MetadataConfiguration"></a>

The metadata configuration for a vector index.

## Contents
<a name="API_S3VectorBuckets_MetadataConfiguration_Contents"></a>

 ** nonFilterableMetadataKeys **   <a name="AmazonS3-Type-S3VectorBuckets_MetadataConfiguration-nonFilterableMetadataKeys"></a>
Non-filterable metadata keys allow you to enrich vectors with additional context during storage and retrieval. You can't use these keys in metadata filters. You can still make a non-filterable key full-text searchable by configuring it separately in `textSearchConfigurations`. You can retrieve non-filterable metadata keys after finding the vectors. For more information about non-filterable metadata keys, see [Vectors](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-vectors.html) and [Limitations and restrictions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-limitations.html) in the *Amazon S3 User Guide*.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 63.
Required: No

 ** textSearchConfigurations **   <a name="AmazonS3-Type-S3VectorBuckets_MetadataConfiguration-textSearchConfigurations"></a>
Full-text search configurations for searchable metadata keys.
Type: Array of [TextSearchConfiguration](API_S3VectorBuckets_TextSearchConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_S3VectorBuckets_MetadataConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/MetadataConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/MetadataConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/MetadataConfiguration)
