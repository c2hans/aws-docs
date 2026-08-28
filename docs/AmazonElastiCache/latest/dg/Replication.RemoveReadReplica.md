---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Replication.RemoveReadReplica.html
---

# Deleting a read replica for Valkey or Redis OSS (Cluster Mode Disabled)
<a name="Replication.RemoveReadReplica"></a>

Information in the following topic applies to Valkey or Redis OSS (cluster mode disabled) replication groups only.

As read traffic on your Valkey or Redis OSS replication group changes, you might want to add or remove read replicas. Removing a node from a replication group is the same as just deleting a cluster, though there are restrictions:
+ You cannot remove the primary from a replication group. If you want to delete the primary, do the following:

  1. Promote a read replica to primary. For more information on promoting a read replica to primary, see [Promoting a read replica to primary, for Valkey or Redis OSS (cluster mode disabled) replication groups](Replication.PromoteReplica.md).

  1. Delete the old primary. For a restriction on this method, see the next point.
+ If Multi-AZ is enabled on a replication group, you can't remove the last read replica from the replication group. In this case, do the following:

  1. Modify the replication group by disabling Multi-AZ. For more information, see [Modifying a replication group](Replication.Modify.md).

  1. Delete the read replica.

You can remove a read replica from a Valkey or Redis OSS (cluster mode disabled) replication group using the ElastiCache console, the AWS CLI for ElastiCache, or the ElastiCache API.

For directions on deleting a cluster from a Valkey or Redis OSS replication group, see the following:
+ [Using the AWS Management Console](Clusters.Delete.md#Clusters.Delete.CON)
+ [Using the AWS CLI to delete an ElastiCache cluster](Clusters.Delete.md#Clusters.Delete.CLI)
+ [Using the ElastiCache API](Clusters.Delete.md#Clusters.Delete.API)
+ [Scaling Valkey or Redis OSS (Cluster Mode Enabled) clusters](scaling-redis-cluster-mode-enabled.md)
+ [Decreasing the number of replicas in a shard](decrease-replica-count.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
