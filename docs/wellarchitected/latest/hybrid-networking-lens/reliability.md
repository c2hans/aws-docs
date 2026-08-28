---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/reliability.html
---

# Reliability
<a name="reliability"></a>

 In this lens, reliability pillar focuses on ensuring hybrid network infrastructures can maintain consistent operations, recover from failures, and adapt to changing demands. In hybrid environments, reliability extends beyond individual components to encompass the complex interconnections between on-premises and cloud networks, where disruptions in either environment or the connecting paths can impact overall system availability.

 Hybrid networks present unique reliability challenges due to their distributed nature, multiple connection types, and dependencies between environments. Organizations must design for resilience across all network components - from physical connections and routing infrastructure to the protocols and services that enable cross - environment communication.

 To achieve reliability, a system must have a well-planned foundation and monitoring in place, with mechanisms for handling changes in demand or requirements. The system should be designed to detect failure and automatically heal itself.

**Topics**
+ [Foundations](foundations.md)
+ [Change management](change-management.md)
+ [Failure management](failure-management.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
