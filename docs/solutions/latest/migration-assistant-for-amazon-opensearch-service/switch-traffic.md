---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/switch-traffic.html
---

# Switch traffic to the target
<a name="switch-traffic"></a>

Switching traffic is the cutover step that completes every migration scenario. This phase moves clients off the source and onto the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection while keeping a rollback path available.

For backfill-only migrations (Scenario 1), there is no capture proxy and no replay. Cut over after backfill and validation complete, repointing clients directly from the source to the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. The capture-proxy and replay preconditions described in this chapter apply only to capture-and-replay (Scenario 2) and zero-downtime (Scenario 3) migrations. See [Migration scenarios](use-the-solution.md#migration-scenarios).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
