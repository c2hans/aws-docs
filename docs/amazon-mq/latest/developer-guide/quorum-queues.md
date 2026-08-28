---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/quorum-queues.html
---

# Quorum queues for RabbitMQ on Amazon MQ
<a name="quorum-queues"></a>

 Quorum queues are a replicated queue type made up of a leader (primary replica) and followers (other replicas). If the leader becomes unavailable, quorum queues uses the [Raft](https://raft.github.io/) consensus algorithm to elect a new leader node by majority of votes, and the previous leader is demoted to a follower node in the same cluster. The remaining followers continue replicating as before. Because each node is in a different availability zone, if one node is temporarily unavailable, message delivery continues with the newly elected leader replica in another availability zone.

 Quorum queues are useful for handling poison messages, which occur when a message fails and is requeued multiple times.

You should not use quorum queues if you:
+  use transient queues
+  have long queue backlogs
+  prioritize low latency

 To declare a quorum queue, set the header `x-queue-type` to `quorum`.

**Topics**
+ [Migrating from classic queues to quorum queues on Amazon MQ for RabbitMQ](quorum-queues-migration.md)
+ [Policy configurations for quorum queues for Amazon MQ for RabbitMQ](quorum-queues-policy-configurations.md)
+ [Best practices for quorum queues for Amazon MQ for RabbitMQ](quorum-queues-best-practices.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MQ. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazon-mq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
