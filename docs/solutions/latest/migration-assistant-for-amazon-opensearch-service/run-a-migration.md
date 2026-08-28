---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/run-a-migration.html
---

# Run a migration
<a name="run-a-migration"></a>

Use this section after you deploy Migration Assistant and want to configure, submit, monitor, or troubleshoot workflows manually. If you want guided assessment, deployment, workflow generation, migration execution, and troubleshooting, start with [AI-assisted migration](agent-assisted-migration.md).

Start with [Configure and run workflows](use-the-solution.md) for the manual Workflow CLI path: load a schema, configure source and target, run a pilot, and execute the full migration.

The remaining pages cover complete runbooks, migration phases, target-specific paths, compatibility transforms, monitoring, troubleshooting, and cleanup:
+  [Playbooks](playbooks.md) - end-to-end runbooks for common source-to-target migration paths.
+  [Migrate metadata](migrate-metadata.md) - migrate index settings, mappings, templates, and aliases to the target.
+  [Backfill](backfill-phase.md) - move historical documents from a source snapshot to the target using Reindex-from-Snapshot.
+  [Reroute client traffic to the capture proxy](reroute-to-proxy.md) - redirect live traffic through the capture proxy before starting replay.
+  [Replay captured traffic](replay-phase.md) - replay captured live traffic to synchronize the target before cutover.
+  [Switch traffic to the target](switch-traffic.md) - cut over clients to the new target cluster.
+  [Migrate to Amazon OpenSearch Serverless NextGen](migrate-to-serverless.md) - target-specific guidance for Serverless NextGen collections.
+  [Migrate from Apache Solr](migrate-from-solr.md) - source-specific guidance for Solr 6.x-9.x migrations.
+  [Transform data and requests](data-transforms.md) - compatibility transforms for metadata, mappings, fields, vectors, live traffic, and Solr requests.
+  [Monitor the solution with Service Catalog AppRegistry](monitoring-the-solution-with-aws-service-catalog-appregistry.md) - monitor deployed resources with Application Manager and CloudWatch Application Insights.
+  [Troubleshooting](troubleshooting.md) - diagnose platform health, connectivity, authentication, workflow, snapshot, metadata, and backfill issues.
+  [Uninstall the solution](uninstall-the-solution.md) - remove Migration Assistant after cutover and the rollback window.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
