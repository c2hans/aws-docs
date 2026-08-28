---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-cross-region.html
---

# Cross-region replication
<a name="msk-replicator-cross-region"></a>

In cross-region replication (CRR), the source and target MSK clusters are in different AWS Regions. Cross-region replication is the foundation for building multi-region resilient streaming applications.

Key requirements for cross-region replication:
+ The source cluster must have multi-VPC private connectivity turned on for IAM access control. See [Cluster owner turns on multi-VPC](mvpc-cluster-owner-action-turn-on.md).
+ You must attach a resource-based permissions policy to the source cluster. See [Prepare the source cluster](msk-replicator-prepare-clusters.md#msk-replicator-prepare-source).
+ You do not need to provide security groups for the source cluster.
+ The Replicator is created in the target cluster's AWS Region.

Replication latency varies based on the network distance between the AWS Regions, the throughput capacity of your clusters, and the number of partitions. For example, replication latency is typically lower between Europe (Ireland) and Europe (London) compared to Europe (Ireland) and Asia Pacific (Sydney).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
