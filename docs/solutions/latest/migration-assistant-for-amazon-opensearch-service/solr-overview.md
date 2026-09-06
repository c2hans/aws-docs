---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/solr-overview.html
---

# Overview
<a name="solr-overview"></a>

The solution migrates [Apache Solr](https://solr.apache.org/) 6.x through 9.x sources, running in either SolrCloud or standalone mode, to OpenSearch 3.x on the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. Apache Solr sources are supported for OpenSearch 3.x targets only; OpenSearch 1.x and 2.x targets are not supported for Solr migrations.

Keep the following constraints in mind when you plan a Solr migration:
+  **SolrCloud required for capture and replay.** Live traffic capture and replay requires your source cluster to be running in SolrCloud mode. Standalone Solr is supported for backfill only.
+  **JSON-format writes only.** The traffic transform layer supports JSON-format write requests only. XML-format update requests (`text/xml`) are not transformed and will not be replayed to the target.
+  **Version string format.** In your workflow configuration, the Solr source version must be written as `SOLR <major>.<minor>.<patch>` — for example, `SOLR 8.11.4`. The solution uses this value to select the correct reader behavior.
+  **Backup-based backfill.** Unlike Elasticsearch and OpenSearch sources, a Solr source is migrated from a Solr backup in [Amazon Simple Storage Service](https://aws.amazon.com/s3) (Amazon S3). Migration Assistant can create that backup during the workflow by calling Solr’s backup APIs, or you can create and stage the backup yourself and reference it as an externally managed snapshot.
