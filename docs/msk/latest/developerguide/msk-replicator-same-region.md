---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-same-region.html
---

# Same-region replication
<a name="msk-replicator-same-region"></a>

In same-region replication (SRR), both the source and target MSK clusters are in the same AWS Region. Same-region replication is useful for data aggregation, distributing data to partners, or migrating between clusters.

Key differences from cross-region replication:
+ The source cluster does not require multi-VPC private connectivity.
+ You do not need to attach a resource-based permissions policy to the source cluster.
+ You must provide security groups for both the source and target clusters. The subnets you select for the source and target clusters must be in the same Availability Zones.
+ The source cluster can still be accessed by other clients using the unauthenticated auth type.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
