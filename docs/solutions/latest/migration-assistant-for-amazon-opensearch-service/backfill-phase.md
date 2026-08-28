---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/backfill-phase.html
---

# Backfill
<a name="backfill-phase"></a>

Backfill moves the documents that already exist on the source cluster into the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. Migration Assistant takes a point-in-time snapshot of the source in [Amazon Simple Storage Service](https://aws.amazon.com/s3) (Amazon S3) — the only time the source is touched — and then uses Reindex-from-Snapshot (RFS) to read Lucene segment files directly from the snapshot and bulk-index them into the target.

Run metadata migration before backfill so that index settings, mappings, templates, and aliases are already in place on the target. See [Migrate metadata](migrate-metadata.md). The snapshot used for metadata migration is fully compatible with the RFS backfill phase, so the snapshot you create in this chapter is the same one RFS reads from.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
