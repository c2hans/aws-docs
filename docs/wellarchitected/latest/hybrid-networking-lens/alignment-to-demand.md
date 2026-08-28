---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/alignment-to-demand.html
---

# Alignment to demand
<a name="alignment-to-demand"></a>

 In hybrid networking architectures, aligning network capacity with actual demand is fundamental to sustainability. Over-provisioned network connections waste energy through unused bandwidth and idle hardware, while under-provisioned links can cause retransmission and increased power consumption. By implementing demand-based capacity management and intelligent routing, organizations can optimize their network resource utilization while maintaining required performance levels.

| HNSUS01: How do you identify and eliminate redundant infrastructure and unnecessary data movement to reduce resource usage? |
| --- |
|   |

 Redundant infrastructure and excessive data movement increase energy consumption, carbon emissions, and costs. Proactively identifying and removing unused assets, consolidating overlapping resources, and minimizing data transfers ensures efficient resource utilization and reduces environmental impact.

| HNSUS02: How do you evaluate business-critical components and trade-offs to align resource usage with sustainability goals? |
| --- |
|   |

 Not all components in a workload are equally critical. By analyzing the purpose, utilization, and environmental impact of each component, you can prioritize optimizations for high-value resources while deprioritizing or retiring non-critical ones.

**Topics**
+ [HNSUS01-BP01 Decommission unused assets and consolidate redundant resources](hnsus01-bp01.md)
+ [HNSUS02-BP01 Prioritize critical components](hnsus02-bp01.md)
+ [HNSUS02-BP02 Perform lifecycle assessments for sustainability trade-offs](hnsus02-bp02.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
