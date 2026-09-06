---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/transform-type-mappings.html
---

# Transform type mappings
<a name="transform-type-mappings"></a>

In Elasticsearch versions before 7.0, a single index could contain multiple mapping types — for example, a `user` type and a `post` type in the same index. OpenSearch and Elasticsearch 7.0 and later support only a single type per index, so the multiple-type structure was deprecated and removed. When you migrate from a source that uses multiple types, Migration Assistant must decide how to reshape each multi-type index before it can be created on the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection.

Migration Assistant resolves this with a built-in transformer that runs during metadata migration and document backfill. By default, the transformer unions legacy mapping types into the source index name. When you need to rename, merge, or drop routed data after the type layer is removed, configure the `TypeMappingSanitizationTransformerProvider` with exact `staticMappings` or pattern-based `regexMappings` across the affected phases. This page describes when type-mapping transformation applies, how to configure it, and how to validate the result.

This work is part of the metadata phase. See [Migrate metadata](migrate-metadata.md) for the surrounding phase that creates index settings, mappings, templates, and aliases on the target.
