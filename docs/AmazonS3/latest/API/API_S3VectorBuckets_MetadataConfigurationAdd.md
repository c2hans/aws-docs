---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_MetadataConfigurationAdd.html
---

# MetadataConfigurationAdd
<a name="API_S3VectorBuckets_MetadataConfigurationAdd"></a>

Text search configurations to add to a vector index.

## Contents
<a name="API_S3VectorBuckets_MetadataConfigurationAdd_Contents"></a>

 ** textSearchConfigurations **   <a name="AmazonS3-Type-S3VectorBuckets_MetadataConfigurationAdd-textSearchConfigurations"></a>
Text search configurations to add. Amazon S3 Vectors begins building the corresponding full-text indexes after the update is accepted.
Type: Array of [TextSearchConfiguration](API_S3VectorBuckets_TextSearchConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_S3VectorBuckets_MetadataConfigurationAdd_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/MetadataConfigurationAdd)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/MetadataConfigurationAdd)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/MetadataConfigurationAdd)
