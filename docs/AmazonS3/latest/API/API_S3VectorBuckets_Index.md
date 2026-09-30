---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_Index.html
---

# Index
<a name="API_S3VectorBuckets_Index"></a>

The attributes of a vector index.

## Contents
<a name="API_S3VectorBuckets_Index_Contents"></a>

 ** creationTime **   <a name="AmazonS3-Type-S3VectorBuckets_Index-creationTime"></a>
Date and time when the vector index was created.
Type: Timestamp
Required: Yes

 ** dataType **   <a name="AmazonS3-Type-S3VectorBuckets_Index-dataType"></a>
The data type of the vectors inserted into the vector index.
Type: String
Valid Values: `float32`
Required: Yes

 ** dimension **   <a name="AmazonS3-Type-S3VectorBuckets_Index-dimension"></a>
The number of values in the vectors that are inserted into the vector index.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 4096.
Required: Yes

 ** distanceMetric **   <a name="AmazonS3-Type-S3VectorBuckets_Index-distanceMetric"></a>
The distance metric to be used for similarity search.
Type: String
Valid Values: `euclidean | cosine`
Required: Yes

 ** indexArn **   <a name="AmazonS3-Type-S3VectorBuckets_Index-indexArn"></a>
The Amazon Resource Name (ARN) of the vector index.
Type: String
Pattern: `arn:aws[-a-z0-9]*:s3vectors:[a-z0-9-]+:[0-9]{12}:bucket/[a-z0-9][a-z0-9-.]{1,61}[a-z0-9]/index/[a-z0-9][a-z0-9-.]{1,61}[a-z0-9]`
Required: Yes

 ** indexName **   <a name="AmazonS3-Type-S3VectorBuckets_Index-indexName"></a>
The name of the vector index.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: Yes

 ** vectorBucketName **   <a name="AmazonS3-Type-S3VectorBuckets_Index-vectorBucketName"></a>
The name of the vector bucket that contains the vector index.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: Yes

 ** encryptionConfiguration **   <a name="AmazonS3-Type-S3VectorBuckets_Index-encryptionConfiguration"></a>
The encryption configuration for a vector index. By default, if you don't specify, all new vectors in the vector index will use the encryption configuration of the vector bucket.
Type: [EncryptionConfiguration](API_S3VectorBuckets_EncryptionConfiguration.md) object
Required: No

 ** indexMode **   <a name="AmazonS3-Type-S3VectorBuckets_Index-indexMode"></a>
The mode that determines how the vector index processes queries.
Valid values:
+  `CLASSIC` - Applies metadata filters during the vector search.
+  `ENHANCED` - Applies metadata filters before the vector search.
Type: String
Valid Values: `CLASSIC | ENHANCED`
Required: No

 ** metadataConfiguration **   <a name="AmazonS3-Type-S3VectorBuckets_Index-metadataConfiguration"></a>
The metadata configuration for the vector index.
Type: [MetadataConfiguration](API_S3VectorBuckets_MetadataConfiguration.md) object
Required: No

## See Also
<a name="API_S3VectorBuckets_Index_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/Index)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/Index)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/Index)
