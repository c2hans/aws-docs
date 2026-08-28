---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/best-practices-rel.html
---

# Best practices
<a name="best-practices-rel"></a>

 HPC workloads can run for hours to days in duration, and often scale out to thousands and even millions of vCPUs. Traditionally, multiple users often access the same large system and require access to domain-specific applications. The best practices below provide guidance on how to best implement these reliability requirements on the cloud.

 **Workload architecture**
+ [ HPCREL01-BP01 Consider instance type flexibility for your workload ](workload-architecture.md#hpcrel01-bp01)
+ [ HPCREL01-BP02 Deploy loosely coupled workloads across multiple Availability Zones ](workload-architecture.md#hpcrel01-bp02)

 **Change management**
+ [ HPCREL02-BP01 Install software packages in a shared location to simplify multi-user, multi-resource software requirements management ](change-management.md#hpcrel02-bp01)
+ [ HPCREL02-BP02 Use package managers to simplify software dependency management when possible ](change-management.md#hpcrel02-bp02)

 **Failure management**
+ [ HPCREL03-BP01 Implement checkpointing ](failure-management.md#hpcrel03-bp01)
+ [ HPCREL03-BP02 Use durable storage to store and back up datasets ](failure-management.md#hpcrel03-bp02)

**Topics**
+ [Foundations](foundations.md)
+ [Workload architecture](workload-architecture.md)
+ [Change management](change-management.md)
+ [Failure management](failure-management.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
