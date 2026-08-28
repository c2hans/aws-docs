---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-storage-management.html
---

# Storage management for Standard brokers
<a name="msk-storage-management"></a>

Amazon MSK provides features to help you with storage management on your MSK clusters.

**Note**
With [Express brokers](msk-broker-types-express.md), you don't need to provision or manage any storage resoures used for your data. This simplifies cluster management and eliminates one of the common causes of operational issues with Apache Kafka clusters. You also spend less as you don't have to provision idle storage capacity and you only pay for what you use.

**Standard broker type**
With [Standard brokers](msk-broker-types-standard.md) you can choose from a variety of storage options and capabilities. Amazon MSK provides features to help you with storage management on your MSK clusters.

For information about managing throughput, see [Provision storage throughput for Standard brokers in a Amazon MSK cluster](msk-provision-throughput.md).

**Topics**
+ [Tiered storage for Standard brokers](msk-tiered-storage.md)
+ [Scale up Amazon MSK Standard broker storage](msk-update-storage.md)
+ [Manage storage throughput for Standard brokers in a Amazon MSK cluster](msk-provision-throughput-management.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
