---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-solr-schema.html
---

# Schema translation reference
<a name="pb-solr-schema"></a>

During metadata migration, Migration Assistant translates the Apache Solr `schema.xml` field types into OpenSearch field types. This playbook summarizes the behavior; the full reference is in [Migrate from Apache Solr](migrate-from-solr.md).

Use [Schema translation](solr-schema-translation.md) as the source of truth for the built-in mapping list. The converter covers common Solr type names such as `string`, `text_general`, `pint`, `plong`, `pdate`, and their multi-valued aliases, and it falls back to Java field type classes such as `solr.StrField`, `solr.TextField`, `solr.IntPointField`, legacy `solr.Trie*Field` classes, `solr.UUIDField`, and `solr.BinaryField` when a schema defines custom type names. It also converts dynamic field patterns into OpenSearch dynamic templates and adds `copyField` destinations when the destination is not already an explicit field.

The evaluated metadata also includes index settings. Migration Assistant sets `index.number_of_shards` from the shard count discovered in the Solr backup and defaults `index.number_of_replicas` to `1`.

For field types or index settings that are not covered by the default translation, or to override a translation, supply a custom metadata transformer through `metadataTransforms` in your workflow configuration. Review the evaluated metadata before approving the `migrateMetadata` step, especially if your Solr schema uses custom field type classes, dotted dynamic field names, broad `copyField` rules, or a target replica count other than `1`. See [Transform field types](transform-field-types.md) for the JavaScript transformer pattern and raw descriptor alternatives.
