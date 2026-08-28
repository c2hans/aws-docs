---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/estimates-for-open-shift-to-aws-eks/business-challange.html
---

# Business challenge
<a name="business-challange"></a>

Platform teams frequently face pressure to provide migration estimates early in the planning process, often before completing a thorough technical assessment. These initial estimates can become fixed commitments, creating risk when unforeseen complexities emerge during execution.

Accurate estimation for OpenShift to Amazon EKS migrations requires addressing both technical and organizational factors. Beyond the technical migration work itself, teams must account for several business and planning challenges:
+ **Limited historical data** – Organizations often lack reference points from similar container platform migrations
+ **Stakeholder alignment** – Multiple teams may have competing priorities and timeline expectations
+ **Skills assessment** – Uncertainty around team capabilities and training requirements for AWS-native services
+ **Dependency mapping** – Complex application interdependencies that become apparent during discovery
+ **Business continuity** – Requirements for minimal downtime and rollback capabilities
+ **Technical debt** – Legacy configurations and workarounds that surface during migration planning
+ **Contractual drivers** – Timeline constraints from licensing agreements or contract renewals
+ **Architectural decisions** – Trade-offs between lift-and-shift approaches versus re-architecting for cloud-native patterns

This guide helps you build estimation frameworks that account for these variables, enabling more accurate planning and stakeholder communication throughout your migration journey.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
