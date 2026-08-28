---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-migration.html
---

# Migration
<a name="msk-replicator-migration"></a>

MSK Replicator supports several migration scenarios. This section describes how to migrate data between clusters, from self-managed Kafka environments to Amazon MSK, and how to transition from other replication tools.

**Topics**
+ [Migrate between Amazon MSK clusters](msk-replicator-migrate-cluster.md)
+ [Migrate from non-MSK Apache Kafka clusters to Amazon MSK Provisioned](msk-replicator-migrate-external.md)
+ [Migrate from MirrorMaker 2 to Amazon MSK Replicator](msk-replicator-migrate-mm2.md)
+ [Assess migration readiness with AI tools](msk-replicator-migrate-ai-assist.md)
+ [Cross-account migration between Amazon MSK clusters](msk-replicator-cross-account.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
