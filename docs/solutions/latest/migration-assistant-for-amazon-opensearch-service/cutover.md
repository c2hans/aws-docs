---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/cutover.html
---

# Cutover and rollback
<a name="cutover"></a>

Switching traffic to the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection is the cutover step. By this point, backfill and validation are complete. For capture-and-replay and zero-downtime migrations, capture has also protected writes during backfill and replay has caught the target up.

Before you switch:
+ for capture-and-replay and zero-downtime migrations, replay has reached the live edge,
+ the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection is healthy,
+ representative application queries work on the target,
+ the application team is ready to move traffic, and
+ the rollback path is still available.

The exact cutover mechanism depends on your environment, but the principle is always the same:

1. Stop pointing clients at the source. For capture-and-replay and zero-downtime migrations, this means stopping traffic to the capture proxy.

1. Point clients directly at the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection.

1. Watch the target closely during the first production traffic window.

In practice, that usually means updating a DNS record, a load balancer backend, an application connection string, or a service-discovery entry. Keep the source cluster available during a rollback window (typically 24–72 hours) before decommissioning. After the rollback window has passed, see [Uninstall the solution](uninstall-the-solution.md) to remove the Migration Assistant infrastructure.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
