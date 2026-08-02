---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/ttm-when-it-applies.html
---

# When type-mapping transformation applies
<a name="ttm-when-it-applies"></a>

Type-mapping transformation applies only when your source cluster predates the removal of multiple mapping types:
+  **Elasticsearch 6.x and earlier** — Indexes can contain multiple types, so transformation is relevant. Elasticsearch 5.x and earlier commonly use multiple types per index; Elasticsearch 6.x permits at most one type per index but still carries the type layer.
+  **Elasticsearch 7.0 and later, and all OpenSearch versions** — Indexes already use a single implicit type (`_doc`), so no type-mapping transformation is needed.

If your source is Elasticsearch 7.0 or later, you can skip this page. If your source is Elasticsearch 6.x or earlier and any index defines more than one type, you must choose how those types are reshaped before the index is created on the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. Migration Assistant applies the same decision consistently across metadata migration and document backfill, so the documents land in the indexes that the transformed mappings describe.

**Note**
Elasticsearch 1.x and 2.x sources are backfill-only in Migration Assistant — live capture and replay are not supported for those versions. Type-mapping transformation still applies to the metadata migration and backfill phases for these older sources.
