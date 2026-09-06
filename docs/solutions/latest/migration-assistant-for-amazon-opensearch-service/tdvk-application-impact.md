---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/tdvk-application-impact.html
---

# Application impact
<a name="tdvk-application-impact"></a>

The transformation produces a queryable vector index, but k-NN query patterns on Amazon OpenSearch Service and Amazon OpenSearch Serverless NextGen can differ from the vector query syntax your application used on Elasticsearch. Plan to review and, where needed, update client query code:
+  **Query syntax differs** — Elasticsearch vector queries (for example, `knn` queries against a `dense_vector` field, or `script_score` with `cosineSimilarity`/`l2norm` functions) are not interchangeable with the OpenSearch k-NN query syntax used against a `knn_vector` field. Confirm the query shape your application sends matches what the target expects.
+  **Similarity scoring may differ** — Even when results are functionally similar, score values and ranking can shift because of the chosen space type and HNSW parameters. Treat exact score parity as something to verify, not assume.
+  **Query-time embeddings** — As described in [Amazon OpenSearch Serverless NextGen considerations](tdvk-serverless.md), applications that relied on a `model_id` to embed query text on the source may need to embed client-side against the target.

Validate these behaviors with representative vector queries in a pilot migration before you cut over production traffic. Use a small index allowlist or a representative non-production subset, as described in [Configure and run workflows](use-the-solution.md), so you can catch query-compatibility issues early. For the general guidance on validating transformed data against client applications, see [Migrate metadata](migrate-metadata.md).
