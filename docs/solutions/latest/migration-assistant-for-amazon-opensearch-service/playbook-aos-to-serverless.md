---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/playbook-aos-to-serverless.html
---

# Playbook: Amazon OpenSearch Service to Amazon OpenSearch Serverless NextGen
<a name="playbook-aos-to-serverless"></a>

This playbook is an end-to-end runbook for migrating an existing [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service) domain to an [Amazon OpenSearch Serverless NextGen](https://aws.amazon.com/opensearch-service/features/serverless) collection, using a vector-search workload as the worked example. For a small domain — a handful of vector indexes totaling a few tens of gigabytes — plan for roughly 90 minutes end to end, most of which is unattended snapshot and backfill time.

This is a backfill-style migration: Reindex-from-Snapshot (RFS) takes a point-in-time snapshot of the source domain, migrates metadata, and bulk-indexes documents into the collection. Amazon OpenSearch Serverless NextGen does not accept snapshot restores, ISM/ILM policies, ingest pipelines, custom plugins, or `_cluster/settings` changes, so the runbook below builds the collection’s shape with security policies and metadata migration rather than a restore. For the broader conceptual comparison, see [Migrate to Amazon OpenSearch Serverless NextGen](migrate-to-serverless.md).

For an at-a-glance summary of how Amazon OpenSearch Serverless NextGen constrains a migration, read the [How Serverless differs](pb-aoss-how-serverless-differs.md) callout before you begin.

**Note**
Amazon OpenSearch Serverless NextGen authenticates every request with AWS Signature Version 4 (SigV4) — there is no basic-auth or fine-grained access control (FGAC) username and password on the target. Both the snapshot source access and the migration’s write access to the collection are governed by [AWS Identity and Access Management](https://aws.amazon.com/iam) (IAM) and by the collection’s data access policy.
