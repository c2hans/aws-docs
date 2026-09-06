---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/migrate-from-solr.html
---

# Migrate from Apache Solr
<a name="migrate-from-solr"></a>

This page describes how to migrate an Apache Solr source to the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection using the Migration Assistant for Amazon OpenSearch Service solution. The solution supports two migration modes for Apache Solr sources:
+  **Backfill** — Migrates your existing documents and schema field types from a Solr backup into the target.
+  **Capture and replay** — Intercepts live traffic flowing to your Solr cluster, transforms Solr requests into OpenSearch-compatible API calls, and replays them against the target in real time for zero-downtime migration.

Before you begin, deploy the solution and confirm connectivity. See [Deploy the solution](deploy-the-solution.md) and [Getting started with the Workflow CLI](use-the-solution.md#getting-started). For an end-to-end, copy-paste walkthrough of a Solr migration, see the [Apache Solr to OpenSearch 3.x playbook](playbook-solr-to-os3.md).
