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
