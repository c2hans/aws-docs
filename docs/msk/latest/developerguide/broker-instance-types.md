---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/broker-instance-types.html
---

# Amazon MSK broker types
<a name="broker-instance-types"></a>

MSK Provisioned offers two broker types - Standard and Express. Standard brokers give you the most flexibility to configure your clusters, while Express brokers offer more elasticity, throughput, resilience, and ease-of-use for running high performance streaming applications.

See the following topics for more details about each offering. The following table also highlights the key feature comparison between Standard and Express brokers.

| Feature | Standard broker | Express broker |
| --- | --- | --- |
| [Storage Management](msk-storage-management.md) | Customer managed (Features include EBS storage, Tiered storage, Provisioned storage throughput, Auto-scaling, Storage capacity alerts) | Fully MSK managed |
| [Supported instances](broker-instance-sizes.md) | T3, M5, M7g | M7g |
| [Sizing and scaling considerations](bestpractices-intro.md) | Throughput, connections, partitions, storage | Throughput, connections, partitions |
| [Broker scaling](msk-update-broker-count.md) | Vertical and horizontal scaling | Vertical and horizontal scaling |
| [Kafka versions](kafka-versions.md) | See [Apache Kafka versions](kafka-versions.md) | Starts at version 3.6 |
| [Apache Kafka Configuration](msk-configuration.md) | More configurable | Mostly MSK managed for higher resilience |
| [Security](security.md) | Encryption, Private/Public access, Authentication & Authorization - IAM, SASL/SCRAM, mTLS, plaintext, Kafka ACLs | Encryption, Private/Public access, Authentication & Authorization - IAM, SASL/SCRAM, mTLS, plaintext, Kafka ACLs |
| [Monitoring](monitoring.md) | CloudWatch, Open Monitoring | CloudWatch, Open Monitoring |

**Note**
You can't change an MSK Provisioned cluster from a Standard broker type to an Express broker type by switching the broker type using the MSK API. You have to create a new cluster with the desired broker type (Standard or Express).

**Topics**
+ [Amazon MSK Standard brokers](msk-broker-types-standard.md)
+ [Amazon MSK Express brokers](msk-broker-types-express.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
