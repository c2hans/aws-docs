---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/solr-migrated-components.html
---

# Migrated components
<a name="solr-migrated-components"></a>

The following table summarizes what the solution migrates from an Apache Solr source and what you must handle separately.

| Component | Status | Notes |
| --- | --- | --- |
| Documents | Migrated | Reconstructed from Lucene stored fields in your Solr backup and bulk-indexed into the target. See [Document reconstruction](solr-document-reconstruction.md). |
| Schema field types | Migrated | Translated from `schema.xml` to OpenSearch mappings for the supported field types listed in [Schema translation](solr-schema-translation.md). |
| Solr plugins | Not migrated | Custom request handlers, search components, and similar plugins have no OpenSearch equivalent and must be re-implemented. |
| ZooKeeper configuration | Not migrated | SolrCloud cluster state and configuration held in ZooKeeper are not carried over. |
| Query traffic | Migrated (capture and replay) | Live traffic capture and replay transforms Solr requests (writes and searches) into OpenSearch-compatible API calls. See [Capture and replay live traffic from Solr](solr-capture-replay.md). |
