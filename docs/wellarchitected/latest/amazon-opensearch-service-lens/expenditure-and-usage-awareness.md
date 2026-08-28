---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/amazon-opensearch-service-lens/expenditure-and-usage-awareness.html
---

# Expenditure and usage awareness
<a name="expenditure-and-usage-awareness"></a>

 To effectively manage costs and drive efficiency, it's essential to understand your organization's expenses, identify cost drivers, and attribute resource costs to specific workloads, teams, or product owners. This understanding informs your decisions about resource allocation and encourages efficient usage behavior.

| AOSCOST02: How do you choose appropriate storage tiering? |
| --- |
|   |

 Implement a tiered data storage strategy for long-term data retention or infrequently accessed read-only data. This approach optimizes cost in OpenSearch domains by offloading less frequently used data to cost-effective storage options.

**Topics**
+ [AOSCOST02-BP01 Use the latest Amazon EBS gp3 volumes with your OpenSearch Service nodes](aoscost02-bp01.md)
+ [AOSCOST02-BP02 Use instances optimized for heavy indexing use cases](aoscost02-bp02.md)
+ [AOSCOST02-BP03 Use the warm storage tier to optimize storage for a significant amount of read-only data](aoscost02-bp03.md)
+ [AOSCOST02-BP04 Use the cold tier storage option to store and retrieve infrequently accessed or historical data](aoscost02-bp04.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
