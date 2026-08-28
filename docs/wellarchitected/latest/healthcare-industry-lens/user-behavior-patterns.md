---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/user-behavior-patterns.html
---

# User behavior patterns
<a name="user-behavior-patterns"></a>

| HCL\_SUS2. How do you match workload infrastructure to user behavior patterns? |
| --- |
|   |

 **Scale infrastructure to continually match user demand and performance requirements**

 Many healthcare workloads are life-critical, and have steady demand 24 x 7. However, other workloads (such as those supporting ambulatory care delivery or revenue cycle workflows) exhibit cyclical utilization patterns with peak demand during business hours. [Minimize the amount of hardware used](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/use-the-minimum-amount-of-hardware-to-meet-your-needs.html) by scaling workloads down during periods of low demand.

 Legacy solutions may use statically provisioned infrastructure, with redundancy for high availability. Consider cloud-native ways to meet business requirements with an elastic, efficient architecture and disaster recovery strategy (like a pilot light architecture rather than active-active).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
