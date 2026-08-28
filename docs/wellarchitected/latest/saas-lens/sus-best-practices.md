---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/sus-best-practices.html
---

# Best practices
<a name="sus-best-practices"></a>

There are six best practice areas for sustainability in the cloud:

**Topics**
+ [Region selection](region-selection.md)
+ [User behavior patterns](user-behavior-patterns.md)
+ [Software and architecture patterns](software-and-architecture-patterns.md)
+ [Data patterns](data-patterns.md)
+ [Hardware patterns](hardware-patterns.md)
+ [Development and deployment patterns](development-and-deployment-patterns.md)

Unlike the other pillars, the numbering of the sustainability best practices indicates the estimated complexity of implementing that best practice. We recommend that you consider this order when planning your sustainability improvement plan.
+ **SaaS SUS 1:** How do you use deployment models (silo, bridge, pool) to align tenant consumption with resource utilization?
+ **SaaS SUS 2:** How do you maximize the value from the resources that the SaaS environment consumes?
+ **SaaS SUS 3:** Do you have a tenant off-boarding plan for inactive tenants? How do you decommission tenant resources that are not being used to limit or prevent waste?
+ **SaaS SUS 4:** How do you provide per-tenant footprint visibility (such as resource utilization and carbon emission data) in your SaaS environment?

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
