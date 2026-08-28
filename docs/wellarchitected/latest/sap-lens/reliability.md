---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/reliability.html
---

# Reliability
<a name="reliability"></a>

The reliability pillar encompasses the ability of a workload to perform its intended function correctly and consistently when it’s expected to. This includes the ability to operate and test the workload through its total lifecycle. For many businesses, being well-architected for reliability is a key requirement for SAP workloads. This is due to the mission critical nature of many SAP workloads and a need to understand the SAP architecture and the restrictions this imposes.

As with other pillars, we recommend reviewing the AWS Well-Architected Framework, particularly for the best practices of foundations, change management, and failure management. When considering reliability with the SAP Lens, focus first on having a clear and balanced understanding of your non-functional requirements across individual systems, including the business priorities that drive these requirements.

You should differentiate between how you achieve availability and reliability, and define your approach to disaster recovery. Availability can be defined as how you design the system so that users can continue to access it by providing resilience for single points of failure. Disaster recovery focuses on one-time recovery objectives where a decision to invoke a planned set of actions is made by the system owner.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
