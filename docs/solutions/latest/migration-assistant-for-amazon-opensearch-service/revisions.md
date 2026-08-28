---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/revisions.html
---

# Revisions
<a name="revisions"></a>

The following table describes the important changes to the documentation since the last release of Migration Assistant for Amazon OpenSearch Service. For notification about updates to this documentation, you can subscribe to an RSS feed.

| Change | Description | Date |
| --- | --- | --- |
| Apache Solr migration support | You can now migrate from Apache Solr 6, 7, 8, and 9 to Amazon OpenSearch Service or Amazon OpenSearch Serverless NextGen. This expands beyond Elasticsearch migration support. Coverage includes bulk data backfill from Solr snapshots, including multi-shard collections, and SolrCloud capture and replay for supported JSON-format traffic through the Solr transform providers. | May 15, 2026 |
| 9× memory reduction for large migrations | Reindex-from-Snapshot (RFS) now streams index data to disk instead of holding it in RAM. Migrations of indexes with 100 GB\+ shards now complete reliably without requiring oversized infrastructure. | May 15, 2026 |
| Zero-downtime change data capture (CDC) pipelines on Amazon EKS | Continuous data sync from source to target runs on a configurable schedule (down to 6-hour cycles). This feature supports Elasticsearch 5.x through 8.x with TLS, and Amazon OpenSearch Serverless NextGen. You can keep source and target in sync during the migration window. You can validate the target on production traffic and cut over with confidence. | May 15, 2026 |
| Kubernetes-native workflow orchestration | Migrations run as managed Argo Workflows on Amazon EKS with automatic retries on transient failures, `workflow reset` and `workflow show` commands, pre-flight validation, TLS by default, and resilient three-broker Apache Kafka. You can recover from transient failures without manual intervention. | May 15, 2026 |
| Secure-by-default networking | The capture proxy defaults to TLS using cert-manager-issued self-signed certificates. Frontend mTLS (client-certificate) authentication is supported. Plaintext proxy traffic is no longer the default; opt out per proxy with `tls.mode: plaintext` only when you intentionally want HTTP. TLS no longer requires opt-in configuration. | May 15, 2026 |
| Source reconstruction for indexes with `_source` disabled | If your source cluster stored indexes without the `_source` field, Migration Assistant now reconstructs the source documents during migration. This unblocks you if you relied on the `_source` disabled optimization in Elasticsearch. | May 15, 2026 |
| Migration Assistant 3.0 documentation refresh | Aligned implementation guide with the latest Migration Assistant 3.0 documentation. Source matrix updated to include Elasticsearch 1.x–2.x (backfill-only), Apache Solr 6.x–9.x, and Amazon OpenSearch Serverless NextGen targets. Added self-contained Amazon EKS deployment instructions, Workflow CLI guide, and expanded troubleshooting coverage. Consolidated external references into implementation guide.Architecture refreshed with control-plane and data-plane framing. | May 15, 2026 |
| Migration Assistant 3.0 | Amazon EKS deployment is now the recommended deployment option. ECS deployment reached end of support July 15, 2026. Added Apache Solr 8.x as a supported source. Added Workflow CLI for declarative migration configuration, built-in approval gates, and interactive monitoring TUI. | April 2026 |

Visit the [Migration Assistant documentation](https://docs.aws.amazon.com/solutions/migration-assistant-for-amazon-opensearch-service/) to track version-specific improvements and fixes.

Original publication date: *November 2023*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
