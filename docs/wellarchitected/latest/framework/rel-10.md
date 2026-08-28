---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-10.html
---

# REL 10. How do you use fault isolation to protect your workload?
<a name="rel-10"></a>

Fault isolation limits the impact of a component or system failure to a defined boundary. With proper isolation, components outside of the boundary are unaffected by the failure. Running your workload across multiple fault isolation boundaries can make it more resilient to failure.

**Topics**
+ [REL10-BP01 Deploy the workload to multiple locations](rel_fault_isolation_multiaz_region_system.md)
+ [REL10-BP02 Automate recovery for components constrained to a single location](rel_fault_isolation_single_az_system.md)
+ [REL10-BP03 Use bulkhead architectures to limit scope of impact](rel_fault_isolation_use_bulkhead.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
