---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Durability.FailureScenarios.html
---

# Failure scenarios
<a name="Durability.FailureScenarios"></a>

If a primary node fails, ElastiCache automatically triggers a failover to a replica, and the new primary takes over write operations. The failed primary is replaced and syncs data from the Multi-AZ transactional log. With synchronous writes, this process ensures no data loss. With asynchronous writes, up to 10 seconds of uncommitted data can be lost during the failover. If a read replica fails, the failed node is replaced and syncs data from the Multi-AZ transactional log regardless of the durability option selected.

When all nodes in a shard fail, all nodes are replaced and sync data from the Multi-AZ transactional log at the same time. With synchronous writes, this process ensures no data loss. With asynchronous writes, up to 10 seconds of uncommitted data can be lost. After committed data is restored, one of the replaced nodes will automatically be elected as the new primary with other nodes as replicas.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
