---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-operations.html
---

# Broker configuration operations
<a name="msk-configuration-operations"></a>

Apache Kafka broker configurations are either static or dynamic. Static configurations require a broker restart for the configuration to be applied. Dynamic configurations do not need a broker restart for the configuration to be updated. For more information about configuration properties and update modes, see Apache Kafka Configuration.

This topic describes how to create custom MSK configurations and how to perform operations on them. For information about how to use MSK configurations to create or update clusters, see [Amazon MSK key features and concepts](operations.md).

**Topics**
+ [Create a configuration](msk-configuration-operations-create.md)
+ [Update configuration](msk-configuration-operations-update.md)
+ [Delete configuration](msk-configuration-operations-delete.md)
+ [Get configuration metadata](msk-configuration-operations-describe.md)
+ [Get details about configuration revision](msk-configuration-operations-describe-revision.md)
+ [List configurations in your account for the current Region](msk-configuration-operations-list.md)
+ [Amazon MSK configuration states](msk-configuration-states.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
