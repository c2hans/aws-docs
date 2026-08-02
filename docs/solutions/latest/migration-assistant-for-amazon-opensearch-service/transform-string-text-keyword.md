---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/transform-string-text-keyword.html
---

# Transform string fields to text and keyword
<a name="transform-string-text-keyword"></a>

Early versions of Elasticsearch (1.x through 5.x) used a single `string` field type for all text. Beginning with Elasticsearch 5.0, that type was split into two distinct types — `text` for full-text, analyzed search and `keyword` for exact-value matching, sorting, and aggregations — and the `string` type was removed entirely in later versions. Because Amazon OpenSearch Service and Amazon OpenSearch Serverless NextGen do not accept the deprecated `string` type, Migration Assistant applies a built-in metadata transformation that rewrites every `string` field to either `text` or `keyword` before the mapping is created on the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection.

This transformation runs automatically as part of metadata migration. You do not need to configure it. This page explains how the conversion decides between `text` and `keyword`, how to inspect your source mappings beforehand, and how to validate query behavior on the target afterward. For the surrounding metadata phase, see [Migrate metadata](migrate-metadata.md).
