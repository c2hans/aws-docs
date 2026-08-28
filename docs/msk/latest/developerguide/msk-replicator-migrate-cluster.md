---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-migrate-cluster.html
---

# Migrate between Amazon MSK clusters
<a name="msk-replicator-migrate-cluster"></a>

Amazon MSK Replicator supports migrations between Amazon MSK clusters in the same AWS account. You can use Identical topic name replication for cluster migration, but your consumers must be able to handle duplicate messages without downstream impact. This is because MSK Replicator provides at-least-once replication, which can lead to duplicate messages in rare scenarios. If your consumers meet this requirement, follow these steps.

1. Create a Replicator that replicates data from your old cluster to the new cluster with Replicator's starting position set to *Earliest* and using Identical topic name replication (**Keep the same topics name** in console).

1. Configure cluster-level settings and permissions on the new cluster. You do not need to configure topic-level settings and "literal" read ACLs, as MSK Replicator automatically copies them.

1. Monitor the `MessageLag` metric in Amazon CloudWatch until it reaches 0, which indicates all data has been replicated.

1. After all data has been replicated, stop producers from writing data to the old cluster.

1. Reconfigure those producers to connect to the new cluster and start them.

1. Monitor `MaxOffsetLag` metric for your consumers reading data from the old cluster until it becomes `0`, which indicates all existing data has been processed.

1. Stop consumers that are connecting to the old cluster.

1. Reconfigure consumers to connect to the new cluster and start them.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
