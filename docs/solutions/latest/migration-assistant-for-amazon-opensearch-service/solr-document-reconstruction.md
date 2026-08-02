---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/solr-document-reconstruction.html
---

# Document reconstruction
<a name="solr-document-reconstruction"></a>

Solr does not store a complete `_source` JSON document the way Elasticsearch and OpenSearch can. During Solr backfill, the SolrReader reconstructs each target `_source` document from Lucene stored fields in the backup.

Keep the following reconstruction behavior in mind when you plan the backup:
+ Fields with `stored=true` are the reliable source for migrated document values. The Solr flat reconstruction path does not recover `stored=false` values from `docValues`, points, indexed terms, or `copyField` destinations; `docValues=true` helps the translated mapping and target query behavior, but it does not by itself make the value available in migrated `_source`.
+ Schema translation can still create a target mapping for a `stored=false` field, but document backfill cannot index a value that is not reconstructable from the backup.
+ If the same field has multiple stored values, such as a stored Solr `multiValued` field, the values are emitted as a JSON array. A field with one stored value is emitted as a scalar.
+ Solr field names that contain dots are treated as literal field names. For example, `address.city` is migrated as the flat `_source` key `"address.city"`, not as `{"address":{"city":…​}}`.
+ Internal Lucene fields whose names start with `_` are not emitted into `_source`. The Solr `id` field is preserved in `_source` and is used as the OpenSearch document ID when it is stored. If multiple stored `id` values exist, the first stored `id` value is used as the document ID.
+ If the stored `id` field is missing, SolrReader assigns a synthetic document ID in the form `solr_doc_<absoluteLuceneDocNumber>`.
+ If a live Lucene document has no reconstructable non-internal stored fields, the document is skipped.

Before taking the production backup, review important Solr fields and make sure values that must exist in the target are stored or can be reloaded another way. After backfill, spot-check representative target documents, especially fields that were `stored=false`, fields that relied on `docValues`, multi-valued fields, `copyField` destinations, and field names that contain dots.
