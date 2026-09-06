---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/rel-10.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL 10. How do you use fault isolation to protect your workload?
<a name="rel-10"></a>

Fault isolated boundaries limit the effect of a failure within a workload to a limited number of components. Components outside of the boundary are unaffected by the failure. Using multiple fault isolated boundaries, you can limit the impact on your workload.

**Topics**
+ [REL10-BP01 Deploy the workload to multiple locations](rel_fault_isolation_multiaz_region_system.md)
+ [REL10-BP02 Select the appropriate locations for your multi-location deployment](rel_fault_isolation_select_location.md)
+ [REL10-BP03 Automate recovery for components constrained to a single location](rel_fault_isolation_single_az_system.md)
+ [REL10-BP04 Use bulkhead architectures to limit scope of impact](rel_fault_isolation_use_bulkhead.md)
