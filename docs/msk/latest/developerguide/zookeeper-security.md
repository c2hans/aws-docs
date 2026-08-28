---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/zookeeper-security.html
---

# Control access to Apache ZooKeeper nodes in your Amazon MSK cluster
<a name="zookeeper-security"></a>

For security reasons you can limit access to the Apache ZooKeeper nodes that are part of your Amazon MSK cluster. To limit access to the nodes, you can assign a separate security group to them. You can then decide who gets access to that security group.

**Important**
This section does not apply for clusters running in KRaft mode. See [KRaft mode](metadata-management.md#kraft-intro).

**Topics**
+ [Disable or enable direct Apache ZooKeeper client access](zookeeper-disable-access.md)
+ [To place your Apache ZooKeeper nodes in a separate security group](zookeeper-security-group.md)
+ [Using TLS security with Apache ZooKeeper](zookeeper-security-tls.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
