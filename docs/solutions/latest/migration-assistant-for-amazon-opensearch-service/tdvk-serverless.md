---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/tdvk-serverless.html
---

# Amazon OpenSearch Serverless NextGen considerations
<a name="tdvk-serverless"></a>

Amazon OpenSearch Serverless NextGen vector search collections (collection type `VECTORSEARCH`) accept vector fields, but they constrain how those fields can be defined. When the target is an Amazon OpenSearch Serverless NextGen collection, Migration Assistant applies additional vector compatibility transformations so the produced `knn_vector` mapping is valid for the collection:
+  **Faiss HNSW for compatibility** — The `knn_vector` field is configured to use a Faiss HNSW method so the mapping aligns with what an Amazon OpenSearch Serverless NextGen vector search collection supports.
+  **No model-based query-time embeddings** — Amazon OpenSearch Serverless NextGen vector search collections do not run inference for query-time embedding generation the way a managed cluster with ML nodes can. Because of this, the produced mapping is constrained to what the collection accepts, and a source mapping that relied on a model reference (such as `model_id`) to embed query text on the source will not embed query text on the collection. Plan for your application to produce the vector embeddings and send them as raw vectors in queries against the collection.

When you migrate vector data to Amazon OpenSearch Serverless NextGen, also review the broader serverless-specific guidance — including authentication with `service: aoss`, data access policies for the migration IAM role, and other collection constraints — in [Migrate to Amazon OpenSearch Serverless NextGen](migrate-to-serverless.md).

**Important**
Because Amazon OpenSearch Serverless NextGen vector search collections do not support model-based, query-time embedding generation, any source application that relied on the cluster to embed query text must be updated to compute embeddings client-side before cutover. Validate this behavior change against the collection during your pilot.
