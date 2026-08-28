---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-express.html
---

# Express broker configurations
<a name="msk-configuration-express"></a>

Apache Kafka has hundreds of broker configurations that you can use to tune the performance of your MSK Provisioned cluster. Setting erroneous or sub-optimal values can affect cluster reliability and performance. Express brokers improve the availability and durability of your MSK Provisioned clusters by setting optimal values for critical configurations and protecting them from common misconfiguration. There are three categories of configurations based on read and write access: [read/write (editable)](msk-configuration-express-read-write.md), [read only](msk-configuration-express-read-only.md), and non-read/write configurations. Some configurations still use Apache Kafka’s default value for the Apache Kafka version the cluster is running. We mark those as Apache Kafka Default.

**Topics**
+ [Custom MSK Express broker configurations (Read/Write access)](msk-configuration-express-read-write.md)
+ [Express brokers read-only configurations](msk-configuration-express-read-only.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
