---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/tft-built-in.html
---

# Built-in field type transformations
<a name="tft-built-in"></a>

Migration Assistant applies the following field-type and vector-compatibility transformations automatically during metadata migration. You do not need to configure or invoke them — they run as part of the Metadata Migration phase whenever the source and target engine versions require them:
+  ** `string` to `text` and `keyword` ** — Converts the deprecated `string` type (Elasticsearch 1.x–5.x) to `text` or `keyword` based on the original `index` property. See [Transform string fields to text and keyword](transform-string-text-keyword.md).
+  ** `flattened` to `flat_object` ** — Converts the `flattened` field type (Elasticsearch 7.3 and later) to `flat_object` (OpenSearch 2.7 and later). See [Transform flattened fields to flat\_object](transform-flattened-flat-object.md).
+  ** `dense_vector` to `knn_vector` ** — Converts `dense_vector` (Elasticsearch 7.x) to `knn_vector` with appropriate similarity mappings and HNSW algorithm parameters, including additional vector compatibility adjustments for newer Amazon OpenSearch Service and Amazon OpenSearch Serverless NextGen targets. See [Transform dense\_vector fields to knn\_vector](transform-dense-vector-knn.md).
+  ** `knn_vector` compatibility** — Lifts legacy `index.knn.*` build parameters into field-level method configuration, converts `nmslib` engines to `faiss` for OpenSearch 3.x targets, and rewrites incompatible `knn_vector` definitions to Faiss HNSW for Amazon OpenSearch Serverless NextGen.

**Note**
The built-in transformations cover the common version-upgrade cases. Metadata migration also applies analysis-component compatibility rules for analyzer, tokenizer, char-filter, and token-filter names that changed between source and target versions. If your source contains field types or analysis components that none of these transformations address — for example a custom or third-party field type, or a type whose mapping you need to reshape in a way the defaults do not — supply a custom transformer as described in the next section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
