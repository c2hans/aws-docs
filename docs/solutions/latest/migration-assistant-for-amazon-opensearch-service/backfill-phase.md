---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/backfill-phase.html
---

# Backfill
<a name="backfill-phase"></a>

Backfill moves the documents that already exist on the source cluster into the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. Migration Assistant takes a point-in-time snapshot of the source in [Amazon Simple Storage Service](https://aws.amazon.com/s3) (Amazon S3) — the only time the source is touched — and then uses Reindex-from-Snapshot (RFS) to read Lucene segment files directly from the snapshot and bulk-index them into the target.

Run metadata migration before backfill so that index settings, mappings, templates, and aliases are already in place on the target. See [Migrate metadata](migrate-metadata.md). The snapshot used for metadata migration is fully compatible with the RFS backfill phase, so the snapshot you create in this chapter is the same one RFS reads from.
