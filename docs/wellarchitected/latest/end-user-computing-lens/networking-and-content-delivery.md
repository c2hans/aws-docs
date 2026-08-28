---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/networking-and-content-delivery.html
---

# Networking and content delivery
<a name="networking-and-content-delivery"></a>

 The optimal networking solution for a workload varies based on latency, throughput requirements, jitter, and bandwidth. Physical constraints, such as the location of users and data sources, will affect the performance of the solution.

|  EUCPERF06: How do you configure network connectivity in your EUC environment for best performance?  |
| --- |
|   |

 In an EUC architecture, there are two key networking configurations to consider:
+  Connections from end users to their most proximal AWS EUC service connection point
+  Connections from the EUC instances to any backend infrastructure and other services

**Topics**
+ [EUCPERF06-BP01 Minimize latency between end users and EUC services](eucperf06-bp01.md)
+ [EUCPERF06-BP02 Minimize latency between EUC instances and dependent services](eucperf06-bp02.md)
+ [EUCPERF06-BP03 Make sure that EUC network configurations don't interfere with service management connections](eucperf06-bp03.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
