---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/data-modeling.html
---

# Data modeling best practices: recommendations for designing data models
<a name="data-modeling"></a>

Effective data modeling is crucial for optimizing performance and minimizing costs when working with Amazon Keyspaces (for Apache Cassandra). This topic covers key considerations and recommendations for designing data models that suit your application's data access patterns.
+ **Partition Key Design ** – The partition key plays a critical role in determining how data is distributed across partitions in Amazon Keyspaces. Choosing an appropriate partition key can significantly impact query performance and throughput costs. This section discusses strategies for designing partition keys that promote even distribution of read and write activity across partitions.
+ **Key Considerations:**
  + **Uniform activity distribution** – Aim for uniform read and write activity across all partitions to minimize throughput costs and leverage burst capacity effectively.
  + **Access patterns** – Align your partition key design with your application's primary data access patterns.
  + **Partition size** – Avoid creating partitions that grow too large, as this can impact performance and increase costs.

To visualize and design data models more easily, you can use the [NoSQL Workbench](workbench.md).

**Topics**
+ [How to use partition keys effectively in Amazon Keyspaces](bp-partition-key-design.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
