---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/CostOptimization_TableUsagePatterns.html
---

# Evaluate your table usage patterns to optimize performance and cost
<a name="CostOptimization_TableUsagePatterns"></a>

This section provides an overview of how to evaluate if you are efficiently using your Amazon Keyspaces tables. There are certain usage patterns which are not optimal for Amazon Keyspaces, and they allow room for optimization from both a performance and a cost perspective.

**Topics**
+ [Perform fewer strongly-consistent read operations](#CostOptimization_TableUsagePatterns_StronglyConsistentReads)
+ [Enable Time to Live (TTL)](#CostOptimization_TableUsagePatterns_TTL)

## Perform fewer strongly-consistent read operations
<a name="CostOptimization_TableUsagePatterns_StronglyConsistentReads"></a>

Amazon Keyspaces allows you to configure [read consistency](consistency.md#ReadConsistency) on a per-request basis. Read requests are eventually consistent by default. Eventually consistent reads are charged at 0.5 RCU for up to 4 KB of data.

Most parts of distributed workloads are flexible and can tolerate eventual consistency. However, there can be access patterns requiring strongly consistent reads. Strongly consistent reads are charged at 1 RCU for up to 4 KB of data, essentially doubling your read costs. Amazon Keyspaces provides you with the flexibility to use both consistency models on the same table.

You can evaluate your workload and application code to confirm if strongly consistent reads are used only where required.

## Enable Time to Live (TTL)
<a name="CostOptimization_TableUsagePatterns_TTL"></a>

[Time to Live (TTL)](TTL.md) helps you simplify your application logic and optimize the price of storage by expiring data from tables automatically. Data that you no longer need is automatically deleted from your table based on the Time to Live value that you set.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
