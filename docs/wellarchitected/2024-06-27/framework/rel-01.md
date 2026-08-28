---
source_url: https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/rel-01.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL 1. How do you manage Service Quotas and constraints?
<a name="rel-01"></a>

For cloud-based workload architectures, there are Service Quotas (which are also referred to as service limits). These quotas exist to prevent accidentally provisioning more resources than you need and to limit request rates on API operations so as to protect services from abuse. There are also resource constraints, for example, the rate that you can push bits down a fiber-optic cable, or the amount of storage on a physical disk.

**Topics**
+ [REL01-BP01 Aware of service quotas and constraints](rel_manage_service_limits_aware_quotas_and_constraints.md)
+ [REL01-BP02 Manage service quotas across accounts and regions](rel_manage_service_limits_limits_considered.md)
+ [REL01-BP03 Accommodate fixed service quotas and constraints through architecture](rel_manage_service_limits_aware_fixed_limits.md)
+ [REL01-BP04 Monitor and manage quotas](rel_manage_service_limits_monitor_manage_limits.md)
+ [REL01-BP05 Automate quota management](rel_manage_service_limits_automated_monitor_limits.md)
+ [REL01-BP06 Ensure that a sufficient gap exists between the current quotas and the maximum usage to accommodate failover](rel_manage_service_limits_suff_buffer_limits.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
