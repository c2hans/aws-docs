---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-solr-scope.html
---

# Scope and architecture
<a name="pb-solr-scope"></a>

The migration moves your Apache Solr collections or cores into indexes on the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection by way of Reindex-from-Snapshot (RFS). Unlike an Elasticsearch or OpenSearch source — where RFS reads a native cluster snapshot — an Apache Solr source is migrated from a Solr **backup** in [Amazon Simple Storage Service](https://aws.amazon.com/s3) (Amazon S3). Migration Assistant then reads that backup, translates the Solr `schema.xml` into OpenSearch index mappings during metadata migration, and bulk-indexes the documents into the target.

The flow for this path is:

```
Pause source writes → Back up Solr to a shared path → Sync backup to Amazon S3 →
Configure workflow → Submit + monitor → Verify counts and queries → Cut over
```

What this playbook covers and does not cover:
+  **Covered** — Document backfill into the target, and metadata migration that translates the Solr `schema.xml` into OpenSearch index settings and mappings.
+  **Not covered** — The optional live Capture and Replay setup for SolrCloud sources. Configure it from the Solr migration chapter after you understand the backfill path. Also plan separate work for security configuration, ingest pipelines, OpenSearch Dashboards saved objects, and any Solr-specific query or relevance tuning, because these are not migrated automatically.

Migration Assistant supports Apache Solr 6.x–9.x as a source. This playbook uses Solr 8.x and 9.x as representative examples; the same steps apply to Solr 6.x and 7.x with the corresponding `SOLR <major>.<minor>.<patch>` version string. For the full supported range and schema translation details, see [Migrate from Apache Solr](migrate-from-solr.md).

**Note**
This playbook targets an Amazon OpenSearch Service domain by default. To target an Amazon OpenSearch Serverless NextGen collection instead, change only the target configuration in [Step 2](pb-solr-step2.md) — set `service: aoss` in the SigV4 `authConfig` and add the migration IAM role to the collection’s data access policy. The backup and backfill steps are identical.
