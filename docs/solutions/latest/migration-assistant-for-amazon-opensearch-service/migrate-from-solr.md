---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/migrate-from-solr.html
---

# Migrate from Apache Solr
<a name="migrate-from-solr"></a>

This page describes how to migrate an Apache Solr source to the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection using the Migration Assistant for Amazon OpenSearch Service solution. The solution supports two migration modes for Apache Solr sources:
+  **Backfill** — Migrates your existing documents and schema field types from a Solr backup into the target.
+  **Capture and replay** — Intercepts live traffic flowing to your Solr cluster, transforms Solr requests into OpenSearch-compatible API calls, and replays them against the target in real time for zero-downtime migration.

Before you begin, deploy the solution and confirm connectivity. See [Deploy the solution](deploy-the-solution.md) and [Getting started with the Workflow CLI](use-the-solution.md#getting-started). For an end-to-end, copy-paste walkthrough of a Solr migration, see the [Apache Solr to OpenSearch 3.x playbook](playbook-solr-to-os3.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
