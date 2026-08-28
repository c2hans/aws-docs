---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/increase-decrease-replica-count.html
---

# Changing the number of replicas
<a name="increase-decrease-replica-count"></a>

You can dynamically increase or decrease the number of read replicas in your Valkey or Redis OSS replication group using the AWS Management Console, the AWS CLI, or the ElastiCache API. If your replication group is a Valkey or Redis OSS (cluster mode enabled) replication group, you can choose which shards (node groups) to increase or decrease the number of replicas.

To dynamically change the number of replicas in your replication group, choose the operation from the following table that fits your situation.

| To Do This | For Valkey or Redis OSS (cluster mode enabled) | For Valkey or Redis OSS (cluster mode disabled) |
| --- | --- | --- |
| Add replicas | [Increasing the number of replicas in a shard](increase-replica-count.md) | [Increasing the number of replicas in a shard](increase-replica-count.md)<br />[Adding a read replica for Valkey or Redis OSS (Cluster Mode Disabled)](Replication.AddReadReplica.md) |
| Delete replicas | [Decreasing the number of replicas in a shard](decrease-replica-count.md) | [Decreasing the number of replicas in a shard](decrease-replica-count.md)<br />[Deleting a read replica for Valkey or Redis OSS (Cluster Mode Disabled)](Replication.RemoveReadReplica.md) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
