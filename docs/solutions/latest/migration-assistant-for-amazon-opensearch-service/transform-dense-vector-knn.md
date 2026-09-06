---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/transform-dense-vector-knn.html
---

# Transform dense\_vector fields to knn\_vector
<a name="transform-dense-vector-knn"></a>

Elasticsearch 7.x introduced the `dense_vector` field type for storing numeric vectors used in k-nearest neighbor (k-NN) and semantic search. Amazon OpenSearch Service and Amazon OpenSearch Serverless NextGen do not use that field type — they use the `knn_vector` field type instead. When you migrate metadata, Migration Assistant applies a built-in transformation that rewrites `dense_vector` mappings into equivalent `knn_vector` mappings on the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection, so your vector indexes can be created on the target without manual mapping edits.

This transformation runs automatically during the metadata migration phase, alongside the other built-in field-type transformations (`string` to `text` and `keyword`, and `flattened` to `flat_object`). For an overview of where metadata migration fits in the workflow, see [Migrate metadata](migrate-metadata.md).

**Note**
This transformation is metadata-only — it changes how the index is **defined** on the target. The vector values themselves are carried over during document backfill from the source snapshot. Migration Assistant does not recompute or re-embed vectors.
