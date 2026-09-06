---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/tdvk-builtin-behavior.html
---

# Built-in transformation behavior
<a name="tdvk-builtin-behavior"></a>

When Migration Assistant encounters a `dense_vector` field in a source mapping, template, or component template, it produces a `knn_vector` field on the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. The transformation maps the source field’s vector definition to the equivalent OpenSearch concepts:
+  **Dimension** — The source vector length is carried over to the `knn_vector` `dimension` property. The number of dimensions does not change.
+  **Similarity** — The source vector similarity is translated to the corresponding OpenSearch space type (`space_type`). For example, a cosine similarity on the source maps to a cosine space type on the target, and a Euclidean (L2) similarity maps to an L2 space type. The transformation chooses an OpenSearch space type that preserves the intended distance semantics.
+  **Algorithm parameters** — The transformation defines a Hierarchical Navigable Small World (HNSW) method (`method.name` is `hnsw`) and sets HNSW build and search parameters such as `ef_construction` and `m` so the resulting index is queryable as soon as documents are backfilled.

The result is a complete, valid `knn_vector` mapping. A simplified example of the kind of mapping the transformation produces is:

```
{
  "properties": {
    "embedding": {
      "type": "knn_vector",
      "dimension": 768,
      "method": {
        "name": "hnsw",
        "space_type": "cosinesimil",
        "engine": "lucene",
        "parameters": {
          "ef_construction": 128,
          "m": 16
        }
      }
    }
  }
}
```

**Note**
The exact `space_type`, `engine`, and parameter values depend on the source definition and the target version. Newer Amazon OpenSearch Service and Amazon OpenSearch Serverless NextGen targets receive additional vector compatibility transformations: legacy `index.knn.*` build settings are moved into field-level method configuration, `nmslib` engines are converted to `faiss` for OpenSearch 3.x targets, and Serverless targets receive Faiss HNSW mappings. Always confirm the final mapping on the target after metadata migration (see [Post-migration validation](tdvk-validation.md)).
