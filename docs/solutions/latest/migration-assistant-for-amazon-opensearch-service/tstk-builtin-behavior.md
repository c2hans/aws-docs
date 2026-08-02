---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/tstk-builtin-behavior.html
---

# Built-in transformation behavior
<a name="tstk-builtin-behavior"></a>

Migration Assistant chooses the target type from the original `index` property on each `string` field:

| Source `string` field | Migrated type | Why |
| --- | --- | --- |
|  `index: analyzed` (the default in Elasticsearch 1.x–5.x) |  `text`  | Analyzed string fields were tokenized for full-text search, which maps directly to the `text` type. |
|  `index: not_analyzed`  |  `keyword`  | Not-analyzed string fields were stored as a single exact token for filtering, sorting, and aggregations, which maps directly to the `keyword` type. |
|  `index: no`  |  `keyword` (not indexed) | The field is converted to `keyword` and retained in the mapping, but it remains non-searchable, preserving the original intent. |

Because analyzed strings were the default in those source versions, most `string` fields become `text` on the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. Fields that your application relied on for exact matching, sorting, or aggregations — and that were explicitly marked `not_analyzed` — become `keyword`.

**Note**
This conversion is one of several automatic field-type transformations Migration Assistant performs during metadata migration, alongside `flattened` to `flat_object` and `dense_vector` to `knn_vector`. You do not enable it separately; it is part of the standard metadata phase.
