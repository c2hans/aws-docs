---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-replicator-cross-account.html
---

# Cross-account migration between Amazon MSK clusters
<a name="msk-replicator-cross-account"></a>

For migrations across different AWS accounts, you must use Apache MirrorMaker 2.0.

[Apache MirrorMaker 2.0](https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=27846330) is an open-source tool that requires manual setup and management, but provides detailed control over the migration process. For more information, see [Kafka geo-replication documentation](https://kafka.apache.org/40/documentation.html#georeplication).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
