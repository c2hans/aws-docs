---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/workload-architecture.html
---

# Workload architecture
<a name="workload-architecture"></a>

| DRHCREL03: What strategies should you implement to provide reliable data access and processing across on-premises, edge, and cloud environments? |
| --- |
|   |

 If a resource failure occurs, healthy resources should continue to serve requests. When you have effective failover strategies, your systems in place can fail over to healthy resources in unimpaired locations. The failover must be implemented in accordance with your data residency requirements across on-premises, edge, and cloud environments.

**Topics**
+ [DRHCREL03-BP01 Use AWS Outposts or Local Zones for scenarios where data must reside within a country or jurisdiction without a local AWS Region](drhcrel03-bp01.md)
+ [DRHCREL03-BP02 Implement failover mechanisms to maintain highly-available data access and processing across on-premises, edge, and cloud environments](drhcrel03-bp02.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
