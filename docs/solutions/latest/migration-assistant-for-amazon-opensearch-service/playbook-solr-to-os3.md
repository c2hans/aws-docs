---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/playbook-solr-to-os3.html
---

# Playbook: Apache Solr 8.x or 9.x to OpenSearch 3.x
<a name="playbook-solr-to-os3"></a>

This playbook is an end-to-end runbook for migrating an Apache Solr 8.x or 9.x deployment — either standalone (single-core) Solr or SolrCloud — into OpenSearch 3.x running on an [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service) domain or an [Amazon OpenSearch Serverless NextGen](https://aws.amazon.com/opensearch-service/features/serverless) collection. It strings the individual migration phases described in [Configure and run workflows](use-the-solution.md) into one ordered sequence tailored to an Apache Solr source. For the general concepts behind a Solr migration, see [Migrate from Apache Solr](migrate-from-solr.md).

**Important**
This playbook’s main procedure is backup-based backfill. If you need zero-downtime migration for a SolrCloud source, add Capture and Replay so writes that arrive after the backup are captured and replayed to the target. Solr replay requires JSON-format write requests and Solr-specific transform provider configuration. Standalone Solr sources remain backfill-only.

This playbook assumes Migration Assistant is already deployed on [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks) (Amazon EKS). If you have not deployed it yet, complete [Deploy the solution](deploy-the-solution.md) first. It also assumes you have confirmed the installed version with `console --version` and loaded the version-matched sample with `workflow configure sample --load` on the Migration Console pod (`migration-console-0`).
