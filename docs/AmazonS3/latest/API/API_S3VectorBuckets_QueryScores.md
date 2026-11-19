---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_QueryScores.html
---

# QueryScores

Relevance scores for a full-text-only or hybrid search result.

## Contents
<a name="API_S3VectorBuckets_QueryScores_Contents"></a>

 ** bm25Scores **   <a name="AmazonS3-Type-S3VectorBuckets_QueryScores-bm25Scores"></a>
The BM25 scores for the searchable metadata keys that the result matched.
Type: Array of [Bm25Score](API_S3VectorBuckets_Bm25Score.md) objects
Required: No

 ** fused **   <a name="AmazonS3-Type-S3VectorBuckets_QueryScores-fused"></a>
The Reciprocal Rank Fusion (RRF) score that combines the vector and full-text rankings. This field is returned only for hybrid requests.
Type: Float
Required: No

 ** vectorDistance **   <a name="AmazonS3-Type-S3VectorBuckets_QueryScores-vectorDistance"></a>
The distance from the query vector. This field is returned when a hybrid result matches the vector search.
Type: Float
Required: No

## See Also
<a name="API_S3VectorBuckets_QueryScores_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/QueryScores)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/QueryScores)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/QueryScores)
