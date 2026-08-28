---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference-replicator/operations.html
---

# Operations
<a name="operations"></a>

The Amazon Managed Streaming for Apache Kafka REST API includes the following operations.
+ [CreateReplicator](v1-replicators.md#CreateReplicator)

  Creates the replicator.

  Note: Enhanced consumer offset syncing is only supported when the `topicNameConfiguration` type is `IDENTICAL`.
+ [DeleteReplicator](v1-replicators-replicatorarn.md#DeleteReplicator)

  Deletes a replicator.
+ [DescribeReplicator](v1-replicators-replicatorarn.md#DescribeReplicator)

  Describes a replicator.
+ [ListReplicators](v1-replicators.md#ListReplicators)

  Lists the replicators.
+ [UpdateReplicationInfo](v1-replicators-replicatorarn-replication-info.md#UpdateReplicationInfo)

  Updates replication info of a replicator.

  Note: `logDelivery` cannot be updated in the same request as `topicReplication` or `consumerGroupReplication`. Update either `logDelivery` or `topicReplication` and `consumerGroupReplication` in separate requests.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
