---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html
---

# Configure read/write capacity modes in Amazon Keyspaces
<a name="ReadWriteCapacityMode"></a>

Amazon Keyspaces has two read/write capacity modes for processing reads and writes on your tables:
+  On-demand (default)
+  Provisioned

 The read/write capacity mode that you choose controls how you are charged for read and write throughput and how table throughput capacity is managed.

**Topics**
+ [Configure on-demand capacity mode](ReadWriteCapacityMode.OnDemand.md)
+ [Configure provisioned capacity mode](ReadWriteCapacityMode.Provisioned.md)
+ [View the capacity mode of a table in Amazon Keyspaces](ReadWriteCapacityMode.ProvisionedThroughput.ManagingCapacity.md)
+ [Change the capacity mode of a table in Amazon Keyspaces](ReadWriteCapacityMode.SwitchReadWriteCapacityMode.md)
+ [Configure pre-warming for tables in Amazon Keyspaces](warm-throughput.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
