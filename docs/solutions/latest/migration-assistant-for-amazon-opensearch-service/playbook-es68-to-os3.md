---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/playbook-es68-to-os3.html
---

# Playbook: Elasticsearch 6.8 to OpenSearch 3.x on Amazon OpenSearch Service
<a name="playbook-es68-to-os3"></a>

This playbook is an end-to-end runbook for migrating a self-managed Elasticsearch 6.8 cluster to an Amazon OpenSearch Service domain running OpenSearch 3.x, using the Migration Assistant for Amazon OpenSearch Service solution deployed on [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks) (Amazon EKS) inside an **existing** virtual private cloud (VPC). It walks through prerequisites, source preparation, deployment into your VPC, a small pilot, the full backfill, cutover, and an optional zero-downtime capture-and-replay phase.

Migration Assistant takes a one-time snapshot of the source cluster, migrates index metadata, and uses Reindex-from-Snapshot (RFS) to bulk-index documents into the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. Because Elasticsearch 6.x indexes can contain multiple mapping types and OpenSearch does not, multi-type (pre-7.0) mappings are resolved automatically by the built-in type-mapping sanitization transformer, which merges the multiple types into a single index (union) by default. You do not configure this behavior with a field in the workflow configuration; if you need a different post-union rename, merge, or drop pattern, see [Transform type mappings](transform-type-mappings.md).

**Note**
Run the pilot on a small index allowlist first, validate it, and only then widen the scope to the full migration. This is the fastest way to catch mapping, authentication, and throughput problems before they affect your whole dataset.

**Important**
Auto-generated document IDs are not preserved during replay. If your source application relies on Elasticsearch assigning `_id` values automatically, plan to validate document identity on the target before cutover. Backfill from a snapshot preserves the document IDs that exist in the snapshot.
